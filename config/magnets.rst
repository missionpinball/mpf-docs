magnets:
========

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+


The ``magnets:`` section of your machine config is used to define magnet
mechanisms from coils and (optionally) switches. There are settings that
control the timing of grabbing, releasing, and "flinging" the ball.

Example:

.. literalinclude:: /example_configs/magnet/config/config.yaml
   :caption: `/config/config.yaml </_static/magnet/config/config.yaml>`_
   :language: yaml

magnet_coil:
------------

The string name of the coil associated with this magnet. Note that this must
be a coil listed in the :doc:`/config/coils` section of your machine config
file.

This setting is required.

Note that is any of the magnet activation times are longer than 255ms and the
magnet pulse power is 100%, then you will need to add ``allow_enable: true``
to the coil's entry in the ``coils:`` section of the machine config.

grab_switch:
------------

The name of a switch (from the :doc:`/config/switches` section of your machine
config file) that, when activated, causes the magnet to activate to (try to)
grab the ball.

Default: ``None``

grab_time:
----------
Single value, type: ``time string (ms)``
(:doc:`Instructions for entering time strings) </config/instructions/time_strings>`).

Default: ``1.5s``

How long the magnet will be energized when attempting to grab a ball.

release_time:
-------------
Single value, type: ``time string (ms)``
(:doc:`Instructions for entering time strings) </config/instructions/time_strings>`).

Default: ``500ms``

How long the magnet disables to release a ball.

fling_drop_time:
----------------
Single value, type: ``time string (ms)``
(:doc:`Instructions for entering time strings) </config/instructions/time_strings>`).

Default: ``250ms``

How long the magnet is deactivated for before the "fling_regrab_time" when it's
flinging a ball.

fling_regrab_time:
------------------
Single value, type: ``time string (ms)``
(:doc:`Instructions for entering time strings </config/instructions/time_strings>`).

Default: ``50ms``

How long the "second" (fling) pulse is for when a magnet is flinging a ball
after its dropped it.

enable_events:
--------------
One or more sub-entries, either as a list of events, or key/value pairs of
event names and delay times. (See the
:doc:`/config/instructions/device_control_events` documentation for details
on how to enter settings here).

Default: ``None``

These events enable the magnet to grab a ball based on the ``grab_switch:``
being activated.

disable_events:
---------------
One or more sub-entries, either as a list of events, or key/value pairs of
event names and delay times. (See the
:doc:`/config/instructions/device_control_events` documentation for details
on how to enter settings here).

Default: ``None``

These events mean the magnet will no longer try to grab a ball if the
``grab_switch:`` is activated.

reset_events:
-------------
One or more sub-entries, either as a list of events, or key/value pairs of
event names and delay times. (See the
:doc:`/config/instructions/device_control_events` documentation for details
on how to enter settings here).

Default: ``machine_reset_phase_3, ball_starting``

These events release a grabbed ball and disable the magnet.

grab_ball_events:
-----------------
One or more sub-entries, either as a list of events, or key/value pairs of
event names and delay times. (See the
:doc:`/config/instructions/device_control_events` documentation for details
on how to enter settings here).

Default: ``None``

These events cause the magnet to immediately attempt to grab a ball. The
magnet will be activated for the ``grab_time:``.

release_ball_events:
--------------------
One or more sub-entries, either as a list of events, or key/value pairs of
event names and delay times. (See the
:doc:`/config/instructions/device_control_events` documentation for details
on how to enter settings here).

Default: ``None``

These events cause the magnet to deactivate for the ``release_time:`` setting.

fling_ball_events:
------------------
One or more sub-entries, either as a list of events, or key/value pairs of
event names and delay times. (See the
:doc:`/config/instructions/device_control_events` documentation for details
on how to enter settings here).

Default: ``None``
