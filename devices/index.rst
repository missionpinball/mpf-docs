Devices
=======

.. toctree::
   :hidden:

   Accelerometers <accelerometer>
   Autofire coils <autofire_coil>
   Ball devices <ball_device>
   Diverters <diverter>
   Drivers (Coils / Solenoids) <driver>
   Drop targets <drop_target>
   Drop target banks <drop_target_bank>
   Dual-would coils <dual_wound_coils>
   Flashers <flasher>
   Flippers <flipper>
   GI (general illumination) <gi>
   Lights <light>
   LEDs <led>
   Playfields <playfield>
   Playfield transfers <playfield_transfer>
   Score reels <score_reel>
   Score reel groups <score_reel_group>
   Servos <servo>
   Shots <shot>
   Shot groups <shot_group>
   Switches <switch>


A *Device* is a "thing" in a pinball machine. (How's that for an explanation!)

In MPF, devices can be physical (switches, LEDs, coils), they can be logical
groupings of physical devices (this switch plus that coil equals a flipper
device).

In MPF, you configure devices in either your machine-wide or mode-specific config files.
Every device has a name, and there configuration options for each device which control
exactly how it behaves (or how its behavior changes depending on what's going on in
your game.
