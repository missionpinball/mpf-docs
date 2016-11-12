MPF Events
==========

.. toctree::
   :titlesonly:
   :maxdepth: 1

   deeper_dive
   event_reference

The concept of *events* is one of the most important concepts in MPF. MPF is an
event-driven framework, which means that some things post events, and other
things can see that a certain event was posted and they can act on it.

Understanding how Events work in MPF
------------------------------------

It's easiest to understand the concept of events by going through some examples.

For example, you might have a ``scoring:`` entry in your config which watches
for an event called *target1_hit*, and when it sees it, it adds 1000 points
to the player's score.

In this case, the scoring system would "register a handler" for the
*target1_hit* event, essentially telling the Event Manager, "If you see an
event called *target1_hit*, let me know."

Then later on, the switch for target 1 gets activated, and the Shot Controller
posts the event called *target1_hit*. The Event Manager says, "Hey, I remember
the scoring system wanted to know about that, so it tells the scoring system
that *target1_hit* was just posted and the scoring system can wake up and deal
with it (adding the points, in this case).

Here are some fun facts about MPF events:

* There are lots and lots of events in MPF. Sometimes they come really fast—a
  dozen or more in a few milliseconds.
* Not every event will have a handler registered. The event is still posted,
  but no one cares.
* Multiple handlers can be registered for the same event. (And they'll all be
  called, one-by-one, based on the priority they asked for when they
  registered.)
* Event handlers are constantly added and removed throughout the lifecycle of
  a game.
* Event names are not case sensitive. (They're technically all converted to
  lowercase internally.)

Things that post (create) events
--------------------------------

In MPF, many things create events. (We could also say they "post events" or
that they "emit events".)

Just to pick some random examples of things that post events:

* A switch is hit
* A player variable changes
* A timer expires
* A mode stops or starts
* A new slide is shown on the display
* etc.

We actually have a giant list of all the events that are posted by everything
in MPF. This is called the :doc:`event_reference`. (It's also linked from the
"Reference" section in the menu on the left of every page in the docs website
since it's so important.)

As you read through the rest of the documentation for various aspects of MPF,
you'll see settings for things like ``events_when_X:`` with the "X" being
some state.

For example, logic blocks have a setting called ``events_when_hit:`` where you
can enter the name of an event. (In that case the name can be whatever you
want, like ``events_when_hit: mpf_is_awesome``, and then when that logic block
is hit, it will post the event *mpf_is_awesome*, and any other components that
are registered for that event will see it and take their respective action.

The point is that not every event in your machine will be in the Event
Reference list since there are lots of places where you can create your own
event names.

Things that take action on (use) events
---------------------------------------

The flipside of things that create/post/emit events is things that consume, use,
and/or take action on certain events. These are the things that look for
certain event names, and then when they see them, they take action.

Some random examples:

* The game mode will look for ball_drain events which it will handle by ending
  the current player's ball.
* The scoring system might look for a shot hit event to add points to the
  player's score.
* A jackpot mode might look for a ramp made event to play a show which will
  flash some lights and show a jackpot slide.
* A mode might look for the event which comes from shooting a ball into a ball
  lock to start a multiball mode.
* etc.

As you'll see as you read through the MPF documentation, there are two main
ways (plus a lot of little ways) to make things happen when certain events
are posted:

In the various "config" players (slide_player, led_player, show_player, etc.),
you create entries based on event names.

For example, in a config file:

::

   slide_player:
      mpf_is_awesome: my_slide

The above config will show the slide called "my_slide" on the display when the
event *mpf_is_awesome* is posted. Of course this could be any event, including
one from the Events Reference list or a custom event like we discussed above.

Also, a lot of things in MPF have ``X_events:`` settings, which are where you
can event event names that cause that action to happen. For example, you may
have a drop target configured like this:

::

   drop_targets:
      my_drop_target:
         switch: s_drop_target_1
         reset_coil: c_drop_target_reset
         reset_events: mpf_is_awesome

In this case, when the event *mpf_is_awesome* is posted, that will cause that
drop target to reset. Again, this is just one random example of the literally
hundreds of things that can take action on events, and these events could be
from the master events list or your own custom events.
