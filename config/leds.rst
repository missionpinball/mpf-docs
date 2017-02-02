leds:
=====

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``leds:`` section of your config is where you...

.. todo::
   Add description.

Required settings
-----------------

The following sections are required in the ``leds:`` section of your config:

number:
~~~~~~~
Single value, type: ``string``.

This is the number of the coil which specifies which driver output the
coil is physically connected to. The exact format used here will
depend on which control system you're using and how the coil is connected.

Click the correct link for the specifics:

* :doc:`FAST Pinball </hardware/fast/leds>`
* :doc:`P-ROC/P3-ROC</hardware/multimorphic/leds>`
* :doc:`OPP </hardware/opp/leds>`
* :doc:`FadeCandy </hardware/fadecandy/index>`
* :doc:`Stern SPIKE </hardware/spike/leds>`
* :doc:`Other Existing Machines (Williams, Stern, Data East, etc. </hardware/existing_machines/index>`

Optional settings
-----------------

The following sections are optional in the ``leds:`` section of your config. (If you don't include them, the default will be used).

color_correction_profile:
~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``None``

.. todo::
   Add description.

debug:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

.. todo::
   Add description.

default_color:
~~~~~~~~~~~~~~
Single value, type: ``color`` (*color name*, *hex*, or list of values *0*-*255*). Default: ``ffffff``

.. todo::
   Add description.

fade_ms:
~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings) </config/instructions/time_strings>` . Default: ``None``

.. todo::
   Add description.

label:
~~~~~~
Single value, type: ``string``. Default: ``%``

.. todo::
   Add description.

off_events:
~~~~~~~~~~~
One or more sub-entries, either as a list of events, or key/value pairs of
event names and delay times. (See the
:doc:`/config/instructions/device_control_events` documentation for details
on how to enter settings here.

Default: ``None``

Events in this list, when posted, turn this LED off (color "black")

on_events:
~~~~~~~~~~
One or more sub-entries, either as a list of events, or key/value pairs of
event names and delay times. (See the
:doc:`/config/instructions/device_control_events` documentation for details
on how to enter settings here.

Default: ``None``

Events in this list, when posted, turn this LED on using it's ``default_color:``

platform:
~~~~~~~~~
Single value, type: ``string``. Default: ``None``

Name of the platform this LED is connected to. The default value of ``None`` means the
default hardware platform will be used. You only need to change this if you have
multiple different hardware platforms in use and this coil is not connected
to the default platform.

See the :doc:`/hardware/platform` guide for details.

polarity:
~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

.. todo::
   Add description.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

.. todo::
   Add description.

type:
~~~~~
Single value, type: ``string`` (case-insensitive). Default: ``rgb``

This describes the channel order of this LED. Can be 1 to many channels (if supported by hardware). Valid channels: r (red), g (green), b (blue), w (white=minimum of red, green and blue), + (always on), - (always off).

When using serial LEDs (e.g. with FAST or Fadecandy), use `rgb` for WS2812 and `grb` for WS2811 LEDs.

x:
~~
Single value, type: ``integer``. Default: ``None``

.. todo::
   Add description.

y:
~~
Single value, type: ``integer``. Default: ``None``

.. todo::
   Add description.

z:
~~
Single value, type: ``integer``. Default: ``None``

.. todo::
   Add description.

