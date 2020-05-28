Sequence Logic Blocks
=====================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/sequences`                                                     |
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

"Sequences" are a type of :doc:`Logic Block </game_logic/logic_blocks/index>`
where you can trigger a new event based on a series of one or more other events
that are first posted in a specific order.

Sequences are almost identical to :doc:`/game_logic/logic_blocks/accruals`, the
only difference being that the steps in
an Accrual Logic Block can be completed in any order, and the steps in
a Sequence Logic Block must be completed in the specific order they're
listed.

An example might be if you have to hit four shots in a specific order to complete
a mode, like this example from the World Tour mode of *Brooks 'n Dunn*:

.. code-block:: mpf-config

  ##! mode: my_mode
  sequences:
    finish_world_tour:
      events:
        - shot_north_america_hit
        - shot_south_america_hit
        - shot_europe_hit
        - shot_australia_hit
      events_when_complete: wt_done

The example above has a single sequence logic block called "finish_world_tour". When
it's enabled, it starts watching for the event *shot_north_america_hit* to be posted.
Once it's posted, then it starts watching for the event *shot_south_america_hit* to
be posted. At this point, if the europe or australia event is posted, it doesn't matter
because this is a "sequence" logic block and the events have to happen in order. So this
logic block will just sit there waiting for the current event only to be posted, and
then once it is, it moves on, and any posted before or after are just ignored.

Once all four events have been posted in order, the event *wt_done* is posted which you
can use to stop the mode or add a score or play a show or whatever you want.

Monitorable Properties
----------------------

For :doc:`dynamic values </config/instructions/dynamic_values>` and
:doc:`conditional events </events/overview/conditional>`,
the prefix for ball holds is ``device.sequences.<name>``.

*value*
   The state of this sequence as list.
   There will be one entry for every element in the sequence.
   For instance, if your sequence has three elements if will be a list of len
   three with index 0 for the status of your first element, 1 for the seconds
   and 2 for the third element.
   Elements will be 0 at the beginning and turn to 1 when completed.

*enabled*
   Boolean (true/false) which shows whether this sequence is enabled.

*completed*
   True if the block is completed. Otherwise False.

Monitorable Properties
----------------------

For :doc:`dynamic values </config/instructions/dynamic_values>` and
:doc:`conditional events </events/overview/conditional>`,
the prefix for ball holds is ``device.accruals.<name>``.

*value*
   The state of this accrual as position.
   In the beginning this will be ``0``.
   Once the first step has been completed it will be ``1``.
   Then ``2`` after the second and so on.

*enabled*
   Boolean (true/false) which shows whether this accrual is enabled.

*completed*
   True if the block is completed. Otherwise False.

This is an example:

.. code-block:: mpf-config

   ##! mode: my_mode
   sequences:
     test_sequence:
       events:
         - shot1_hit
         - shot2_hit
         - shot3_hit
       reset_on_complete: false
   event_player:
     test_event{device.sequences.test_sequence.value == 1}: shot1_was_hit
     test_event{device.sequences.test_sequence.value == 2}: shot2_was_hit
     test_event{device.sequences.test_sequence.value == 3}: shot3_was_hit
     test_event{device.sequences.test_sequence.completed}: sequence_completed
   ##! test
   #! start_game
   #! start_mode my_mode
   #! mock_event shot1_was_hit
   #! mock_event shot2_was_hit
   #! mock_event shot3_was_hit
   #! mock_event sequence_completed
   #! assert_int_condition 0 device.sequences.test_sequence.value
   #! post test_event
   #! assert_event_not_called shot1_was_hit
   #! assert_event_not_called shot2_was_hit
   #! assert_event_not_called shot3_was_hit
   #! post shot1_hit
   #! assert_int_condition 1 device.sequences.test_sequence.value
   #! assert_bool_condition False device.sequences.test_sequence.completed
   #! post test_event
   #! assert_event_called shot1_was_hit
   #! assert_event_not_called shot2_was_hit
   #! assert_event_not_called shot3_was_hit
   #! assert_event_not_called sequence_completed
   #! post shot3_hit
   #! post shot2_hit
   #! post test_event
   #! assert_event_called shot1_was_hit
   #! assert_event_called shot2_was_hit
   #! assert_event_not_called shot3_was_hit
   #! assert_event_not_called sequence_completed
   #! assert_int_condition 2 device.sequences.test_sequence.value
   #! assert_bool_condition False device.sequences.test_sequence.completed
   #! post shot3_hit
   #! post test_event
   #! assert_event_called shot1_was_hit
   #! assert_event_called shot2_was_hit
   #! assert_event_called shot3_was_hit
   #! assert_event_called sequence_completed
   #! assert_int_condition 3 device.sequences.test_sequence.value
   #! assert_bool_condition True device.sequences.test_sequence.completed

Related Events
--------------

* :doc:`/events/logicblock_name_complete`
* :doc:`/events/logicblock_name_hit`
* :doc:`/events/logicblock_name_updated`

.. include:: common_problems.rst
