Devices
=======

.. toctree::
   :hidden:

   Accelerometers <accelerometer>
   Autofire Coils <autofire_coil>
   Ball Devices <ball_device>
   Diverters <diverter>
   Drivers (Coils / Solenoids) <driver>
   Drop Targets <drop_target>
   Dual-Wound Ccils <dual_wound_coils>
   Flashers <flasher>
   Flippers <flipper>
   GI (general illumination) <gi>
   Kickback Lanes <kickback>
   Lights <light>
   LEDs <led>
   Loops / Orbits / Ramps <loop>
   Magnets <magnet>
   Playfields <playfield>
   Playfield transfers <playfield_transfer>
   Plungers <plunger>
   Pop Bumpers <pop_bumper>
   Rollover Switches <rollover>
   Score Reels <score_reel>
   Servos <servo>
   Slingshot <slingshot>
   Switches <switch>
   Stand-up Targets <target>
   Trough / Ball Drain <trough>


A *Device* is a "thing" in a pinball machine. (How's that for an explanation!)

In MPF, devices can be physical (switches, LEDs, coils), they can be logical
groupings of physical devices (this switch plus that coil equals a flipper
device).

In MPF, you configure devices in either your machine-wide or mode-specific config files.
Every device has a name, and there configuration options for each device which control
exactly how it behaves (or how its behavior changes depending on what's going on in
your game.
