
The `coils:` section of the config files is used to map coil
(`solenoid`_) names to driver board outputs. We can also set the
default pulse times, set tags, and specify power levels for coils that
get held on. This section *can* be used in your machine-wide config
files. This section *cannot* be used in mode-specific config files.
Here's an example section:


::

    
    coils:
        flipper_right_main:
            number: A0-B0-0
            pulse_ms: 30
            tags:
        flipper_right_hold:
            number: A0-B0-1
            tags:
        knocker:
            number: A0-B1-0
            pulse_ms: 20
            tags:
        pop_bumper_left:
            number: A0-B1-1
            pulse_ms: 18
            tags: ball_search
        ball_gate:
            number: A0-B1-2
            hold_power: 3
            tags: ball_search


The options are as follows:



<name>:
~~~~~~~

Each subsection of *coils:* is the name of the coil as you'd like to
refer to it in your game code. This can really be anything you want,
but it's obviously best to pick something that makes sense.



number: (required)
~~~~~~~~~~~~~~~~~~

This is the number of the coil which specifies which driver output the
coil is physically connected to. The exact format used here will
depend on whether you're using a P-ROC or FAST controller, and what
type of driver board you're using. See the platform-specific how to
guides for details:


+ `FAST Pinball Controller driver numbering`_
+ `P-ROC driver numbering`_
+ `P3-ROC driver numbering`_
+ WPC driver numbering (keep reading below)




WPC driver board number format
``````````````````````````````

If you're using a WPC driver board (like if you dropped your P-ROC or
FAST controller into an existing pinball machine), you can enter the
coil number from the operators manual and the P-ROC platform driver
code will convert it to the proper driver number. In this case you'd
preface them with the letter 'C'. Here's an example from a Williams
Judge Dredd machine:


::

    
     trip_drop_target:
         number: C10
         tags:
     diverter:
         number: C11
         tags:
     trough:
         number: C13
     sling_left: 
         number: C15
         tags:
     sling_right: 
         number: C16
         tags:


In the case of WPC driver boards, you can also specify coil numbers
for flipper coils connected to a Fliptronics board. For example (again
from Judge Dredd):


::

    
    flipper_lower_right_main: 
         number: FLRM
     flipper_lower_right_hold: 
         number: FLRH
     flipper_lower_left_main: 
         number: FLLM
     flipper_lower_left_hold: 
         number: FLLH
     flipper_upper_right_main: 
         number: FURM
     flipper_upper_right_hold: 
         number: FURH
     flipper_upper_left_main: 
         number: FULM
     flipper_upper_left_hold: 
         number: FULH




pulse_ms:
~~~~~~~~~

The default amount of time, in milliseconds, that this coil will pulse
for. This can be overridden in other ways, but this is the default
that will be used most of the time. Default is *10ms*, which is
extremely weak, but set low for safety purposes.



hold_power:
~~~~~~~~~~~

This setting lets you control how much power is sent to the coil when
it's "held" in the on position. This is an integer value from 0-8
which controls the relative power:


+ 0: 0% power (e.g. "off")
+ 1: 12.5%
+ 2: 25%
+ 3: 37.5%
+ 4: 50%
+ 5: 62.5%
+ 6: 75%
+ 7: 87.5%
+ 8: 100% (see the "allow_enable" section below)


Different hardware platforms implement the hold power in different
ways, so this 0-8 *hold_power* setting provides a generic interface
that works with all hardware platforms. (You can also add platform-
specific settings here for more fine-grained control of how the hold
power is applied. See the How To guide for your specific hardware
platform for details.) This `hold_power:` section is optional, and you
only need it for coils you intend to hold on. In other words, if a
coil is just pulsed (which is most of them), then you don't need to
worry about this section.



allow_enable:
~~~~~~~~~~~~~

MPF will not enable any coil at 100% power unless you also add an
`allow_enable: true` entry to that coils' settings. We include this as
a safety precaution since many coils will burn up if you enable them
on solid, so the fact that you have to explicitly allow this for a
coil prevents you from screwing something up and accidentally enabling
a coil that isn't supposed to be enabled. If you have a `hold_power:`
setting less than 8 (full power), then you don't need this
`allow_enable:` entry since you are implying you want to hold the coil
by adding the *hold_power* setting. The default hold_power is 100%, so
if you just want to be able to enable a coil at 100% then just add
`allow_enable: true` and you don't have to add a *hold_power* entry.
If you try to enable a coil that does not have *hold_power* configured
or *allow_enabled* set to true, then the coil will not actually be
enabled and you'll get a warning in your log file.



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
event documentation`_. Coils make use of the following device control
events:



enable_events:
~~~~~~~~~~~~~~

Enabled (hold on) this coil. This requires that *allow_enable* is true
or that a *hold_power* setting is configured. Default is *None*.



disable_events:
~~~~~~~~~~~~~~~

Disables this coil (meaning that if it's active, it's shut off).
Default is *None*.



pulse_events:
~~~~~~~~~~~~~

Pulses this coil for the default pulse_ms milliseconds. Default is
*None*.



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

.. _P-ROC driver numbering: https://missionpinball.com/docs/howto/how-to-use-a-p-roc-with-mpf/
.. _solenoid: http://www.pinballmedic.net/coil_chart.html
.. _FAST Pinball Controller driver numbering: https://missionpinball.com/docs/howto/how-to-use-a-fast-pinball-controller-with-mpf/
.. _P3-ROC driver numbering: https://missionpinball.com/docs/howto/how-to-use-a-p3-roc-with-mpf/
.. _device control event documentation: https://missionpinball.com/docs/configuration-file-reference/important-config-file-concepts/configuring-device-control-events/


