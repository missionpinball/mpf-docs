
Sequences are a type of Logic Block where you can trigger a new event
based on a series of one or more other events.They are a key part of
implementing `game logic`_ in MPF. Sequences are almost identical to
`Accrual Logic Blocks`_, the only difference being that the steps in
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
                enable_events: ball_started
                disable_events: ball_ended
                reset_events: ball_ended


Some settings for Sequence Logic Blocks apply to all logic blocks, so
you can `read about them there`_, including:


+ The “name” of the counter (e.g. “tilt” or “super_jets” in the
  examples above)
+ enable_events
+ disable_events
+ reset_events
+ events_when_complete
+ restart_on_complete
+ disable_on_complete
+ reset_each_ball


These other settings are specific to the Sequencelogic blocks:



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

.. _Accrual Logic Blocks: /docs/configuration-file-reference/accruals/
.. _game logic: https://missionpinball.com/docs/game-logic-rules/
.. _our note about how to enter lists of lists: /docs/configuration-file-reference/adding-lists-and-lists-of-lists-to-config-files/
.. _built-in events: https://missionpinball.com/docs/system-components/events/built-in-events/
.. _read about them there: https://missionpinball.com/docs/configuration-file-reference/logicblocks/%20


