---
title: Recipe: Skillshot (with Auto-Rotate)
---

# Recipe: Skillshot (with Auto-Rotate)


This guide shows you how to build an MPF config for a skillshot with
automatically-rotating targets. When the player's turn starts the
target shots will rotate one "lit" shot rapidly, and when the ball is
plunged the rotation will stop and the lit shot will flash as the
skillshot target.

## Step 1. Create a skillshot mode and shots

Skillshots are a self-contained set of rules, so it's wise to create a
separate mode that can be started when a player's ball starts and ended
after the skillshot is hit (or missed).

``` mpf-config
#config_version=5
modes:
  - skillshot_with_auto_rotate
switches:
  s_dropbank_1:
    number: 1
  s_dropbank_2:
    number: 2
  s_dropbank_3:
    number: 3
  s_dropbank_4:
    number: 4
  s_dropbank_5:
    number: 5
lights:
  l_dropbank_1:
    number: 1
  l_dropbank_2:
    number: 2
  l_dropbank_3:
    number: 3
  l_dropbank_4:
    number: 4
  l_dropbank_5:
    number: 5

##! mode: skillshot_with_auto_rotate
# mode will be defined below
```

The first thing our mode needs is [shots:](../config/shots.md). Each possible target will be a shot (in this example,
we'll have five). Each shot has a switch, a light, and a shot profile
to track its state. The sample code below uses dropbank switches for the
skillshot, but you are free to use any switches you like.

Each shot will also have unique `advance_events` configured, which will
be explained in detail in section 4. What's important to note now is
that the first shot includes `advance_events: mode_skillshot_started` so
that this shot will automatically light when the mode starts, as the
first shot in the rotation.

``` mpf-config
#! switches:
#!   s_dropbank_1:
#!     number: 1
#!   s_dropbank_2:
#!     number: 2
#!   s_dropbank_3:
#!     number: 3
#!   s_dropbank_4:
#!     number: 4
#!   s_dropbank_5:
#!     number: 5
##! mode: skillshot_with_auto_rotate
#! shot_profiles:
#!   skillshot_profile:
#!     states:
#!       - name: off
mode:
  start_events: start_mode_skillshot_with_auto_rotate
  stop_events: stop_mode_skillshot_with_auto_rotate
  priority: 1000

shots:
  skillshot_drop_1:
    switch: s_dropbank_1
    advance_events: mode_skillshot_with_auto_rotate_started, advance_skillshot_1
    profile: skillshot_profile
    show_tokens:
      leds: l_dropbank_1
  skillshot_drop_2:
    switch: s_dropbank_2
    advance_events: advance_skillshot_2
    profile: skillshot_profile
    show_tokens:
      leds: l_dropbank_2
  skillshot_drop_3:
    switch: s_dropbank_3
    advance_events: advance_skillshot_3
    profile: skillshot_profile
    show_tokens:
      leds: l_dropbank_3
  skillshot_drop_4:
    switch: s_dropbank_4
    advance_events: advance_skillshot_4
    profile: skillshot_profile
    show_tokens:
      leds: l_dropbank_4
  skillshot_drop_5:
    switch: s_dropbank_5
    advance_events: advance_skillshot_5
    profile: skillshot_profile
    show_tokens:
      leds: l_dropbank_5
```

## Step 2. Create a profile for the targets

We can create a [shot profile](../config/shot_profiles) for the targets that starts with the light off, lights it
solid after one advancement, and makes it flash after a second
advancement. By default, a shot will advance its profile when the shot
is hit, but we don't want that here so we'll set
`advance_on_hit: false`.

When the mode starts, all shots will be in the first profile state
"off". The first shot will immediately advance to the "on" state
(from the `advance_events: mode_skillshot_with_auto_rotate_started`
noted above). Every time the shot group rotates, the next shot in
sequence will shift to "on". This creates the rotation effect of the
lit shot moving across the targets.

When the ball is plunged, whichever shot is in the "on" state will be
advanced to the "lit" state and its light will flash. When any shot is
hit, we'll check whether it is "lit" or not to know whether the
skillshot should be awarded.

``` mpf-config
##! mode: skillshot_with_auto_rotate
shot_profiles:
  skillshot_profile:
    advance_on_hit: false
    states:
      - name: off
        show: off
      - name: on
        show: on
      - name: lit
        show: flash
```

## Step 3. Create a shot_group for the lanes, and a rotation timer

To tell MPF that the five shots are related to each other, we create a
[shot group](../config/shot_groups.md) with all
the shots in it.

Shot groups are powerful because they control behavior of all the shots
together. In this case, we'll use our shot group control the rotation
of the shots, and a [timer](../config/timers.md) to trigger a rotation every half-second.

``` mpf-config
#! switches:
#!   s_dropbank_1:
#!     number: 1
#!   s_dropbank_2:
#!     number: 2
#!   s_dropbank_3:
#!     number: 3
#!   s_dropbank_4:
#!     number: 4
#!   s_dropbank_5:
#!     number: 5
##! mode: skillshot_with_auto_rotate
#! shots:
#!   skillshot_drop_1:
#!     switch: s_dropbank_1
#!   skillshot_drop_2:
#!     switch: s_dropbank_2
#!   skillshot_drop_3:
#!     switch: s_dropbank_3
#!   skillshot_drop_4:
#!     switch: s_dropbank_4
#!   skillshot_drop_5:
#!     switch: s_dropbank_5

shot_groups:
  skillshot:
    shots:
      - skillshot_drop_1
      - skillshot_drop_2
      - skillshot_drop_3
      - skillshot_drop_4
      - skillshot_drop_5
    rotate_events: timer_skillshot_rotate_tick

timers:
  skillshot_rotate:
    tick_interval: 500ms
    start_running: true
    control_events:
      - event: s_plunger_lane_inactive
        action: stop
```

The `rotate_events` will move the state of the shots each time the timer
ticks, and the ball leaving the plunger lane will stop the timer and
thus stop the rotation.

## Step 4. Flash the lit shot when the rotation stops

When the timer stops, one of the shots will be in the "on" state.
Whichever shot this is should be advanced to the "lit" state so the
light is flashing, and we can use conditional events to listen for the
timer stop and advance *only* the lit shot.

Shot profile states are numbered starting with zero, so our "off"
state is number 0 and the "on" state is number 1. The following code
will only post the advance event for a shot if that shot is in state
number 1, a.k.a. "on".

``` mpf-config
##! mode: skillshot_with_auto_rotate
event_player:
  timer_skillshot_rotate_stopped:
    - advance_skillshot_1{device.shots.skillshot_drop_1.state==1}
    - advance_skillshot_2{device.shots.skillshot_drop_2.state==1}
    - advance_skillshot_3{device.shots.skillshot_drop_3.state==1}
    - advance_skillshot_4{device.shots.skillshot_drop_4.state==1}
    - advance_skillshot_5{device.shots.skillshot_drop_5.state==1}
```

Each shot configured in step 1 above has `advance_events` that
correspond to its shot number, so the above event player will trigger
the correct shot to advance to its "lit" state.

## Step 5. Rewards for skillshot

When the player hits the lit shot, they get an award of points. We can
use the [variable_player:](../config/variable_player.md) for
this.

When a shot in a shot group is hit, the shot group will post an event
with the state name of the shot that was hit. This way, we can check
when *any* shot is hit rather than having to check each shot
individually.

``` mpf-config
##! mode: skillshot_with_auto_rotate
variable_player:
  skillshot_lit_hit:
    score: 20_000
```

## Step 6. End the mode on skillshot hit, or any other hit

After any skillshot shot is hit, the skillshot mode should end. We can
again use the shot group to detect *any* shot being hit, but we'll use
a hit event *without* a state name because it doesn't matter whether
the shot was lit or not.

We also want to end the skillshot mode if any other switch on the
playfield was hit, which we can detect from the *playfield_active*
event. However, when the skillshot is hit the *playfield_active* event
will post before the *skillshot_lit_hit* event, so if we end the mode
immediately then no score will be awarded. Instead, we add a 1 second
delay after playfield activation before ending the mode.

``` mpf-config
##! mode: skillshot_with_auto_rotate
event_player:
  # Add these lines after timer_skillshot_rotate_stopped (defined above)
  skillshot_hit: stop_mode_skillshot
  playfield_active: stop_mode_skillshot|1s
```

## Full Example Code

The full code from this example can be found as a fully-working game
template in the MPF Examples repository.

<https://github.com/missionpinball/mpf-examples/tree/dev/cookbook/skillshot_with_auto_rotate>

## Related Docs

* [shots:](../config/shots.md)
* [shot_groups:](../config/shot_groups.md)
* [shot_profiles:](../config/shot_profiles.md)
* [timers:](../config/timers.md)
* [variable_player:](../config/variable_player.md)
