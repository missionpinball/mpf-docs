Ball Search
===========

MPF's *ball_search* module contains the logic for ball search (where the pinball machine fires coils and moves
motors to look for balls that are stuck on the playfield).

Ball search in MPF is fairly automatic. It's enabled when MPF thinks that balls are on the playfield, and disabled when
no balls are free. (This means that even when a machine tilts, ball search is still active until the balls drain, etc.)

There are multiple "rounds" of ball search. When ball search first starts, it activates the "low risk" devices, like
pop bumpers and diverters. If it still can't find the ball, then it will start resetting drop targets and firing eject
coils to try to find it. If it still can't find the ball, it will kick a new one into play.

All of this is configurable.