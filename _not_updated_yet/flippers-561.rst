
The *flippers:* section of the config files contains all the settings
for the flippers in a pinball machine. This sectioncan be used in your
machine-wide config files. This sectioncanbe used in mode-specific
config files. Here's an example from a *Judge Dredd* machine with four
flippers. (Note *Judge Dredd* technicallyhas four flipper buttons too,
but it's the style where you push the button part way in to flip the
lower flipper, and all the way in to flip the upper flipper too. But
as far as the game code is concerned, it sees two separate switches in
each flipper button—one that's activated via the half-press, and the
second via the full press.) Also note that flippers are kind of
complex and there's a lot of options. Read the `flippers section of
the documentation`_ for all the details. You should definitelyread
that first before digging into the configuration options here.


::

    
        flippers:
            lower_left:
                main_coil: c_flipper_lower_left_main
                hold_coil: c_flipper_lower_left_hold
                activation_switch: s_flipper_left
                eos_switch: flipperLwL_EOS
                label: Left Main Flipper
            lower_right:
                main_coil: c_flipper_lower_right_main
                hold_coil: c_flipper_lower_right_hold
                activation_switch: s_flipper_right
                eos_switch: flipperLwR_EOS
                label: Right Main Flipper
            upper_left:
                main_coil: flipperUpLMain
                hold_coil: flipperUpLHold
                activation_switch: flipperUpL
                eos_switch: flipperUpL_EOS
                label: Upper Left Flipper
            upper_right:
                main_coil: flipperUpRMain
                hold_coil: flipperUpRHold
                activation_switch: flipperUpR
                eos_switch: flipperUpR_EOS
                label: Upper Right Flipper


You configure flippers by putting a *flippers:* entry in your
configuration file. Then you create a sub-entry for each flipper. (In
the config file above, the flipper sub-entries are named *lower_left*,
*lower_right*, *upper_left*, and *upper_right*.



main_coil:
~~~~~~~~~~

The name of the main flipper coil. For flippers that only have single-
wound coils, this is where you specify that coil. In that case you
would also configure the lower-power hold option for this coil in the
` *coils:* section`_ of your config.



hold_coil:
~~~~~~~~~~

The name of the hold coil winding for dual-wound flipper coils.



activation_switch:
~~~~~~~~~~~~~~~~~~

The switch that controls this flipper. (i.e. the flipper button)



eos_switch:
~~~~~~~~~~~

If you're using an end of stroke switch with this flipper, enter the
switch name here.



use_eos:
~~~~~~~~

True or False, controls whether you're using an EOS switch



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
event documentation`_. Flippers make use of the following device
control events:



enable_events:
~~~~~~~~~~~~~~

Enables this flipper. Default is *ball_started*.



disable_events:
~~~~~~~~~~~~~~~

Disabled this flipper. Default is *ball_ending*.



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

.. _flippers section of the documentation: https://missionpinball.com/docs/mpf-core-architecture/devices/logical-devices/flipper/
.. _ section: https://missionpinball.com/docs/configuration-file-reference/coils/
.. _device control event documentation: https://missionpinball.com/docs/configuration-file-reference/important-config-file-concepts/configuring-device-control-events/


