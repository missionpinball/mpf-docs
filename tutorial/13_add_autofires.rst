Tutorial step 13: Add slingshots, pop bumpers, and other "autofire" devices
===========================================================================

While we're setting up the basic playfield devices, let's configure
the "autofire" devices like slingshots and pop bumpers. (An "autofire
device" is anything where you have one switch and one coil and the
switch being hit automatically causes the coil to fire.) This makes
the game more fun since it's kind of sad to see a ball hit a slingshot
and nothing happen. You add these autofire devices in the
``autofire_coils:`` section of your machine configuration. It's pretty
simple. Just create an entry for the name you'd like to give that
device, and then add sub-entries for the ``switch:`` and ``coil:`` for
that device. For example, here's the ``autofire_coils:`` configuration
for *Demolition Man*, which has two standard slingshots, and upper
slingshot near the pop bumpers, and two pop bumpers (which we happen
to refer to as "jets" in this config):

.. code-block:: mpf-config

   #! switches:
   #!   s_left_slingshot:
   #!     number: 1
   #!   s_right_slingshot:
   #!     number: 2
   #!   s_top_slingshot:
   #!     number: 3
   #!   s_left_jet:
   #!     number: 4
   #!   s_right_jet:
   #!     number: 5
   #! coils:
   #!   c_left_slingshot:
   #!     number: 0
   #!   c_right_slingshot:
   #!     number: 1
   #!   c_top_slingshot:
   #!     number: 2
   #!   c_left_jet_bumper:
   #!     number: 3
   #!   c_right_jet_bumper:
   #!     number: 4
   autofire_coils:
     left_slingshot:
       coil: c_left_slingshot
       switch: s_left_slingshot
     right_slingshot:
       coil: c_right_slingshot
       switch: s_right_slingshot
     upper_slingshot:
       coil: c_top_slingshot
       switch: s_top_slingshot
     left_jet:
       coil: c_left_jet_bumper
       switch: s_left_jet
     right_jet:
       coil: c_right_jet_bumper
       switch: s_right_jet

Autofire devices in MPF are somewhat intelligent. They will only be
activated while a ball is in play during a game, which means they
automatically deactivate themselves during attract mode and if the
player tilts. (You can override these default settings as well as
configure additional MPF events that will cause them to activate or
deactivate. See the :doc:`/config/autofire_coils` section of the configuration
file reference for details, though you don't have to do that now.)

Remember if you want to adjust the strength of these coils, you can do
that in the coil's ``default_pulse_ms:`` setting in the ``coils:`` section of
your config.

Check out the complete config.yaml file so far
----------------------------------------------

If you want to see a complete ``config.yaml`` file up to this point, it's in the ``mpf-examples/tutorial/step_13``
folder.

You can run this file directly by switching to that folder and then running the following command:

::

   C:\mpf-examples\tutorial>mpf both
