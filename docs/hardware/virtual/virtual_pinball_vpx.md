---
title: The Virtual Pinball (VPX) Platform
---

# The Virtual Pinball (VPX) Platform


Related Config File Sections:

* [hardware:](../../config/hardware.md)

[VPX](https://en.wikipedia.org/wiki/Visual_Pinball) can be used (on
Windows) to emulate the hardware of a pinball machine to test your game
without real hardware. For instructions to download and install Visual
Pinball please see
[here](https://www.vpforums.org/index.php?app=tutorials&article=1).

This can be useful for software and hardware development. To use the VPX
platform you need to install it, along with the [MPF-VPX
bridge](https://github.com/missionpinball/mpf-vpcom-bridge) and add some
VPX scripts to your VPX table.

The bridge will connect to the running MPF machine when you start your
VPX table. As the VPX table is used only to emulate the hardware and
should not contain any game logic.

## Installation

Copy the file `register_vpcom.py` to your local machine folder. To
register the bridge run a CMD shell as Administrator, then

``` console
python register_vpcom.py --register
```

(You can use `--unregister` to uninstall the bridge)

## Use VPX in MPF

In your `config.yaml` configure virtual_pinball as your platform:

``` mpf-config
hardware:
  platform: virtual_pinball
```

or if you already have physical hardware configured start MPF with the
`--vpx` commandline option (similar to `-X`):

``` console
mpf both --vpx
```

## Configure VPX

In VPX you need to adjust your script to talk to MPF. You can also looks
this up in the example project inside the [bridge
repository](https://github.com/missionpinball/mpf-vpcom-bridge). The
GameName set in VPX is not used to check or validate the MPF machine.

### Setup controller and timers

* add `Set Controller = CreateObject("MPF.Controller")`
* add a Timer `MPFTimer` with an interval of 10 to 50ms. Keep this
    well below the minimal `default_pulse_ms` set in MPF for solenoids
* add a `Sub MPFTimer_Timer` to update all the lights and solenoids

### In Table_Init

* call Controller.run
* set the Trough switch(es) or create balls for a physical Trough (as
    in the demo table)
* init NC switches to False

### In Drain_Hit (for 1-Ball games)

* set the Trough switch(es)

### To use autofire_coils (Slings, Pops etc)

* add a droppable wall to each bumper. This will be used in
    `Sub CheckAutofireCoils` to disable/enable the bumper
* if necessary place an invisible wall behind the slingshots to stop
    the ball once the slingshots are disabled
* add each autofire object in VPX to `Sub CheckAutofireCoils`
* use the normal `Slingshot_Slingshot` and `Bumper_Hit` events

### Switch Handling

* add `Controller.Switch(MPFSwitchNumber)=SwitchState` to the
    `Switch_Hit/_Unhit` events. Use "" to include string type numbers
* add `Controller.PulseSW(MPFSwitchNumber)` to the `Switch_Hit` event
    of targets, slingshots and bumpers

### Controlled Lights (all types)

* create a collection "ControlledLamps"
* assign all controlled VPX lamps (Matrix, GI, LED, Flashers) to the
    collection "ControlledLamps" and call `InitLamps`

### LEDs and Lamps

* in `Sub UpdateLamps` add a case for every MPF light and LED number,
    setting the state of the VPX lamp/LED. Use "" to include string
    type numbers

### GI strings

* create a collection for each GI string, assign the GI lamps to the
    collections as needed
* assign all GI lamps to the collection "ControlledLamps" and
    call`InitLamps`
* in `Sub UpdateGI` add a case for every MPF gi string number, setting
    the state of the VPX GI collection. Use "" to include string type
    numbers

### Flashers

* assign all flasher lamps to the collection "ControlledLamps" and
    call `InitLamps`
* in `Sub UpdateFlashers` add a case for every MPF flasher number,
    setting the state of the VPX flasher. Use "" to include string
    type numbers

### Solenoids

* add all normal solenoids to the `Sub InitSolenoids`, to initialize
    them as `False`
* in `Sub UpdateSolenoids` add a case for every MPF coil number,
    setting the state of the VPX solenoid. Use "" to include string
    type numbers

### Flippers

* add the Flipper routines (`Solenoids` and `KeyUp/KeyDown`) as in the
    demo table. Flippers are handled as autofire coils and can be
    enabled/disabled using hrdware rules.

## To run a game

1.  start VPX as Administrator
2.  start MPF, wait until the display has been initialized
3.  start VPX table

To exit a game shut down the VPX table first

## What if it did not work?

Have a look at our
[hardware troubleshooting guide](../troubleshooting_hardware.md).
