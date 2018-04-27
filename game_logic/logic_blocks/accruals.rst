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


