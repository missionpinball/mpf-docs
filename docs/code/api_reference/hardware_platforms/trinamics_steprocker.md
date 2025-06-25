
# self.machine.hardware_platforms[‘trinamics_steprocker’]

``` python
class mpf.platforms.trinamics_steprocker.TrinamicsStepRocker(machine)
```

Bases: `mpf.core.platform.StepperPlatform`

Supports the Trinamics Step Rocker via PySerial.

Works with Trinamics Step Rocker. TBD other ‘TMCL’ based steppers eval boards

## Accessing the trinamics_steprocker platform via code

Hardware platforms are stored in the `self.machine.hardware_platforms` dictionary, so the trinamics_steprocker platform is available via `self.machine.hardware_platforms['trinamics_steprocker']`.

## Methods & Attributes

The trinamics_steprocker platform has the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`configure_stepper(number: str, config: dict) → mpf.platforms.trinamics_steprocker.TrinamicsTMCLStepper`

Configure a smart stepper device in platform.

Parameters:

* **number** – Number of the stepper.
* **config (dict)** – Configuration of device

`classmethod get_stepper_config_section()`

Return config validator name.

`initialize()`

Initialise trinamics steprocker platform.

`stop()`

Close serial.
