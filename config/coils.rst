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

.. code-block:: mpf-config

    coils:
      flipper_right_main:
        number: A0-B0-0
        default_pulse_ms: 30
        max_pulse_ms: 100
        default_pulse_power: 0.7
        max_pulse_power: 1.0
      flipper_right_hold:
        number: A0-B0-1
        default_hold_power: 0.25
        max_hold_power: 0.5
      knocker:
        number: A0-B1-0
        default_pulse_ms: 20
        max_pulse_ms: 100
      pop_bumper_left:
        number: A0-B1-1
        default_pulse_ms: 18
        max_pulse_ms: 100
      ball_gate:
        number: A0-B1-2
        default_hold_power: 0.375
        max_hold_power: 0.5

.. include:: /hardware/voltages_and_power/common_ground_warning.rst

The options are as follows:

.. config


Required settings
-----------------

The following sections are required in the ``coils:`` section of your config:

number:
~~~~~~~
Single value, type: ``string``. Defaults to empty.

This is the number of the coil which specifies which driver output the
coil is physically connected to. The exact format used here will
depend on which control system you're using and how the coil is connected.

See the :doc:`/hardware/numbers` guide for details.


Optional settings
-----------------

The following sections are optional in the ``coils:`` section of your config. (If you don't include them, the default will be used).

allow_enable:
~~~~~~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

MPF will not enable any coil at 100% power unless you also add an
``allow_enable: true`` entry to that coils' settings. We include this as
a safety precaution since many coils will burn up if you enable them
on solid, so the fact that you have to explicitly allow this for a
coil prevents you from screwing something up and accidentally enabling
a coil that isn't supposed to be enabled. If you have a ``default_hold_power:``
setting less than 8 (full power), then you don't need this
``allow_enable:`` entry since you are implying you want to hold the coil
by adding the *default_hold_power* setting. The default default_hold_power is 100%, so
if you just want to be able to enable a coil at 100% then just add
``allow_enable: true`` and you don't have to add a *default_hold_power* entry.
If you try to enable a coil that does not have *default_hold_power* configured
or *allow_enabled* set to true, then the coil will not actually be
enabled and you'll get an error in your log file.

default_hold_power:
~~~~~~~~~~~~~~~~~~~
Single value, type: float(0,1). Defaults to empty.

This setting lets you control how much power is sent to the coil when
it's "held" in the on position. This is an float value from 0-1 (i.e.
0% power to 100% power) which controls the relative power.

Different hardware platforms implement the hold power in different
ways, so this 0-1 *default_hold_power* setting provides a generic interface
that works with all hardware platforms. (You can also add platform-
specific settings here for more fine-grained control of how the hold
power is applied. See the How To guide for your specific hardware
platform for details.) This ``default_hold_power:`` section is optional, and you
only need it for coils you intend to hold on. In other words, if a
coil is just pulsed (which is most of them), then you don't need to
worry about this section.

This provides the default value for any enable calls on the coil. Devices
might call enable with a different power setting.

default_pulse_ms:
~~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Defaults to empty.

The default amount of time, in milliseconds, that this coil will pulse
for. This can be overridden in other ways, but this is the default
that will be used most of the time. Default is *10ms*, which is
extremely weak, but set low for safety purposes.

default_pulse_power:
~~~~~~~~~~~~~~~~~~~~
Single value, type: float(0,1). Defaults to empty.

The power factor which controls how much power is applied during the initial
pulse phase of the coil's activation. (Note that not all hardware platforms
support variable pulse power.) See the section on *default_hold_power:* above for
details. It will also used in rules.

default_recycle:
~~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

Controls whether this coil should add a small delay before it's allowed to
be fired again. (This is used on things like pop bumpers and slingshots to
prevent "machine gunning.")

This is a boolean setting because it's implemented differently depending on
the hardware platform used. See the documentation for your specific hardware
platform if you'd like more control than what's available with the straight
on/off settings.

disable_events:
~~~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

Disables this coil (meaning that if it's active, it's shut off).

enable_events:
~~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

Enables (holds on) this coil. This requires that *allow_enable* is true
or that a *default_hold_power* or *max_hold_power* setting is configured.

max_hold_power:
~~~~~~~~~~~~~~~
Single value, type: float(0,1). Defaults to empty.

This controlls the maximum allowed hold power for this this coil. While
*default_hold_power* sets the default for all enable calls on the coil
this defined the upper limit. If this is not set MPF will use *default_hold_power*.
Usually you can omit this setting.

max_pulse_ms:
~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Defaults to empty.

Maximum allowed pulse time for this coil.
If set, MPF will raise an error if any code tries to pulse the coil for more
than ``max_pulse_ms``.

max_pulse_power:
~~~~~~~~~~~~~~~~
Single value, type: float(0,1). Default: ``1.0``

Set the maxium pulse power. If pulse is called on the coil without any parameters
*default_pulse_power* is used.

platform:
~~~~~~~~~
Single value, type: ``string``. Defaults to empty.

Name of the platform this coil is connected to. The default value of ``None`` means the
default hardware platform will be used. You only need to change this if you have
multiple different hardware platforms in use and this coil is not connected
to the default platform.

See the :doc:`/hardware/platform` guide for details.

platform_settings:
~~~~~~~~~~~~~~~~~~
Single value, type: dict. Defaults to empty.

Dict of platform specific settings.
Consult your platform documentation for those settings.

psu:
~~~~
Single value, type: string name of a :doc:`psus <psus>` device. Default: ``default``

Specify to which :doc:`power supply unit <psus>` this coil is connected.
This is used for power management. In some cases, MPF can deliberately delay
coil pulses to prevent too many coils from firing and drawing to much current
from your PSU.

pulse_events:
~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

:doc:`device control events </config/instructions/device_control_events>` format.

Default: ``None`` (Note that if you add an entry here, it will replace the default. So if you
also want the default value(s) to apply, add them too.)

Event(s) that pulse this coil (at its default_pulse_ms and power settings).

console_log:
~~~~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level for the console log for this device.

debug:
~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

See the :doc:`documentation on the debug setting </config/instructions/debug>`
for details.

file_log:
~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level for the file log for this device.

label:
~~~~~~
Single value, type: ``string``. Default: ``%``

A descriptive name for this device which will show up in the service menu
and reports.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Defaults to empty.

Special / reserved tags for coils: *None*

See the :doc:`documentation on tags </config/instructions/tags>` for details.


Related How To guides
---------------------

* :doc:`/mechs/coils/index`
