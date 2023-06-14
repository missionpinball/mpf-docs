---
title: Ball Locks
---

# Ball Locks


Related Config File Sections:

* [multiball_locks:](../config/multiball_locks.md)
* [ball_holds:](../config/ball_holds.md)

MPF supports ball locks which are used to hold a ball that has entered a
[Ball Devices](../mechs/ball_devices/index.md). To separate
use-cases MPF supports two cases of ball locks:

* [Multiball_locks](multiballs/multiball_locks.md) which lock balls for a multiball. Locked balls are no
    longer in play (i.e. deducted from ball count).
* [Ball_holds](ball_holds.md) which only hold balls temporarily. This is used to play
    animations or stop the ball during a video mode. Those balls are
    technically still in play.
