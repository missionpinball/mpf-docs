# rpi_dmd API Reference

`self.machine.hardware_platforms['rpi_dmd']`

``` python
class mpf.platforms.rpi_dmd.RpiDmdPlatform(machine)
```

Bases: `mpf.core.platform.RgbDmdPlatform`

Raspberry Pi GPIO RGB DMD.

## Accessing the rpi_dmd platform via code

Hardware platforms are stored in the `self.machine.hardware_platforms` dictionary, so the rpi_dmd platform is available via `self.machine.hardware_platforms['rpi_dmd']`.

## Methods & Attributes

The rpi_dmd platform has the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`configure_rgb_dmd(name: str)`

Configure rgb dmd.

`initialize()`

Initialise platform.

`stop()`

Stop platform.
