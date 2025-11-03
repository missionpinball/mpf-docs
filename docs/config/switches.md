---
title: "switches: Config Reference"
---

# switches: Config Reference

--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

The *switches:* section of the config files is used to map switch names
to controller board inputs. You can map both direct and matrix switches.
Here's an example section:

``` yaml
switches:
  flipper_lwr_eos:
    number: SF1
  flipper_lwr:
    number: SF6
  fire_r:
    number: S12
    tags: plunger
  start:
    number: S13
    tags: start
  plumbbob:
    number: S14
    tags: tilt
  outlane_l:
    number: S16
    tags: playfield_active
    debounce: normal
  inlane_l:
    number: S17
    tags: playfield_active
    debounce: quick
  trough1:
    number: S81
    type: 'NC'
  shooter_lane:
    number: S82
    events_when_activated: ball_in
    events_when_deactivated: ball_out
```

Each subsection of `switches:` is a switch name, which is how you refer
to the switch in your game code. A fully working example for the Cobra
board can be found in
[OPP Switches](../hardware/opp/switches.md),
that example might be as well helpful when using other hardware to
understand what events are being fired when using a switch.

When configuring switches, then there are several parameters for each
switch:

## Required settings

The following sections are required in the `switches:` section of your
config:

### number:

Single value, type: `string`. Defaults to empty.

This is the number of the switch which specifies which switch input the
switch is physically connected to. The exact format used here will
depend on which control system you're using and how the switch is
connected.

Note: In a virtual environment with [keyboard:](keyboard.md) section you don't have to fill in a switch number. With a
keyboard section the switch is activated by a defined keyboards key.

See the [How to configure "number:" settings](../hardware/numbers.md) guide for
details.

## Optional settings

The following sections are optional in the `switches:` section of your
config. (If you don't include them, the default will be used).

### debounce:

Single value, type: one of the following options: auto, quick, normal.
Default: `auto`

The debounce setting to use in hardware. `quick` means very low to no
debounce (could also be named "off"). `normal` implies debounce "on"
and should be used in most cases. The exact timings of those settings
depend on your hardware platform. (`quick` usually is 0-1ms, `normal` is
1-4ms).

The main purpose of this is to reduce the number of events/amount of
communication from the hardware. For targets and swiches in debounce
`normal` should be good in almost all cases.

However, in some cases, you want to disable debounce (e.g. use `quick`)
when using [hardware rules](autofire_coils.md) such as pop bumpers or sling shots. `auto` will use `normal`
if no hardware rules are configured or `quick` when rules are
configured. Therefore, you usually can leave this at `auto`.

Switch debouncing is somewhat different from debouncing in other domains
since the switch has to be active for the whole period of debouncing (at
least during sampling). It could also be referred as "minimum
activation time" (as one discipline of debouncing). If you want to make
sure that the switch does not activate again within a certain period
have a look at `ignore_window_ms` (another discipline of debouncing). If
you want to control the fire rate of your
[coil](coils.md) have a look at the
`recycle` setting (configurable in some platforms).

See [Debouncing in Pinball Machines](../mechs/switches/debounce.md) for
details.

### events_when_activated:

List of one (or more) events. Those will be posted by the device.
Defaults to empty.

A list of one or more names of events that MPF will post when this
switch goes active. These events are posted exactly as they're entered,
in addition to the events that are posted based on the switch's tags.
See as well the `tags` section below. In addition, an event will be
posted based on the switch name, `<switch name>_active`.

The events will only be visible in the `mpf monitor` if they are
consumed by something, e.g. `light_player` or if `debug:true` is defined
for them. They will be posted regardless of the `debug` setting, it is
only a question of visibility in the `mpf monitor`.

### events_when_deactivated:

List of one (or more) events. Those will be posted by the device.
Defaults to empty.

A list of one or more names of events that MPF will post when this
switch goes inactive. These events are posted exactly as they're
entered, in addition to the events that are posted based on the
switch's tags. See as well the `tags` section below. In addition, an
event will be posted based on the switch name, `<switch name>_inactive`.

The events will only be visible in the `mpf monitor` if they are
consumed by something, e.g. `light_player` or if `debug:true` is defined
for them. They will be posted regardless of the `debug` setting, it is
only a question of visibility in the `mpf monitor`.

### ignore_window_ms:

Single value, type: `time string (ms)`
([Instructions for entering time strings](instructions/time_strings.md)). Default: `0`

Specifies a duration of time during which additional switch activations
will be ignored.

For example, if you set `ignore_window_ms: 100`, then a switch is
activated once, then again 50ms later, the second activation will be
ignored. The timer is set based on the last switch hit that *activated*
the switch, so if another switch hit came in 105ms after the first
(which would be 55ms after the second), it will also count.

### ignore_during_ball_search:

Single value, type: `boolean` (`true`/`false`). Default: `false`

Specifies whether this switch should be ignored during [Ball Search](../game_logic/ball_search/index.md).
Keep in mind that this works together with the `playfield_active` tag.

So just a practical example. If you set this value to `true`, Ball Search will ignore the switch's active state and will continue on searching.
USE WITH CAUTION!
Setting this value to `true` will cause the switch to be completely ignored by the Ball Search, meaning it won't reset the Ball Search timer when hit.
This behavior can start unwanted Ball Searches.

You can find further info here on [How to configure Ball Search](../game_logic/ball_search/configuring_ball_search.md).

### platform:

Single value, type: `string`. Defaults to empty.

Name of the platform this switch is connected to. The default value of
`None` means the default hardware platform will be used. You only need
to change this if you have multiple different hardware platforms in use
and this switch is not connected to the default platform.

See the [Mixing-and-Matching hardware platforms](../hardware/platform.md) guide for
details.

### platform_settings:

Single value, type: `dict`. Defaults to empty.

Dict of platform specific settings. See your
[platform documentation](../hardware/index.md)
about this.

### type:

Single value, type: one of the following options: NC, NO. Default: `NO`

You can add `NC` as a type (like `type: NC`) to indicate that this
switch is a normally closed switch, i.e. it's closed when it's
inactive and open when it's active. This is mostly used for optos.

Switches which are type NC are automatically inverted by the Switch
Controller. In other words an NC switch is still "active" when it's
being activated, but the Switch Controller knows that activation
actually occurs when the switch opens, rather than closes. Setting the
type to NC here means that you never have to worry about this inversion
anywhere else in your game code.

### x:

Single value, type: `number` (will be converted to floating point).
Defaults to empty.

X Position of this switch on the playfield. Currently unused.

### y:

Single value, type: `number` (will be converted to floating point).
Defaults to empty.

Y Position of this switch on the playfield. Currently unused.

### z:

Single value, type: `number` (will be converted to floating point).
Defaults to empty.

Z Position of this switch on the playfield. Currently unused.

### console_log:

Single value, type: one of the following options: none, basic, full.
Default: `basic`

Log level for the console log for this device.

### debug:

Single value, type: `boolean` (`true`/`false`). Default: `false`

Set this to true to get additional debug output. You need to set this
flag to see event you have defined for this switch in mpf monitor.

### file_log:

Single value, type: one of the following options: none, basic, full.
Default: `basic`

Log level for the file log for this device.

### label:

Single value, type: `string`. Default: `%`

Name of this switch in service mode.

### tags:

List of one (or more) values, each is a type: `string`. Defaults to
empty.

You can add tags to switches to logically group them in your game code
to make it easier to do things. (Like "if all the switches tagged with
`droptarget_bank1` are active, then do something.") Tags are also used
to create MPF events which are automatically posted with an `sw_`
prefix, by tag, when a switch is activated. For example, if you have a
switch tagged with "hello", then every time that switch is activated,
it will post the event `sw_hello`. If you have a switch tagged with
"hello" and "yo", then every time that switch is activated it will
post the events `sw_hello` and `sw_yo`. MPF also makes use of several
tags on its own.

In addition, events will be posted based on the switch name,
`<switch name>_active` and `<switch name>_inactive`.

The events will only be visible in the `mpf monitor` if they are
consumed by something, e.g. `light_player` or if `debug:true` is defined
for them. They will be posted regardless of the `debug` setting, it is
only a question of visibility in the `mpf monitor`.

#### Built-in Tags

Special-purpose tags for switches include:

* `playfield_active` - This tag should be used for all switches on the
    playfield that indicate a ball is loose on the playfield. This tag
    is used by the playfield to know that balls are on it. Note that if
    you have more than one playfield, the tag name is
    (playfield_name)\_active, so if you have a playfield called "upper
    playfield", you'd tag the switches on that playfield with
    "upper_playfield_active". Many devices (such as slingshots and VUKs) will
    manage this behavior for you and will generate error "CFE-ball_device-13"
    if you have this tag when you should not. Removing the tag will fix the error.
    See: [Ball Search](../game_logic/ball_search/configuring_ball_search.md)
* `start` - Lets MPF know that this switch is used to start a game.
    (Note that in MPF, the game start process is kicked off when this
    switch is released, not pressed, which allows the "time held down"
    to be sent to MPF to perform alternate game start actions.) See: [Start Button](../tutorial/9_start_button.md).
    With MPF 0.80, the `start` tag is used by the high_score mode to select a letter or submit the name text.
* `left_flipper` and `right_flipper` - MPF will provide automatic [flipper_cradle](../events/flipper_cradle.md)
    and [flipper_cancel](../events/flipper_cancel.md) events if your cabinet flipper buttons are tagged with
    their respective flippers. With MPF 0.80, the built-in high_score mode and slide hook onto these two flipper tags
    to control character selection and submission.
* `no_audit` and `no_audit_free` - The MPF switch auditor will not create audits for switches using these tags.
    The `no_audit` will exclude the switch in all cases, and `no_audit_free` will only exclude the switch while in free play.

#### Tags for optional built-in modes

Some of the default modes included with MPF include switch tag hooks so that it is easy for you to incorporate features into your game.

##### Tilt Mode

MPF's default tilt mode supports both slam tilt and plumb-bob tilt detection, either or both tags may be used.
See: [Tilt](../game_logic/tilt/index.md)

* `tilt_warning` - This is added to a plumb-bob style tilt switch.
* `slam_tilt` - This is added to a slam tilt type switch. 

##### High Score Mode

(*tag support new in MPF 0.80*)

The built-in [high_score mode](../game_logic/high_scores/index.md) in MPF 0.80 and high_score slide in GMC allow players
to select letters and submit their high score via use of an [MPFTextInput](../gmc/reference/mpf-text-input.md) in Godot.

* `left_flipper` and `right_flipper` - These tags are reused by the high score text input to move
    the highlighted item left or right
* `start` - The start tag is reused by the high score mode to select the highlighted item

##### Service Mode

The Service Mode code included with MPF is intended for four-button service doors
and has support for coin door detection and other features. The way this works is
through a variety of tags, including the re-use of some existing tags.
See: [Service Mode](../game_logic/service_mode.md)

* `service_esc`, `service_down`, `service_up`, and `service_enter` - When using the builtin
    Service Mode, you will want to tag four different switches with these tags so the
    operator can use the interface without keyboard or mouse access.
* `service_door_open` or `service_door_closed` - Service mode will hook into
    the open or closed detection behavior of your coin door switch if you include
    one of these tags. Only one is necessary, but both are available depending on
    whether your switch is normally open or normally closed.
* `start`, `left_flipper`, and `right_flipper` - Service mode will reuse these three tags
    that you likely already had defined for other machine features. (See section above.)


## Monitorable Properties

For
[dynamic values](instructions/dynamic_values.md) and
[conditional events](../events/overview/conditional.md), the syntax for switches is `device.switches.(name).state`.
Though uncommon, it is possible to query the current state of a switch in this way.

## Related How To guides

* [Switches](../mechs/switches/index.md)
* [How to configure opto switches](../mechs/switches/optos.md)
* [Mechanical Switches](../mechs/switches/mechanical_switches.md)
