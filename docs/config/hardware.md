---
title: "hardware:"
---

# hardware:


--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

The `hardware:` section of your machine config file is where you
configure the options for the
[physical hardware controller boards](../hardware/index.md) that MPF will use.

If you intend to use MPF with physical hardware, at a minimum you'll
have a `platform:` and `driverboards:` section in your machine config,
like this:

``` yaml
hardware:
  platform: fast
  driverboards: fast
```

## Device-specific defaults

The following optional settings can be used to set default platforms for
a specific class of devices. Note that `virtual` and `smart_virtual` are
valid options for all of these, though they are not included in the
lists below. Also note that those lists are not exhaustive.

!!! note

    The list of platforms is incomplete here. See the
    [MPF compatible control systems / hardware](../hardware/index.md) for details which
    platforms are supported by MPF.

## Optional settings

The following sections are optional in the `hardware:` section of your
config. (If you don't include them, the default will be used).

### accelerometers:

List of one (or more) values, each is a type: `string`. Default:
`default`

See [DMD Platforms in MPF](../hardware/dmd_platforms.md) for
supported platforms.

### coils:

List of one (or more) values, each is a type: `string`. Default:
`default`

For instance:

* `p_roc`
* `p3_roc`
* `fast`
* `opp`
* `apc`
* `snux`

Almost all platforms in [MPF compatible control systems / hardware](../hardware/index.md)
are supported here.

### dmd:

List of one (or more) values, each is a type: `string`. Default:
`default`

See [DMD Platforms in MPF](../hardware/dmd_platforms.md) for
supported platforms.

### driverboards:

Single value, type: `string`. Defaults to empty.

Specifies the default type of driver boards you're using. If you have a
homebrew machine, this will probably match your platform. If you're
using an existing machine, then this will be whatever type of
driverboard is installed in the machine.

* `pdb` P-ROC Driver Boards, PD-16, PD-8x8, etc.)
* `fast` FAST IO boards (0804, 1616, 3208, etc.)
* `opp` OPP wing boards
* `wpc95` Williams WPC-95
* `wpc` Williams WPC
* `wpcAlphaNumeric` Williams WPC with alphanumeric 14-pin connected
    segmented display
* `sternSAM` Stern SAM
* `sternWhitestar` Stern Whitestar

### hardware_sound_system:

List of one (or more) values, each is a type: `string`. Default:
`default`

See [MPF compatible control systems / hardware](../hardware/index.md) for supported
platforms.

### i2c:

List of one (or more) values, each is a type: `string`. Default:
`default`

See [I2C Platforms in MPF](../hardware/i2c_platforms.md) for
supported platforms.

### lights:

List of one (or more) values, each is a type: `string`. Default:
`default`

Almost all platforms in [MPF compatible control systems / hardware](../hardware/index.md)
are supported here.

### platform:

List of one (or more) values, each is a type: `string`. Default:
`virtual`

Specifies the default platform that will be used by all devices in the
config. We say this is the "default" platform, because it's possible
to use more than one platform at time. (Maybe you use a P-ROC for coils
and switches and a FadeCandy for RGB LEDs, etc.) See the
[Mixing-and-Matching hardware platforms](../hardware/platform.md) for more details on
this.

See [MPF compatible control systems / hardware](../hardware/index.md) for a complete list.

### rgb_dmd:

List of one (or more) values, each is a type: `string`. Default:
`default`

See [DMD Platforms in MPF](../hardware/dmd_platforms.md) for
supported platforms.

### segment_displays:

List of one (or more) values, each is a type: `string`. Default:
`default`

See [Segment Display Platforms in MPF](../hardware/segment_display_platforms.md)
for supported platforms.

### servo_controllers:

List of one (or more) values, each is a type: `string`. Default:
`default`

See [Servo Platforms in MPF](../hardware/servo_platforms.md) for
supported platforms.

### stepper_controllers:

List of one (or more) values, each is a type: `string`. Default:
`default`

See [Stepper Platforms in MPF](../hardware/stepper_platforms.md) for
supported platforms.

### switches:

List of one (or more) values, each is a type: `string`. Default:
`default`

Almost all platforms in [MPF compatible control systems / hardware](../hardware/index.md)
are supported here.

## Related How To guides

* [MPF compatible control systems / hardware](../hardware/index.md)
