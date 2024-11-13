
# monitor_stop (BCP command)

New in version 0.33.

Request from the media controller to the pin controller to stop monitoring events in the specified category. Once a monitor has been started, events will continue to be automatically sent to the media controller from the pin controller via BCP until they are stopped using the monitor_stop or remove_trigger commands.

## Origin
Media controller

## Parameters
### category
Single string value, type: one of the following options: events, devices, machine_vars, player_vars, switches, modes, ball, or timer.

The value of category determines the category of events to stop monitoring. Options for category are:

* `events` - All events in the pin controller
* `devices` - All device state changes
* `machine_vars` - All machine variable changes
* `player_vars` - All player variable changes
* `switches` - All switch state changes
* `modes` - All mode events (start, stop)
* `core_events` - Core MPF events (ball handing, player turn, etc.)

## Response
None
