---
title: Shots
---

# Shots


Related Config File Sections:

* [shots:](../../config/shots.md)
* [shot_profiles:](../../config/shot_profiles.md)
* [shot_groups:](../../config/shot_groups.md)

In MPF, a "shot" is a switch (or combination) of switches that the
player shoots for. Examples include:

* A standup target, drop target, or rollover lane
* A ramp, loop, or orbit
* A toy, subway, or VUK

Most shots have lights or LEDs associated with them which are on, off,
flashing, and/or certain colors to reflect what "state" the shot is
in.

Broadly speaking, a shot is anything the player shoots at during a game.
It could be a standup target, a lane, a ramp, a loop, a drop target, a
pop bumper, a toy, etc.

In MPF, you define switches (or a sequence of switches) as a "shot".
Then whenever that shot is made, MPF posts events which you can use to
trigger scores, achievements, shows, etc.

Some shots are made up of a single switch (like a standup target). But
you can also configure shots that are only considered to be hit based on
series of switches that must be hit in the right order within a certain
time frame. For example, you might have an orbit shot with three
switches: *orbit_left*, *orbit_top*, and *orbit_right*. You could
configure one shot called *left_orbit* that's triggered when the
switches *orbit_left*, *orbit_center*, and *orbit_right* are hit (in
that order) within 3 seconds, and you could configure a second shot
called *right_orbit* that's triggered when the switches *orbit_right*,
*orbit_center*, and *orbit_left* are hit within 3 seconds. (So, same
switches, but two different shots depending on the order they're hit.)

You can also configure different "states" for shots, e.g. "What state
is that shot in?" That can be things like lit, unlit, complete,
flashing, etc. You can also configure shows for each state (the unlit
state means the light is off, flashing means that the light is flashing,
etc.), and you can configure different scoring based on whether state
the shot is in (1,000 points if unlit, 5,000 if lit, etc.). All of this
is completely configurable.

You can also group multiple shots into "shot groups" and then do
certain things when all the shots in the group are in the same state.
For example, you could have three standup targets configured as three
separate shots that all start in the "unlit" state, but then once all
three shots are advanced to the "complete" state, you could add
100,000 points and start another mode.

Shots are also are integrated into MPF's modes system, so you can
configure a shot to do different things in different modes.

For example, a ramp shot might do nothing more than score 1,000 points
in your base mode, but when the multiball mode is running, that same
shot would score a jackpot. You can also configure whether notification
of a shot being hit is passed down from one mode to the lower priority
modes below it. (In the jackpot example we just mentioned, you probably
just want to score the million points for the jackpot if that shot is
made while the multiball mode is running and *not* score the 1,000
points for that shot from the base mode even though the base mode is
still running under the multiball mode.

It's important to understand, however, that in order to achieve these different results using the same shot, that you will need to define your shots on a "per mode" basis. Meaning, in the example above, you would define the ramp shot once in your base mode, and then you would define the same shot again (with a name distinct from the shot name used in the base mode) in your multiball mode. This is also important when you begin to apply shot profiles to your shots, as you'll likely want distinct profile behavior per mode you design as well.

## Example

This is an example of a shot in a mode:

``` yaml
#! switches:
#!   lane_l:
#!     number:
#! lights:
#!   lane_l:
#!     number:
##! mode: inlanes
shots:
  my_shot:
    switch: lane_l
    show_tokens:
      light: lane_l
```

The shot will use the default profile which has the states `unlit` and
`lit`. It will start `unlit` and go to `lit` after the first hit. The
first hit will post
[shot_my_shot_unlit_hit](../../events/shot_state_hit.md) and the second hit will post
[shot_my_shot_lit_hit](../../events/shot_state_hit.md). Those events are commonly used to trigger logic based on
the shot.

## Monitorable Properties

For
[dynamic values](../../config/instructions/dynamic_values.md) and
[conditional events](../../events/overview/conditional.md), the prefix for multiballs is `device.shots.(name)`.

### *state*

Index of the current state. Will start at 0 and increments when the shot advances.

### *state_name*

String representation of the state of the shot. Might be 'lit',
'unlit' or whatever is inside your shot_profile.

This is an example:

``` yaml
#! switches:
#!   lane_l:
#!     number:
#!   s_target:
#!     number:
#! lights:
#!   lane_l:
#!     number:
##! mode: inlanes
shots:
  my_shot:
    switch: lane_l
    show_tokens:
      light: lane_l
event_player:
  s_target_active{device.shots.my_shot.state_name=='lit'}: start_multiball
##! test
#! start_game
#! start_mode inlanes
#! mock_event start_multiball
#! hit_and_release_switch s_target
#! assert_event_not_called start_multiball
#! hit_and_release_switch lane_l
#! assert_event_not_called start_multiball
#! hit_and_release_switch s_target
#! assert_event_called start_multiball
```

In the example the event `start_multiball` will be posted when the
switch `s_target` is hit and the shot is in state `lit`.

## Related Events

* [(shot_name)_hit](../../events/shot_hit.md)
* [(shot_name)\_(profile)_hit](../../events/shot_profile_hit.md)
* [(shot_name)\_(profile)\_(state)_hit](../../events/shot_profile_state_hit.md)
* [(shot_name)\_(state)_hit](../../events/shot_state_hit.md)

## Related How To Guides

* [Tutorial step 18: Add your first shot](../../tutorial/18_shots.md)
* [Shots on inlane/outlanes](../../mechs/switches/rollover_switches.md)
* [Shots in game modes](../../cookbook/multiple_timed_shots.md)
* [Implement a Mode for Top Lanes with Multiplier and Scoring](../../cookbook/top_lanes_with_multiplier.md)
* [Shots in other modes](../../game_design/other_modes.md)
