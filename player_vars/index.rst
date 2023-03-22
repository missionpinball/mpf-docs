Player Variables Reference
==========================

Here's a list of all the different "built in"
:doc:`player variables </game_logic/players/index>` that MPF uses.

You can use these in your config files to trigger game logic or to display as
text on your display.

Note that you can also create your own player variables in your configs, and
most likely your machine will have several orders of magnitude more player
variables than this list here.

Video about player and machine variables:

.. youtube:: PUxEsNUGXPY

That said, here's a list of the "built in" player variables and how they work:

.. toctree::
   :maxdepth: 1

   index <_index>
   ball <ball>
   extra_ball_(name)_awarded <extra_ball_name_awarded>
   extra_balls <extra_balls>
   (logic_block)_state
config_section: counters, accruals, sequences <logic_block_state
config_section: counters, accruals, sequences>
   (mode)_(timer)_tick <mode_timer_tick>
   number <number>
   random_(x).(y) <random_x.y>
   restart_modes_on_next_ball <restart_modes_on_next_ball>
   score <score>
Related Events
--------------

.. include:: /events/include_player_vars.rst
