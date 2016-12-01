Types of events
---------------

There are several different *types* of events in MPF, including:

+ Basic events
+ Boolean events
+ Queue events
+ Relay events

You can find the details of how to use each of these events by reading
through the API documentation for the event manager, but here's a
quick overview.

Basic Events
~~~~~~~~~~~~

The basic event is just a just a simple event name. Your code just calls the
Event Manager and tells it to post an event with a given name, like
events.post(‘your_event_name’). Then the event manager calls each of the
registered handlers one-by-one. If you have specified a callback, like
events.post('your_event_name', callback=self.some_function), that callback will
be called after the last registered handler has returned after handling the
event.

Boolean Events
~~~~~~~~~~~~~~
Boolean events are used when the you want get some feedback from all
of the handlers that have registered for that event. When you post a
boolean event, if any of the registered handlers return `False` then
the event manager will stop processing the event. (i.e. the remaining
handlers are not notified.) Boolean events are typically used with
callbacks, where the event manager will pass a value of `False` to a
callback if one of the handlers returns False. For example, you might
have an event called *request_to_start_game* that's a boolean event.
When that event is posted (perhaps because the player pushed the start
button during the attract mode), the event manager will receive that
event and contact all the registers handlers one-by-one. You'd
typically post that event with a callback of something like
`self.result_of_start_game_request`. Then if any registered handler
returns False, the event manager will call the callback and pass the
False result, like `self.result_of_start_game_request(False)`. Then
your `result_of_start_game_request()` method might choose to do
nothing if it gets a result of False, or it might choose to actually
start a game if it's called without the False value. What types of
handlers might you register for an event called
*request_to_start_game*? There could be many. The ball controller
might want to make sure all the balls are in their home position. The
tilt module might want to make sure the plumb bob tilt isto be settled
and not swinging. If the game is not set to free play, the credits
module has to make sure there's least one credit in the game. Any one
of these modules can deny a game start by registering itself as a
handler for the *request_to_start_game* event and then returning False
if it doesn't want to allow the start. This, by the way, is a great
example of the power and flexibility of using events for this kind of
thing instead of manually hard coding each of these modulesinto the
game code. If the game is set to free play, then the credits module
does not load, so it's not part of the process of watching for a
request to start a game. This means your game starting code doesn't
have to know anything about a credits module or whether or not it's
active. The game starting code just posts the event and will start the
game as long asno one denies it. (Once the game start request is
approved, then a second event is posted which actually starts the
game. That's the one that the credits module will register for to
actually decrement a credit from the machine.) This extensibility is
how you can add functionality to your own game that might need to
approve or deny a game start. For example maybe you have some complex
playfield toy that has to be in a known position in order for the game
to start. So you could have your game code register a handler for the
*request_to_start_game* event which you could deny if your toy wasn't
ready to go. That's how you can inject yourself into the game starting
process without having to hack any of the core Mission Pinball
Framework code. Note: you can see an example of the
*request_to_start_game* boolean event in action in our MPF Game Start
Sequence documentation.

If any handler returns False, that event is not sent to the remaining
handlers. (The order the handlers are called can be set by specifying a priority
when a handler is registered.) If a boolean event has a callback and one of the
handlers returns False, the callback is still called with a special parameter
``ev_result=False``. This lets you take some action (if you want) on that event
failing.

Queue Events
~~~~~~~~~~~~
Queue events are used when an event handler wants to temporarily
"pause" the event processing while it finishes up some task. This is
called a queue event because the event manager literally creates a
little queue of events it's waiting for, and then when that queue is
cleared it calls the callback. An example of this might be after a
tilt. When that happens the game controller will post a *ball_ending*
event (since the tilt ends the ball), but the ball controller might
not actually want the game to move on until the ball has drained into
the trough. So the *ball_ending* event is posted as a queue event,
like this:

::

    events.post_queue('ball_ending', callback=self.ok_to_end_ball)

When a queue event is posted, the event manager will create an event
queue instance and pass it as a parameter to all the registered event
handlers. So if your ball controller wants to make sure all the balls
have drained before the game moves on, it will register a handler for
the *ball_ending* event. In that handler code, if the ball controller
is not ready for the ball to end then it can call a `queue.wait()`
command to tell the event manager that it would like it to wait before
finishing. Then after the ball drains, the ball controller can call a
`queue.clear()` to remove it's hold request from the queue. Once that
event's queue is totally clear, the event manager will call the
callback that was originally included with the event posting. Here's
an example of all this in action. (This should probably move to the
Advanced Programming section of this documentation.) Add a handler for
your event as normal:

::

    self.machine.events.add_handler('ball_starting', self.block)

In the handler method, give it a parameter named “queue”. Also save
queue so you can access it later. Do whatever you need to do then call
queue.wait(). Your handler will be called immediately.

::

    def block(self, queue):
        self.queue = queue
        ...
        self.queue.wait()

Then in your code that clears the wait:

::

    self.queue.clear()

Note if none of the registered event handlers call queue.wait(), then
the callback will be called immediately. If you want to kill a queue
event (i.e. without just waiting forever), then in your registered
handler, do two things:

::

    queue.kill()  # Clears the queue and does not call the callback
    return False  # Causes future (lower priority) handlers not to be called

Relay events
~~~~~~~~~~~~

Relay events are used when you want to pass kwargs from one event to
the next. In this case the handler literally takes whatever one event
returned and passes them as kwargs to the next event. The idea is you
can pass some kwargs around that each event can modify. For example,
if a ball drains, the game calls a ball drain event with kwargs
balls=1. Then if there’s some other module that wants to save that
ball, it can receive balls=1 and change it to balls=0. Then when the
event gets back to the original caller, it has new data. Note a
handler must return a dictionary that will later be packed via \**. So
a handler would do:

::

    return {‘balls’: 1}

to have the next handler be called like:

::

    handler(balls=1)

Relay events tend to work well with callbacks since you aren’t
guaranteed they’ll fire right away.To use a relay event, add
ev_type=’relay’ to your event post.
