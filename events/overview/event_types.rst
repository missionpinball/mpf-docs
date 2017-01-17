Types of events
===============

There are several different *types* of events in MPF, including:

+ Basic
+ Queue

You can find the details of how to use each of these events by reading
through the API documentation for the event manager, but here's a
quick overview.

Basic Events
------------

The basic event is a simple event with a name (and possibly
keyword argument pairs) that is posted.

The event manager will call the registered handlers one-by-one
in the order of their priority (from when they registered).

Queue Events
------------
Queue events are similar to basic events, except that the event
won't actually finish until all the handlers say it's ok to do so.

The *game_ending* event is an example of a queue event. When the
game is over, *game_ending* is posted, and when that's done,
*game_ended* is posted and the attract mode starts again. However
there are several modes that might want to "block" the completion
of game_ending until they can do whatever they need to do. For
example, if match is enabled, it will want to block game_ending until
it can run the match animation. If a player has achieved a high
score, the high score mode will want to block game ending, etc.

You can create your own queue events with the
:doc:`/config/queue_event_player` and :doc:`/config/queue_relay_player`
config file sections.

Note for Programmers
--------------------

If you're a programmer and familiar with Python, you'll notice in the
source code that there are more types of events than just basic and
queue events. The basic and queue events are the only ones that
are exposed via config files, but you'll notice there are
boolean and relay events, and that there are asynchronous versions
of all events too. See the API reference for details.
