---
title: Playfield transfer
---

# Playfield transfer


Related Config File Sections:

* [playfields:](../../config/playfields.md)
* [playfield_transfers:](../../config/playfield_transfers.md)

*MPF Device*

If you want to track balls across multiple playfields you can use a
[playfield_transfer](../../config/playfield_transfers.md) device to move a ball from one playfield to another. This is
mostly useful in head2head games. However, you can also use it to track
balls on a mini-playfield. In some cases you can also use a
[ball_device](../../config/ball_devices.md) which
captures from one playfield and ejects to another playfield to achieve
the same result.

## Related Events

* [playfield_transfer_(playfield_transfer)_ball_transferred](../../events/playfield_transfer_playfield_transfer_ball_transferred.md)
