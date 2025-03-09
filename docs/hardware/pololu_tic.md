---
title: How to use Pololu Tic in MPF
---

# How to use Pololu Tic in MPF


Related Config File Sections:

* [hardware:](../config/hardware.md)
* [pololu_tic:](../config/pololu_tic.md)
* [tic_stepper_settings:](../config/tic_stepper_settings.md)
* [switches:](../config/switches.md)
* [steppers:](../config/steppers.md)

The Pololu Tic is a stepper controller which can control one stepper via
USB. Multiple versions with different power rating exist but they all
work the same from the perspective of MPF.

[TODO: Add a picture of a Pololu Tic](../about/help.md)

Overview video about
[steppers](../mechs/steppers.md):

<div class="video-wrapper">
<iframe width="560" height="315" src="https://www.youtube.com/embed/YaRNBU0OHGc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Installation

To use the Pololu Tic you need to install `ticcmd` from Pololu. Follow
their [Installation instructions for
ticcmd](https://www.pololu.com/docs/0J71/3).

## Connecting your stepper

Connect your stepper according to the Pololu manual.

## Configuring your stepper

Afterwards, you can use steppers from MPF. This is an example:

``` mpf-config
#config_version=5
hardware:
  stepper_controllers: pololu_tic

switches:
  s_home:
    number: 1

steppers:
  stepper1:
    number: 1
    homing_mode: switch
    homing_switch: s_home
    named_positions:
      10: test_00
      20: test_01
      50: test_10
    platform_settings:
      max_acceleration: 20000
```

You can set certain pololu-specific settings in `platform_settings`. See
[tic_stepper_settings:](../config/tic_stepper_settings.md) for
details.

## What if it did not work?

Have a look at our [hardware troubleshooting guide](troubleshooting_hardware/index.md).
