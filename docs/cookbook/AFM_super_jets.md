---
title: Recipe: Attack From Mars Super Jets
---

# Recipe: Attack From Mars Super Jets


This guide shows you how to build an MPF config for *Attack From Mar's*
Super Jets feature. The idea is you can use this as a guide to implement
a similar feature in your machine.

!!! note

    This recipe requires MPF 0.33 or newer.

This guide uses the following concepts in MPF that you should be
familiar with:

* [Modes](../game_logic/modes/index.md)
* [Counter Logic Blocks](../game_logic/logic_blocks/counters.md)
* [Shows](../shows/index.md)

You can find the complete runnable machine config for this recipe in the
`cookbook/AFM_super_jets` folder of the [mpf-examples
repository](https://github.com/missionpinball/mpf-examples) on GitHub.

## What is a Super Jets mode?

In Attack From Mars, Super Jets occur when the player hits the jet
bumpers in the top right of the playfield 100 times in the course of a
game. The effect of Super Jets is that once the mode is active, each jet
bumper hit is worth 3,000,000 points instead of 1,000,000. The mode
stops when the ball drains, but once achieving it, it only takes 25 more
jet bumper hits to restart it.

Here are the specific rules we need to implement:

**Super Jets**

* Jet Bumper hits are initially 1,000,000 per hit.
* Each completion of the two inlanes above the jet bumpers add 50,000
    to each jet bumper hit (1,050,000, 1,100,000, and so on.)
* Lit inlanes are movable with the flippers.
* One the inlane value reaches 2,000,000 per it, the inlanes stop
    adding 50,000 when completed.
* Super Pops occur when 100 jet bumper hits occue in the game. The
    amount of hits carry over to the next ball.
* Once the Super Pops mode has been made, the mode is active until the
    ball drains.
* Super Pops can be restarted by hitting the jet bumpers 25 more
    times.
* Once Super Pops have been made, the Super Pops insert on the
    playfield turns on and stays on.

## Step 1. The machine-wide prerequisites

Before we dig into how to handle the mode itself, we need to create a
machine-wide config that has all the devices we'll need, including the
switches for the jet bumpers and lanes.

Here's what our machine config looks like. (Note that this is complete
in terms of what we need to make this recipe work, but if you have a
real Attack From Mars then you'll probably have a lot more than this in
your machine config file. Also, the coil, switch, and light numbers are
generic and need to be changes for a real machine.)

Notice the "player_vars" section. It has a player variable named
"sj_active". We will explain this later on, but for now we'll just
say that it is how we will tell if we are starting Super Jets for the
first time or resuming it after starting it but draining.

``` yaml
#config_version=5

player_vars:
  sj_active:
    value_type: int
    initial_value: 0

modes:
  - super_jets_setup
  - super_jets

switches:
  s_left_flipper:
    number: 0
    tags: left_flipper
  s_right_flipper:
    number: 71
    tags: right_flipper
  s_credit:
    number: 6
    tags: start
  s_outhole:
    number: 8
    tags:
  s_left_bumper:
    number: 17
    tags:  jets
  s_middle_bumper:
    number: 18
    tags: jets
  s_right_bumper:
    number: 19
    tags: jets
  s_right_rollover:
    number: 22
    tags: playfield_active, right_rollover
  s_left_rollover:
    number: 23
    tags: playfield_active, left_rollover
  s_trough_5:
    number: 36
    tags:
  s_trough_4:
    number: 37
    tags:
  s_trough_3:
    number: 38
    tags:
  s_trough_2:
    number: 39
    tags:
  s_trough_1:
    number: 40
    tags:

virtual_platform_start_active_switches: s_trough_1 s_trough_2 s_trough_3 s_trough_4 s_trough_5

coils:
 c_flipper_left_main:
   number: 0
   default_pulse_ms: 20
 c_flipper_left_hold:
   number: 1
   allow_enable: true
 c_flipper_right_main:
   number: 2
   default_pulse_ms: 20
 c_flipper_right_hold:
   number: 3
   allow_enable: true
 c_trough_eject:
   number: 4
   allow_enable: true
 c_left_bumper:
   number: c01
   label:
   tags:
   default_pulse_ms: 25
 c_middle_bumper:
   number: c02
   label:
   tags:
   default_pulse_ms: 25
 c_right_bumper:
   number: c03
   label:
   tags:
   default_pulse_ms: 25
 c_ball_eject:
   number: c12
   label:
   tags:
   default_pulse_ms: 20
 c_outhole:
   number: c14
   label:
   tags:
   default_pulse_ms: 20

lights:
  l_right_rollover:
    number: 5
  l_left_rollover:
    number: 7
  l_super_jets:
    number: 9

ball_devices:
  bd_drain:
    ball_switches: s_outhole
    eject_coil: c_outhole
    eject_targets: bd_trough
    tags: drain, outhole
  bd_trough:
    ball_switches: s_trough_1, s_trough_2, s_trough_3, s_trough_4, s_trough_5
    eject_coil: c_ball_eject
    tags: trough, home

  autofire_coils:
    left_jet:
     coil: c_left_bumper
     switch: s_left_bumper
   mid_jet:
     coil: c_middle_bumper
     switch: s_middle_bumper
   right_jet:
     coil: c_right_bumper
     switch: s_right_bumper

playfields:
    playfield:
        default_source_device: bd_trough
        tags: default

##! mode: super_jets_setup
# mode will be defined below
##! mode: super_jets
# mode will be defined below
```

## Step 2. Add Super Jets values

We'll start off with the easier mode first as all the heavy lifting is
handled by the setup mode for Super Jets. In super_jets.yaml, we set up
our starting events for the mode itself, the values of the jet bumpers
when Super Jets are active, and also a call to show a slide stating that
Super Jets are active.

``` mpf-config
##! mode: super_jets
mode:
  start_events: Super_Jets_Go, Super_Jets_Resume_Go
  priority: 300
variable_player:
  s_left_bumper_active:
    score: 3000000|block
  s_middle_bumper_active:
    score: 3000000|block
  s_right_bumper_active:
    score: 3000000|block


show_player:
  mode_super_jets_started:
    super_jets_startup:
      loops: 0
    Super_Jets_on:
      show_tokens:
        lights: l_super_jets
```

Stepping through how we're using each setting:

``` yaml
start_events: Super_Jets_Go, Super_Jets_Resume_Go
```

The way the super_jets mode is called is if either "Super_Jets_Go" or
"Super_Jets_Resume_Go" are posted.

``` yaml
s_left_bumper_active:
  score: 3000000|block
```

Everytime "s_left_bumper_active" is seen, the score has 3,000,000
points added onto it. The [\|block](#) is used to prevent any
other instances that awards points for hitting "s_left_bumper_active"
from adding points as well.

This code is used for all three jets.

``` yaml
show_player:
  mode_super_jets_started:
    super_jets_startup:
      loops: 0
```

The Show Player shows the slide names "super_jets_started" at the
start of the mode. The settings in super_jets_started.yaml dictate the
size, font, and duration of the slide being used.

``` yaml
Super_Jets_on:
  show_tokens:
    lights: l_super_jets
```

Plays the show called "Super_Jets_on" when this mode starts, lighting
the Super Jets light on the playfield.

## Step 3. Create an setup mode for Super Jets

Next we need to create a mode called "super_jets_setup" to control
when to call the "super_jets" mode. There's lot going on here, but
we'll go through it step by step.

``` yaml
##! mode: super_jets_startup
#config_version=5

    mode:
      start_events: ball_starting
      priority: 200

    shots:
      jets:
        switch: s_right_bumper, s_left_bumper, s_middle_bumper
      right_rollover:
        switch: s_right_rollover
        show_tokens:
          light: l_right_rollover
      left_rollover:
        switch: s_left_rollover
        show_tokens:
          light: l_left_rollover

    shot_groups:
      rollover_lanes:
        shots: right_rollover, left_rollover
        rotate_left_events: s_left_flipper_active
        rotate_right_events: s_right_flipper_active
        reset_events:
          rollover_lanes_lit_complete: 1s

    counters:
      lb_jets_count:
        count_events: jets_hit
        starting_count: 0
        count_complete_value: 100
        count_interval: 1
        direction: up
        persist_state: true
        events_when_complete: Super_Jets_Go
        debug: true
      lb_jets_resume:
        enable_events: mode_base_started{current_player.sj_active>0}
        count_events: jets_hit
        starting_count: 0
        count_complete_value: 25
        count_interval: 1
        direction: up
        persist_state: false
        events_when_complete: Super_Jets_Resume_Go
        debug: true
        reset_on_complete: true
      lb_rollover_complete_count:
        count_events: rollover_lanes_complete
        events_when_hit: rollover_lanes_done
        starting_count: 0
        count_complete_value: 40
        reset_on_complete: false
        direction: up
        persist_state: false

    event_player:
      Super_Jets_Go:
        start_mode_super_jets
      Super_Jets_Go_Again:
       start_mode_super_jets

    variable_player:
      s_left_bumper_active:
        score: 1000000 + (device.counters.lb_rollover_complete_count.value * 50000)
      s_middle_bumper_active:
        score: 1000000 + (device.counters.lb_rollover_complete_count.value * 50000)
      s_right_bumper_active:
        score: 1000000 + (device.counters.lb_rollover_complete_count.value * 50000)
      rollover_lanes_complete:
        score: 1000
      mode_super_jets_started:
        sj_active:
          int: 1
          action: set

   show_player:
     mode_super_jets_setup_started{current_player.sj_active>0}:
       Super_Jets_on:
         show_tokens:
           lights: l_super_jets
```

Let's look at each of these settings:

``` yaml
start_events: ball_starting
```

Here, we are saying that we want "super_jets_setup" to start as soon
as the game starts a ball, including extra balls.

``` yaml
shots:
  jets:
    switch: s_right_bumper, s_left_bumper, s_middle_bumper
  right_rollover:
    switch: s_right_rollover
    show_tokens:
      light: l_right_rollover
  left_rollover:
    switch: s_left_rollover
    show_tokens:
      light: l_left_rollover
```

This section establishes our shots. Any time "s_right_bumper",
"s_left_bumper", or "s_middle_bumper" is activated, the shot "jet"
will register a hit.

"right_rollover" and "left_rollover" will show a hit any time their
associated switch is made. Also, when their shots are made, their
corresponding insert will also light up because we have a
"show_tokens" section listing a light.

``` yaml
shot_groups:
  rollover_lanes:
    shots: right_rollover, left_rollover
    rotate_left_events: s_left_flipper_active
    rotate_right_events: s_right_flipper_active
    reset_events:
      rollover_lanes_lit_complete: 1s
```

This section is to set up the behavior of our rollover lanes. First, we
list our shots, "right_rollover" and "left_rollover". Then we
designate our left flipper as a switch to rotate our shots left, and the
right flipper to rotate the shots right. This is how we can use the
flippers to move a lit rollover to the other lane to try and get the
ball to go into an unlit rollover lane and complete the rollovers.
"reset_events" is used to pause the shot group for 1 second as the
rollover lanes are reset so they are both off again.

``` yaml
counters:
  lb_jets_count:
    count_events: jets_hit
    starting_count: 0
    count_complete_value: 100
    count_interval: 1
    direction: up
    persist_state: true
    events_when_complete: Super_Jets_Go
    debug: true
  lb_jets_resume:
    enable_events: mode_base_started{current_player.sj_active>0}
    count_events: jets_hit
    starting_count: 0
    count_complete_value: 25
    count_interval: 1
    direction: up
    persist_state: false
    events_when_complete: Super_Jets_Resume_Go
    debug: true
    reset_on_complete: true
  lb_rollover_complete_count:
    count_events: rollover_lanes_complete
    events_when_hit: rollover_lanes_done
    starting_count: 0
    count_complete_value: 40
    reset_on_complete: false
    direction: up
    persist_state: false
```

This is the heart of the mode. There are three counters here to help
control the program.

"lb_jets_count" is the main counter. It is set up to increment from 0
to 100 every time the jets shot registers a hit, which is set up to
include all the jet bumpers. By using "persist_state: true" we have
the program not reset the count to 0 if the ball drains. If it takes all
3 balls for the player to hit 100 hits, they can still get Super Jets to
start. When the counter hits 100, it causes the event "Super_Jets_Go"
to post, and the event player later in the code handles what needs to be
done now that it has posted.

"lb_jets_resume" is a similar counter, but it has a few very important
differences. First, it has an "enable_events" requirement. If
"sj_active" is not greater than 0, this counter will not run. That
means that the previous counter, "lb_jets_count", had to start the
super_jets mode first, and that the variavle "sj_active" has to
somehow be set to greater than 0. When it is active, the counter counts
up from 0 to 25. At 25, the counter stops and posts the
"Super_Jets_Resume_Go" event. Another important difference is that we
use "persist_state: false" to reset the counter on every ball. For
example, a player can't get 12 hits in the jets, drain, and then expect
Super Jets to start by hitting the jets just 13 more times. It has to be
25 without draining.

The final counter is for the rollover lanes,
"lb_rollover_complete_count". We use this to track how many times the
rollovers are comeplete, form 0 to 40. We use 40, because 50,000 \* 40 =
2,000,000 which is the maximum addition of points we can add to the jets
if not in Super Jets mode. By using "persist_state: false" we reset
the count on the end of every ball back to 0.

``` yaml
event_player:
  Super_Jets_Go:
    start_mode_super_jets
  Super_Jets_Go_Again:
    start_mode_super_jets
```

Here is where we call our modes depending on what events are posted by
the mode. Both events, "Super_Jets_Go" and "Super_Jets_Resume_Go"
call the same mode to start, "super_jets", but because we have two
different counters calling the mode under different conditions, we have
to set it up like this.

``` yaml
variable_player:
  s_left_bumper_active:
    score: 1000000 + (device.counters.lb_rollover_complete_count.value * 50000)
  s_middle_bumper_active:
    score: 1000000 + (device.counters.lb_rollover_complete_count.value * 50000)
  s_right_bumper_active:
    score: 1000000 + (device.counters.lb_rollover_complete_count.value * 50000)
  rollover_lanes_complete:
    score: 1000
  mode_super_jets_started:
    sj_active:
      int: 1
      action: set
```

This is how the scoring is handled before Super Pops is active. Each jet
bumper hit is worth 1,000,000 at the start. But, we also have to add
50,000 points for each time the rollovers are completed. To do that, we
take the value of the counter, "lb_rollover_complete_count" and
multiply it by 50000. Then we add that value to the standard 1,000,000.
Remember in "super_jets" that we added [\|block](#) to the
end of the scoring? That was in part to keep these lines from continuing
to add to the score, and to just have the scoring from
"super_jets.yaml" to appear.

We also have a small score for when the rollover lanes are completed.

What is "sj_active"? This is a player variable set up previously to
help with determining when to use which counter to activate super jets.
Initially, the game sets "sj_active" to an integer value of 0. But,
when Super Pops are activated by "lb_jets_count" because we hit the
target of 100 hit, the variable player sets "sj_active" to an integer
of 1 as the mode starts. Now, if the ball drains, and a new ball is
launched, "lb_jets_resume" will be enabled to start counting, and
because its count ends at 25 instead of 100, it will call super_jets
before "lb_jets_count". "sj_active" will also stay at a value of 1
because every time the super_jets mode is called, we set "sj_active"
is set to 1.

``` yaml
show_player:
  mode_super_jets_setup_started{current_player.sj_active>0}:
    Super_Jets_on:
      show_tokens:
        lights: l_super_jets
```

When "sj_active" has been set to 1, it is greater than 0. Now, the
light for Super Jets will stay on from now on whenever a ball starts,
and the super_jets_setup mode starts.

## Step 4. Set up your Super Jets Slide

Here we set up a quick slide that pops up on the DMD when we've started
Super Pops.

``` yaml
##! mode: super_jets_startup
    - duration: 2s
    slides:
      super_jets_startup:
        widgets:
        - type: text
          text: SUPER JETS
          font_size: 20
          y: 60%
          priority: 200
```

## Step 5. Add the light for Super Jets

And finally, we set up a lightshow for turning on the Super Jets insert
on the playfield.

``` yaml
##! mode: Super_Jets_on
    - time: 0
    lights:
      l_super_jets: ff
```

At this point you should have a working Super Pop mode. If any of this
feels unclear or I've muddied up the explanation, feel free to join the
discussion in the forums at
<https://groups.google.com/forum/#!topic/mpf-users/oVwBRQOgodY> .
