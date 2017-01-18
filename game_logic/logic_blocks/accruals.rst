Accrual Logic Blocks
====================

Accruals are a type of :doc:`Logic Block </game_logic/logic_blocks/index>`
where you can trigger a new event based on a series of one or more other events.

Accruals are almost identical to :doc:`/game_logic/logic_blocks/sequences`, the
only difference being that the steps in an Accrual Logic Block can be completed
in any order, and the steps in a Sequence Logic Block must be completed in the
specific order they're listed.

Here are the Logic Blocks that we use for our
Big Shot pinball machine:

::

    logic_blocks:
        accruals:
            light_special:
                events:
                    - sw_eightball,
                    - drop_targets_solids_lit_complete, drop_targets_stripes_lit_complete
                events_when_complete: lighting_special, action_target_specialright_light
                enable_events: ball_started, collect_special
                disable_events: ball_ended, lighting_special
                reset_events: ball_ended, lighting_special

            collect_special:
                events:
                    - target_specialLeft_lit_hit, target_specialRight_lit_hit
                events_when_complete:
                    collect_special
                enable_events: lighting_special
                disable_events: ball_ended, collect_special
                reset_events: ball_ended, collect_special

            lighteightball:
                events:
                    - sw_eightball
                events_when_complete:
                    action_light_ball8_on
                    action_light_eightBall500_on
                enable_events: ball_started
                disable_events: ball_ended
                reset_events: ball_ended

            unlighteightball:
                events:
                    - collect_special
                events_when_complete:
                    action_light_ball8_off
                    action_light_eightball500_off
                enable_events: ball_started
                disable_events: ball_ended
                reset_events: ball_ended

            openDiverter:
                events:
                    - balldevice_eightballhole_ball_enter
                events_when_complete:
                    open_diverter
                enable_events: ball_started
                disable_events: ball_ended
                reset_events: ball_ended

Settings
--------

The structure of accrual logic blocks is like this:

.. code-block:: yaml

   logic_blocks:
      accruals:
         logic_block_1:
            <settings>
         logic_block_2:
            <settings>
         logic_block_3:
            <settings>

Note that the actual name of the logic block doesn't really matter. Mainly
it's used in the logs.

events:
~~~~~~~

This is where you configure the actual events that make up the "steps"
of your Accrual Logic Block. "Accrual" is another work for "sum" or
"total", and Accrual Logic Blocks fire their completion event after
each (and every) step has been completed. The real power of Accrual
Logic Blocks is that you can enter more than one events for each step,
and *only one* of the of the events of that step has to happen for
that step to be complete. Another way to look at it is that there's an
*AND* between all the steps. For the Accrual to complete, you need
Step 1 *AND* Step 2 *AND* Step 3. But since you can enter more than
one event for each step, you could think of those like *OR*s. So you
have Step 1 (event1 *OR* event2) *AND* Step 2 (event3) *AND* Step 3
(event4 *OR* event5). It might seem kind of confusing at first, but
you can build this up bit-by-bit and figure them out as you go along.
You can enter anything you want for your events, whether it's one of
MPF's built-in events or a made-up event that another Logic Block
posts when it completes. (This is how you chain multiple Logic Blocks
together to form complex logic.) The steps of an Accrual Logic Block
can be completed in any order. (In fact, that's the whole point. If
you want a Logic Block where the steps have to be completed in order,
that's what the Sequence Logic Blocks are for.) Read
our note about how to enter lists of lists into the config files to make sure you
get the configuration right.

player_variable:
~~~~~~~~~~~~~~~~

This lets you specify the name of the player variable that will hold
the progress for this logic block. If you don’t specify a name, the
player variable used will be called *<accrual_name>_status*.

.. include:: common.rst
