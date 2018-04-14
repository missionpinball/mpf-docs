sequences:
==========

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **NO**  |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

.. overview

See also :doc:`sequences </game_logic/logic_blocks/sequences>`.

Settings
--------

The structure of sequence logic blocks is like this:

.. code-block:: yaml

  sequences:
     the_name_of_this_logic_block:
        <settings>
     some_other_logic_block:
        <settings>
     a_third_logic_block:
        <settings>

Note that the actual name of the logic block doesn't really matter. Mainly
they're just used in the logs.

events:
~~~~~~~

The events section of a sequence logic block is where you define the
events this logic block will watch for in order to make progress towards
completion.

The real power of logic blocks is that you can enter more than one
event for each step, and *only one* of the of the events of that step has to
happen for that step to be complete.

Another way to look at it is that there's an *AND THEN* between all the steps.
For the Sequence to complete, you need Step 1 *AND THEN* Step 2 *AND THEN* Step 3.
But since you can enter more than one event for each step, you could think of
those like *OR*s. So you have Step 1 (event1 *OR* event2) *AND THEN* Step 2 (event3)
*AND THEN* Step 3 (event4 *OR* event5), like this:

.. code-block:: mpf-config

   ##! config: mode1
   sequences:
      my_sequence:
         events:
            - event1, event2
            - event3
            - event4, event5

It might seem kind of confusing at first, but
you can build this up bit-by-bit and figure them out as you go along.

You can enter anything you want for your events, whether it's one of
MPF's built-in events or a made-up event that another logic block
posts when it completes. (This is how you chain multiple logic blocks
together to form complex logic.)

For example:

.. code-block:: mpf-config

   ##! config: mode1
   sequences:
      logic_block_1:
         events:
            - event1
            - event2
            - event3
            - event4
            - event5
         events_when_complete: logic_block_1_done
      logic_block_2:
         events:
            - event1, event2, event3
            - event4
            - event5
         events_when_complete: logic_block_2_done

In the example above, there are two logic blocks. The first one just has five
steps that need to complete (in 1-2-3-4-5 exact order since we're dealing with
sequence logic blocks), and each step only has one event that will mark is as
complete.

In the second example, if event 1, 2, or 3 is posted, that will count for step 1, and then
both events 4 and 5 need to be posted for steps 2 and 3. (Again, in order, so event
1, 2, or 3 has to be posted before the logic block will even start looking for event 4.)

So in the second one, you could get event2, event4, then event5 posted, for example,
and that will lead to *logic_block_2_done* being posted.

Note that you can have two logic blocks with the same events at the same time, and
MPF will track the state of each logic block separately.

.. include:: /game_logic/logic_blocks/common.rst
