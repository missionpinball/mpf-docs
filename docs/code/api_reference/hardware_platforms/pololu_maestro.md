
# self.machine.hardware_platforms[‘pololu_maestro’]

``` python
class mpf.platforms.pololu_maestro.PololuMaestroHardwarePlatform(machine)
```

Bases: `mpf.core.platform.ServoPlatform`

Supports the Pololu Maestro servo controllers via PySerial.

Works with Micro Maestro 6, and Mini Maestro 12, 18, and 24.

## Accessing the pololu_maestro platform via code

Hardware platforms are stored in the `self.machine.hardware_platforms` dictionary, so the pololu_maestro platform is available via `self.machine.hardware_platforms['pololu_maestro'].`

## Methods & Attributes

`The pololu_maestro platform has the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`configure_servo(number: str)`

Configure a servo device in platform.

Parameters:

* **number** – Number of the servo.

`initialize()`

Initialise platform.

`stop()`

Close serial.
