# device_manager API Reference

`self.machine.device_manager`

``` python
class mpf.core.device_manager.DeviceManager(machine)
```

Bases: `mpf.core.mpf_controller.MpfController`

Manages all the devices in MPF.

## Accessing the device_manager in code

There is only one instance of the device_manager in MPF, and it’s accessible via self.machine.device_manager.

## Methods & Attributes

The device_manager has the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`create_devices(collection_name, config)`

Create devices for a collection.

`create_machinewide_device_control_events(**kwargs)`

Create machine wide control events.

`get_device_control_events(config) → Generator[Tuple[str, Callable, int, Device], None, None]`

Scan a config dictionary for control_events. Yields events, methods, delays, and devices for all the devices and control_events in that config.


Parameters:

* **config** – An MPF config dictionary (either machine-wide or mode- specific).
  * The event name
  * The callback method of the device
  * The delay in ms
  * The device object

`get_monitorable_devices()`

Return all devices which are registered as monitorable.

`initialize_devices()`

Initialise devices.

`load_devices_config(validate=True)`

Load all devices.

`notify_device_changes(device, notify, old, value)`

Notify subscribers about changes in a registered device.

Parameters:

* **device** – The device that changed.
* **notify** – Attribute name which changed.
* **old** – The old value.
* **value** – The new value.

`register_monitorable_device(device)`

Register a monitorable device.

Parameters:

* **device** – The device to register.

`stop_devices()`

Stop all devices in the machine.
