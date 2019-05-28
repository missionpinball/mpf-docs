accruals:
=========

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

See also :doc:`accruals </game_logic/logic_blocks/accruals>`.

The structure of accrual logic blocks are like this:

.. code-block:: yaml

  accruals:
     the_name_of_this_logic_block:
        <settings>
     some_other_logic_block:
        <settings>
     a_third_logic_block:
        <settings>

Note that the actual name of the logic block doesn't really matter. Mainly
they're used in the logs.


Required settings
-----------------

The following sections are required in the ``accruals:`` section of your config:

events:
~~~~~~~
List of one (or more) values, each is a type: ``string``.

The events section of an accrual logic block is where you define the
events this logic block will watch for in order to make progress towards
completion.

The real power of logic blocks is that you can enter more than one
event for each step, and *only one* of the of the events of that step has to
happen for that step to be complete.

Another way to look at it is that there's an *AND* between all the steps.
For the Accrual to complete, you need Step 1 *AND* Step 2 *AND* Step 3.
But since you can enter more than one event for each step, you could think of
those like *OR*s. So you have Step 1 (event1 *OR* event2) *AND* Step 2 (event3)
*AND* Step 3 (event4 *OR* event5), like this:

.. code-block:: mpf-config

   accruals:
      my_accrual:
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

  accruals:
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
steps that need to complete (in any order since we're dealing with accrual logic
blocks), and each step only has one event that will mark is as complete. So basically
any of those five events 1-5 can be posted in any order, and then *logic_block_1_done*
will be posted.

In the second example, if event 1, 2, or 3 is posted, that will count for step 1, and then
both events 4 and 5 need to be posted for steps 2 and 3. (Again, in any order.)

So in the second one, you could get event4, event2, then event5 posted, for example,
and that will lead to *logic_block_2_done* being posted.

Note that you can have two logic blocks with the same events at the same time, and
MPF will track the state of each logic block separately. So in the above config with
those two logic blocks, if the events were posted in the order event2, event3, event4,
then event5, that would complete logic block 2. Then later if event1 was posted, that
would complete logic block 1.

Optional settings
-----------------

The following sections are optional in the ``accruals:`` section of your config. (If you don't include them, the default will be used).

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

Currently unused.


.. include:: /game_logic/logic_blocks/player_variable.rst

.. include:: /game_logic/logic_blocks/common.rst
