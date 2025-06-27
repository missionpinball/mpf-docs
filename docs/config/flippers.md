---
title: "flippers: Config Reference"
---

# flippers: Config Reference

--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

The `flippers:` section of your config contains all the settings for the
flippers in a pinball machine.

Here's an example from a *Judge Dredd* machine with four flippers.
(Note *Judge Dredd* technically has four flipper buttons too, but it's
the style where you push the button part way in to flip the lower
flipper, and all the way in to flip the upper flipper too. But as far as
the game code is concerned, it sees two separate switches in each
flipper button----one that's activated via the half-press, and the
second via the full press.)

Also note that flippers are kind of complex and there are a lot of
options. Read the [Flippers](../mechs/flippers/index.md)
tech note for details. (You should definitely read that first before
digging into the configuration options here.)

!!! note

    The `flippers:` section of the config is only used for controlled
    flippers in newer machines. Early solid-state (pre-WPC) machines used
    enable relays to enable the flippers, and those are configured
    elsewhere. (See the How To guides for details.)

``` yaml
#! switches:
#!   s_flipper_left:
#!     number:
#!   flipperLwL_EOS:
#!     number:
#!   s_flipper_right:
#!     number:
#!   flipperLwR_EOS:
#!     number:
#!   flipperUpL:
#!     number:
#!   flipperUpL_EOS:
#!     number:
#!   flipperUpR:
#!     number:
#!   flipperUpR_EOS:
#!     number:
#! coils:
#!   c_flipper_lower_left_main:
#!     number:
#!   c_flipper_lower_left_hold:
#!     number:
#!   c_flipper_lower_right_main:
#!     number:
#!   c_flipper_lower_right_hold:
#!     number:
#!   flipperUpLMain:
#!     number:
#!   flipperUpLHold:
#!     number:
#!   flipperUpRMain:
#!     number:
#!   flipperUpRHold:
#!     number:
flippers:
  lower_left:
    main_coil: c_flipper_lower_left_main
    hold_coil: c_flipper_lower_left_hold
    activation_switch: s_flipper_left
    eos_switch: flipperLwL_EOS
    label: Left Main Flipper
  lower_right:
    main_coil: c_flipper_lower_right_main
    hold_coil: c_flipper_lower_right_hold
    activation_switch: s_flipper_right
    eos_switch: flipperLwR_EOS
    label: Right Main Flipper
  upper_left:
    main_coil: flipperUpLMain
    hold_coil: flipperUpLHold
    activation_switch: flipperUpL
    eos_switch: flipperUpL_EOS
    label: Upper Left Flipper
  upper_right:
    main_coil: flipperUpRMain
    hold_coil: flipperUpRHold
    activation_switch: flipperUpR
    eos_switch: flipperUpR_EOS
    label: Upper Right Flipper
```

## Required settings

The following sections are required in the `flippers:` section of your
config:

### main_coil:

Single value, type: `string` name of a [coils:](coils.md) device. Defaults to empty.

The name of the main flipper coil. For flippers that only have
single-wound coils, this is where you specify that coil. In that case
you would also configure the lower-power hold option for this coil in
the [coils:](coils.md) section of your
config.

## Optional settings

The following sections are optional in the `flippers:` section of your
config. (If you don't include them, the default will be used).

### activation_switch:

Single value, type: `string` name of a
[switches:](switches.md) device. Defaults to
empty.

The switch that controls this flipper (i.e. the flipper button). This
setting is optional because you can also use `sw_flip_enable` below but
`activation_switch` is far more common and recommended instead.

### ball_search_hold_time:

Single value, type: `time string (ms)`
([Instructions for entering time strings](instructions/time_strings.md)). Default: `1s`

How long this flipper will be activated for when it is activated during
ball search.

### ball_search_order:

Single value, type: `integer`. Default: `100`

A relative value which controls the order individual devices are pulsed
when ball search is running. Lower numbers are checked first. See the
[Ball Search](../game_logic/ball_search/index.md)
documentation for details.

### disable_events:

List of one (or more) device control events
([Instructions for entering device control events](instructions/device_control_events.md)). Default: `ball_will_end, service_mode_entered`

(Note that if you add an entry here, it will replace the default. So if
you also want the default value(s) to apply, add them too.)

Disables this flipper (meaning pushing the flipper button doesn't
active the flipper).

### enable_events:

List of one (or more) device control events
([Instructions for entering device control events](instructions/device_control_events.md)). Default: `ball_started`

(Note that if you add an entry here, it will replace the default. So if
you also want the default value(s) to apply, add them too.)

Enables this flipper.

### eos_active_ms_before_repulse:

Single value, type: `time string (ms)`
([Instructions for entering time strings](instructions/time_strings.md)). Default: `500`

If you specify `repulse_on_eos_open` MPF will wait this many
milliseconds until issuing an EOS repulse. The rational for this is that
we do not want to stress the main coil too much. For instance if the
hold coil break we do not want to continuously pulse the coil.

### eos_switch:

Single value, type: `string` name of a
[switches:](switches.md) device. Defaults to
empty.

EOS switch on this flipper (if there is one).

### eos_switch_overwrite:

One or more sub-entries. Each in the format of `string` : `string`

One or more sub-entries, each in the format of `string` : `string` If
you're using an end of stroke switch with this flipper, enter the
switch name here.

### hold_coil:

Single value, type: `string` name of a [coils:](coils.md) device. Defaults to empty.

The name of the hold coil winding for dual-wound flipper coils.

### hold_coil_overwrite:

Single value, type:
[coil_overwrites:](coil_overwrites.md).
Defaults to empty.

Overwrites settings on the hold_coil. See
[coil_overwrites:](coil_overwrites.md) for details.

### include_in_ball_search:

Single value, type: `boolean` (`true`/`false`). Default: `false`

Controls whether this flipper is included in ball search.

Usually flippers aren't included in ball search. However if you have
upper flippers, it's probably good to include them in the ball search
since it's often possible for an upper flipper to disable and hold a
ball under the flipper. Usually this isn't an issue since the player
can just flip to release the ball. However if the machine has tilted (or
the flippers are otherwise disabled), then it's possible for a flipper
to come down on the ball and get it stuck. So you definitely want to
include upper flippers in ball search.

BTW, this is something that happened to us in *Wizard of Oz*, so that's
how we thought to include an option for flippers in ball search. :)

### main_coil_overwrite:

Single value, type:
[coil_overwrites:](coil_overwrites.md).
Defaults to empty.

Overwrites settings on the main_coil. See
[coil_overwrites:](coil_overwrites.md) for details.

### playfield:

Single value, type: `string` name of a
[playfields:](playfields.md) device. Default:
`playfield`

change this value if you have more than one playfield and you're
managing them separately.

### power_setting_name:

Single value, type: `string`. Defaults to empty.

A [machine setting](settings.md) to
use to adjust the (relative) power. It can be used to allow the operator
to adjust the power in service mode.

This is an example:

``` yaml
coils:
  c_flipper_main:
    number:
switches:
  s_flipper:
    number: 1
    tags: left_flipper
flippers:
  f_test_flippers_with_settings:
    main_coil: c_flipper_main
    power_setting_name: flipper_power
    activation_switch: s_flipper
```

MPF comes with a [setting](settings.md) called `flipper_power` by default and you can add additional
ones.

### repulse_on_eos_open:

Single value, type: `boolean` (`true`/`false`). Default: `false`

Whether MPF should repulse the main coil of the flipper when the EOS
reopens and the flipper buttons are still active. Not all platforms
support this in hardware. MPF might emulate this in software for
platforms which do not support this. Consult your platform manual if in
doubt.

### sw_flip_events:

List of one (or more) device control events
([Instructions for entering device control events](instructions/device_control_events.md)). Defaults to empty.

If the flipper is enabled this will flip the flipper from software. This
will usually have some delay and jitter so use with care. In almost all
cases it is prefered to use an `activation_switch` which will use
hardware rules internally to flip the flipper.

### sw_release_events:

List of one (or more) device control events
([Instructions for entering device control events](instructions/device_control_events.md)). Defaults to empty.

Disables a flipper from software. Use this together with
`sw_flip_events`.

### switch_overwrite:

One or more sub-entries. Each in the format of `string` : `string`

One or more sub-entries, each in the format of `string` : `string`
Overwrites settings on the activation_switch. See
[switch_overwrites:](switch_overwrites.md) for details.

### use_eos:

Single value, type: `boolean` (`true`/`false`). Default: `false`

Controls whether an EOS switch is used to disable the main winding or to
switch to lower-power pwm mode.

### console_log:

Single value, type: one of the following options: none, basic, full.
Default: `basic`

Log level for the console log for this device.

### debug:

Single value, type: `boolean` (`true`/`false`). Default: `false`

See the
[documentation on the debug setting](instructions/debug.md) for details.

### file_log:

Single value, type: one of the following options: none, basic, full.
Default: `basic`

Log level for the file log for this device.

### label:

Single value, type: `string`. Default: `%`

A descriptive name for this device which will show up in the service
menu and reports.

### tags:

List of one (or more) values, each is a type: `string`. Defaults to
empty.

Special / reserved tags for flippers: *None*

See the
[documentation on tags](instructions/tags.md) for details.

## Related How To guides

* [Flippers](../mechs/flippers/index.md)
