coils:
======

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``coils:`` section of your config is used to map coil
(solenoid) names to driver board outputs. You can also set the
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

Required settings
-----------------

The following sections are required in the ``coils:`` section of your config:

<name>:
~~~~~~~

Each subsection of *coils:* is the name of the coil as you'd like to
refer to it in your game code. This can really be anything you want,
but it's obviously best to pick something that makes sense.

number:
~~~~~~~
Single value, type: ``string``.

This is the number of the coil which specifies which driver output the
coil is physically connected to. The exact format used here will
depend on which control system you're using and how the coil is connected.

Click the correct link for the specifics:

* :doc:`FAST Pinball </hardware/fast/drivers>`
* :doc:`P-ROC/P3-ROC</hardware/multimorphic/drivers>`
* :doc:`OPP </hardware/opp/drivers>`
* :doc:`Existing Machines (Williams, Stern, Data East, etc. </hardware/existing_machines/index>`

Optional settings
-----------------

The following sections are optional in the ``coils:`` section of your config. (If
you don't include them, the default will be used).

allow_enable:
~~~~~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

MPF will not enable any coil at 100% power unless you also add an
``allow_enable: true`` entry to that coils' settings. We include this as
a safety precaution since many coils will burn up if you enable them
on solid, so the fact that you have to explicitly allow this for a
coil prevents you from screwing something up and accidentally enabling
a coil that isn't supposed to be enabled. If you have a ``hold_power:``
setting less than 8 (full power), then you don't need this
``allow_enable:`` entry since you are implying you want to hold the coil
by adding the *hold_power* setting. The default hold_power is 100%, so
if you just want to be able to enable a coil at 100% then just add
``allow_enable: true`` and you don't have to add a *hold_power* entry.
If you try to enable a coil that does not have *hold_power* configured
or *allow_enabled* set to true, then the coil will not actually be
enabled and you'll get a warning in your log file.

debug:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

See the :doc:`documentation on the debug setting </config/instructions/debug>`
for details.

disable_events:
~~~~~~~~~~~~~~~
List of one or more events (with optional delay timings), in the
:doc:`device control events </config/instructions/device_control_events>` format.

Default: ``None`` (Note that if you add an entry here, it will replace the default. So if you
also want the default value(s) to apply, add them too.)

Disables this coil (meaning that if it's active, it's shut off).

enable_events:
~~~~~~~~~~~~~~
List of one or more events (with optional delay timings), in the
:doc:`device control events </config/instructions/device_control_events>` format.

Default: ``None`` (Note that if you add an entry here, it will replace the default. So if you
also want the default value(s) to apply, add them too.)

Enables (holds on) this coil. This requires that *allow_enable* is true
or that a *hold_power* setting is configured.

hold_power:
~~~~~~~~~~~
Single value, type: int(0,8). Default: ``None``

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
platform for details.) This ``hold_power:`` section is optional, and you
only need it for coils you intend to hold on. In other words, if a
coil is just pulsed (which is most of them), then you don't need to
worry about this section.

label:
~~~~~~
Single value, type: ``string``. Default: ``%``

A descriptive name for this device which will show up in the service menu
and reports.

platform:
~~~~~~~~~
Single value, type: ``string``. Default: ``None``

Name of the platform this coil is connected to. The default value of ``None`` means the
default hardware platform will be used. You only need to change this if you have
multiple different hardware platforms in use and this coil is not connected
to the default platform.

See the :doc:`/hardware/platform` guide for details.

pulse_events:
~~~~~~~~~~~~~
List of one or more events (with optional delay timings), in the
:doc:`device control events </config/instructions/device_control_events>` format.

Default: ``None`` (Note that if you add an entry here, it will replace the default. So if you
also want the default value(s) to apply, add them too.)

Event(s) that pulse this coil (at its default pulse_ms and power settings).

pulse_ms:
~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings) </config/instructions/time_strings>` . Default: ``None``

The default amount of time, in milliseconds, that this coil will pulse
for. This can be overridden in other ways, but this is the default
that will be used most of the time. Default is *10ms*, which is
extremely weak, but set low for safety purposes.

pulse_power:
~~~~~~~~~~~~
Single value, type: int(``0``-``8``). Default: ``None``

The power factor which controls how much power is applied during the initial
pulse phase of the coil's activation. (Note that not all hardware platforms
support variable pulse power.) See the section on *hold_power:* above for
details.

recycle:
~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

Controls whether this coil should add a small delay before it's allowed to
be fired again. (This is used on things like pop bumpers and slingshots to
prevent "machine gunning.")

This is a boolean setting because it's implemented differently depending on
the hardware platform used. See the documentation for your specific hardware
platform if you'd like more control than what's available with the straight
on/off settings.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

Special / reserved tags for coils: *None*

See the :doc:`documentation on tags </config/instructions/tags>` for details.
