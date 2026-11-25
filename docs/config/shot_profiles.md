---
title: "shot_profiles: Config Reference"
---

# shot_profiles: Config Reference

--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**YES** :white_check_mark:|

The `shot_profiles:` section of your config is where you configure the
settings for various *shot profiles* that you can then apply to your
[shots](shots.md), using the [*profile*](shots.md#profile) property.

Here's an example:

``` yaml
##! mode: mode1
shot_profiles:
  my_default_profile:
    states:
      - name: unlit
        show: "off"
      - name: lit
        show: "on"
```

This is actually the same as the default profile that all shots will use unless
another is explicitly set.

## \(name\):

This is the name of the shot profile, which is how you'll refer to it
elsewhere in your config files when you apply it to shots. The sample
shot_profiles: section of the config file above contains a profile named
"default" (which is actually included in the system-wide
`mpfconfig.yaml` file).

### advance_on_hit:

Single value, type: `boolean` (Yes/No or True/False). Default: `True`

This setting controls whether the active shot profile advances to its
next state when the shot is hit. The default is true, but you can set
this to false if you want to manually advance the shot some other way.
(If this is false, you can still advance the shot with *advance_events*,
for example.)

### block:

Single value, type: `boolean` (Yes/No or True/False). Default: `false`

Lets you control whether hits to a shot using this profile block hits
to other enabled shots sharing the same switch in lower-priority modes.
The default value is `false` if you don't specify this, meaning that
blocking is NOT enabled.

If you have `block: true` in a shot profile, then when a shot using
that profile is hit, it blocks lower-priority modes' shots on the same
switch from also registering a hit. If you set `block: false`, then the
hit will propagate down to enabled shots on that switch in lower-priority
modes. This will continue until it reaches a shot whose profile has
`block: true` or until it reaches the end of the mode list.

This is better explained with an example.

Imagine you have four top lanes which you use in your base mode in a
normal lane-change fashion (e.g., `base_lane_1` through `base_lane_4`,
using the default profile with `unlit` -> `lit` states). Now imagine you
also define separate shots in a skillshot mode using those same switches
(e.g., `skillshot_lane_1` through `skillshot_lane_4`, using a skillshot
profile with `flashing` -> `complete` states).

By default, if the player hits a lane while the skillshot mode is
running, the higher-priority skillshot gets the hit and blocks the
lower-priority base mode shot from registering it. If you add
`block: false` to your skillshot profile, then hitting the lane advances
the skillshot from `flashing` to `complete` *and* lets the hit propagate
down to the base mode shot, advancing it from `unlit` to `lit`. Both
*skillshot_lane_1_skillshot_flashing_hit* and
*base_lane_1_default_unlit_hit* events will be posted.


### loop:

Single value, type: `boolean` (Yes/No or True/False). Default: `False`

Controls whether the states of this profile "loop" when they reach the
end. If true, then the shot being hit when the profile is in the last
state causes the profile to "loop" around back to the first state.
This is useful if you want to create a "toggle" shot where you could
create a profile with two steps (lit and unlit) and then set loop to be
true. (If you have more than two steps in the shot profile, then the
looping will go from the last one back to the first one.) The default is
false, meaning when the profile reaches its last state, it will just
stay there even if it's hit again.

### player_variable:

Single value, type: `string`. Default: `None`

This is a profile setting that lets you specify the name of the player
variable that will be used to track the status of this shot when this
profile is applied. If you don't specify the name of a player variable,
it will automatically use *\(shot_name\)_\(profile_name\)* as the
player variable.

### rotation_pattern:

List of one (or more) values, each is a type: `string`. Default: `R`

This setting lets you specify a custom rotation pattern that's used
when an event from this profile's rotation_events: section is posted.
You enter it as a list of Ls and Rs, for example:

``` yaml
##! mode: mode1
shot_profiles:
  my_default_profile:
    states:
      - name: unlit
        show: "off"
      - name: red
        show: led_color
        show_tokens:
          color: red
      - name: blue
        show: "flash"
        show_tokens:
          color: blue
    rotation_pattern: L, L, L, L, R, R, R, R
```

In the above example, the first four times a rotation_event is posted,
this shot group will rotate to the left, then the next four to the
right, then the next four to the left, etc. The pattern will loop. This
is how you could specify a single lit target that "sweeps" back and
forth across a group of five targets, for example. This only impacts
*rotation_events*, not *rotate_left_events* and *rotate_right_events*
since those events imply a direction.

### show:

Single value, type: `string`. Default: `None`

The name of the show associated with this shot profile. Note that you
can specify a single show which applies to the entire shot profile
(here), or you can specify a different show for each step/state (in the
`states:` section, covered below.

If you specify a show here, then the show will not auto play, and
instead will advance to the next step with each step/state advancement
of the shot. This is useful for simple things like turning a light on or
off. For more complex scenarios, you can set a full show per step/state
below.

### show_when_disabled:

Single value, type: `boolean` (Yes/No or True/False). Default: `False`

Controls whether the lights or LEDs for shots which have this profile
applied will be active when this shot is disabled. By default this is
*False*, so when the shot is disabled, the show it was running will be
turned off, and thus the lights turned off. (Of course, the lights or
LEDs can still be controlled by other light scripts, light shows, manual
commands, etc.)

If you change this to *True*, and the shot profile associated with this
shot has a light turned on in its show, then when you disable the shot,
the light will stay lit.

### state_names_to_not_rotate:

List of one (or more) values, each is a type: `string`. Default: `None`

This is a list of state names that will be used to determine which shots
in a shot group will be rotated or skipped.
By default, no states are included, meaning all states will rotate.

This property can be useful if you only want to rotate a subset of states.
For example, you might have a set of standup targets defined as three shots
with three states, *unlit*, *on_target*, and *locked*.
During normal play you might have one of the targets marked as *on_target*\
at any time, with the others unlit, rotating which target is active based
on a timer or some gameplay event.
When the *on_target* shot is hit, you advance that target to *locked* and
set a new shot to be *on_target*. Using `state_names_to_not_rotate: locked`
you can keep the already-locked shots in place, and only rotate among the
remaining shots.

## states:

The `states:` section contains the following nested sub-settings

Under each shot profile name, a setting called *states:* lets you
specify various properties for the target in different states. You can
configure multiple states in the order that you want them to be stepped
through. (You use a dash, then a space, then a setting to indicate that
items should be a list. The following sections explain the settings for
each state:

### name:

Single value, type: `string`.

This is the name of the step. In other words, it's what "state" the
shot is in when this profile step is active.

### loops:

Single value, type: `integer`. Default: `-1`

Loops setting from the show player, controls how many times the show
loops (`-1` is unlimited).

### manual_advance:

Single value, type: `boolean` (Yes/No or True/False). Default: `False`

If True, the show does not automatically advance to the next step.

### priority:

Single value, type: `integer`. Default: `0`

The priority shift of the show that's played.

### show:

Single value, type: `string`. Default: `None`

The name of the show that will be played when a shot with this profile
applied is in this step (or state).

### show_tokens:

One or more sub-entries, each in the format of type: `str`:`str`.
Default: `None`

Show tokens for the show.

### speed:

Single value, type: `number` (will be converted to floating point).
Default: `1`

Playback speed of the show.

### start_step:

Single value, type: `integer`. Default: `1`

The step number the show will start on.

### sync_ms:

Single value, type: `integer`. Default: `None`

The sync_ms value of the show.

## Related How To guides

* [Shots](../game_logic/shots/index.md)
* [Shot Profiles](../game_logic/shots/shot_profiles.md)
