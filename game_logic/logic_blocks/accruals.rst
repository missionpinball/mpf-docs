Accrual Logic Blocks
====================

Accruals are a type of :doc:`Logic Block </game_logic/logic_blocks/index>`
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

.. code-block:: yaml

   logic_blocks:
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

Settings
--------

The structure of accrual logic blocks are like this:

.. code-block:: yaml

   logic_blocks:
      accruals:
         the_name_of_this_logic_block:
            <settings>
         some_other_logic_block:
            <settings>
         a_third_logic_block:
            <settings>

Note that the actual name of the logic block doesn't really matter. Mainly
they're used in the logs.

events:
~~~~~~~

The events section of an accrual logic block is where you define the
events this logic block will watch for in order to make progress towards
completion.

The real power of accrual logic blocks is that you can enter more than one
event for each step, and *only one* of the of the events of that step has to
happen for that step to be complete.

Another way to look at it is that there's an *AND* between all the steps.
For the Accrual to complete, you need Step 1 *AND* Step 2 *AND* Step 3.
But since you can enter more than one event for each step, you could think of
those like *OR*s. So you have Step 1 (event1 *OR* event2) *AND* Step 2 (event3)
*AND* Step 3 (event4 *OR* event5).

It might seem kind of confusing at first, but
you can build this up bit-by-bit and figure them out as you go along.

You can enter anything you want for your events, whether it's one of
MPF's built-in events or a made-up event that another logic block
posts when it completes. (This is how you chain multiple logic blocks
together to form complex logic.)

For example:

.. code-block:: yaml

   logic_blocks:
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
any of those five events 1-5 can be posted in any order, adn then *logic_block_1_done*
will be posted.

In the second example, if event 1, 2, or 3 is posted, that will count for step 1, and then
both events 4 and 5 need to be posted for steps 2 and 3. (Again, in any order.)

So in the second one, you could get event4, event2, then event5 posted, for example,
and that will lead to *logic_block_2_done* being posted.

Note that you can have two logic blocks with the same events at the same time, and
MPF will track the state of each logic block separately. So in the above config with
those two logic blocks, if the events were posted:

event2, event3, event4, then event5 were posted, that would complete logic block 2,
then later if event1 was posted, that would complete logic block 1.

player_variable:
~~~~~~~~~~~~~~~~

By default, the current "state" (or progress) of accrual logic blocks
are stored in a :doc:`player variable </players/index>` called *<accrual_name>_status*.
For example, a logic block called "logic_block_1" would store its state
in a player variable called *logic_block_1_status*.

However, you can use the ``player_variable:`` setting to change this to
any player variable you want.

Making this change doesn't really affect anything other than the name of the
variable. It's just for convenience if you prefer a different name.

.. include:: common.rst
