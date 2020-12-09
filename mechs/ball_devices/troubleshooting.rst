Troubleshooting P-Roc/P3-Roc
============================

If you got problems in general we first recommend to read our
:doc:`troubleshooting guide </troubleshooting/index>`.
Here we go into details for ball devices (troughs, plungers, lock devices and
more) in particular.


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
