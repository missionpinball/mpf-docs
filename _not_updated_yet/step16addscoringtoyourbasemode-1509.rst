
By now you have a "playable" game with a base game mode, and you've
added a score display to the DMD, but it's still pretty boring since
nothing is actually configured to register a score yet. So in this
step we're going to add some scoring.



(A) Understand in "scoring" works in MPF
----------------------------------------

MPF includes a system module called the `Score Controller`_ which is
responsible for for adding (or subtracting) points from a player's
score. Actually, that's not a completely accurate description. We
should really say that the Score Controller is responsible for adding
or subtracting value from any player variable. (A player variable is
just a key/value pair that is stored on a per-player basis.) The
*score* is the most obvious player variable. But MPF also uses player
variables to track what ball the player is on, how many extra balls
the player has, etc. You can create player variables to track anything
you want. Ramps made, combos made, number of modes completed, aliens
destroyed, etc. Even though it's called the *score* controller, the
score controller is responsible for adding and subtracting value from
any player variable based on events that happen in MPF. You configure
which events add or subtract value to which player variables in the
*scoring:* section of a mode's configuration file. The *scoring:*
section is only valid in a mode's config file (e.g. all scoring events
are tied to modes). You cannot add a *scoring:* section to your
machine config file.



(B) Add a *scoring:* section to your base.yaml config file
----------------------------------------------------------

The first step is simply to add a scoring: section to your base mode's
*base.yaml* config file. So in this case, that will be
*your_machine/modes/base/config/base.yaml*. Add a new top level
configuration item called *scoring:*, like this:


::

    
    scoring:




(C) Add point values for events
-------------------------------

Then inside the *scoring:* section, you create sub-entries for MPF
events that you map back to a list of player variables whose value you
want to change. By default, whenever a switch is hit in MPF, it posts
an event *<switch_name>_active*. (A second event called
*<switch_name>_inactive* is also posted when the switch opens back
up.) To give the player points when a switch is hit, add sub-entries
tothe `scoring:`section of your config file, with some switch name
followed plus `_active`, like this:


::

    
    scoring:
        s_right_inlane_active:
            score: 100
        s_left_flipper_active:
            score: 1000


Now save your config, start a game, hit the "L" key to launch a ball
and then hit the "Q" key to trigger the right inlane switch . You
should immediately see a score of 100 points, and then if you hit the
"Z" key for the left flipper, you'll see the player's score increase
by 1000 points. You can hit it as many times as you want to see the
score increase: ` `_

*Right inlane*: 100 points. Hitting the *left flipper* seven times:
7,000 points.

The `slide_player:` entries in MPF that contain player variables
(remember the `%score%` text entry?) will automatically update
themselves whenever the player variable changes.

At this point you can add different tags to different switches and
then add separate entries for each of them in your `scoring:` section
to assign different point values to each switch.

When youcreate more modes in the future, you can actually configure
that a score event in a higher-priority mode "blocks" the scoring
event in a lower-priority mode. So you could have a pop bumper that is
worth 100 points in a base mode, but then you could also make it worth
5,000 points in a super jets mode while blocking the 100 point score
from the base mode. (More on that later.)

Later on you can also configure *shots*which can control lights and
manage sequences of switches and lots of other cool things, so that's
how you can track the ball moving left-to-right or right-to-left
around a loop, and from there you'll be able to configure different
scoring events for each direction. (Again, we'll get to this later.)

.. _Score Controller: https://missionpinball.com/docs/mpf-core-architecture/system-modules/score-controller/


