
While we're setting up the basic playfield devices, let's configure
the "autofire" devices like slingshots and pop bumpers. (An "autofire
device" is anything where you have one switch and one coil and the
switch being hit automatically causes the coil to fire.) This makes
the game more fun since it's kind of sad to see a ball hit a slingshot
and nothing happen. You add these autofire devices in the
`autofire_coils:` section of your machine configuration. It's pretty
simple. Just create an entry for the name you'd like to give that
device, and then add sub-entries for the `switch:` and `coil:` for
that device. For example, here's the `autofire_coils:` configuration
for *Demolition Man*, which has two standard slingshots, and upper
slingshot near the pop bumpers, and two pop bumpers (which we happen
to refer to as "jets" in this config):


::

    
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
deactivate. See the ` `autofire_coils:` section`_ of the configuration
file reference for details, though you don't have to do that now.)
Remember if you want to adjust the strength of these coils, you can do
that in the coil's `pulse_ms:` setting in the ` `coils:` section`_ of
your config. As in previous steps,if you want to see a complete
`config.yaml` file up to this point, it’s available in the MPF package
at `<your_mpf_root>/machine_files/tutorial/config/step14.yaml`. (You
need to rename this file to `config.yaml` to use it.) And remember if
you’re using physical hardware, your coil and switch numbers will be
different than the ones in the sample file, since you’ll need to
configure them based on your driver boards’ actual inputs and outputs.

.. _ section: https://missionpinball.com/docs/configuration-file-reference/coils/
.. _ section: https://missionpinball.com/docs/configuration-file-reference/autofire-coils/


