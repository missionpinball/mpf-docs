# auditor API Reference

`self.machine.auditor`

``` python
class mpf.plugins.auditor.Auditor(machine: MachineController)
```

Bases: `object`

Writes switch events, regular events, and player variables to an audit log file.

## Accessing the auditor in code
There is only one instance of the auditor in MPF, and it’s accessible via self.machine.auditor.

## Methods & Attributes

The auditor has the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`audit(audit_class, event, **kwargs)`

Log an auditable event.
Parameters:

* **audit_class** – A string of the section we want this event to be logged to.
* **event** – A string name of the event we’re auditing.
* ****kwargs** – Not used, but included since some of the audit events might include random kwargs.

`audit_event(eventname, **kwargs)`

Record this event in the audit log.
Parameters:

* **eventname** – The string name of the event.
* ****kwargs** – not used, but included since some types of events include kwargs.

`audit_player(**kwargs)`

Write player data to the audit log. Typically this is only called at the end of a game.

Parameters:
* ****kwargs** – not used, but included since some types of events include kwargs.

`audit_shot(name, profile, state)`

Record shot hit.

`audit_switch(change: mpf.core.switch_controller.MonitoredSwitchChange)`

Record switch change.

`disable(**kwargs)`

Disable the auditor.

`enable(**kwargs)`

Enable the auditor.

This method lets you enable the auditor so it only records things when you want it to. Typically this is called at the beginning of a game.

Parameters:

* ****kwargs** – No function here. They just exist to allow this method to be registered as a handler for events that might contain keyword arguments.

`enabled`

Attribute that’s viewed by other core components to let them know they should send auditing events. Set this via the enable() and disable() methods.
