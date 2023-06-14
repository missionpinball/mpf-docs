---
title: "digital_outputs:"
---

# digital_outputs:


--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

The `digital_outputs:` section of your config is where you configure
digital outputs. Those can be either mapped to a light or a driver and
support only enabling and diabling. In contrast to a light,
`digital_outputs` do not support any fading or pwm/brightness. Opposed
to drivers, `digital_outputs` do not support pulsing, pattern or
hardware rules. Use them to control digital logic. MPF uses them to
control [motors](motors.md) with
additional control logic.

Some platforms such as Stern Spike, Gottlieb System 1 or Gottlieb System
80 use lights outputs to control logic. In other platforms you usually
use drivers.

## Required settings

The following sections are required in the `digital_outputs:` section of
your config:

### number:

Single value, type: `string`. Defaults to empty.

The number of your light or driver. The exact meaning of this number
depends on your platform but is exactly the same as if this was a light
or driver (depending on the `type` setting).

### type:

Single value, type: one of the following options: light, driver.
Defaults to empty.

Whether this output is mapped as light or driver.

## Optional settings

The following sections are optional in the `digital_outputs:` section of
your config. (If you don't include them, the default will be used).

### disable_events:

List of one (or more) device control events
([Instructions for entering device control events](instructions/device_control_events.md)). Defaults to empty.

Those events will disable this output when posted.

### enable_events:

List of one (or more) device control events
([Instructions for entering device control events](instructions/device_control_events.md)). Defaults to empty.

Those events will enable this output when posted.

### light_subtype:

Single value, type: `string`. Defaults to empty.

If this is mapped as light (`type: light`) you can set the `subtype`
here (see [lights](lights.md) for
details about `subtype`). The exact meaning depends on your platform.

### platform:

Single value, type: `string`. Defaults to empty.

In case you want to overwrite the default platform (as defined in
`hardware:`), you can choose a platform for this output.

### platform_settings:

Single value, type: dict. Defaults to empty.

Dict of platform specific settings. Consult your platform documentation
for those settings.

### console_log:

Single value, type: one of the following options: none, basic, full.
Default: `basic`

Log level for the console log for this device.

### debug:

Single value, type: `boolean` (`true`/`false`). Default: `false`

Set this to true to see additional debug output. This might impact the
performance of MPF.

### file_log:

Single value, type: one of the following options: none, basic, full.
Default: `basic`

Log level for the file log for this device.

### label:

Single value, type: `string`. Default: `%`

Name of this device in service mode.

### tags:

List of one (or more) values, each is a type: `string`. Defaults to
empty.

Not used.

## Related How To guides

* [Motors](../mechs/motors.md)
* [How to use Step Stick Steppers in MPF](../hardware/stepstick.md)
* [Using the Stern Spike Trough](../mechs/troughs/spike_trough.md)
* [Configuring and Enabling Flippers/Pop Bumpers/Slingshots in LISY](../hardware/lisy/flippers_slings_popbumpers.md)
* [Arduino Pinball Controller](../hardware/apc/index.md)
* [How to configure coils/drivers/magnets (P-ROC/P3-ROC)](../hardware/multimorphic/drivers.md)
