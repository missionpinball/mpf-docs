---
title: DC Motors
---

# DC Motors


Related Config File Sections:

* [dc_motors:](../config/dc_motors.md)

DC motors can generally run forward and backward, and may offer controlled and uncontrolled stopping, as well as switch-limited operation or other special features.
Using a particular motor action requires that both your control platform and your motor unit are compatible, wired correctly, and support the specific action and parameters given.
If you are unsure whether your hardware works together, DO NOT EXPIRIMENT. You may damage either your control hardware or your motor itself, or worse.

Some motors can be implemented through coil, servo, or stepper control, which use their own configuration types.
When using dedicated DC motor control hardware (such as the FAST-EXP-0051), you can use the `dc_motor` device type.

## Hardware

DC motors come in a variety of voltages and form factors. Specialist motor types include linear actuators and quadrature motor encoders.

## Config as a DC motor device:

``` yaml
fast:
  exp:
    boards:
      0051board:
        model: FP-EXP-0051

dc_motors:
  dc_motor:
    number: 0051board-1
    control_events:
      mid_motor:
        duration: 500ms
        power: 0.25
      reverse_motor:
        action: reverse_pulse
        duration: 2s
        power: 0.75

event_player:
  my_trigger_event:
    - mid_motor
    - reverse_motor|500ms
```
