---
title: API Reference - score_queue_player
---

# score_queue_player API Reference

`self.machine.score_queue_player`

``` python
class mpf.config_players.score_queue_player.ScoreQueuePlayer(machine)
```

Bases: `mpf.core.config_player.ConfigPlayer`

SS style scoring based on config.

## Accessing the score_queue_player_player in code

The score_queue_player_player is available via `self.machine.score_queue_player`.

## Methods & Attributes

The score_queue_player has the following methods & attributes available. Note that methods & attributes inherited from the base class are not included here.

`get_express_config(value: Any) → dict`

Parse express config.

`static is_entry_valid_outside_mode(settings) → bool`

Score queue is only valid in game.

`play(settings: dict, context: str, calling_context: str, priority: int = 0, **kwargs) → None`

Variable name.

`validate_config_entry(settings: dict, name: str) → dict`

Validate one entry of this player.

## Related Pages:

* [How to implement solid state game style score queues](../../../game_logic/scoring/ss_style_score_queues.md)
* [score_queue_player: Config Reference](../../../config/score_queue_player.md)
