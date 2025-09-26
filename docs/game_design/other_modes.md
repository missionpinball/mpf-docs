---
title: Other Game Modes
---

# Other Game Modes

There are a few very typical modes in almost all machines. These can either
run at start or all the time. There are also some common modes (with simple
implementations provided by MPF for your convenience) that run either after
a ball ends, or after a game ends.

## All the time/Before ball start

These modes run all the time or before ball start.

### Credits Mode

Count coins and denies game start on insufficient credits. See
[Coins & Credits](../game_logic/credits.md) for details. Credits must run
before a game so that credits may be managed, but also during a game because
credits may be carried between games, or award for various reasons during play.

### Attract Mode

Attract mode stops on game start, and is started again when a game ends and no further followups are running.
See [Attract (mode)](../game_logic/modes/attract.md).

### Tilt Mode

Tilt usually run the whole time. It will end the game on tilt and could be configured to
remove credits on slam tilt outside of a game. See [Tilt](../game_logic/tilt/index.md) for details.

### Service Mode

See [Service Mode](../game_logic/service_mode.md) for details. If you use the standard MPF service mode,
it is actually running all the time in preparation for service inputs, so that it can pause play and
take over control.

## Ball End Modes

See [Ball End Modes](ball_end_modes.md) for information about modes that run after each ball end, such as Bonus.

## Game End Modes

See [Game End Modes](game_end_modes.md) for information about modes that run after the game is over,
such as [High Score Mode](../game_logic/high_scores/index.md) and [Match Mode](../game_logic/match_mode.md).
