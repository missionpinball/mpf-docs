Stepper Motors
==============

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/steppers`                                                      |
+------------------------------------------------------------------------------+

:doc:`TODO: Add a picture of a stepper </about/help_us_to_write_it>`

Stepper motors offer digitally controlled precise movement of mechanisms. They reqire a separate
driver board that interfaces with the host computer by USB or through the pinball machine
controller. Steppers have a unique design with two or more sets of coils which when energized 
sequentually turn the armature a set distance, typically 1.8 degrees. 

It is useful to compare stepper motors to servo motors. While in many cases they can 
be used interchangably, each has advantages and disadvantages. The principle adantage of 
steppers is precision. If used within their torque window, steppers can reproduceably count
thousand of steps, reverse them, and land back at the starting position.  Generally steppers are
faster than servo motors which transmit torque through a gear assembly. Disadvantages of steppers
include less torque than offered by servo motors and requiring a driver controller. Also, unlike
servos, steppers do not include a feedback mechanism to report the rotational angle of the 
armature. This deficit requires that a stepper use a homing mechanism (typically a switch) to 
inform software when the assembly is at an extreme of linear or rotational position.
Lastly, steppers are subject to rotational drift when not energized, whereas servos maintain
position in their off state.

Stepper controller boards require a minimum of two digital inputs, one for rotational direction 
and one to trigger a rotational step. Usually one or more additional inputs are also used to 
control the power state of the driver board and/or motor coils. Some driver boards also allow
programming of microstepping to command rotation at less than that of a full step.  

MPF abstracts the nitty gritty of stepper control allowing steppers to be used with a minimum
of YAML programming. On startup, an event is issued to rotate the motor to a home position. 
Once homed, further events can be issued which rotate the motor an arbitriary number of steps in
either direction as required by the application.

See: http://docs.missionpinball.org/en/latest/mechs/servos/index.html?highlight=servo#
