Devices
=======

A *Device* is a "thing" in a pinball machine. (How's that for an explanation!)

In MPF, devices can be physical (switches, LEDs, coils), they can be logical
groupings of physical devices (this switch plus that coil equals a flipper device),
or they can be abstract concepts used in your game (ball locks, multiballs, ball saves, etc.)

In MPF, you configure devices in either your machine-wide or mode-specific config files.
Every device has a name, and there configuration options for each device which control
exactly how it behaves (or how its behavior changes depending on what's going on in
your game.

Here's a list of all the devices that exist in the MPF:

.. toctree::
   :maxdepth: 2
   :titlesonly:

   physical/index
   logical/index
   abstract/index
