Shots
=====

In MPF, a "shot" is a switch (or combination) of switches that the player shoots
for. Examples include:

* A standup target, drop target, or rollover lane
* A ramp, loop, or orbit
* A toy, subway, or VUK

Most shots have lights or LEDs associated with them which are on, off, flashing, and/or
certain colors to reflect what "state" the shot is in.


Broadly speaking, a shot is anything the player shoots at during a
game. It could be a standup target, a lane, a ramp, a loop, a drop
target, a pop bumper, a toy, etc.



You can read the :doc:`full shots documentation </game_logic/shots/index>` for
details, but the short version
is that in MPF, you define switches (or a sequence of switches) as a "shot". Then
whenever that shot is made, MPF posts events which you can use to trigger scores,
achievements, shows, etc.

Some shots are made up of a single switch (like a standup target). But you can
also configure shots that are only considered to be hit based on series of switches that
must be hit in the right order within a certain time frame. For
example, you might have an orbit shot with three switches:
*orbit_left*, *orbit_top*, and *orbit_right*. You could configure one
shot called *left_orbit* that's triggered when the switches
*orbit_left*, *orbit_center*, and *orbit_right* are hit (in that
order) within 3 seconds, and you could configure a second shot called
*right_orbit* that's triggered when the switches *orbit_right*,
*orbit_center*, and *orbit_left* are hit within 3 seconds. (So, same
switches, but two different shots depending on the order they're hit.)

The beauty of using shots is that you just define all the switches and timing
once, and then every time you want to use that shot in your game, you just need
to work with the "right_orbit" shot and not have to worry about all the details
of the switches and timing.

You can also configure different "states" for shots, e.g. "What state is that shot in?"
That can be things like lit, unlit, complete, flashing, etc. You can also configure
shows for each state (the unlit state means the light is off, flashing means that
the light is flashing, etc.), and you can configure different scoring based on
whether state the shot is in (1,000 points if unlit, 5,000 if lit, etc.). All of this
is completely configurable.

You can also group multiple shots into "shot groups" and then do certain things
when all the shots in the group are in the same state. For example, you could have
three standup targets configured as three separate shots that all start in the
"unlit" state, but then once all three shots are advanced to the "complete" state,
you could add 100,000 points and start another mode.

Shots are also are integrated into MPF's modes system, so you
can configure a shot to do different things in different modes.

For example, a ramp shot might do nothing more than score 1,000 points in your base
mode, but when the multiball mode is running, that same shot would score a jackpot.
You can also configure whether notification of a shot being hit is passed down from
one mode to the lower priority modes below it. (In the jackpot example we just
mentioned, you probably just want to score the million points for the jackpot if that
shot is made while the multiball mode is running and *not* score the 1,000 points
for that shot from the base mode even though the base mode is still running under the
multiball mode.

.. toctree::

   shot_group
   shot_profiles
