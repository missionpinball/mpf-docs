
# self.machine.hardware_platforms[‘smbus2’]

``` python
class mpf.platforms.smbus2.Smbus2(machine)
```

Bases: `mpf.core.platform.I2cPlatform`

I2C platform which uses the smbus interface on linux via the smbus2 python extension.

## Accessing the smbus2 platform via code

Hardware platforms are stored in the `self.machine.hardware_platforms` dictionary, so the smbus2 platform is available via `self.machine.hardware_platforms['smbus2']`.

## Methods & Attributes

The smbus2 platform has the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`configure_i2c(number: str) → mpf.platforms.smbus2.Smbus2I2cDevice`

Configure device on smbus2.

`initialize()`

Check if smbus2 extension has been imported.
