Mode config files
=================

Modes usually start with a ``mode:`` section (see :doc:`mode </config/mode>`) which
defines their priority and when they start or stop:

.. code-block:: mpf-config

    ##! mode: mode1
    mode:
      start_events: ball_starting
      stop_events: timer_mode_timer_complete, shot_right_ramp
      priority: 300

Not all config sections can be used in your machine-wide config (see
:doc:`machine_config <machine_config>`).
Some devices may only exist in modes (usually if they require an active
game with one or more players).
You can see if this is the case at the top of the relevant
:doc:`config </config/index>` section.
For instance :doc:`extra_balls </config/extra_balls>` are player-bound and
can only be used in modes.
