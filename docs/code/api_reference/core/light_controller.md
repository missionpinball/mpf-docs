
# self.machine.light_controller

`class mpf.core.light_controller.LightController(machine: mpf.core.machine.MachineController)`

Bases: mpf.core.mpf_controller.MpfController

Handles light updates and light monitoring.

## Accessing the light_controller in code

There is only one instance of the light_controller in MPF, and it’s accessible via `self.machine.light_controller`.

## Methods & Attributes

The `light_controller` has the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`initialise_light_subsystem()`

Initialise the light subsystem.

`monitor_lights()`

Update the color of lights for the monitor.

