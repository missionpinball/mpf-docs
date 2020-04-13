state_machines:
===============

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

.. overview

The ``state_machines:`` section of your config is where you configure generic :doc:`state machines </game_logic/logic_blocks/state_machines>`.

Settings in Machine Config Files
--------------------------------

If the ``state_machines:`` section is placed in a config file, it will retain its state across games.  When the game is started, the value is initialized, and it will retain in its state until the game is turned off.  So to reset this, a transition would need to happen upon game end.

Settings in Mode Config Files
-----------------------------

If the ``state_machines:`` section is placed in a mode file, it will retain its state across balls, but will be reset to its base mode for each game.  It is player specific, and will retain the correct value fo each player in a given game.

.. config


Required settings
-----------------

The following sections are required in the ``state_machines:`` section of your config:

states:
~~~~~~~
One or more sub-entries. Each in the format of ``string`` : :doc:`state_machine_states <state_machine_states>`

List all of your states here, with their applicable settings.
Go to :doc:`state_machine_states <state_machine_states>` to see a full list of all settings under ``states:``.
For example:

.. code-block:: mpf-config

   ##! mode: my_mode
   state_machines:
     my_state:
       states:
         start:
           label: Start state
         step1:
           label:
           show_when_active:
             show: on
             show_tokens: None
           events_when_started: step1_start
           events_when_stopped: step1_stop
         step2:
           label: Step 2
       transitions:

The first state must be ``start:`` or MPF will throw errors when trying to
initialize this value (you can change this using ``starting_state`` setting).
All other states can be any string as defined by the user.

transitions:
~~~~~~~~~~~~
List of one (or more) values, each is a type: :doc:`state_machine_transitions <state_machine_transitions>`. Defaults to empty.

These move from any state to another state, including backward or back to the first step, when a given event is posted.

List all your transitions here (we start with the same steps as above):

.. code-block:: mpf-config

   ##! mode: my_mode
   state_machines:
     my_state:
       states:
         start:
           label: Start state
         step1:
           label:
           show_when_active:
             show: on
             show_tokens: None
           events_when_started: step1_start
           events_when_stopped: step1_stop
         step2:
           label: Step2
       transitions:
         - source: start
           target: step1
           events: state_machine_proceed
         - source: step1
           target: step2
           events: state_machine_proceed2
           events_when_transitioning: going_to_step2
         - source: step2
           target: start
           events: state_machine_proceed3
         - source: step1, step2
           target: start
           events: state_machine_reset


Optional settings
-----------------

The following sections are optional in the ``state_machines:`` section of your config. (If you don't include them, the default will be used).

persist_state:
~~~~~~~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

If set to true MPF will restore the state of a logic_block on mode restart.

starting_state:
~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``start``

The start state of your state machine.

console_log:
~~~~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level for the console log for this device.

debug:
~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

Set this to true to see additional debug output. This might impact the performance of MPF.

file_log:
~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level for the file log for this device.

label:
~~~~~~
Single value, type: ``string``. Default: ``%``

Name of this device in service mode.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Defaults to empty.

Not used.


.. toctree::
   :maxdepth: 1
   :hidden:

   state_machine_transitions: <state_machine_transitions>
   state_machine_states: <state_machine_states>


Related How To guides
---------------------

* :doc:`/game_logic/logic_blocks/state_machines`
* :doc:`/game_logic/skill_shot/index`
