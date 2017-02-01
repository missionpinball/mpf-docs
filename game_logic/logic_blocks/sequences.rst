Sequence Logic Blocks
=====================

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

.. code-block::

    logic_blocks:
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

Settings
--------

The structure of sequence logic blocks is like this:

.. code-block:: yaml

   logic_blocks:
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

.. code-block:: yaml

   logic_blocks:
      sequences:
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

.. code-block:: yaml

   logic_blocks:
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
MPF will track the state of each logic block separately. So in the above config with
those two logic blocks, if the events were posted in the order event2, event3, event4,
then event5 were posted, that would complete logic block 2,
then later if event1 was posted, that would complete logic block 1.

player_variable:
~~~~~~~~~~~~~~~~

By default, the current "state" (or progress) of sequence logic blocks
are stored in a :doc:`player variable </game_logic/players/index>` called
*<sequence_name>_step*.
For example, a logic block called "logic_block_1" would store its state
in a player variable called *logic_block_1_step*.

However, you can use the ``player_variable:`` setting to change this to
any player variable you want.

Making this change doesn't really affect anything other than the name of the
variable. It's just for convenience if you prefer a different name.

Note that this player variable stores the state of this logic block in a numeric
value that represents which step is complete. In other words, when a sequence
logic block is just started or reset, the player variable tracking it is set to
``0``. Then that increases by one as each step is complete.

.. include:: common.rst
