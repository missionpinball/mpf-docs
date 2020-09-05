state_machine_transitions:
==========================

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **NO**  |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``state_machine_transitions:`` section of your config is where you configure the transitions of your :doc:`state machine <state_machines>`.

Transitions will only be available if the state machine is in one of the states listed in ``source``.
In that case the machine will transition to the state listed in ``target``.
See :doc:`state machines </game_logic/logic_blocks/state_machines>` for details.

.. config


Required settings
-----------------

The following sections are required in the ``state_machine_transitions:`` section of your config:

events:
~~~~~~~
List of one (or more) events.

If the state machine is in one of the states listed in ``source`` this event
will transition the machine to the state listed in ``target``.

source:
~~~~~~~
List of one (or more) values, each is a type: ``string``.

Transitions will only be available if the state machine is in one of the states listed in ``source``.

target:
~~~~~~~
Single value, type: ``string``.

The machine will transition to this state if it is in a state listed in
``source`` and one of the ``events`` is posted.


Optional settings
-----------------

The following sections are optional in the ``state_machine_transitions:`` section of your config. (If you don't include them, the default will be used).

events_when_transitioning:
~~~~~~~~~~~~~~~~~~~~~~~~~~
List of one (or more) events.

This event will be posted when the transition is triggered.


Related How To guides
---------------------

* :doc:`/game_logic/logic_blocks/state_machines`
