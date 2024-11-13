
# self.machine.hardware_platforms[‘step_stick’]

`class mpf.platforms.step_stick.StepStickDigitalOutputPlatform(machine)`

Bases: mpf.core.platform.StepperPlatform

Drive a stepper using a StepStick controller on a digital output.

## Accessing the step_stick platform via code

Hardware platforms are stored in the `self.machine.hardware_platforms` dictionary, so the step_stick platform is available via `self.machine.hardware_platforms['step_stick']`.

## Methods & Attributes

The step_stick platform has the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`configure_stepper(number: str, config: dict) → mpf.platforms.interfaces.stepper_platform_interface.StepperPlatformInterface`

Configure a stepper driven by StepStick on a digital output.

`classmethod get_stepper_config_section()`

Return config section.

