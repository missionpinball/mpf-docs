
# self.machine.hardware_platforms[‘pololu_tic’]

`class mpf.platforms.pololu.pololu_tic.PololuTICHardwarePlatform(machine)`

Bases: mpf.core.platform.StepperPlatform

Supports the Pololu TIC stepper drivers via ticcmd command line.

## Accessing the pololu_tic platform via code

Hardware platforms are stored in the `self.machine.hardware_platforms` dictionary, so the pololu_tic platform is available via `self.machine.hardware_platforms['pololu_tic']`.

## Methods & Attributes

The pololu_tic platform has the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`configure_stepper(number: str, config: dict) → mpf.platforms.pololu.pololu_tic.PololuTICStepper`

Configure a smart stepper device in platform.

Parameters:

* **number** – Number of this stepper.
* **config (dict)** – Configuration of device

`classmethod get_stepper_config_section()`

Return config validator name.

`stop()`

De-energize the stepper and stop sending the command timeout refresh.

