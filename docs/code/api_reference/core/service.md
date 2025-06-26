# service API Reference

`self.machine.service`

``` python
class mpf.core.service_controller.ServiceController(machine)
```

Bases: `mpf.core.mpf_controller.MpfController`

Provides all service information and can perform service tasks.

## Accessing the service in code

There is only one instance of the service in MPF, and it's accessible via `self.machine.service`.

## Methods & Attributes

The service has the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`add_technical_alert(device, issue)`

Add an alert about a technical problem.

`get_coil_map() → List[mpf.core.service_controller.CoilMap]`

Return a map of all coils in the machine.

`get_light_map() → List[mpf.core.service_controller.LightMap]`

Return a map of all lights in the machine.

`get_switch_map()`

Return a map of all switches in the machine.

`is_in_service() → bool`

Return true if in service mode.

`start_service()`

Start service mode.

`stop_service()`

Stop service mode.
