
The Mission Pinball Framework is capable of supporting the concept of
"valid playfield" via a valid_playfield.py plugin. *Valid playfield*
is a term in the pinball world that means the playfield is "active" or
"live" after a new ball is plunged. It's basically used to tell the
game that the ball was plunged successfully and that nothing screwed
up in the launch process. If a ball drains before the playfield has
been marked valid, the game thinks something weird happens and just
loads another ball in the plunger. Various manufacturers have used the
valid playfield differently over the years. Some machinesrequire as
many as three playfield switch hits before they mark the playfield as
valid, and players over the years have `found ways to exploit this`_
by plunging the ball to hit a target and then purposefully not
flipping so the ball drains without the playfield marked as valid,
essentially letting them rack up points without even playing. (To
learn more about this, check out `PAPA's game-specific tournament
notes`_. Do a search on the page for 'valid' to learn all about
various valid playfield exploits on certain games.) If you choose to
use the valid playfield functionality, rhere are several different
ways valid playfield can be configured in MPF, depending on your
preferences and hardware. For example, if you have a switch(or
switches) that you know the ball will always roll over on its way into
play, you can use those switches to mark the playfield as valid. If
not then you have to depend on the ball hitting other random switches.
You can configure how many switch hits need to happen in order for the
playfield to be marked as valid. Typically this is just 1 or 2, but
you can play with it to see what works for you. (See the `Game
section`_and `BallDevices`_ section of theconfiguration file reference
for details on configuring valid playfield options.) Note that the
valid playfield functionality is optional. If you don't use it, then
the ball will "count" as long as it has hit at least one playfield
target after it was launched. If you want the ball to only count after
hitting two (or more) targets, then you can use the valid playfield
module to track this.



Activating this plugin
~~~~~~~~~~~~~~~~~~~~~~

Add `valid_playfield.ValidPlayfield` to the `Plugins:` section of
your`Machine Configuration Files`_.



Customizing this plugin
~~~~~~~~~~~~~~~~~~~~~~~

You can configure several options for this plugin in
the``ValidPlayfield:` section`_of your Machine Configuration Files.

.. _BallDevices: /docs/configuration-file-reference/devices/balldevices/
.. _Machine Configuration Files: /docs/configuration-file-reference/
.. _found ways to exploit this: https://pinside.com/pinball/forum/topic/tourney-lingo-valid-playfield-switch
.. _`ValidPlayfield:` section: /docs/configuration-file-reference/validplayfield/
.. _PAPA's game-specific tournament notes: http://papa.org/learning-center/director-resources/directors/game-notes/
.. _Game section: /docs/configuration-file-reference/game/


