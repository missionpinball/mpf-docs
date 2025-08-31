---
title: Player Variables Reference
---

# Player Variables Reference

Here's a list of all the different "built in"
[player variables](../game_logic/players.md) that MPF uses.

You can use these in your config files to trigger game logic or to
display as text on your display.

### Video about player and [machine variables](../machine_vars/index.md):

<div class="video-wrapper">
<iframe width="560" height="315" src="https://www.youtube.com/embed/PUxEsNUGXPY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Related Configs

* [player_vars: Config Reference](../config/player_vars.md)
* [variable_player: Config Reference](../config/variable_player.md)

Note that you can also create your own player variables in your configs,
and most likely your machine will have several orders of magnitude more
player variables than this list here.

That said, here's a list of the "built in" player variables and how
they work:

* [index](_index.md)
* [ball](ball.md)
* [extra_ball_(name)_awarded](extra_ball_name_awarded.md)
* [extra_balls](extra_balls.md)
* [logic_block_state](logic_block_state.md)
* [(mode)\_(timer)\_tick](mode_timer_tick.md)
* [number](number.md)
* [random_(x).(y)](random_x.y.md)
* [restart_modes_on_next_ball](restart_modes_on_next_ball.md)
* [score](score.md)

## Related Events

* [player_(var_name)](../events/player_player_var.md)
