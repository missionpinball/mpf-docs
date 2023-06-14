---
title: p_roc:
---

# p_roc:


--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

The `p_roc:` section of your config is where you configure hardware
specific bits about the P-Roc or P3-Roc. In most cases you can omit this
config and stick with the defaults.

## Optional settings

The following sections are optional in the `p_roc:` section of your
config. (If you don't include them, the default will be used).

### console_log:

Single value, type: one of the following options: none, basic, full.
Default: `none`

Log level for the console log for this platform.

### debug:

Single value, type: `boolean` (`true`/`false`). Default: `false`

Set this to `True` if you want to know what is going on under the hood.
We will usually ask you to set this if you experience any hardware
related problems and send us your log.

### display_flash_duty:

Single value, type: `number` (will be converted to floating point).
Default: `0.5`

--8<-- "todo.md"

### display_flash_frequency:

Single value, type: `number` (will be converted to floating point).
Default: `1.0`

--8<-- "todo.md"

### dmd_timing_cycles:

List of one (or more) values, each is a type: `integer`. Defaults to
empty.

Only P-Roc (not P3-Roc).

Those values determine the timing to drive the different shades of your
DMD. See [How to configure mono/traditional DMD (P-ROC)](../hardware/multimorphic/dmd.md) for
details.

### dmd_update_interval:

Single value, type: `time string (ms)`
([Instructions for entering time strings](instructions/time_strings.md)). Default: `33ms`

Only P-Roc (not P3-Roc).

The update interval of your DMD. Usually you do not have to change this.

### driverboards:

Single value, type: one of the following options: wpc, wpcAlphanumeric,
wpc95, sternSAM, sternWhitestar, pdb, custom, None. Defaults to empty.

Similar to `driverboards` in the [hardware:](hardware.md) section. Use this setting if you use multiple playforms
(i.e. FAST and P3-Roc) in one machine.

### file_log:

Single value, type: one of the following options: none, basic, full.
Default: `basic`

Log level for the file log for this platform.

### lamp_matrix_strobe_time:

Single value, type: `time string (ms)`
([Instructions for entering time strings](instructions/time_strings.md)). Default: `100ms`

Default: `100ms`

The column strobe time for your lamp matrix. See
[How to configure Matrix Lights (P-ROC/P3-ROC)](../hardware/multimorphic/lights.md) for
details.

### pd_led_boards:

One or more sub-entries. Each in the format of `integer` :
[pd_led_boards:](pd_led_boards.md)

A map of PD-LED boards with their ID as key and a
[configuration map](pd_led_boards.md) as
value. This can be used to configure indivdual features per board.

See [Servos on a PD-LED (P-ROC/P3-ROC)](../hardware/multimorphic/servos.md),
[Steppers on a PD-LED (P-ROC/P3-ROC)](../hardware/multimorphic/steppers.md) or
[How to configure LEDs on the PD-LED (P-ROC/P3-ROC)](../hardware/multimorphic/leds.md) for details.

### trace_bus:

Single value, type: `boolean` (`true`/`false`). Default: `false`

Log all calls to libpinproc. This will cause a lot of additional log
lines and might considerably slow down MPF. Use only during debugging.

### use_separate_thread:

Single value, type: `boolean` (`true`/`false`). Default: `true`

Whether MPF should spawn a separate thread to talk to the P/P3-Roc or
not. If you set this to `False` any IO to the P/P3-Roc will block the
game loop which might cause lags unrelated to the hardware. This has a
small overhead but should be enabled in most cases.

### use_watchdog:

Single value, type: `boolean` (`true`/`false`). Default: `true`

Enable or disable the watchdog. Usually you want to keep this enabled.

### watchdog_time:

Single value, type: `time string (ms)`
([Instructions for entering time strings](instructions/time_strings.md)). Default: `1s`

Watchdog timeout. The P/P3-Roc will disable all coils when the watchdog
expires.

## Related How To guides

* [How to configure Multimorphic (P-ROC & P3-ROC) hardware](../hardware/multimorphic/index.md)
