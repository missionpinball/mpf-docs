Motors
======

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/motors`                                                        |
+------------------------------------------------------------------------------+
| :doc:`/config/digital_outputs`                                               |
+------------------------------------------------------------------------------+
| :doc:`/config/switches`                                                      |
+------------------------------------------------------------------------------+

Hardware
--------

:doc:`TODO: Add a picture of a kickback </about/help_us_to_write_it>`

:doc:`/about/help_us_to_write_it`


Config
------

In this example we configure a motorized drop target bank which can move up
and down with two position switches.

.. code-block:: mpf-config

   switches:
     s_position_up:
       number:
     s_position_down:
       number:

   digital_outputs:
     c_motor_run:
       number:
       type: driver

   motors:
     motorized_drop_target_bank:
       motor_left_output: c_motor_run
       position_switches: !!omap
         - up: s_position_up
         - down: s_position_down
       reset_position: down
       go_to_position:
         go_up: up
         go_down: down

The motor can run continuously and drives a camshaft which moves the bank up
and down.
MPF will figure the position using two position switches `s_position_up` and
`s_position_down`.
To enable the motor we use a digitial_output `c_motor_run` which maps to a
driver.
On reset the bank moves down and can afterwards be commanded using the events
`go_up` and `go_down`.


The following is an example to drive the slimer in Stern Ghostbusters:

.. code-block:: mpf-config

   switches:
     s_slimer_home:
       number: 8-1
     s_slimer_away:
       number: 8-2

   digital_outputs:
     c_slimer_motor_forward:
       number: 8-3
       type: light
     c_slimer_motor_backward:
       number: 8-4
       type: light

   motors:
     ghostbusters_slimer:
       motor_left_output: c_slimer_motor_forward
       motor_right_output: c_slimer_motor_backward
       position_switches: !!omap
         - home: s_slimer_home
         - away: s_slimer_away
       reset_position: home
       go_to_position:
         slimer_home: home
         slimer_away: away

The slimer motor can move in two directions using two digital_outputs
`c_slimer_motor_forward` and `c_slimer_motor_backward` which map to
lights in Spike.
The switches `s_slimer_home` and `s_slimer_away` are used by to determine
the current position.
To command the slimer use the events `slimer_home` or `slimer_away`.


Related Events
--------------

.. include:: /events/include_motors.rst
