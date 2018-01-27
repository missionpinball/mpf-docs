servos:
=======

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``servos:`` section of your config is where you specify any servo devices in
your machine, as well as configuring their range of motion and a mapping of events
that will cause the servos to move to certain positions.

Here's an example ``servos:`` section, with two servos defined called *servo1*
and *servo2*:

::

   servos:
      servo1:
         servo_min: 0.1
         servo_max: 0.9
         positions:
             0.0: servo1_down
             0.8: servo1_up
         reset_position: 0.5
         reset_events: reset_servo1
         number: 1
      servo2:
         positions:
             0.2: servo2_left
             1.0: servo2_home
         reset_position: 1.0
         reset_events: reset_servo2
         number: 2

Then for each servo in your ``servos:`` section, the following settings apply:

Required settings
-----------------

The following sections are required in the ``servos:`` section of your config:

number:
~~~~~~~
Single value, type: ``string``.

This is the number of the servo which specifies which driver output the
servo is physically connected to. The exact format used here will
depend on which control system you're using and how the servo is connected.

See the :doc:`/hardware/numbers` guide for details.

Optional settings
-----------------

The following sections are optional in the ``servos:`` section of your config. (If you don't include them, the default will be used).

debug:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

Enables more detailed debug information to be added to the log (when verbose
logging is enabled).

label:
~~~~~~
Single value, type: ``string``. Default: ``%``

A friendly name for this servo that will be used in reports and the service
menu.

platform:
~~~~~~~~~
Single value, type: ``string``. Default: ``None``

Name of the platform this servo is connected to. The default value of ``None`` means the
default hardware platform will be used. You only need to change this if you have
multiple different hardware platforms in use and this coil is not connected
to the default platform.

See the :doc:`/hardware/platform` guide for details.

positions:
~~~~~~~~~~
One or more sub-entries, each in the format of type: ``float``:``str``. Default: ``None``

This is a sub-section mapping of servo positions to MPF event names. For example:

::

  positions:
      0.1: servo1_down
      0.9: servo1_up
      0.45: servo1_mid

In MPF, servo ranges of motion are represented as numbers between 0.0 and 1.0.
So 0.0 puts the servo at the extreme end of its range on one side as set by the servo_min: 
discussed below, and 1.0 moves it to the end of motion on the other side as set by the
servo_max: as set below. You can use positions in between with
as much precision as your servo controller will allow. (For example, a value of .4444
will tell the servo to move to 44.44% of the way between its minimum and maximum
position.

The values in this ``positions:`` list represent MPF events that, when posted,
tell this servo to move to a certain position. So in the example above, when the
*servo1_up* event is posted, this servo will move to position 0.9 (90% of the way
between its min and max).

You can add as many events here as you want, and the same event can be used
for multiple servos.

reset_events:
~~~~~~~~~~~~~
One or more sub-entries, either as a list of events, or key/value pairs of
event names and delay times. (See the
:doc:`/config/instructions/device_control_events` documentation for details
on how to enter settings here.

Default: ``None``

Events in this list, when posted,

Default: ``machine_reset_phase_3, ball_starting, ball_will_end, service_mode_entered``

A list of events, or a list of events with delays, that cause the servo to
move to its reset position (discussed below).

Note that by default, *ball_starting* is a reset event, so if you don't want
the servo to reset on the start of each ball, you can override that like this:

::

  reset_events: machine_reset_phase_3, ball_will_end, service_mode_entered

reset_position:
~~~~~~~~~~~~~~~
Single value, type: ``number`` (will be converted to floating point). Default: ``0.5``

The position the servo will move to when its reset.

servo_max:
~~~~~~~~~~
Single value, type: ``number`` (will be converted to floating point). Default: ``1.0``

A numerical value that's sent to the servo which represents the servo's max
position in relation to the servo_max: set in the controllers configuration. 
The actual value for this is normalized to 0.0 to 1.0 here.
The controllers will convert it for the corresponding hardware.

Note that the position settings earlier are always 0.0 to 1.0, and the max
(and min, discussed below) are used to calculate what actual values are sent
to the servo.

So if you have ``servo_max: 1.0`` and ``servo_min: 0.5``, and then you set
the servo position to 0.5, the actual value sent will be 0.75. That position
will be converted to an actual position in the hardware controller.

servo_min:
~~~~~~~~~~
Single value, type: ``number`` (will be converted to floating point). Default: ``0.0``

Like ``servo_max:`` above, except the minimum lower-end setting for values that
are sent to the servo controller.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

Tags work like tags for any device. Nothing special here.

include_in_ball_search:
~~~~~~~~~~~~~~~~~~~~~~~
Boolean (True/False or Yes/No). Default is ``True``.

Controls whether this servo is included in ball search.

ball_search_min:
~~~~~~~~~~~~~~~~
Single value, type: ``number`` (will be converted to floating point). Default: ``0.0``

The value of the initial position that this servo will go to in ball search.

First position in ball search

ball_search_max:
~~~~~~~~~~~~~~~~
Single value, type: ``number`` (will be converted to floating point). Default: ``1.0``

The value of the second position that this servo will go to in ball search.

ball_search_wait:
~~~~~~~~~~~~~~~~~
Time value. Default ``5s``.

How long this servo will pause in each position (min and max) before moving to the other position while ball
search is active.
