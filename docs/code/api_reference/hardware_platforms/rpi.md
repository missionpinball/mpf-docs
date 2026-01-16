---
title: API Reference - rpi
---

# rpi API Reference

`self.machine.hardware_platforms['rpi']`

``` python
class mpf.platforms.rpi.rpi.RaspberryPiHardwarePlatform(machine)
```

Bases: `mpf.core.platform.SwitchPlatform`, `mpf.core.platform.DriverPlatform`, `mpf.core.platform.ServoPlatform`, `mpf.core.platform.I2cPlatform`

Control the hardware of a Raspberry Pi.

Works locally and remotely via network.

## Accessing the rpi platform via code

Hardware platforms are stored in the `self.machine.hardware_platforms` dictionary, so the rpi platform is available via `self.machine.hardware_platforms['rpi']`.

## Methods & Attributes

The rpi platform has the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`clear_hw_rule(switch: mpf.core.platform.SwitchSettings, coil: mpf.core.platform.DriverSettings)`

Raise exception.

`configure_driver(config: mpf.core.platform.DriverConfig, number: str, platform_settings: dict) → mpf.platforms.interfaces.driver_platform_interface.DriverPlatformInterface`

Configure an output on the Raspberry Pi.

`configure_i2c(number: str)`

Configure I2c device.

`configure_servo(number: str) → mpf.platforms.interfaces.servo_platform_interface.ServoPlatformInterface`

Configure a servo.

`configure_switch(number: str, config: mpf.core.platform.SwitchConfig, platform_config: dict) → mpf.platforms.interfaces.switch_platform_interface.SwitchPlatformInterface`

Configure a switch with pull up.

`get_hw_switch_states()`

Return current switch states.

`initialize()`

Initialise platform.

`send_command(cmd)`

Add a command to the command queue.

`set_pulse_on_hit_and_enable_and_release_and_disable_rule(enable_switch: mpf.core.platform.SwitchSettings, eos_switch: mpf.core.platform.SwitchSettings, coil: mpf.core.platform.DriverSettings, repulse_settings: Optional[mpf.core.platform.RepulseSettings])`

Raise exception.

`set_pulse_on_hit_and_enable_and_release_rule(enable_switch: mpf.core.platform.SwitchSettings, coil: mpf.core.platform.DriverSettings)`

Raise exception.

`set_pulse_on_hit_and_release_and_disable_rule(enable_switch: mpf.core.platform.SwitchSettings, eos_switch: mpf.core.platform.SwitchSettings, coil: mpf.core.platform.DriverSettings, repulse_settings: Optional[mpf.core.platform.RepulseSettings])`

Raise exception.

`set_pulse_on_hit_and_release_rule(enable_switch: mpf.core.platform.SwitchSettings, coil: mpf.core.platform.DriverSettings)`

Raise exception.

`set_pulse_on_hit_rule(enable_switch: mpf.core.platform.SwitchSettings, coil: mpf.core.platform.DriverSettings)`

Raise exception.

`stop()`

Stop platform.
