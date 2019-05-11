State Machine Logic Block
=========================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/state_machines`                                                |
+------------------------------------------------------------------------------+

+------------------------------------------------------------------------------+
| Related How To Guides                                                        |
+==============================================================================+
| :doc:`integrating_logic_blocks_and_shows`                                    |
+------------------------------------------------------------------------------+

"State machines" are a type of :doc:`Logic Block </game_logic/logic_blocks/index>`
where you can trigger state transitions based on the current state and an event.

This is an example:

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
           label:
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

   ##! test
   #! start_game
   #! start_mode my_mode
   #! mock_event going_to_step2
   #! assert_str_condition start device.state_machines.my_state.state
   #! post state_machine_proceed
   #! assert_str_condition step1 device.state_machines.my_state.state
   #! assert_event_not_called going_to_step2
   #! post state_machine_proceed2
   #! assert_str_condition step2 device.state_machines.my_state.state
   #! assert_event_called going_to_step2

Monitorable Properties
----------------------

For :doc:`dynamic values </config/instructions/dynamic_values>` and
:doc:`conditional events </events/overview/conditional>`,
the prefix for ball holds is ``device.state_machines.<name>``.

*state*
   The state of this state machine as string.
   This will be on of your entries in your states section.
