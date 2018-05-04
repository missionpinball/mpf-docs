state_machines:
===============

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

+------------------------------------------------------------------------------+
| Related Tutorial                                                             |
+==============================================================================+
| :doc:`/game_logic/logic_blocks/integrating_logic_blocks_and_shows`           |
+------------------------------------------------------------------------------+

.. overview

The ``state_machines:`` section of your config is where you configure generic state machines.


Required settings
-----------------

The following sections are required in the ``state_machines:`` section of your config:

states:
~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``subconfig(state_machine_states)``.

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
List of one (or more) values, each is a type: sub-configurating containing state_machine_transitions settings.

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


