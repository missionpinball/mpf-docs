Sequence Logic Blocks
=====================

Sequences are a type of :doc:`Logic Block </game_logic/logic_blocks/index>`
where you can trigger a new event
based on a series of one or more other events. Sequences
are almost identical to :doc:`/game_logic/logic_blocks/accruals`, the
only difference being that the steps in
an Accrual Logic Block can be completed in any order, and the steps in
a Sequence Logic Block must be completed in the specific order they're
listed.

::

    logic_blocks:
        sequences:
            light_special:
                events:
                    - shot_target
                    - balldevice_right_popper_ball_enter
                    - sw_leftStandup, sw_rightStandup
                events_when_complete: start_multiball

events:
~~~~~~~

This is where you configure the actual events that make up the "steps"
of your SequenceLogic Block. The real power of SequenceLogic Blocks is
that you can enter more than one eventsfor each step, and *only one*
of the of the events of that step has to happen for that step to be
complete. You can enter anything you want for your events, whether
it's one of MPF's `built-in events`_ or a made-up event that another
Logic Block posts when it completes. (This is how you chain multiple
Logic Blocks together to form complex logic.) The steps of a
SequenceLogic Block mustbe completed in order. (If you want a Logic
Block where the steps can becompleted in any order, that's what the
AccrualLogic Blocks are for.) Read `our note about how to enter lists
of lists`_ into the config files to make sure you get the
configuration right. In the example above, the `shot_target`event has
to fire first, then a ball has to enter the right popper, then the
player has to hit either the right or left standup


player_variable:
~~~~~~~~~~~~~~~~

This lets you specify the name of the player variable that will hold
the progress for this logic block. If you don’t specify a name, the
player variable used will be called `<sequence_name>_status`.

.. include:: common
