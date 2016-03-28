
You can configure your `flashers`_ via the *flashers:* section of your
configuration file. This section *can* be used in your machine-wide
config files. This section *cannot* be used in mode-specific config
files. Here's an example from a Williams *Road Show* machine:


::

    
    flashers:
        f_little_flipper:
            number: c37
            label: Flasher above middle left flipper
            tags: white
        f_left_ramp:
            number: c38
            label: Flasher above Bob's Bunker
            tags: yellow
        f_back_white:
            number: c39
            flash_ms: 40
            label: Two white rear wall flashers
            tags: white
        f_back_yellow:
            number: c40
            flash_ms: 40
            label: Two yellow rear wall flashers
            tags: yellow
        f_back_red:
            number: c41
            flash_ms: 40
            label: Two red rear wall flashers
            tags: red
        f_blasting_zone:
            number: c42
            label: Blasting Zone flasher
            tags: white
        f_right_ramp:
            number: c43
            label: Flasher in front of Red
            tags: white
        f_jets_at_max:
            number: c44
            label: Playfield insert in the pop bumpers
            tags: white




<FlasherName>:
~~~~~~~~~~~~~~

Each subsection of *flashers:*is the name of the flasheras you’d like
to refer to it in your game code. This can really be anything you
want, but it’s obviously best to pick something that makes sense.



number: (required)
~~~~~~~~~~~~~~~~~~

This is the number for the flasherwhich specifies which driver output
the flasheris physically connected to. The exact format used here will
depend on whether you’re using a P-ROC or FAST controller, and what
type of driver board you’re using. (Williams WPC, System 11, Stern,
P-ROC PD-16, etc.) Since flashers are are connected to driver outputs
(just like coils), the number scheme here is identical to coils. Refer
to the ` *number:*section of the *coils:*configuration documentation`_
for details on how to enter these numbers for different platforms.
(The example file above is for WPC driver boards, which is why the
flasher numbers are in the *Cxx* format.)



flash_ms:
~~~~~~~~~

The default time, in milliseconds, that this flasher will flash for
when it's sent a "flash" command.



Device Control Events
---------------------

Device control events are events you can use to control devices. They
are configured in your machine-wide or mode config with settings that
end in *_events*. For example, if a device has a setting for
*enable_events:* and you add an event to that setting, then when that
event is posted, the device will enable. You can add single events or
lists of events to these settings, and you can also configure time-
delays for how much time passes between the event being posted and the
action to take place. Details are available in the `device control
event documentation`_. Flashers make use of the following device
control events:



flash_events:
~~~~~~~~~~~~~

Causes this flasher to flash using it's default *flash_ms:* time.
Default is *None*.



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

.. _flashers: https://missionpinball.com/docs/mpf-core-architecture/devices/low-level-devices/flasher/
.. _configuration documentation: https://missionpinball.com/docs/configuration-file-reference/coils/
.. _device control event documentation: https://missionpinball.com/docs/configuration-file-reference/important-config-file-concepts/configuring-device-control-events/


