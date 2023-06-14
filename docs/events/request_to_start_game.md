---
title: request_to_start_game
---

# request_to_start_game


--8<-- "event.md"

This event is posted when to start a game. This is a boolean event. Any
handler can return *False* and the game will not be started. Otherwise
when this event is done, a new game is started.

Posting this event is the only way to start a game in MPF, since many
systems have to "approve" the start. (Are the balls in the right
places, are there enough credits, etc.)

*This event does not have any keyword arguments*
