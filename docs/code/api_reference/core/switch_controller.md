# self.machine.switch_controller

``` python
class mpf.core.switch_controller.SwitchController(machine: mpf.core.machine.MachineController)
```

Bases: `mpf.core.mpf_controller.MpfController`

Tracks all switches in the machine, receives switch activity, and converts switch changes into events.

## Accessing the switch_controller in code

There is only one instance of the switch_controller in MPF, and it’s accessible via `self.machine.switch_controller`.

## Methods & Attributes

The switch_controller has the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`add_monitor(monitor: Callable[[mpf.core.switch_controller.MonitoredSwitchChange], None])`

Add a monitor callback which is called on switch changes.

`add_switch_handler(switch_name, callback, state=1, ms=0, return_info=False, callback_kwargs=None) → mpf.core.switch_controller.SwitchHandler`

Register a handler to take action on a switch event.

Parameters:

* **switch_name** – String name of the switch you’re adding this handler for.
* **callback** – The method you want called when this switch handler fires.
* **state** – Integer of the state transition you want to callback to be triggered on. Default is 1 which means it’s called when the switch goes from inactive to active, but you can also use 0 which means your callback will be called when the switch becomes inactive
* **ms – Integer** - If you specify a ‘ms’ parameter, the handler won’t be called until the witch is in that state for that many milliseconds.
* **return_info** – If True, the switch controller will pass the parameters of the switch handler as arguments to the callback, including switch_name, state, and ms. If False (default), it just calls the callback with no parameters.
* **callback_kwargs** – Additional kwargs that will be passed with the callback.

You can mix & match entries for the same switch here.

`add_switch_handler_obj(switch, callback, state=1, ms=0, return_info=False, callback_kwargs=None)`

Register a handler to take action on a switch event. Same as add_switch_handler but you can pass a switch object instead of a name.

`static get_active_event_for_switch(switch_name)`

Return the event name which is posted when switch_name becomes active.

`is_active(switch, ms=None)`

Query whether a switch is active.

Parameters:

* **switch** – Switch object to check.
* **ms** – Milliseconds that the switch has been active. If this is non-zero, then this method will only return True if the switch has been in that state for at least the number of ms specified.

Returns: True if the switch_name has been active for the given number of ms. If ms is not specified, returns True if the switch is in the state regardless of how long it’s been in that state.

`is_inactive(switch, ms=None)`

Query whether a switch is inactive.

Parameters:

* **switch** – Switch object to check.
* **ms** – Milliseconds that the switch has been inactive. If this is non-zero, then this method will only return True if the switch has been in that state for at least the number of ms specified. number of ms. If ms is not specified, returns True if the switch is in the state regardless of how long it’s been in that state.

`is_state(switch: mpf.devices.switch.Switch, state, ms=0.0)`

Check if switch is in state. Query whether a switch is in a given state and (optionally) whether it has been in that state for the specified number of ms.

Parameters:

* **switch** – Switch object to check.
* **state** – Bool of the state to check. True is active and False is inactive.
* **ms** – Milliseconds that the switch has been in that state. If this is non-zero, then this method will only return True if the switch has been in that state for at least the number of ms specified.

Returns: True if the switch_name has been in the state for the given number of ms. If ms is not specified, returns True if the switch is in the state regardless of how long it’s been in that state.

`log_active_switches(**kwargs)`

Write out entries to the INFO log file of all switches that are currently active.

`process_switch(name, state, logical=False, timestamp=None)`

Process a new switch state change for a switch by name.  This is the method that is called by the platform driver whenever a switch changes state. It’s also used by the “other” modules that activate switches, including the keyboard and OSC interfaces. State 0 means the switch changed from active to inactive, and 1 means it changed from inactive to active. (The hardware & platform code handles NC versus NO switches and translates them to ‘active’ versus ‘inactive’.)

Parameters:

* **name** – The string name of the switch.
* **state** – Boolean or int of state of the switch you’re processing, True/1 is active, False/0 is inactive.
* **logical** – Boolean which specifies whether the ‘state’ argument represents the “physical” or “logical” state of the switch. If True, a 1 means this switch is active and a 0 means it’s inactive, regardless of the NC/NO configuration of the switch. If False, then the state parameter passed will be inverted if the switch is configured to be an ‘NC’ type. Typically the hardware will send switch states in their raw (logical=False) states, but other interfaces like the keyboard and OSC will use logical=True.
* **timestamp** – Timestamp when this switch change happened.

`process_switch_by_num(num, state, platform, logical=False, timestamp=None)`

Process a switch state change by switch number.

Parameters:

* **num** – The switch number (based on the platform number) for the switch you’re setting.
* **state** – The state to set, either 0 or 1.
* **platform** – The platform this switch is on.
* **logical** – Whether the state you’re setting is the logical or physical state of the switch. If a switch is NO (normally open), then the logical and physical states will be the same. NC (normally closed) switches will have physical and logical states that are inverted from each other.
* **timestamp** – Timestamp when this switch change happened.

`process_switch_obj(obj: mpf.devices.switch.Switch, state, logical, timestamp=None)`

Process a new switch state change for a switch by name.

Parameters:

* **obj** – The switch object.
* **state** – Boolean or int of state of the switch you’re processing, True/1 is active, False/0 is inactive.
* **logical** – Boolean which specifies whether the ‘state’ argument represents the “physical” or “logical” state of the switch. If True, a 1 means this switch is active and a 0 means it’s inactive, regardless of the NC/NO configuration of the switch. If False, then the state parameter passed will be inverted if the switch is configured to be an ‘NC’ type. Typically the hardware will send switch states in their raw (logical=False) states, but other interfaces like the keyboard and OSC will use logical=True.
* **timestamp** – Timestamp when this switch change happened.

This is the method that is called by the platform driver whenever a switch changes state. It’s also used by the “other” modules that activate switches, including the keyboard and OSC interfaces. State 0 means the switch changed from active to inactive, and 1 means it changed from inactive to active. (The hardware & platform code handles NC versus NO switches and translates them to ‘active’ versus ‘inactive’.)

`register_switch(switch: mpf.devices.switch.Switch)`

Add a switch object to the switch controller for tracking.

Parameters:

switch – Switch object to add

`remove_monitor(monitor: Callable[[mpf.core.switch_controller.MonitoredSwitchChange], None])`

Remove a monitor callback.

`remove_switch_handler(switch_name, callback, state=1, ms=0)`

Remove a registered switch handler. Currently this only works if you specify everything exactly as you set it up. (Except for return_info, which doesn’t matter if true or false, it will remove either / both.

`remove_switch_handler_by_key(switch_handler: mpf.core.switch_controller.SwitchHandler)`

Remove switch handler by key returned from `add_switch_handler`.

`remove_switch_handler_by_keys(switch_handlers: List[mpf.core.switch_controller.SwitchHandler])`

Remove switch handlers by list of keys returned from `add_switch_handler`.

`remove_switch_handler_obj(switch, callback, state=1, ms=0)`

Remove a registered switch handler. Same as remove_switch_handler but takes a switch object instead of the name.

`update_switches_from_hw()`

Update the states of all the switches be re-reading the states from the hardware platform. This method works silently and does not post any events if any switches changed state.

`verify_switches() → bool`

Verify that switches states match the hardware. Loops through all the switches and queries their hardware states via their platform interfaces and then compares that to the state that MPF thinks the switches are in. Throws logging warnings if anything doesn’t match.  This method is notification only. It doesn’t fix anything.

`wait_for_any_switch(switches: List[mpf.devices.switch.Switch], state: int = 1, only_on_change=True, ms=0)`

Wait for the first switch in the list to change into state.

Parameters:

* **switches** – Iterable of switches. Whichever switch changes first will trigger this wait.
* **state** – The state to wait for. 0 = inactive, 1 = active, 2 = opposite to current.
* **only_on_change** – Bool which controls whether this wait will be triggered now if the switch is already in the state, or whether it will wait until the switch changes into that state.
* **ms** – How long the switch needs to be in the new state to trigger the wait.

`wait_for_switch(switch: mpf.devices.switch.Switch, state: int = 1, only_on_change=True, ms=0)`

Wait for a switch to change into a state.

Parameters:

* **switch** – String to wait for.
* **state** – The state to wait for. 0 = inactive, 1 = active, 2 = opposite to current.
* **only_on_change** – Bool which controls whether this wait will be triggered now if the switch is already in the state, or whether it will wait until the switch changes into that state.
* **ms** – How long the switch needs to be in the new state to trigger the wait.
