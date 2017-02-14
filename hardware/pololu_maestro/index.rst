Pololu Maestro Servo Controller
===============================

MPF supports servos connected to Pololu Maestro servo controllers. Each Maestro
can control multiple servos, with models that control 6, 12, 18, or 24 servos.

.. image:: /hardware/images/pololu_maestro.jpg

1. Install the Pololu Maestro drivers
-------------------------------------

Just like any hardware device you connect to a computer, you need to install
the drivers so your computer can see it. It is easier to do the initial 
hardware configuration on a Windows PC. Follow the "Getting Started" section of the 
`Pololu Maestro Servo Controller User's Guide <https://www.pololu.com/docs/0J40/all>`_.
You will need to set Maestro's serial mode to USB Dual Port on the Serial Settings tab
of the Maestro Control Center.

2. Configure your hardware platform section
-------------------------------------------

Next, you need to tell MPF that you want to use the ``pololu_maestro`` platform
for servos. (MPF supports several different models of servo controllers.)

To do this, add ``servo_controllers: pololu_maestro`` to the ``hardware:`` section
of your machine-wide config file, like this:

::

   hardware:
     platform: fast
     driverboards: fast
     servo_controllers: pololu_maestro

This tells MPF that you want the default servo platform to be ``pololu_maestro``.
If you happen to be using multiple different types of servo controllers, you can
override the default by adding a ``platform:`` entry to individual servo devices
(just like any device in MPF that can have its platform overwritten in the device
config).

3. Configure the serial port
----------------------------

Next, you need to tell MPF what port the Maestro is connected to. (Note that
when you plug in the Maestro, you'll see two serial ports appear. You want to
use the first one (the lower number).

Add a section to your machine-wide config like this:

::

   pololu_maestro:
     port: COM5

On Linux or Mac, it will probably look like this:

::

   pololu_maestro:
      port: /dev/ttyACM0

4. Add your servo devices
-------------------------

Now that all your hardware is configured, you can add the actual servos to your
machine config. In MPF, servos are just like any other device (light, LEDs,
coils, etc.) You add a ``servos:`` section to your config, and then create sub
entries in there for each servo you have.

For example:

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

Okay, there's a lot going on in there. Let's break it down.

First, all these config options are explained in-depth in the :doc:`servos: section </config/servos>`
of the config file reference. But let's point out a few Maestro-specific things
here.

The ``number:`` of the servo is simply which channel on the Maestro board each
servo is connected to. These numbers start with 0, so a Micro Maestro 6 supports
six servos via numbers 0-5, the Mini Maestro 12 supports twelve servos numbered
0-11, etc.

All servo positioning in MPF is controlled via a floating point value from 0.0 to 1.0.
In other words, if you tell a servo to go to position 0.0, that will be one end
of its motion, and position 1.0 will be the other end. A value of 0.4 will tell the
servo to move to a position that's 40% along from the start limit to the stop limit, etc.

So that's universal, 0.0 - 1.0, throughout MPF.

The way servos actually move to a position is that the servo controller sends
a series of microsecond-level pulses which the servo reads and can then
translate into a certain position. The actual value of these pulses varies
depending on the servo controller and servos you actually have.

So in the MPF config for each servo, you need to configure ``servo_min:`` and
``servo_max`` values which tell MPF what numerical values it should actually
send to the servo for its minimum and maximum positions.

The only way you can know what these values are is to read the documentation that
comes with your servo controller. If you're using Windows, the Pololu Maestro
driver setup includes an app called the Maestro Control Center you can use
to send different values to the servo in real time, so you can use this to
figure out what min and max values you should use.

Since the actual vales you send to the servo are 0.0 to 1.0, MPF uses the min
and max values, plus your 0.0-1.0 number, to calculate the actual value that's
sent to the servo.

For example, if you have ``servo_min: 500`` and ``servo_max: 2000``, then you
send a value of ``0.4`` to the servo, the actual number sent will be 1100.
(2000 - 500 = 1500, 1500 x .4 = 600, 500 + 600 = 1100)

When you're figuring out your max and min values, you'll probably find that the
values which represent the full range of motion of the servo itself are actually
wider than the range of motion your servo has when it's installed in your machine.

For example, you might find that a values of 3000 and 9000 give your servo a
full 180-degree range of motion, but when installed in your machine, you might
find that the servo should only ever move between 10 degrees and 80 degrees.

In that case you'd specify ``servo_min: 3330`` and ``servo_max: 5640`` (since
you don't want to accidentally move the servo further than it's limit and
break something.) Then your MPF values of 0.0 to 1.0 will represent the actual
usable range of motion (0.0 will be 10 degrees, 0.5 will be 45 degrees, 1.0 will
be 80 degrees, etc.).

Note that the Maestro Control Center can actually write min and max values for
each servo channel to the controller itself. In that case those values will
take precedent over anything you configure in MPF. (Though the range of motion
will still be calculated based on the values in MPF.)

5. Using the servo in your game
-------------------------------

The servo's ``position:`` setting contains a list of numerical servo values
mapped to MPF events. So to move a servo in your game, just add the position
you want to the list and then post that event.

Again, see the :doc:`servos: section </config/servos>` of the config file
reference for details.

6. Future enhancements
----------------------

The Pololu Maestro servo controllers can accept speed and acceleration settings
which specify how fast the servo moves to the new position, and how (or whether)
it accelerates and decelerates when starting and stopping.

These settings have not been implemented in MPF. (They're not hard, we just
haven't done it.) So if you need them, contact us and we'll add them.)

Also the multiple Pololu Maestro controllers can be chained together (via
a single USB port). We also don't have support for that. (It requires adding
and additional address setting to the servo config.) Again if you want that,
let us know and we'll add it.
