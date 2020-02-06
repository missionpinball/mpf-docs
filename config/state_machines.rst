state_machines:
===============

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

.. overview

+------------------------------------------------------------------------------+
| Related Tutorial                                                             |
+==============================================================================+
| :doc:`/game_logic/logic_blocks/integrating_logic_blocks_and_shows`           |
+------------------------------------------------------------------------------+

The ``state_machines:`` section of your config is where you configure generic :doc:`state machines </game_logic/logic_blocks/state_machines>`.


Required settings
-----------------

The following sections are required in the ``state_machines:`` section of your config:

states:
~~~~~~~
One or more sub-entries, each in the format of ``string`` : :doc:`state_machine_states <state_machine_states>`
List all of your states here. For examples:

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

transitions:
~~~~~~~~~~~~
List of one (or more) values, each is a type: :doc:`state_machine_transitions <state_machine_transitions>`.

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
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

If set to true MPF will restore the state of a logic_block on mode restart.

console_log:
~~~~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level for the console log for this device.

debug:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

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
List of one (or more) values, each is a type: ``string``.

Not used.


.. toctree::
   :maxdepth: 1
   :hidden:

   state_machine_transitions: <state_machine_transitions>
   state_machine_states: <state_machine_states>


