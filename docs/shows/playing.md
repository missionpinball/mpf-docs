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

!!! note

    Please make sure to always stop your show when you don't need it anymore. For example you run a show (show 1) on segment display, that show displays the player number. After the game is over another show (show 2) kicks in and that new show writes something on that display (so no more showing the actual player). Now you want to start the next game, the old show (show 1) starts again. If the player number has not changed, and it doesn't for example in a 1-player game, mpf believes the old execution of show 1 is still valid since nothing has changed and won't update the display (which again you have overwritten in a different show).

Check the [show_player:](../config/show_player.md)
documentation for details.
