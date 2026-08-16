---
title: How to use Step Stick Steppers in MPF
---

# How to use Step Stick Steppers in MPF


Related Config File Sections:

* [hardware:](../config/hardware.md)
* [step_stick_stepper_settings:](../config/step_stick_stepper_settings.md)
* [digital_outputs:](../config/digital_outputs.md)
* [switches:](../config/switches.md)
* [steppers:](../config/steppers.md)

MPF can drive steppers on a StepStick (or DRV8825) connected via a
[digital output](../config/digital_outputs.md). Depending on the jitter of the output the speed might be
limited to a few steps per second (like 50-200).

[TODO: Add a picture of a step stick or DRV8825](../about/help.md)

Overview video about
[steppers](../mechs/steppers.md):

<div class="video-wrapper">
<iframe width="560" height="315" src="https://www.youtube.com/embed/YaRNBU0OHGc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Configuring your stepper

A step stick stepper needs two or three outputs which define the
hardware number: `direction_output:step_output` or
`direction_output:step_output:enable_output`. In addition, you need a
`homing_switch` so MPF can find the `0` position of your stepper at
startup.

This is an example:

``` yaml
#config_version=5
hardware:
  stepper_controllers: step_stick
digital_outputs:
  c_direction:
    number: 1
    type: driver
  c_step:
    number: 2
    type: driver
  c_enable:
    number: 3
    type: driver
switches:
  s_home:
    number: 1
steppers:
  stepper1:
    number: c_direction:c_step:c_enable   # enable is optional
    homing_mode: switch
    homing_switch: s_home
    named_positions:
      10: test_00
      20: test_01
      50: test_10
    platform_settings:  # optional speed settings
      low_time: 20ms
      high_time: 20ms
```

You might want to change the speed in the
[platform_settings](../config/step_stick_stepper_settings.md) section. `1000 / (low_time + high_time)` will be your number
of steps per second.

## Connecting your stepper driver

Connect the `DIR` pin to your `direction_output`, `STP` to your
`step_output` and `GND` to your ground. If use an `enable_output`
connect it to `EN`. Otherwise, pull it to `GND` or the driver will not
work. Connect `SLP` and `RST` to `VDD` (not all driver have all of
them). In addition, you need to pull `M0`, `M1` and `M2` to VDD or GND
to configure the step resolution. Your stepper will connect to `1A`,
`1B`, `2A` and `2B`. Connect power to `VMOT` (do not forget to also
connect ground of your stepper power supply; see
[Voltages and Power](voltages_and_power/voltages_and_power.md)). See the datasheet for details about your driver.

## What if it did not work?

Have a look at our [hardware troubleshooting guide](troubleshooting_hardware/index.md).
