Devices
=======

A *Device* is a logical piece of pinball hardware. Every pinball machine is made
up of hundreds of devices. Devices are hierarchical, meaning that certain
devices can be made of up other devices. For example, there are low-level
devices are like switches, coils, and lights. Each of these is a device with
certain properties (name, status, etc.) and methods (turn on, fire now, are you
open or closed, etc.)

Then you can group these low-level devices to create higher-level, logical
devices. For example you might group an eject coil and seven optical switches
into a ball device you call the "trough," or you might group a switch and a coil
together into a logical level device you call a "pop bumper." Even these logical
devices can be made up of other devices. A single switch low- level device might
be used to create a logical device which is a single drop target. Then you might
combine five individual drop targets, plus a reset coil, into an even higher
level logical device called a drop target bank.

Here's a list of all the devices that exist in the MPF:

Physical devices
----------------

+ Switch
+ Coil
+ Matrix Light
+ RGB LED
+ Flasher
+ GI String
+ Servo
+ Motor

Logical devices
---------------

+ Autofire Coil
+ Flipper
+ Ball Device (anything that holds balls, like the trough, plunger
  lane, playfield lock, etc.)
+ Score Reel
+ Score Reel Group
+ Drop Target
+ Drop Target bank
+ Shot
+ Shot Group
+ Diverter


Abstract Devices
----------------

+ Ball Lock
+ Ball Saver
+ Multiball


.. toctree::
   Ball device <ball_device>
   Switch <switch>
