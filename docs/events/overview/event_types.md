---
title: Types of events
---

# Types of events


There are several different *types* of events in MPF, including:

* Basic
* Queue

You can find the details of how to use each of these events by reading
through the API documentation for the event manager, but here's a quick
overview.

Video about events in MPF:

<div class="video-wrapper">
<iframe width="560" height="315" src="https://www.youtube.com/embed/G3UbVP8gFU0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Basic Events

The basic event is a simple event with a name (and possibly keyword
argument pairs) that is posted.

The event manager will call the registered handlers one-by-one in the
order of their priority (from when they registered).

## Queue Events

Queue events are similar to basic events, except that the event won't
actually finish until all the handlers say it's ok to do so.

The *game_ending* event is an example of a queue event. When the game is
over, *game_ending* is posted, and when that's done, *game_ended* is
posted and the attract mode starts again. However there are several
modes that might want to "block" the completion of game_ending until
they can do whatever they need to do. For example, if match is enabled,
it will want to block game_ending until it can run the match animation.
If a player has achieved a high score, the high score mode will want to
block game ending, etc.

You can create your own queue events with the
[queue_event_player:](../../config/queue_event_player.md) and
[queue_relay_player:](../../config/queue_relay_player.md) config file
sections.

Queue Events are categorized in the Events Reference by their device
or other grouping type, but are also listed together in the
[Queue Events event listing page](../queue_events/index.md).

## Note for Programmers

If you're a programmer and familiar with Python, you'll notice in the
source code that there are more types of events than just basic and
queue events. The basic and queue events are the only ones that are
exposed via config files, but you'll notice there are boolean and relay
events, and that there are asynchronous versions of all events too. See
the API reference for details.
