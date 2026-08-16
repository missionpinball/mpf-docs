---
title: "CFE-ConfigValidator-1: Section not valid outside of game modes"
---

# CFE-ConfigValidator-1: Section not valid outside of game modes

This error occurs when MPF needs to reference player variables in a
device but you defined the device in a non-game
[mode](../config/mode.md) (i.e. with
`game_mode: false`) such as the attract mode. Game modes will always end
when the game ends. Non-game modes can run all the time but they should
not access player variables as they do not exist outside of a game.
Certain devices enforce the latter.

## Examples

For instance, a [counter](../config/counters.md) can store its state in a player variable which is only
possible in a game mode:

``` yaml
##! mode: my_game_mode
mode:
  start_events: ball_started
  stop_events: ball_stopped
  game_mode: true    # this is the default

counters:
  counter_per_player:
    count_events: count_up
    persist_state: true
```

However, if you set `persist_state: False` in your counter it can also
be used outside of a mode:

``` yaml
##! mode: attract
mode:
  game_mode: false

counters:
  counter_outside_of_a_game:
    count_events: count_up
    persist_state: false
```

Those settings are described in the
[config reference](../config/index.md) of your
device.

## Common Pitfalls

### Variable_Players

[Variable player](../config/variable_player.md) will by default use player variables. However, if you use
`action: add_machine` or `action: set_machine` you can also use it to
add/set machine variables which work in non-game modes.

### Attract Mode

Attract mode only runs outside of a game so you cannot reference player
here. However, you can use machine variables

### Match Mode and High Score Mode

Those modes run at game end and are technically no longer game modes.
Therefore, you cannot reference a player here. You might want to put
your stuff into a custom mode which run at ball end (but not game end)
instead (i.e. the bonus mode). Alternatively, you might want to use
machine variables instead of player variables.

## Need more help troubleshooting?

Have a look at our [Troubleshooting](../troubleshooting/index.md) section. It might give you some hints for certain classes of
problems.

## What if this did not fix your problem?

Please tell us about your error in the [community forum](../community/index.md) and we might
be able to update this page afterwards. Or even better:
[You help us to update it afterwards](../about/help_docs.md).

## Is something missing here? Do you have a helpful hint for others experiencing this error?

Please
[create a Pull Request and add it](../about/help_docs.md). Alternatively, please tell us in the [community forum](../community/index.md).

## Related How To guides

* [Logic Blocks](../game_logic/logic_blocks/index.md)
* [config reference](../config/index.md)
