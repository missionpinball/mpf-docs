---
title: Player Variables Reference
---

# Player Variables Reference


Here's a list of all the different "built in"
[player variables](../game_logic/players.md) that MPF uses.

You can use these in your config files to trigger game logic or to
display as text on your display.

Video about player and machine variables:

<div class="video-wrapper">
<iframe width="560" height="315" src="https://www.youtube.com/embed/PUxEsNUGXPY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

Note that you can also create your own player variables in your configs,
and most likely your machine will have several orders of magnitude more
player variables than this list here.

That said, here's a list of the "built in" player variables and how
they work:

* [index](_index.md)
* [ball](ball.md)
* [extra_ball](../index.md)(name)_awarded](extra_ball_name_awarded)
* [extra_balls](extra_balls.md)

config_section: counters, accruals, sequences <logic_block_state
config_section: counters, accruals, sequences> (mode)_(timer)_tick
<mode_timer_tick> number <number> [random](../index.md)(x).(y) <random_x.y>
restart_modes_on_next_ball <restart_modes_on_next_ball> score
<score>

## Related Events

* [player_(name)](../events/player_player_var.md)
