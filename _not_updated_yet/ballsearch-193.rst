Note: The Ball Search functionality is not fully implemented and will
change. We recommend that you do not use ball search for the time
being.
The `ball_search:`section of the config files controls how the ball
search functionality works. (Duh, right?) Here's an example:


::

    
    ball_search:
     secs until ball search start: 10
     secs between ball search rounds: 3
     secs between ball search coils: .15
     if ball search fails: continue
     phase secs: [10, 10, 30]
     missing balls on startup: ignore # search, halt #todo


Parameters:



Secs until ball search start:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

How many seconds of no activity before the ball search begins. This
timer only runs when there are uncontained balls, and if the switches
tagged with pause_ball_search are not active. (Typically this is the
flipper buttons, since you don't want the ball search to start if a
player is holding a flipper button.) To do: We need to make it so that
releasing these switches doesn't reset the timer, since we want to
start a ball search if the player is tapping the flipper buttons in
frustration.



Secs between ball search rounds:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A ball search "round" is one complete cycle of all the ball search
coils. If you imagine how the ball search works in a pinball machine,
you know all the coils fire really fast, one right after the other.
Then there's a pause, then they fire again. So it's like pop pop pop
pop pop pause... pop pop pop pop pop pop pause... This *secs between
ball search rounds* is how long that "pause" is between each round of
coil firings.This is typically 3-5 seconds.



Secs between ball search coils:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is how many seconds there are between each coil firing. (So,
between the "pop pop pop" described above.) This is typically a
fraction of a second, like 0.15 or 0.25.



If ball search fails:
~~~~~~~~~~~~~~~~~~~~~

Controls when happens when a ball search fails


+ Keep Looking (the machine just stays in ball search mode forever)
+ Serve Ball (the machine serves up another ball)




Phasesecs:
~~~~~~~~~~

Ball searching in the Mission Pinball Framework has a concept of
*phases*. Each phase could be seen as doing a deeper, more intense
search. For example, the first phase might fire all the easy coils,
like pop bumpers, lane gets, slingshots, etc. If the ball is still not
found after doing that a few times, then we can move on to the next
phase where we might try firing the eject coils from ball devices.
Firing the eject coils is a bit more dangerous since we don't want to
eject a known ball from a container, so we might first fire the eject
coils from devices that we think are empty. If we still can't find the
ball then we might try firing coils from devices that we know have
balls in them, though if we do that and we end up finding a ball we
have to take into consideration that we might have simply emptied that
device instead of locating our missing ball. The *Phase secs*
parameter is a list of how many seconds total we want to run each ball
search phase. So in the example above, we have `Phase secs: [10, 10,
30]` which means we'll try the first phase of coils for 10 seconds,
then the second phase for 10 seconds, and finally the third phase for
30 seconds. NOTE: This functionality has not yet been implemented.
It's actually kind of complex and on our to do list. :)



Missing balls on startup: (Not yet implemented)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Controls how the machine deals with missing balls when it starts up.
Note there are also config file settings that specify how many balls
should be installed in the machine, as well as the minimum and maximum
it can have in order to start a game.


+ ignore (The machine does nothing, as long as the number of balls
  falls between the min and max numbers.)
+ search (The machine does a ball search. It runs until it times out,
  and then the machine continues as normal.)
+ search-abortable (The machine does a ball search, but if a player
  pushes start or puts money in then it aborts the search, even if it
  hasn't found the missing balls.)
+ halt (The machine will not allow games to start. This is what
  happens if the number of balls it finds are below the minimum number
  required to play.)




