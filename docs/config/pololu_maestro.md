---
title: "pololu_maestro:"
---

# pololu_maestro:


--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

The `pololu_maestro:` section of your config is where you configure the
serial port that a Pololu Maestro servo controller is connected to.

When you attach a Pololu Maestro, two serial ports will appear. You want
to specific the first (lower numbered) port here. For example:

``` mpf-config
pololu_maestro:
  port: COM5
```

Note that there are a few other settings you need to configure in other
areas to use a Pololu Maestro servo controller. See the
[How To guide](../hardware/pololu_maestro.md) for details.

## Required settings

The following sections are required in the `pololu_maestro:` section of
your config:

### port:

Single value, type: `string`. Defaults to empty.

The name of the serial port.

## Optional settings

The following sections are optional in the `pololu_maestro:` section of
your config. (If you don't include them, the default will be used).

### console_log:

Single value, type: one of the following options: none, basic, full.
Default: `none`

Log level for the console log for this platform.

### debug:

Single value, type: `boolean` (`true`/`false`). Default: `false`

See the
[documentation on the debug setting](instructions/debug.md) for details.

### file_log:

Single value, type: one of the following options: none, basic, full.
Default: `basic`

Log level for the file log for this platform.

### servo_max:

Single value, type: `integer`. Default: `9000`

Quarter-microseconds to use for the max servo value. The default (9000)
translates to 2250 microseconds or 2.25ms.

### servo_min:

Single value, type: `integer`. Default: `3000`

Quarter-microseconds to use for the max servo value. The default (3000)
translates to 750 microseconds or 0.75ms.

## Related How To guides

* [Pololu Maestro Servo Controller](../hardware/pololu_maestro.md)
