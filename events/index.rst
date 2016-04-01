Events
======

The concept of *events* is one of the most important concepts in MPF. MPF is an
event-driven framework, which means that almost everything that happens
generates an event, and then things that need to react to certain events receive
notification that an event occurred and can act on it.

Understanding how Events work in MPF
------------------------------------

It's easiest to understand the concept of events by going through some examples.
(These examples are not actual Python code, rather, they're just some
pseudocode-like example.) The main two actions with events are "posting" events
(which is where some component posts an event to the Event Manager), and
"handling" events (where some component registers to do some action when an
event happens). So let's apply this to an event like a new ball starting.

You can imagine that lots of things would need to happen, which means that lots
of components need to register (or "add a handler" in MPF parlance) for that
event. For example, when a new ball goes live:

+ The ball save timer needs to start.
+ The skill shot need to start.
+ The display needs to switch over to show the current player score.
+ The music system needs to start playing the background music.
+ The auditing system needs to start the timer to record average ball
  times, etc.
+ The tilt system needs to start watching for tilts.
+ Etc.

So when a new ball is starting, the game mode might tell the Event Manager a
post an event called *ball_starting*. Then the Event Manager will look through
its list of registered handlers and look to see if anyhave been registered
"ball_starting." If it finds them, it will contact them one-by-one so they can
do whatever they need to do for that event. The real beauty of using events for
certain modules to notify other modules is that the notifying module doesn't
know or care whether any (if any) handlers have been registered.

This allows the game code to be extremely modular. You can add your own
components which can listen for events to "insert" themselves into the game, or
you can remove built-in modules without breaking anything. (It also makes it
really easy to "program" your game with config files—-essentially all your
config files are is big lists of what happens when certain events are posted.

.. note:: Event names in MPF are not case sensitive. If you post an event called
   *My_Event*, it will actually be posted as *my_event*. Similarly if you
   register an event handler to listen for an event called *My_Event*, it will
   actually register itself to listen for *my_event*.

The event queue
---------------

The Event Manager only processes one event at a time. So when it gets an event
to post, it will call the handlers that have registered for notification of that
event one-by-one. If one of those handlers wants to post another event of its
own, that's fine. But when it posts the event since the Event Manager is busy,
it will add the new event to an event queue. Then after the first event is done
(meaning after all the event handlers have been called for the first event), the
Event Handler will call the next event in the queue. The event queue can hold
multiple events, and they will be called one-by-one in the order they were
posted.


Handler Priorities
------------------

When you have some code you want to register to be a handler for an event, you
can optionally specify a priority. (Priority is just an integer value.) The
default priority for events is 1. If you want a guarantee that a certain event
handler will fire last, then register that handler with a priority that's lower
than any other handler for that event. And if you want to guarantee that a
handler fires first, register it with a higher priority. (In this case, "higher"
and "lower" are literal. A handler with a priority of 500 will be called before
a handler of 100.)

The actual integer values of the priorities are arbitrary. They're called
one-by-one, one after the other, in order from highest to lowest. Whether your
priorities are 3, 2, and 1, or 1000, 100 and 0, or 1000, 999, 998, and 1 makes
no difference.

MPF automatically registers event handlers from modes with the priority of that
mode, meaning high-priority modes get access to an event before lower-priority
modes. (This is useful since it gives higher-priority modes a chance to "block"
events from lower-priority modes.)

Event callbacks
---------------

When you post an event, you have the option to pass a *callback* as a parameter.
A callback is a function or method that you want to be called once the event is
done processing. (i.e. it's called once all the handlers that have registered
for that event have been called. If no handlers are registered, the callback is
called immediately.) One "gotcha" with callbacks is they're called after the
event is done processing. If the event manager is busy (because another event is
in progress), then the callback won't actually be called until the actual event
is processed, which might not be immediate. In most cases you combine callbacks
with special types of events. So to understand how this all works, we need to
look at the different types of events you can call.

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

The basic event is just a just a simple event name. Your code just
calls the Event Manager and tells it to post an event with a given
name, like `events.post('your_event_name')`. Then the event manager
calls each of the registered handlers one-by-one. If you have
specified a callback, like ```events.post('your_event_name',
callback=self.some_function)``, that callback will be called after the
last registered handler has returned after handling the event.


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



Best practices for using events
-------------------------------

When a handler responds to an event, the "flow" of the code goes into
that handler. This means that you do *not* want a handler to take too
long to return. If there's something that a handler needs to do that
takes a long time, it should set up a task, a timer, or register to do
work based on the "timer_tick" event. In other words, your handlers
should return quickly.



FAQs on events
--------------

We've received several questions from users about events, so we're
sharing a list of questions that have been asked as well as our
answers:

 The documentation states, "One 'gotcha' with callbacks is
 they'recalled after the event is done processing. If the event manager
 isbusy (because another event is in progress), then the callback
 won'tactually be called until the actual event is processed, which
 mightnot be immediate." Does this mean that the callback is
 calledafter the event has beensent to all registered handlers or until
 the current handler iscomplete?

The callback is called after all the handlers for that event have been called.
When an event is posted, if there's another current event in progress (meaning
that the new event was actually posted by a handler from some prior event), then
the new event is added to the queue. (The queue is essentially a list of events
that still need to be called). So all the handlers for the current in-progress
event are called, then the callback is called (if a callback was specified).
Then when that callback is done, that event is "done" and theEvent Managerchecks
the queuelist to see if another event should be posted. Technically speaking
only the Event Manager can post an event. All the other code bits that post
events are really saying, "Hey event manager, can you please post this event?"
And the event manager is like, "yeah yeah, I'll do it when I'm not busy."

You can see this in action with verbose logging enabled where the event manager
receives an event at one point, but the actual "post" of that event might not
happen until hundreds of lines later.

 How do boolean results factor into this? This stops the event
 frombeing sent to the remaining handlers?

Correct. If any handler returns False, that event is not sent to the remaining
handlers. (The order the handlers are called can be set by specifying a priority
when a handler is registered.) If a boolean event has a callback and one of the
handlers returns False, the callback is still called with a special parameter
``ev_result=False``. This lets you take some action (if you want) on that event
failing.

 How does the event caller know when all handlers have completed
 processing?

When you call any method in Python, when that method gets to the end
of its code, it will "return" to whatever called it. (Even if that
method calls another method, that second method will get to the end of
its code and return back to the point that called it in the first
method, then the first method will finish and return to whatever
called it, etc.) The Event Handler is essentially just a mapping of
event names to handler methods and priorities, so when it sees an
event called "foo", it will see there are three registered handlers,
so it will call the first one, and when that one returns it calls the
second one, and when that one returns it calls the third one, and when
that one returns the event method is over and then it returns and the
game loop continues. If you add an infinite loop (or just any loop
that takes a long time) into one of your handlers, then MPF will get
"stuck" there. So it's up to each handler to do what it needs to do
quickly and then return.

 The event manager is a big queue. First In, First Out. For example, we
 have 5 handlers for the event "foo". "foo" will be sent to all 5 before
 discarding the event and popping the event off the queue in order to
 send out the next event. But what I am trying to figureout is when the
 event manager must send to all 5 or when it can terminate early. In
 other words, if handler #2 returns a False for a boolean event, then
 handler #3,#4 and #5 never see the event? Correct?


Correct.

 Now if it's not a boolean event, is there anything that can
 alsostop/suppress the event from being seen by all the handlers? Or is
 itsent to all '5' regardless of the handlers results?

Correct, if it is *not* a boolean event, then the event is sent to all
5 handlers regardless of the results. Nothing can stop it. If you
don't want this behavior, then post a boolean event instead of a
regular event.

List of events used in MPF
--------------------------

.. toctree::

   ball_search_failed <ball_search_failed>
   ball_search_started <ball_search_started>
   ball_search_stopped <ball_search_stopped>
   collecting_balls <collecting_balls>
   collecting_balls_complete <collecting_balls_complete>
   init_phase_(number) <init_phase_x>
   loading_assets <loading_assets>
   machine_var_(name) <machine_var_name>
   machine_reset_phase_(number) <machine_reset_phase_x>
   player_(var_name) <player_var_name>
   player_add_success <player_add_success>
   reset_complete <reset_complete>
   shutdown <shutdown>
