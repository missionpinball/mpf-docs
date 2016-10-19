
The *playfields:* section of the machine-wide config file is where you
configure `playfields`_. This section *can* be used in your machine-
wide config files. This section *cannot* be used in mode-specific
config files. Here's an example of a machine with two playfields:


::

    
    playfields:
        playfield:
            tags: default
        lower_playfield:
            tags: lower


You don't have to include a playfields: section in your machine-wide
config since the *mpfconfig.yaml* default config contains the settings
for the default playfield, like this:


::

    
    playfields:
        playfield:
            tags: default


Note that there are no settings that are specific to playfields. All
you have to do is add them to the list. However, since devices in MPF
require at least one setting entry, each of the playfields in the
example above contain a *tags:* entry just so they have something to
make the syntax correct. The tags aren't actually used for anything
though. If you have multiple playfields, it's important to for one of
them to be named *playfield*. That one will be the default playfield
that other ball devices will eject their balls to if you don't
configure them with eject targets.



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

.. _playfields: https://missionpinball.com/docs/mpf-core-architecture/mechs/logical-mechs/playfield/


