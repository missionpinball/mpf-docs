Accrual Logic Blocks
====================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/accruals`                                                      |
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

"Accruals" are a type of :doc:`Logic Block </game_logic/logic_blocks/index>`
where you can trigger a new event based on a series of one or more other events.

Accruals are almost identical to :doc:`/game_logic/logic_blocks/sequences`, the
only difference being that the steps in an Accrual Logic Block can be completed
in any order, and the steps in a Sequence Logic Block must be completed in the
specific order they're listed.

An example might be if you have 3 different things which need to happen in your
machine, and when they're all complete, some other event is posted which
kicks off some kind of award mode.

You would use an accrual if these 3 events can happen in any order. If they
need to happen in a specific 1-2-3 sequence, then you would use a *sequence*
logic block instead. (And if you just need the same event to happen three times,
then you would use a *counter* logic block instead.

For example, let's say you had a mode where you wanted three shots to be hit,
in any order, and when they were all hit, you lit another shot. You'd use
an accrual logic block like this:

.. code-block:: mpf-config

  ##! mode: my_mode
  accruals:
    name_of_my_logic_block:
      events:
        - shot1_hit
        - shot2_hit
        - shot3_hit
      events_when_complete: enable_winning_shot

There are much more settings (as you'll see below), but the basic logic block
above (which is called "name_of_my_logic_block") will watch for the events
*shot1_hit*, *shot2_hit*, and *shot3_hit* to be posted. Once all three of them
have been posted once, this logic block will post an event called *enable_winning_shot*
which you can use to play a show, light some other shot, play a sound, award points, etc.

Again, since this is an accrual logic block, those three events can be happen in
any order. If one of them is posted twice, that's fine. It doesn't count as one of the
other events nor does it "undo" the fact that it was hit.

Monitorable Properties
----------------------

For :doc:`dynamic values </config/instructions/dynamic_values>` and
:doc:`conditional events </events/overview/conditional>`,
the prefix for ball holds is ``device.accruals.<name>``.

*value*
   The state of this accrual as list.
   There will be one entry for every element in the accrual.
   For instance, if your accrual has three elements if will be a list of len
   three with index 0 for the status of your first element, 1 for the seconds
   and 2 for the third element.
   Elements will be 0 at the beginning and turn to 1 when completed.

*enabled*
   Boolean (true/false) which shows whether this accrual is enabled.

*completed*
   True if the block is completed. Otherwise False.

This is an example:

.. code-block:: mpf-config

   ##! mode: my_mode
   accruals:
     test_accrual:
       events:
         - shot1_hit
         - shot2_hit
         - shot3_hit
       reset_on_complete: false     # this is needed for the last event player
   event_player:
     test_event{device.accruals.test_accrual.value[0]}: shot1_was_hit
     test_event{device.accruals.test_accrual.value[1]}: shot2_was_hit
     test_event{device.accruals.test_accrual.value[2]}: shot3_was_hit
     test_event{device.accruals.test_accrual.completed}: accrual_completed
   # Note: For this last conditional logic to be able to evaluate as true, the accrual setting
   # reset_on_complete must be set to No/False. Otherwise the accrual will reset instantly and this will never be true.
   ##! test
   #! start_game
   #! start_mode my_mode
   #! mock_event shot1_was_hit
   #! mock_event shot2_was_hit
   #! mock_event shot3_was_hit
   #! mock_event accrual_completed
   #! assert_bool_condition False device.accruals.test_accrual.value[0]
   #! assert_bool_condition False device.accruals.test_accrual.value[1]
   #! assert_bool_condition False device.accruals.test_accrual.value[2]
   #! post test_event
   #! assert_event_not_called shot1_was_hit
   #! assert_event_not_called shot2_was_hit
   #! assert_event_not_called shot3_was_hit
   #! post shot1_hit
   #! assert_bool_condition True device.accruals.test_accrual.value[0]
   #! assert_bool_condition False device.accruals.test_accrual.value[1]
   #! assert_bool_condition False device.accruals.test_accrual.value[2]
   #! assert_bool_condition False device.accruals.test_accrual.completed
   #! post test_event
   #! assert_event_called shot1_was_hit
   #! assert_event_not_called shot2_was_hit
   #! assert_event_not_called shot3_was_hit
   #! assert_event_not_called accrual_completed
   #! post shot3_hit
   #! post shot2_hit
   #! post test_event
   #! assert_event_called shot1_was_hit 2
   #! assert_event_called shot2_was_hit
   #! assert_event_called shot3_was_hit
   #! assert_event_called accrual_completed
   #! assert_bool_condition True device.accruals.test_accrual.value[0]
   #! assert_bool_condition True device.accruals.test_accrual.value[1]
   #! assert_bool_condition True device.accruals.test_accrual.value[2]
   #! assert_bool_condition True device.accruals.test_accrual.completed

Related Events
--------------

* :doc:`/events/logicblock_name_complete`
* :doc:`/events/logicblock_name_hit`
* :doc:`/events/logicblock_name_updated`

.. include:: common_problems.rst
