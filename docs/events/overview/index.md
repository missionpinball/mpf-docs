---
title: Events Overview
---

# Events Overview


Video about events in MPF:

<div class="video-wrapper">
<iframe width="560" height="315" src="https://www.youtube.com/embed/G3UbVP8gFU0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

It's easiest to understand the concept of events by going through some
examples.

For example, you might have a `variable_player:` entry in your config
which watches for an event called *target1_hit*, and when it sees it, it
adds 1000 points to the player's score, like this:

``` mpf-config
##! mode: base
variable_player:
  target1_hit:
    score: 1000
```

What's really happening behind the scenes here is MPF's
variable_player system tells the event system, "Hey, if you see an
event called *target1_hit*, let me know about it." (This is called
"registering a handler", because the variable_player system is
registering with the event since that it can handle that event.)

Then later on, the switch for target 1 gets activated, and the shot
controller posts the event called *target1_hit*. The Event Manager says,
"Hey, I remember the variable_player system wanted to know about
that", so it tells the variable_player system that *target1_hit* was
just posted and the variable_player system can wake up and deal with it
(adding the points, in this case).

So really there are two parts to the events system:

* Things that generate (post) events.
* Things that take action on (handle) events.

Let's look at each of these.

## Things that generate (post) events

There are hundreds of different things that post events in MPF (for all
sorts of reasons). Just to pick some random examples of things that post
events:

* A switch is hit
* A player variable changes
* A timer expires
* A mode stops or starts
* A new slide is shown on the display
* A ball drains
* A ball enters a ball device
* A new player's turn starts
* etc.

We actually have a giant list of all the events that are posted by
everything in MPF. This is called the
[event_reference](../index.md). (It's
also linked from the "Reference" section in the menu on the left of
every page in the docs website since it's so important.)

As you read through the rest of the documentation for various aspects of
MPF, you'll see settings for things like `events_when_XX:` with the
"XX" being some state.

For example, logic blocks have a setting called `events_when_hit:` where
you can enter the name of an event. (In that case the name can be
whatever you want, like `events_when_hit: mpf_is_awesome`, and then when
that logic block is hit, it will post the event *mpf_is_awesome*, and
any other components that are registered for that event will see it and
take their respective action.

This means that while the event reference is useful because it shows all
the *built-in* events, your machine will have lots of other events not
on that list that you define.

## Things that take action on (handle) events

The flip side of things that post events is things that taken action on
(or "handle") events. These are the things that watch for certain
event names, and then when they see them, they take action.

Some random examples:

* The game mode will look for ball_drain events which it will handle
    by ending the current player's ball.
* The variable_player system might look for a shot hit event to add
    points to the player's score.
* A jackpot mode might look for a ramp made event to play a show which
    will flash some lights and display a jackpot slide.
* A mode might look for the event which comes from shooting a ball
    into a ball lock to start a multiball mode.
* etc.

As you'll see as you read through the MPF documentation, there are two
main ways (plus a lot of little ways) to make things happen when certain
events are posted:

In the various
[config players](../../config_players/index.md)
([slide_player](../../config_players/slide_player.md),
[light_player](../../config_players/light_player.md),
[show_player](../../config_players/show_player.md), etc.), you create entries based on event names.

For example, in a config file:

``` mpf-mc-config
#! slides:
#!   my_slide:
#!     - type: text
#!       text: "MPF IS AWESOME"
slide_player:
  mpf_is_awesome: my_slide
##! test
#! post mpf_is_awesome
#! advance_time_and_run .1
#! assert_text_on_top_slide "MPF IS AWESOME"
```

The above config will show the slide called "my_slide" on the display
when the event *mpf_is_awesome* is posted. Of course this could be any
event, including one from the Events Reference list or a custom event
like we discussed above.

Also, a lot of things in MPF have `XX_events:` settings, (the "XX"
will be some word) which is where you can event event names that cause
that action to happen. For example, you may have a drop target
configured like this:

``` mpf-config
#! switches:
#!   s_drop_target_1:
#!     number: 1
#! coils:
#!   c_drop_target_reset:
#!     number: 1
drop_targets:
  my_drop_target:
    switch: s_drop_target_1
    reset_coil: c_drop_target_reset
    reset_events: mpf_is_awesome
```

In this case, when the event *mpf_is_awesome* is posted, that will cause
that drop target to reset. Again, this is just one random example of the
literally hundreds of things that can take action on events, and these
events could be from the master events list or your own custom events.

## The Event Manager

One of MPF's internal core components is called the *Event Manager*.
The event manager keeps track of the hundreds of handlers that have
registered for different events, and it's what other components contact
when they want to post and event.

When an event is posted, the event manager contacts the handlers to let
them know that they need to take action on their event.

Luckily the complexity of the event manager is hidden from you---all you
have to know is that events are posted and handlers can act on them.

Finally, here are a few more random thoughts about events in MPF:

* There are lots and lots of events in MPF. Sometimes they come really
    fast---a dozen or more in a few milliseconds.
* Not every event will have a handler registered. If something posts
    an event and nothing is registered to handle it, so be it!
* Multiple handlers can be registered for the same event. In this case
    the event manager just notifies the handlers one-by-one.
* Event handlers are constantly added and removed throughout the
    lifecycle of a game. (For example, when a mode starts, all sorts of
    handlers are registered to watch for things that mode needs, and
    when the mode ends, those handlers are removed.)
* Event names are *not* case sensitive. (They're technically all
    converted to lowercase internally.)
