external_show_start (BCP command)
=================================

Parameters: name, priority, leds, lights, flashers, gis Origin:
Mediacontroller **Response:** None Startsan externally-
controlled`hardwareshow`_ (including LEDs, lights, flashers, and/or GI
effects) with an associated show name and priority. Externally-
controlled shows provide real-time device control via
external_show_frame BCP commands. All devices that will be managed by
the show must be included in the device listparameters (leds, lights,
flashers, gis). The order in which the devices are listed in the
device listparameters is important as all subsequentdevice datavalue
updates will correspond to the order established in the show start
command. The device list parameters are optional, but at least one
must be included in order to start a valid hardware show.
Parameter Description name The name of the external show priority The
priority of the external show relative to all other hardware shows in
the pin controller. leds A comma-separated list of LED device names to
include in this show. lights A comma-separated list of light device
names to include in this show. flashers A comma-separated list of
flasher device names to include in this show. gis A comma-separated
list of GI device names to include in this show.
