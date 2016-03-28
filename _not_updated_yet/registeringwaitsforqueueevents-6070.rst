
Remember that events in MPF can have key/value pairs (or keyword
attributes) passed along with them. (For example, when a new player's
turn starts, the event *player_turn_start* is posted along with
keyword attributes *player* (the player object) and *number* (the
integer number of that player). When a queue event is posted, it
includes an attribute called queue which is a link to a QueuedEvent
object that the event handler can interact with. In many cases, you
might not need to register a "wait", so you would just ignore that
queue object in your event handler. But if you want MPF to hold up
progress until your handler is done, you can do so by registering a
wait with the QueuedEvent that was passed. This is easier to
understand with an example. Let's say that we want to hook into the
ball_ending event with some method. The usual way we do this is to
register a handler, like this:


::

    
    self.machine.events.add_handler('ball_ending', self.block)


In this case, the event manager will call self.block() when the
ball_ending event is posted. Nothing special there. Now let's look at
our block() method and see what we can do with it:


::

    
    def block(self, queue, **kwargs):
        pass # do something


Note that in the arguments of this function, we've included the
keyword *queue* (in addition to the usual ***kwargs* which we include
in almost every function that we tie to events just to catch any
unexpected parameters.) The *queue* keyword will be used since we're
registering this function as a handler for an event that we know is a
QueuedEvent. If you are also using this function as a handler for a
non-queue event, then you'd want to include a default value since non-
queue events won't include a *queue* parameter. So that would be `def
block(self, queue=None, **kwargs)`. The queue parameter will be the
QueuedEvent object for this queue event. The QueuedEvent has a few
methods as `outlined in the API documentation`_. (As of this writing
it doesn't appear those are fully documented, so we'll add that for
the next update.) The two we care about are `wait()` (which registers
a wait request) and the `clear()` (which clears a previously-
registered wait). So we can update our event handler like this:


::

    
    def block(self, queue, **kwargs):
        self.queue = queue
        self.queue.wait()
        # now do something


In this code, we save a reference to the QueuedEvent as `self.queue`
so that we have a way to access it later. Then we call
`self.queue.wait()` which simply lets the event manager know that we
want it to wait for us before proceeding. Now we can do whatever we
want... start a mode, post some events... whatever. Then when we're
done we simply call `self.queue.clear()` and that will remove our
wait. Note that it's possible to have multiple waits registered on a
single QueuedEvent. The event manager maintains a count of the number
of waits that have been requested (increasing it by one with each
`wait()` call and decreasing it with each `clear()`). Then when the
count is zero, it proceeds with whatever the original callback was
when the queue event was posted. In the case of *ball_ending*, once
the queue is clear it will move on to *ball_ended* which will trigger
the player turn rotation, then the next ball starting, then serving
the ball to the plunger, etc.



Putting this into practice with a bonus mode
--------------------------------------------

Ok, so now you have the theory and some examples. Now let's build an
actual bonus mode. We'll call this mode "bonus", and we'll create both
a `bonus.yaml` for its mode config as well as a `bonus.py` for its
mode code. (Don't forget to add the blank __init__.py files in your
bonus and code folder). In `bonus.yaml`, you can set up the mode like
this:


::

    
    #config_version=3
    
    mode:
      start_events: ball_ending
      stop_events: show_bonus_timer_done
      code: bonus.Bonus
      priority: 500  # prob want this higher than your game modes


Then in your `bonus.py`, you could do something like:


::

    
    from mpf.system.mode import Mode
    
    class Bonus(Mode):
    
        def mode_start(self, queue, **kwargs):
            self.queue = queue
            self.queue.wait()
    
            # now do your math for the bonus
            # you want some slides for this?
            # prob easiest to post some events with params
            # then add those to your slide_player: in the mode config
    
            self.machine.events.post('bonus_slide_1', points=2000, loops=2)
    
            # maybe set a timer on that event too to end the mode?
    
        def mode_stop(self, **kwargs):
            self.queue.clear()


asdf

.. _outlined in the API documentation: http://missionpinball.github.io/mpf/mpf.system.events.html?highlight=queuedevent#mpf.system.events.QueuedEvent


