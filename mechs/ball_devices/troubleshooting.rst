Troubleshooting P-Roc/P3-Roc
============================

If you got problems in general we first recommend to read our
:doc:`troubleshooting guide </troubleshooting/index>`.
Here we go into details for ball devices (troughs, plungers, lock devices and
more) in particular.

Add debug
---------

First, add a ``debug: true`` entry into your trough config in the
``ball_devices:`` section. Then when you run with verbose logging (``-v``),
you'll get extra debugging information in the log.

Received unexpected ball
------------------------

You might get a line in your log telling your that the device received an
unexpected ball.
This is usually not an issue.
It means that the device did not expect the ball.
For instance, if a ball drains into a trough or jumps into the shooter that
is unexpected for the device.
In most cases you will see this message when a ball drained.

So what are expected balls?
In modern machines the trough ejects a ball into the shooter lane in which case
the shooter lane device expects the ball from the trough.
This is connected to ball tracking and retry behaviour of devices.

Ball Count Does Not Match
-------------------------

If your log file shows a number of balls contained in your trough that
doesn't match how many balls you actually have, that could be:

* You didn't add all the ball switches to the *ball_switches:*
  section of the trough configuration
* You're using a physical machine but a switch isn't adjusted
  properly so the ball is not actually activating it. (Seriously, we
  can't tell you how many times that's happened! We've also found that
  on some machines, if you only have one ball in the trough that the
  single ball isn't heavy enough to roll over the top of the eject coil
  shaft. In that case we just add a few more balls to the machine and it
  seems to take care of it.) Either way, if you have a ball in the
  trough, the switch entry in your log should show that the switch is
  active (*State:1*), like this:

::

    2014-10-27 20:05:29,891 : SwitchController : <<<<< switch: trough1, State:1 >>>>>

If you see State:1 immediately followed by another entry with State:0,
that means the ball isn't activating the switch even though it might
be in the trough.


.. include:: ../include_troubleshooting.rst
