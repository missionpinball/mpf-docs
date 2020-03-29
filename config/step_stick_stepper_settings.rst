step_stick_stepper_settings:
============================

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **NO**  |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``step_stick_stepper_settings:`` section of your config is where you
configure the :doc:`Stepstick hardware platform </hardware/stepstick/index>`.


Optional settings
-----------------

The following sections are optional in the ``step_stick_stepper_settings:`` section of your config. (If you don't include them, the default will be used).

high_time:
~~~~~~~~~~
Single value, type: ``time string (secs)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`) . Default: ``20ms``

How long should the digital output be held to high during a step pulse?
This time depends on the latency/jitter of your output and the speed your
stepper can be moved.
Usually the jitter of your output is the limiting factor.

low_time:
~~~~~~~~~
Single value, type: ``time string (secs)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`) . Default: ``20ms``

How long should the digital output be held to low after a step pulse?
This time depends on the latency/jitter of your output and the speed your
stepper can be moved.
Usually the jitter of your output is the limiting factor.
