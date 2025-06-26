# smartmatrix API Reference

`self.machine.hardware_platforms['smartmatrix']`

``` python
class mpf.platforms.smartmatrix.SmartMatrixHardwarePlatform(machine)
```

Bases: `mpf.core.platform.RgbDmdPlatform`

SmartMatrix RGB DMD.

## Accessing the smartmatrix platform via code

Hardware platforms are stored in the `self.machine.hardware_platforms` dictionary, so the smartmatrix platform is available via `self.machine.hardware_platforms['smartmatrix']`.

## Methods & Attributes

The smartmatrix platform has the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`configure_rgb_dmd(name: str)`

Configure rgb dmd.

`initialize()`

Initialise platform.

`stop()`

Stop platform.
