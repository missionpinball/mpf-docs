Tutorial step 15: Add scoring
=============================

By now you have a "playable" game with a base game mode, and you've
got a score showing on the display, but it's still pretty boring since
nothing is actually configured to register a score yet. So in this
step we're going to add some scoring.

1. Understand in scoring works in MPF
-------------------------------------

MPF includes a core module called the *Variable Player* which is
responsible for adding (or subtracting) points from a player's
score. Actually, that's not a completely accurate description. We
should really say that the variable player is responsible for adding
or subtracting value from any player variable. (A player variable is
just a key/value pair that is stored on a per-player basis.)
The *score* is the most obvious player variable. But MPF also uses player
variables to track what ball the player is on, how many extra balls
the player has, etc. You can create player variables to track anything
you want. Ramps made, combos made, number of modes completed, aliens
destroyed, etc.

The variable player is responsible for adding and subtracting value from
any player variable based on events that happen in MPF. You configure
which events add or subtract value to which player variables in the
``variable_player:`` section of a mode's configuration file.

2. Add a *variable_player:* section to your base.yaml mode config file
----------------------------------------------------------------------

The first step is simply to add a ``variable_player:`` section to your base mode's
*base.yaml* config file. So in this case, that will be
``<your_machine>/modes/base/config/base.yaml``. Add a new top level
configuration item called *variable_player:*, like this:

.. code-block:: yaml

   variable_player:

3. Add point values for events
------------------------------

Then inside the ``variable_player:`` section, you create sub-entries for MPF
events that you map back to a list of player variables whose value you
want to change. By default, whenever a switch is hit in MPF, it posts
an event *<switch_name>_active* . (A second event called
*<switch_name>_inactive* is also posted when the switch opens back
up.) To give the player points when a switch is hit, add sub-entries
to the ``variable_player:`` section of your config file, with some switch name
followed by "_active", like this:

.. code-block:: mpf-config

   ##! mode: base
   variable_player:
     s_right_inlane_active:
       score: 100
     s_left_flipper_active:
       score: 1000

Now save your config, start a game (``S``), hit the ``L`` key to launch a ball,
then hit the ``Q`` key to trigger the right inlane switch . You
should immediately see a score of 100 points. Then if you hit the
``Z`` key for the left flipper, you'll see the player's score increase
by 1000 points. You can hit it as many times as you want to see the
score increase:

Remember from the previous step that the ``slide_player:`` section of the config
contains a text widget with a value of ``(score)`` in parentheses, and any values
in parentheses are updated automatically when the underlying player variable
changes. So that's how the display is updating automatically here.

By the way, there's a :doc:`reference list of many built-in events </events/index>`
in the documentation, so you can browse through that to get an idea of the various
types of events that exist which you can use to trigger display slides or score
events.

Note that ``variable_player:`` events in a mode's config file are only actually active when
that mode is active. So the section we're adding in this step is in the base mode's
config, which we've set to start any time a ball starts. But if the base mode ever
wasn't running, then the ``s_right_inlane_active`` and ``s_left_flipper_active`` events
wouldn't trigger a score.

When you create more modes in the future, you can actually configure
that a score event in a higher-priority mode "blocks" the variable_player/scoring
event in a lower-priority mode. So you could have a pop bumper that is
worth 100 points in a base mode, but then you could also make it worth
5,000 points in a super jets mode while blocking the 100 point score
from the base mode since if the scoring from both modes was active, you'd get
two scoring events--the 100 from the base mode and the 5,000 from the super jets mode.
(More on that later.)

Later on you can also configure *shots* which can control lights and
manage sequences of switches and lots of other cool things, so that's
how you can track the ball moving left-to-right or right-to-left
around a loop, and from there you'll be able to configure different
scoring events for each direction. (Again, we'll get to this later. For now you can
just wire up scoring to a switch to see it working.)

4. Play with more player variables
----------------------------------

As we said, you can add or subtract value from any player variable via the ``variable_player:``
section--even player variables that you make up.

For example, try changing your scoring section to this:

.. code-block:: mpf-config

   # we will initially set the value to 0 when the machine starts up
   player_vars:
     potato:
       initial_value: 0

   ##! mode: base
   # in your base mode (modes/base/config/base.yaml)
   variable_player:
     s_right_inlane_active:
       score: 100
     s_left_flipper_active:
       score: 1000
       potato: 1
     s_right_flipper_active:
       potato: -2

We use the word "potato" here to illustrate that player variables can be anything. So now when the left flipper is
active, the player variable called "score" will increase by 1000, and the player variable called "potato" will increase
by one. (If you make a reference to a player variable that hasn't been defined before, it will automatically be
created with a value of 0.)

Also notice that when the right flipper is hit, the player variable called "potato" will have a value of 2 subtracted
from it.

Player variables exist and are tracked even if they're not displayed anywhere. So if you run your game now and start
flipping, the potato value will change. Again, player variables are stored on a per-player basis, so if you start adding
additional players to the game, they'll each have their own copies of their own player variables. Also the player
variables are destroyed when the game ends. (It is possible to save certain variables from game-to-game, but we'll
discuss those later, as those are not player variables.)

So now that we're tracking this potato variable, let's add it to the display. To do this, let's add another widget to
the slide that is show when the base mode starts. (So we're going to be editing ``<your_machine>/modes/config/base.yaml``
again. Add the potato text entry, like this:

.. code-block:: mpf-mc-config

   #! player_vars:
   #!   potato:
   #!     initial_value: 0
   ##! mode: base
   # in your base mode (modes/base/config/base.yaml)
   slide_player:
     mode_base_started:
       widgets:
         - type: text
           text: (score)
           number_grouping: true
           min_digits: 2
           font_size: 100
         - type: text
           text: PLAYER (number)
           y: 10
           x: 10
           font_size: 50
           anchor_x: left
           anchor_y: bottom
         - type: text
           text: BALL (ball)
           y: 10
           x: right-10
           anchor_x: right
           anchor_y: bottom
           font_size: 50
         - type: text
           text: 'POTATO VALUE: (potato)'
           y: 40%
   ##! test
   #! start_game
   #! start_mode base
   #! advance_time_and_run .1
   #! assert_text_on_top_slide "PLAYER 1"
   #! assert_text_on_top_slide "BALL 1"
   #! assert_text_on_top_slide "POTATO VALUE: 0"

Notice that we put ``text: 'POTATO VALUE: (potato)'`` in quotes. That's because we actually want to show the colon as part
of the text that's displayed on the screen. However colons are important in YAML files. So if we made our entry
like this: ``text: POTATO VALUE: (potato)``, then we would get a YAML processing error because the YAML processor
would freak out. "OH MY THERE ARE TWO COLONS?? WHAT'S THIS MEAN??? <crash>"

So we use quotes to tell it that the second colon is just part of our string.

Now you can run your game (via ``mpf both``), S to start a game, L to launch a ball, then use the Z and / keys to left
and right flip which will adjust the potato value accordingly.

Notice that when you first start a game, the onscreen text says ``POTATO VALUE: (potato)``. That's because when this
slide is first displayed, there is no player variable called "potato"--it's not created until you hit a flipper
button--so the text widget doesn't know what to do with "potato", so it just prints it as is. Later we'll learn how to
properly initialize variables, but the main thing for now is to see how the scoring and slide player works.

Check out the complete config.yaml file so far
----------------------------------------------

If you want to see a complete ``config.yaml`` file up to this point, it's in the ``mpf-examples/tutorial/step_15``
folder with the name ``config.yaml``. You can run it be switching to that folder and running ``mpf both``:

.. code-block:: doscon

   C:\mpf-examples\tutorial_step_15>mpf both
