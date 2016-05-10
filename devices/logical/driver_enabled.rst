Driver-enabled device
=====================

*MPF Device*


A *driver-enabled device* is a type of device that has two states
(enabled and disabled), and it's enabled by holding a driver on. (e.g.
when the driver is on, the device is enabled. When the driver is off,
it's disabled.) These are rare in modern machines but were common in
early solid state machines (up through System 11 and some early WPC
machines).

Examples of driver-enabled devices are the flippers and pop bumpers in
System 11 machines (and some early WPC machines). In those days they didn't have the computing power
to process switch activations with quick coil firings in software, yet they still
needed to be able to disable the flippers and pop bumpers when a game wasn't in
progress or when the player tilted. So they were implemented in a way
where they had a driver which they turned on to enable the flippers.
(That driver was connected to a relay.) When it was on, the flippers
were enabled. When it was off, they were disabled.

MPF has a special
device type called a driver-enabled device which is used for these
types of devices. They're configured in the `driver_enabled: </config/driver_enabled`_
section of your config files.



