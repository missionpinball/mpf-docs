---
title: Playfields
---

# Playfields


Related Config File Sections:

* [playfields:](../../config/playfields.md)
* [playfield_transfers:](../../config/playfield_transfers.md)

Believe it or not, the playfield in MPF is technically a
[ball device](../ball_devices/index.md).
This is needed since MPF wants to know where all the balls are at all
times, so it needs to know which balls are "in" the playfield device.

The playfield is also responsible for tracking balls that
"disappeared" from it without going into other devices----a process
which kicks off the
[ball search](../../game_logic/ball_search/index.md). The default playfield ball device (called *playfield*) is
created automatically based on settings in the `mpfconfig.yaml` default
configuration file. Most machines only have one playfield, though if you
have a mini-playfield or a head-to-head machine then you can configure
additional playfield devices.

Ball tracking and ball search is performed per playfield in MPF.
Therefore, most devices in MPF belong to one playfield and mark it as
active when they see a ball. You should configure the exact playfield
for every device as soon as you have more than one playfield in your
machine. Otherwise, MPF will complain about unexpected balls (e.g. you
will see [unexpected_ball_on_(name)](../../events/unexpected_ball_on_playfield.md) events), ball search might at the wrong time and ball
tracking might go haywire. To transfer balls you can use
[playfield transfer](playfield_transfer.md)
or [ball devices](../ball_devices/index.md). A ball device might capture from one playfield and eject to
another.
