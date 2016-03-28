
The *autofire_coils:* section of your config file contains all the
settings for the coils which you would like to fire automatically
based on a switch activationin a pinball machine. (See the `Autofire
coils device documentation`_ for the full explanation.) This
sectioncan be used in your machine-wide config files. This
sectioncanbe used in mode-specific config files. Here’s an example:


::

    
    autofire_coils:            
        left_sling:
            coil: c_left_sling
            switch: s_left_sling
        right_sling:
            coil: c_right_sling
            switch: s_right_sling


Note that autofire coils in MPF are 1-to-1 in terms of coils-to-
switches, so a single entry is for one switch to control one coil. On
some platforms, you can have two switches control a single coil (or
two coils controlled by a single switch), but to do that you would
create two separate *autofire_coils:* entries with one coil and one
switch each. (And again, that's platform-specific. Check your hardware
platform documentation for details.) Also if you're wiring your
slingshots and you want two switches to control a single coil, on
nearly 100% of pinball machines in the world, those two switches are
wired together and use a single input, so the hardware sees them as a
single switch. (Just be sure to wire them in parallel, not series, so
that either switch closing causes the hardware to see the switch
activation.) The top-level setting is the name you can refer to this
autofire coil as, such as `left_sling:`or `right_sling:`in the example
above. Sub-options include:



coil:
~~~~~

The name of the coil you want to fire. (Actually, perhaps we should
phrase it as the name of the coil you want to change the state on,
because you can also use these autofire coil rules to cause coils to
stop firing based on a switch change.)



switch:
~~~~~~~

The name of the switch that fires that coil.



reverse_switch:
~~~~~~~~~~~~~~~

Boolean which controls whether this autofire device fires when the
switch is active or inactive. The default behavior is that the coil is
fired when the switch goes to an active state. If you want to reverse
that, so the coil fires when the switch goes to inactive, then set
this to False. (This is what you would use if you have an opto.)
Default is *False*.



pulse_ms:
~~~~~~~~~

The number of milliseconds you want this coil to pulse for. If you
don't specify a value here then it will use the default setting that
you specified for that coil in the Coils section of the configuration
file.



pulse_power:
~~~~~~~~~~~~

This is the power of the initial pulse on a 0-8 scale. (0 is 0%, 4 is
50%, 8 is 100%, etc.)



hold_power:
~~~~~~~~~~~

This is the power of the hold on a 0-8 scale. (0 is 0%, 4 is 50%, 8 is
100%, etc.)



pwn_on_ms:
~~~~~~~~~~

The number of millisecond for the "on" portion of a pwm-based hold
action. Not all platforms support this, so see your platform-specific
How To guide for details.



pwm_off_ms:
~~~~~~~~~~~

The number of millisecond for the "off" portion of a pwm-based hold
action. Not all platforms support this, so see your platform-specific
How To guide for details.



pulse_power32:
~~~~~~~~~~~~~~

A 32-bit pwm mask for the initial pulse of the coil. Not all platforms
support this, so see your platform-specific How To guide for details.



hold_power32:
~~~~~~~~~~~~~

A 32-bit pwm mask for the hold power of the coil. Not all platforms
support this, so see your platform-specific How To guide for details.



pulse_pwm_mask:
~~~~~~~~~~~~~~~

An 8-bit pwm mask for the initial pulse of the coil. Not all platforms
support this, so see your platform-specific How To guide for details.



hold_pwm_mask:
~~~~~~~~~~~~~~

An 8-bit pwm mask for the hold power of the coil. Not all platforms
support this, so see your platform-specific How To guide for details.



delay:
~~~~~~

The number of milliseconds the coil will delay before firing or
starting the coil action after the switch is activated. Note that not
all platforms support this. (The P-ROC does not. The FAST Controller
does.)



recycle_ms:
~~~~~~~~~~~

The minimum number of milliseconds you want between subsequent firings
of this same rule. Put another way, if this autofire coil rule fires,
then it will ignore additional switch actions until this `recycle_ms:`
time is up. Note that not all hardware platforms support this in the
same way. The P-ROC only has a delay option for 125ms. That is, there
is either no delay, or a 125ms delay. Nothing in the middle. The FAST
Controller lets you set the delay to whatever you want.



debounced:
~~~~~~~~~~

True or False. Whether this rule should fire based on the switch being
debounced or not. In most cases you should use False since you want
these hardware rules to fire as fast as possible, but you can use True
if you get a lot of random phantom firings.



drive_now:
~~~~~~~~~~

True or False. If True, the hardware controller will check the current
state of the switches and update the state of the coil when the rule
is applied. If False, the rule will only apply the next time the
switches change state. A good example of this is for your flipper
switches. When there's no game in progress, the autofire coil rules
for the flipper are disabled, since you don't want the flippers to
operate. Now imagine if a player holds in a flipper button and then
starts a game. If they keep holding the button, you would want the
flipper to activate as soon as they were enabled, which you would do
by settings this to True. If this was False then the hardware
controller would not apply the rule based on the current state of the
switches when the rule was activated, meaning the player would have to
release and then push the flipper button again for the first flip,
which would be weird. (By the way, the flipper example above was just
to illustrate the point of how the *drive_now:*setting works. In
reality you don't have to manually configure all your autofire coil
rules for flippers—instead you just set up the flippers in the `
*flippers:*section of the config files`_ and all the rules are set up
for you automatically.



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
event documentation`_. Autofire coils make use of the following device
control events:



enable_events:
~~~~~~~~~~~~~~

Enables this autofire coil by writing the hardware rule to the pinball
controller hardware. Default is *ball_started*.



disable_events:
~~~~~~~~~~~~~~~

Disables this autofire coil by clearing the hardware rule from the
pinball controller hardware.. Default is *ball_ending*.



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

.. _section of the config files: docs/configuration-file-reference/flippers/
.. _device control event documentation: https://missionpinball.com/docs/configuration-file-reference/important-config-file-concepts/configuring-device-control-events/
.. _Autofire coils device documentation: https://missionpinball.com/docs/mpf-core-architecture/devices/logical-devices/autofire-coil/


