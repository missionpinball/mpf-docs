
The *playfield_transfers:* section of the machine-wide config file is
where you configure `playfield transfer devices`_. This section *can*
be used in your machine-wide config files. This section *cannot* be
used in mode-specific config files. Here's an example configuration:


::

    
    playfield_transfers:
        tube:
            ball_switch: pf_tube
            captures_from: playfield
            eject_targets: lower_playfield


Settings for *playfield_transfers* include:



ball_switch:
~~~~~~~~~~~~

The name of the switch that, when activated, means that the ball has
just transferred from the *captures_from:* playfield to the
*eject_targets:* playfield.



eject_targets:
~~~~~~~~~~~~~~



captures_from:
~~~~~~~~~~~~~~



Settings that apply to all device types
---------------------------------------

There are some settings that apply to all types of devices that also
apply here.



tags:
~~~~~

A list of one or more tags that apply to this device. Tags allow you
to access groups of devices by tag name.



label:
~~~~~~

The plain-English name for this device that will show up in operator
menus and trouble reports.



debug:
~~~~~~

Set this to *true* to add lots of logging information about this shot
to the debug log. This is helpful when you’re trying to troubleshoot
problems with this shot. Default is *False*.

.. _playfield transfer devices: https://missionpinball.com/docs/mpf-core-architecture/mechs/logical-mechs/playfield-transfer/


