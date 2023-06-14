---
title: "pololu_tic:"
---

# pololu_tic:


--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

The `pololu_tic:` section of your config is where you configure your
[Pololu Tic Stepper Controller](../hardware/pololu_tic.md).

See [/hardware/pololu_tic/index](tic_stepper_settings.md) for
`platform_settings` in your steppers.

## Optional settings

The following sections are optional in the `pololu_tic:` section of your
config. (If you don't include them, the default will be used).

### console_log:

Single value, type: one of the following options: none, basic, full.
Default: `none`

Log level for the console log for this platform.

### debug:

Single value, type: `boolean` (`true`/`false`). Default: `false`

Set this to true to see additional debug output. This might impact the
performance of MPF.

### file_log:

Single value, type: one of the following options: none, basic, full.
Default: `basic`

Log level for the file log for this platform.

## Related How To guides

* [How to use Pololu Tic in MPF](../hardware/pololu_tic.md)
