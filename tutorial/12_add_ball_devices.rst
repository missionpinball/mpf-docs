Tutorial step 12: Add the rest of your ball devices
===================================================

Now that you've added all your switches and coils, you'll probably
notice that the ball is *still* getting stuck in devices on the
playfield when it enters them. This is because MPF doesn't know that
certain switches and coils are associated with ball devices, so MPF
doesn't know that it should fire a coil when a certain switch becomes
active. So the next step is to create configuration entries for the
rest of your ball devices.

The good news is that once you do this, a
ball entering a device will automatically be ejected, so when you're
done with this step, your ball shouldn't get stuck anywhere.

To do
this, take a look at all the ball devices around your playfield and
then create entries for each one in the *ball_devices:* section of
your config file. Depending on your machine, you might have 5 or 6 of
these. (Ball devices are anything where the ball could go where it's
held and not actively rolling around on the playfield.) At a bare
minimum, you need to add ``ball_switches:``, ``eject_coil:``, and
``eject_timeouts:`` settings for each ball device you add. The
``eject_timeouts:`` entry is critical, because if a ball ejects to the
playfield but then doesn't hit a switch right away, this is the how
long MPF will wait before assuming the ball made it out of the device
successfully. (Again, set this timeout to be the longest amount of
time that could pass with a ball failing to eject and falling back
in.) Simple playfield kickouts might be fine with 500ms or 750ms, and
VUKs might be around 2 or 3 seconds.

After you add all your ball
devices, you should be able to play a game without the ball getting
stuck anywhere! (And if you start MPF with balls already stuck in
devices, MPF will automatically eject the balls when it boots because
these additional devices do not have "home" listed as one of their
tags.) Here's the ``ball_devices:`` section from a *Demolition Man*
config file:

.. code-block:: mpf-config

    #! switches:
    #!   s_trough1:
    #!     number: 1
    #!   s_trough2:
    #!     number: 2
    #!   s_trough3:
    #!     number: 3
    #!   s_trough4:
    #!     number: 4
    #!   s_trough5:
    #!     number: 5
    #!   s_trough6:
    #!     number: 6
    #!   s_trough_jam:
    #!     number: 7
    #!   s_plunger_lane:
    #!     number: 8
    #!   s_eject:
    #!     number: 9
    #!   s_bottom_popper:
    #!     number: 10
    #!   s_top_popper:
    #!     number: 11
    #!   s_elevator_hold:
    #!     number: 12
    #! coils:
    #!   c_trough_eject:
    #!     number: 0
    #!   c_plunger_eject:
    #!     number: 1
    #!   c_retina_eject:
    #!     number: 2
    #!   c_bottom_popper:
    #!     number: 3
    #!   c_top_popper:
    #!     number: 4
    ball_devices:
      bd_trough:
        tags: trough, home, drain
        ball_switches: s_trough1, s_trough2, s_trough3, s_trough4, s_trough5, s_trough_jam
        eject_coil: c_trough_eject
        entrance_count_delay: 300ms
        jam_switch: s_trough_jam
        eject_targets: bd_plunger
        debug: true

      bd_plunger:
        ball_switches: s_plunger_lane
        entrance_count_delay: 300ms
        eject_timeouts: 3s
        eject_coil: c_plunger_eject
        player_controlled_eject_event: sw_launch

      bd_retina_hole:
        ball_switches: s_eject
        eject_coil: c_retina_eject
        eject_timeouts: 1s

      bd_lower_vuk:
        ball_switches: s_bottom_popper
        eject_coil: c_bottom_popper
        eject_timeouts: 2s

      bd_upper_vuk:
        ball_switches: s_top_popper
        eject_coil: c_top_popper
        eject_timeouts: 2s

      bd_elevator:
        ball_switches: s_elevator_hold
        mechanical_eject: true
        eject_timeouts: 500ms

    playfields:
      playfield:
        tags: default
        default_source_device: bd_plunger

Remember that if you need to adjust the eject coil pulse time, you do
that in the coil's property in the ``coils:`` section of your config
file, not in the ball device configuration.

Check out the complete config.yaml file so far
----------------------------------------------

If you want to see a complete ``config.yaml`` file up to this point, it's in the ``mpf-examples/tutorial/step_12``
folder.

You can run this file directly by switching to that folder and then running the following command:

.. code-block:: doscon

   C:\mpf-examples\tutorial>mpf both
