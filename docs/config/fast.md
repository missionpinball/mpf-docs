---
title: "fast: Config Reference"
---

# fast: Config Reference

--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files|**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|


# 2026 Documentation Update

The following config documentation is relevant for MPF 0.57.4 and 0.80.0. Last updated Dec 18, 2025.

The `fast:` section of your machine-wide config is where you configure hardware options that are specific to the FAST Pinball Controller.
The [FAST website](https://fastpinball.com/mpf/config/) also has thorough documentation and examples for MPF 0.57 and 0.80 compatible configurations.

## fast: config reference

The top-level `fast:` key contains subsections for each of the various component networks available with FAST.
You do not need to include any section that is not present in your machine.

### net:

This contains the configuration for the NET IO boards, which handle switches and drivers.
See [fast:net: config reference](fast/fast_net.md) for details.

### exp:

This contains the configuration for the EXP boards, which handle lights and various motors and accessories.

### exp_int:

When using the Raspberry PI directly connected to a Neuron board, the Neuron's LED ports are not accesible on the normal `exp` bus.
To enable use of these headers, define the `FP-EXP-2000` model board in the `exp_int` instead of `exp` configuration.
If using other EXP boards, you still define those on the normal `exp` configuration.
For an example, see this [pull request](https://github.com/missionpinball/mpf/pull/1895) on Github.

### aud:

This contains the configuration for sounds played through the FAST Audio board.


# Pre-2024 Documentation

The following documentation was current in mid 2023, some settings and structures may have changed since then:

## fast: config settings

The `fast:` section of your machine-wide config is where you configure
hardware options that are specific to the FAST Pinball Controller. Note
that we have a how to guide which includes
[all the FAST-specific settings](../hardware/fast/index.md) throughout your entire config file, so be sure to read that
if you have FAST hardware.


### ports:

List of one (or more) values, each is a type: `string`. Defaults to
empty.

A comma-separated list of the serial port names your FAST controller
uses.

``` yaml
fast:
  ports: com3, com4, com5
```

## Optional settings

The following sections are optional in the `fast:` section of your
config. (If you don\'t include them, the default will be used).

### baud:

Single value, type: `integer`. Default: `921600`

The baud rate for the FAST COM ports.

### console_log:

Single value, type: one of the following options: none, basic, full.
Default: `none`

Log level for the console log for this platform.

### debug:

Single value, type: `boolean` (`true`/`false`). Default: `false`

See the [documentation on the debug setting](instructions/debug.md) for details.

### dmd_buffer:

Single value, type: `integer`. Default: `3`

Max backlog for the DMD port to prevent overflows in the FAST CPU.

### driverboards:

Single value, type: one of the following options: fast, wpc, None.
Defaults to empty.

Which driverboards are you using? Most likely `fast`. Similar to
`driverboards` in the [hardware:](hardware.md)
section. Use this setting if you use multiple playforms (i.e. FAST and
P3-Roc) in one machine.

### file_log:

Single value, type: one of the following options: none, basic, full.
Default: `basic`

Log level for the file log for this platform.

### hardware_led_fade_time:

Single value, type: `time string (ms)`
[Instructions for entering time strings](instructions/time_strings.md). Default: `0`

Controls how quickly LEDs will fade to their new color when they receive
a color instruction from MPF.

The default is 0, which means if you set an LED to be red, it will turn
red instantly. But if you set `hardware_led_fade_time: 20`, that means
that when an LED receives an instruction to turn RED, it will smoothly
fade from whatever color it is now to red over a period of 20ms.

You can play with different settings to pick something you like. Some
people prefer the instant 0ms snappiness that\'s possible with LEDs.
Others like to set this value to something like `100ms` which gives LEDs
the more gentle fade style reminiscent of incandescent bulbs.

### ignore_rgb_crash:

Single value, type: `boolean` (`true`/`false`). Default: `false`

Ignore if the RGB CPU crashes. It will restart and the light will mostly
recovery within a few seconds. If you set this to `False` MPF will
shutdown when this happens because the hardware state is undefined when
this happens.

### net_buffer:

Single value, type: `integer`. Default: `10`

Max backlog for the NET port to prevent overflows in the FAST CPU.

### rgb_buffer:

Single value, type: `integer`. Default: `3`

Max backlog for the RGB port to prevent overflows in the FAST CPU.


## Related How To guides

* [How to configure MPF for FAST Pinball hardware](../hardware/fast/index.md)
