servos:
=======

*Config file section*

* Valid in machine config files: **YES**
* Valid in mode config files: **NO**

.. overview

The ``servos:`` section of your config is where you specify any servo devices in
your machine, as well as configuring their range of motion and a mapping of events
that will cause the servos to move to certain positions.

Here's an example ``servos:`` section, with two servos defined called *servo1*
and *servo2*:

::

   servos:
      servo1:
         servo_min: 3000
         servo_max: 9000
         positions:
             0.1: servo1_down
             0.9: servo1_up
         reset_position: 0.5
         reset_events: reset_servo1
         number: 1
      servo2:
         servo_min: 0
         servo_max: 10000
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

The number (or channel) of this servo. See the platform documentation or the
how to guies for your specific servo for details of how this number works, since
every platform is different.


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

The platform interface that this servo is attached to. Note that you can add
a ``servo_controllers:`` section to the ``hardware:`` section of your machine
config that's used as the default platform for servos, so you only need to add
the ``platform:`` section here if you have a servo that's not connected to your
default servo platform. (In other words, you only need this here if you have
multiple different servo platforms at the same time in your machine.)

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
So 0.0 puts the servo at the extreme end of its range on one side, and 1.0 moves
it to the end of motion on the other side. You can use positions in between with
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
One or more sub-entries, each in the format of type: ``str``:``ms``. Default: ``ball_starting``

A list of events, or a list of events with delays, that cause the servo to
move to its reset position (discussed below).

Note that by default, *ball_starting* is a reset event, so if you don't want
the servo to reset on the start of each ball, you can override that like this:

::

  reset_events: None

reset_position:
~~~~~~~~~~~~~~~
Single value, type: ``number`` (will be converted to floating point). Default: ``0.5``

The position the servo will move to when its reset.

servo_max:
~~~~~~~~~~
Single value, type: ``number`` (will be converted to floating point). Default: ``1.0``

A numerical value that's sent to the servo which represents the servo's max
position. The actually value for this will depend on your servo controller
hardware. So controllers use values like 0.0 to 1.0 here, others use values
like 3000 to 9000. So check your servo controller documentation.

Note that the position settings earlier are always 0.0 to 1.0, and the max
(and min, discussed below) are used to calculate what actual values are sent
to the servo.

So if you have ``servo_max: 9000`` and ``servo_min: 3000``, and then you set
the servo position to 0.5, the actual value sent will be 6000.

servo_min:
~~~~~~~~~~
Single value, type: ``number`` (will be converted to floating point). Default: ``0.0``

Like ``servo_max:`` above, except the minimum lower-end setting for values that
are sent to the servo controller.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

Tags work like tags for any device. Nothing special here.


