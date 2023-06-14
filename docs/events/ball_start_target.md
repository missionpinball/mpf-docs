---
title: ball_start_target
---

# ball_start_target


--8<-- "event.md"

Posted when a new ball starts and is ready to be physically ejected to
the playfield.

This is a relay event.

## Keyword arguments

(See the [Conditional Events](overview/conditional.md)
guide for details for how to create entries in your config file that
only respond to certain combinations of the arguments below.)

`target`

:   The name of the ball_device target where the ball will be ejected
    to. Can be modified by a relay event handler to change the target
    before the ball is ejected.
