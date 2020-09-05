state_machine_states:
=====================

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **NO**  |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``state_machine_states:`` section of your config is where you configure the states of your :doc:`state machine <state_machines>`.

See :doc:`state machines </game_logic/logic_blocks/state_machines>` for details.

.. config


Optional settings
-----------------

The following sections are optional in the ``state_machine_states:`` section of your config. (If you don't include them, the default will be used).

events_when_started:
~~~~~~~~~~~~~~~~~~~~
List of one (or more) events.

The event will be posted when the state machine enters this state.
This is the entry action for this state in your finite state machine.

events_when_stopped:
~~~~~~~~~~~~~~~~~~~~
List of one (or more) events.

The event will be posted when the state machine leaves this state.
This is the exit action for this state in your finite state machine.

label:
~~~~~~
Single value, type: ``string``.

The full name/description of this state.

show_when_active:
~~~~~~~~~~~~~~~~~
Single value, type: :doc:`show_config <show_config>`.

A show which is played when the state machine is in this state.
This is kind of an entry action as you could use ``events_when_started`` and
a :doc:`show_player` to achieve the same.
It is meant as a helper because it is common to play one show per step.


Related How To guides
---------------------

* :doc:`/game_logic/logic_blocks/state_machines`
