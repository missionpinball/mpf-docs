---
title: Ball Tracking
---

# Ball Tracking


Keeping track of where all the balls are at any given time is a big part
of a pinball. There are four components that make up MPF's ball
tracking and management system:

* The Ball Controller, which is a core MPF module that manages
    everything.
* Individual [Ball Devices](../mechs/ball_devices/index.md)
    (troughs, locks, etc.) which track how many balls they're currently
    holding, request new balls, eject balls, etc.
* The [Playfields](../mechs/playfields/index.md) device
    which is a special type of ball device that tracks how many balls
    are loose on the playfield at any given time.
* Individual [Diverters](../mechs/diverters/index.md)
    which are integral in routing balls to devices that request them.

These four components are active at all times---regardless of whether or
not a game is in progress. In other words, if MPF is running, it's
tracking balls.

Note that tracking the number of balls on a playfield is somewhat
complex. See the [How MPF tracks the number of balls on a playfield](../mechs/playfields/ball_tracking.md) guide for important details about how this works in MPF.
