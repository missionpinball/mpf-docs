Counter Logic Blocks
====================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/counters`                                                      |
+------------------------------------------------------------------------------+

+------------------------------------------------------------------------------+
| Related How To Guides                                                        |
+==============================================================================+
| :doc:`integrating_logic_blocks_and_shows`                                    |
+------------------------------------------------------------------------------+
| :doc:`/game_logic/logic_blocks/scoring_based_on_logic_blocks`                |
+------------------------------------------------------------------------------+
| :doc:`/game_logic/logic_blocks/integrating_logic_blocks_and_lights`          |
+------------------------------------------------------------------------------+
| :doc:`/game_logic/logic_blocks/integrating_logic_block_and_slides`           |
+------------------------------------------------------------------------------+
| :doc:`/game_logic/logic_blocks/persisting_state_in_a_player_variable`        |
+------------------------------------------------------------------------------+

"Counters" are :doc:`logic blocks </game_logic/logic_blocks/index>`
that track the number of times a certain event happens towards the
progress of a completion goal.

Examples include:

* Hit a target (or shot) X number of times to advance.
* Hit pop bumpers 75 times to start a Super Jets mode.
* Counting the number of combos made
* Keeping track of a bonus multiplier (maybe you use the shot group lane
  completion event to count progress towards the bonus multiplier, but you
  configure the max count to be 6, and then if it's hit again, you award
  an extra ball).

You can use optional parameters to specify whether multiple occurrences in
a very short time window should be grouped together and counted as one
hit, the counting interval, and whether this counter counts up or
down.

Here's an example of a counter you could use to track progress towards super
jets:

.. code-block:: mpf-config

  ##! mode: my_mode
  counters:
    super_jets:
      count_events: sw_pop
      events_when_hit: pop_hit
      starting_count: 75
      count_complete_value: 0
      direction: down
      events_when_complete: super_jets_start

And here's the logic block we use for the :doc:`Addams Family mansion awards </cookbook/TAF_mansion_awards>`
to make sure the mansions is initialized only once per game:

.. code-block:: mpf-config

  ##! mode: my_mode
  counters:
    initialize_mansion:
      count_events: mode_chair_lit_started
      events_when_complete: initialize_mansion
      count_complete_value: 1
      persist_state: true

Monitorable Properties
----------------------

For :doc:`dynamic values </config/instructions/dynamic_values>` and
:doc:`conditional events </events/overview/conditional>`,
the prefix for ball holds is ``device.counters.<name>``.

*value*
   The count of this counter.

*enabled*
   Boolean (true/false) which shows whether this counter is enabled.

*completed*
   True if the block is completed. Otherwise False.

This is an example:

.. code-block:: mpf-config

   ##! mode: my_mode
   counters:
     test_counter:
       count_events: count_up
       reset_on_complete: false
       count_complete_value: 3
   event_player:
     test_event{device.counters.test_counter.value > 1}: count_above_one
     test_event{device.counters.test_counter.completed}: count_completed
   ##! test
   #! start_game
   #! start_mode my_mode
   #! mock_event count_above_one
   #! mock_event count_completed
   #! post test_event
   #! assert_event_not_called count_above_one
   #! post count_up
   #! assert_int_condition 1 device.counters.test_counter.value
   #! post test_event
   #! assert_event_not_called count_above_one
   #! post count_up
   #! assert_int_condition 2 device.counters.test_counter.value
   #! assert_bool_condition False device.counters.test_counter.completed
   #! post test_event
   #! assert_event_called count_above_one
   #! assert_event_not_called count_completed
   #! post count_up
   #! assert_int_condition 3 device.counters.test_counter.value
   #! assert_bool_condition True device.counters.test_counter.completed
   #! post test_event
   #! assert_event_called count_completed

Related Events
--------------

* :doc:`/events/logicblock_name_complete`
* :doc:`/events/logicblock_name_hit`
* :doc:`/events/logicblock_name_updated`

.. include:: common_problems.rst
