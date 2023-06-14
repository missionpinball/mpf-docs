---
title: Starting & stopping shows
---

# Starting & stopping shows


Now that you know how to create shows, how do you start and stop them?

The easiest way is with the [show_player:](../config/show_player.md) section of either a machine-wide or mode config files.

You can use the show player to start, stop, pause, resume, advance, step
back, and update shows. (That's a lot!) You can also use it to set the
playback speed, set up show synchronization, and set up show repeats and
looping.

Note that any shows which were started via a `show_player:` section in a
mode config file will automatically be stopped when that mode stops.

So check the [show_player:](../config/show_player.md)
documentation for details.
