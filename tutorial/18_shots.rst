Tutorial step 18: Add your first shot
=====================================

At this point you have a machine you can turn on, lights flash, the
display works plays, you can hit start, you have a base mode with some
simple scoring, and you can play complete games. Not bad! In this step
we're going to introduce you to a key MPF concept called "shots", which is
an important concept in MPF and something that you'll use *a lot* when you're
putting together your game logic.

1. What's a shot?
-----------------

First, take a look at the :doc:`introduction to shots </game_logic/shots/index>`
documentation to understand what a shot is.

2. Create your first shot
-------------------------

To define your a shot, you add a ``shots:`` entry to a config file in a mode,
and then under there, you set the switch, timing, and other details that
make up that shot.

You'd typically define your shots per mode, since
the behavior differs depending on the mode.
If you want a shot to be available in every mode you can also put them in
the ``base`` mode which is usually active all the time.

.. note::

   Before 0.30 you could define shots per machine-wide. This caused very complex
   configs and is no longer supported. You can put shots into your base mode
   if you want them to be active all the time during a game.

Let's start by creating our first shot in the base mode's config file (base.yaml).

.. code-block:: mpf-config

    #! switches:
    #!   s_right_inlane:
    #!     number: 1
    ##! mode: base
    shots:
      my_first_shot:
        switch: s_right_inlane  # pick a switch that's valid in your machine

Depending on your machine, you might not actually have a switch
called "s_right_inlane", so feel free to pick a different switch name. For
now just keep it simple—a standup or a lane switch or something.

Also, to make following the tutorial easier, go ahead and call this
shot "my_first_shot" even if you're using a different switch name. You
can change the name of the shot to something more meaningful later.

Next, find the ``variable_player:`` section that you added in Step 15, and change the
first entry from ``s_right_inlane_active:`` to ``my_first_shot_hit``,
like this:

.. code-block:: mpf-config

   ##! mode: base
   variable_player:
     my_first_shot_hit:  # this was s_right_inlane_active
       score: 100
     s_flipper_lower_left_active:
       score: 1000
       potato: 1
     s_flipper_lower_right_active:
       potato: -2

Do you understand what this is doing?

Remember that the variable_player section will add (or remove) value from a player
variable when certain events happen. So the OLD entry from Step 15 would
increase the score by 100 points when the event "s_right_inlane_active" happened, and the
NEW entry changes that so the 100 points are added when the event
"my_first_shot_hit" happens.

This illustrates something to know about shots: Whenever a shot is "hit", then
an event is posted with the name of the shot plus "_hit" added onto it.

So in this case, the shot "my_first_shot" will post then event
"my_first_shot_hit" whenever that shot is made.

If you save your changed config file and run MPF again, start a game
with the ``S`` key, then hit the right inlane switch with the ``Q`` key,
you should see the player's score increase by 100 points.

So it kind of looks like nothing really changed, except now we're using
a real shot instead of scoring based on the switch entry.

At this point you might think that this is overly complicated. After all,
everything worked fine before without having to mess with shots and all,
so why bother?

Again, this is just a simple example to get you started. The real power of
shots comes in as you define more complex shots, as you get into shot
profiles (doing different things depending on the state of the shot), and
enabling, disabling, blocking, and overriding shots based on different
modes.

3. Change the shot profile
--------------------------

Every shot in MPF has a "shot profile" applied to it. (Since we didn't
specify a profile in the shot we just created, it uses a default profile
called, wait for it... "default".)

A shot profile is a list of steps (or states) for a shot. For example,
the default profile (which is built-in to MPF) has two states:

#. unlit
#. lit

When a new game starts, the shots in MPF start at the first step of
the profile. In other words, the shot called "my_first_shot" starts
in the "unlit" state. Then, when the shot is hit, the profile is
advanced to the next step. (So when "my_first_shot" is hit, that shot
advances from the "unlit" to the "lit" state.)

You can apply the same profile to multiple shots (and the state of each
shot is tracked separately), so if you have "my_first_shot" and "my_second_shot",
they both start "unlit", but if you hit "my_second_shot", then it
advances to "lit" but "my_first_shot" stays in the "unlit" state.

Shot profiles have all sorts of settings (which we'll get to in a bit),
including options for what happens when the shot is hit when it's in the
final state—does it just stay there or does it go back to the first state?
(The built in "default" shot profile will stay in the lit state even if
it's repeatedly hit.)

Also, tracking which state a shot is at is done on a per-player basis, so
if Player 1 advances a shot from "unlit" to "lit", then when Player 2
starts, that shot will be back in the "unlit" state.

One of the cool things about shot profiles is you can tie them to shows,
and then when you define your shots, you can specify how those shows are
played. In other words, you can associate a light or LED with your shot,
and then that light will be off when the shot is "unlit" and then turn
on when the shot is lit.

Let's do that now.

3a. Associate a light/led with your shot
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To do this, go back to the mode config where you defined the shot (base.yaml)
and change the ``shots:`` section.

If you have LEDs in your machine, change it to this:

.. code-block:: mpf-config

   #! switches:
   #!   s_right_inlane:
   #!     number: 1
   ##! mode: base
   shots:
     my_first_shot:
       switch: s_right_inlane
       show_tokens:
         led: led_1 # pick an LED that's valid in your machine

If you have a lamp matrix, change it to this:

.. code-block:: mpf-config

   #! switches:
   #!   s_right_inlane:
   #!     number: 1
   ##! mode: base
   shots:
     my_first_shot:
       switch: s_right_inlane
       show_tokens:
         light: l_light_quick_freeze # pick a light that's valid in your machine

In either case, be sure to pick an LED or light name that is a valid light
in your machine.

For now don't worry about what "show_tokens" is or what's happening. (We'll
get to that.)

Save your config, then re-run MPF and start a game. The light or LED you
picked should be off.

Now hit the switch for the shot. You should see the 100 point score increase,
and you should also see the light or LED turn on. (If it's an RGB LED, it will
turn on white. We can change that later.)

If you hit the switch again, you'll still get 100 points each time (since the
"my_first_shot_hit" is happening each time), but the light won't turn off
since the shot is staying in the "lit" state since the default shot profile
isn't configured to go back to the first step when it gets to the last step.

3b. Create a custom shot profile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Next, let's create a custom shot profile that has more than the "lit" and
"unlit" steps.

To do this, we'll add a section to the mode's config file (base.yaml)
called ``shot_profiles:``. Create that section now, and define a shot
profile called "my_first_profile" with the following settings:

.. code-block:: mpf-config

   ##! mode: base
   shot_profiles:
     my_first_profile:
       states:
         - name: unlit  # step 1
           show: off
         - name: flashing  # step 2
           show: flash
         - name: lit  # step 3
           show: on
       loop: true

Take a look at this shot profile to see what's happening.

First, notice that in the ``my_first_profile:`` section, there's a subsection
called "states". This is a list of all the states (steps) that shots will
use when this profile is applied. (Note the dashes to separate each step.)

The states/steps are listed in the order they'll cycle through as the shot
is hit.

Each step has a ``name:`` setting which is the name of the step (or, more
accurately, the name of the state that shot is in when a shot with
that profile applied to it is at the step).

Also notice that each step has a ``show:`` setting. This is the name of the MPF
show (just like display show we created in Step 16 or the light show we
created in Step 18). These shows need to be valid shows within MPF. In this
case we're using shows named "off", "flash", and "on", as those are valid
names for three shows that are built-in to MPF.

What's basically happening here is that when a shot with this profile
applied is at the first step of the profile, the state name will be called
"unlit" and the show called "off" will be played. Then when the shot is hit,
it will advance to the next step, which is called "flashing" in this case.
The show called "unlit" will be stopped, and then the show called "flash"
will be played. If the shot is hit again, it will advance to the "lit"
state, the "flash" show will stop, and the show called "on" will be started.

This shot profile also includes a ``loop: true``
setting that means when a shot is hit that's in the last step of the profile,
it will loop back to the first step. (So hitting the shot when it's lit means
the shot will loop back to "unlit".)

3c. Apply the new profile to the shot
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Simply creating a shot profile doesn't mean that any shots use it. It just
means that profile is available to be used, much like how creating a show
is separate from playing the show.

So next we need to tell our shot that it should use the new profile we
just created by adding a ``profile:`` setting.

.. code-block:: mpf-config

   #! switches:
   #!   s_right_inlane:
   #!     number: 1
   ##! mode: base
   #! shot_profiles:
   #!   my_first_profile:
   #!     states:
   #!       - name: unlit  # step 1
   #!         show: off
   #!       - name: flashing  # step 2
   #!         show: flash
   #!       - name: lit  # step 3
   #!         show: on
   #!     loop: true
   shots:
     my_first_shot:
       switch: s_right_inlane
       show_tokens:
         led: l_led1 # or use light: here, depending on your machine
       profile: my_first_profile

Save your config and re-run MPF. Once you start a game, the light or LED
from your shot should be off. Hit the switch for the shot, and the light
or LED should starting flashing. (It will be slow—1 second on, 1 second off.)
Hit it again, and it should go on solid. Hit it again and the shot will go
back to the "unlit" state. Hit it again and the light or LED should flash. Etc.

Note that you must actually start a game for this to work. Shots are only
active when games are in progress, and the state is tracked per-player which
means that players must exist, etc.

If you play a multi-player game, you should see that the state of that
shot is maintained and restored separately for each player.

3d. Apply custom scoring based on state
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remember that the ``scoring:`` section of the base mode config scores 100
points each time that shot is hit. So as you're hitting the switch over and
over to cycle through the states, each time you do that the player gets 100
points.

That scoring entry is based on the ``my_first_shot_hit``, which is generated
every time that shot is hit since shots make events in the form ``<shot_name>_hit``.

However, each time a shot is hit, there's two ADDITIONAL events posted which
are ``<shot_name>_<profile>_hit`` and ``<shot_name>_<profile>_<state>_hit``.

For example, when you start a new game with the shot and shot profile we've
been working with, when you hit the switch for that shot, three shot-related
events will be generated:

* my_first_shot_hit (shot + "hit")
* my_first_shot_my_first_profile_hit (shot + profile + "hit")
* my_first_shot_my_first_profile_unlit_hit (shot + profile + state + "hit")

When you hit that same shot a second time, the following three events will
be generated: The first two are the same since they're based on shot name
and profile name, but the last one is different because the shot's state is
different.

* my_first_shot_hit (shot + "hit")
* my_first_shot_my_first_profile_hit (shot + profile + "hit")
* my_first_shot_my_first_profile_flashing_hit (shot + profile + state + "hit")

Hitting that shot again will generate the following three events:

* my_first_shot_hit (shot + "hit")
* my_first_shot_my_first_profile_hit (shot + profile + "hit")
* my_first_shot_my_first_profile_lit_hit (shot + profile + state + "hit")

And so on...

Now let's look at how we can give the player a different number of points when
they hit that shot depending on what state the shot's in.

Here's the existing variable_player section from the base mode config:

.. code-block:: mpf-config

   ##! mode: base
   variable_player:
     my_first_shot_hit:
       score: 100
     s_flipper_lower_left_active:
       score: 1000
       potato: 1
     s_flipper_lower_right_active:
       potato: -2

Again, the player gets 100 points each time that shot is made regardless of what
state it's in since the scoring event is the generic shot hit event which does
not include details of what state the shot is in.

Now let's change the variable_player section to this:

.. code-block:: mpf-config

   ##! mode: base
   variable_player:
     my_first_shot_my_first_profile_unlit_hit:
       score: 100
     my_first_shot_my_first_profile_flashing_hit:
       score: 1000
     s_flipper_lower_left_active:
       score: 1000
       potato: 1
     s_flipper_lower_right_active:
       potato: -2

We changed the name of the event for the first variable_player entry from
"my_first_shot_hit" to "my_first_shot_my_first_profile_unlit_hit". This means
those 100 points will only be added if that shot is hit while it has the
"my_first_profile" applied AND while that profile is in the state "unlit".

The next entry, for 1000 points, will only be called when that shot is hit with
"my_first_profile" applied while it's in the state "flashing".

Save your config and run your game. If you hit the switch for the shot, you
should get 100 points and the light should start flashing. Hit it again, and you
should get 1000 points and the light should turn on steady. Hit it a third time,
and you should get no points, but the light will also turn off since the
profile is set to loop and it will go back to the first (unlit) state.

In other words, hitting the ``Q`` key (or the actual switch if you have a real
machine) should result in the following sequence of total score (one for each
hit): 100, 1100, 1100, 1200, 2200, 2200, 2300, 3300, 3300...

4. Add a second mode and score the shot from there
--------------------------------------------------

One of the most powerful features of shot profiles is that shots can have
multiple profiles defined at the same time (with each active mode having
the ability to apply its own profile).

To illustrate this, we're going to create a new mode, called "mode2". So
go ahead and create a ``mode2`` folder in your ``modes`` folder, then add
the ``config`` folder into that folder, and then create the ``mode2.yaml``
mode configuration file for that mode.

Open up the ``mode2.yaml`` file and add the following lines. (We'll explain
them step-by-step next.)

.. code-block:: mpf-mc-config

   ##! mode: mode2
   #config_version=5
   # mode2 config file

   mode:
     start_events: mode2_start
     stop_events: mode2_stop
     priority: 200

   widgets:
     mode2_start_banner:
       type: text
       text: MODE 2 STARTED
       font_size: 50
       color: lime
       y: 80%
       expire: 1s

   widget_player:
     mode_mode2_started: mode2_start_banner

   variable_player:
     my_first_shot_hit:
       score: 1
   ##! test
   #! start_game
   #! start_mode mode2
   #! advance_time_and_run .1
   #! assert_text_on_top_slide "MODE 2 STARTED"

Remember that you also have to go back into your machine-wide config file to add the new
``- mode2`` entry to your ``modes:`` section. While we're in there, let's also add
``keyboard:`` entries for some events we can use to stop and start the mode.

Here are changes you'll make to the machine-wide config file:

.. code-block:: yaml

   # from the machine-wide config.yaml file

   modes:
     - base
     - mode2

   ...

   keyboard:  # existing keyboard entries not shown.
     n:
       event: mode2_start
     m:
       event: mode2_stop

Now save your files and run your machine. Then press the following keys:

* ``S`` - starts the game
* ``Q`` - hits your shot, score jumps to 100
* ``Q`` - hits your shot, score jumps to 1100
* ``N`` - starts mode2. You should see a 1-second green message showing this
* ``Q`` - hits your shot, score jumps to 1101
* ``Q`` - hits your shot, score jumps to 1202

You can press ``M`` to stop mode2 (though there is no on-screen message) and then
continue to hit ``Q`` and notice the score jumps through the [+100, +1000, 0] cycle
over and over.

You can press ``N`` again to start mode2 and notice that every time you press ``Q``,
you the score increases +1 (in addition to the [+100, +1000, 0] from the base mode.

Press ``M`` to stop mode2 again and notice that the +1 scoring stops.

So what's happening here?

First, notice that in the ``mode2.yaml`` file, we configured the following
variable_player entry:

.. code-block:: mpf-config

   ##! mode: mode2
   variable_player:
     my_first_shot_hit:
       score: 1

Notice that that variable_player entry is just based on "my_first_shot" being hit. It
does not contain any of the profile or state information in it, which means that
it will always score the +1 regardless of the state of that shot.

Of course even while mode2 is running, the base mode is also running. That means
that when both modes are running, mode2 is always scoring +1 per hit, and the
base mode is cycling through the [+100, +1000, 0] scoring depending on what
state the shot is in.

When you stop mode2 (with the ``M`` key), that removes the scoring from mode2,
but since the base mode is still running, you still get the scoring from there.

5. Configure a new shot profile in mode2
----------------------------------------

In the previous step, we added a new mode and accessed the shot from within
that mode, but that new mode still used the same shot profile as the base
mode.

However, it's also possible to create a brand-new shot profile in a mode
that will be applied to the shot when that mode is active.

This is useful if you want to "override" a shot profile from a lower mode
based on a higher priority mode. For example, maybe you have a stand-up
target in your base mode that you're using for some basic scoring. But then
in a jackpot mode, you want that target to flash a light instead of just
the regular on/off behavior from the base mode. You would do this by
applying a different shot profile in the jackpot mode.

To illustrate this, open up your ``mode2.yaml`` file and:

#. Updated the ``variable_player:`` section from the example below
#. Add the ``shots:`` section from below
#. Add the ``shot_profiles:`` section from below

.. code-block:: mpf-config

   #! switches:
   #!   s_right_inlane:
   #!     number: 1
   ##! mode: mode2
   # snippet from mode2.yaml
   variable_player:
     my_first_shot_mode2_flashing_hit:
       score: 10000
     my_first_shot_mode2_lit_hit:
       score: 100

   shots:
     my_first_shot_mode2:
       switch: s_right_inlane
       profile: mode2

   shot_profiles:
     mode2:
       states:
         - name: flashing
           show: flash
           speed: 5
         - name: lit
           show: on
       loop: false
       block: true

Save your files and run your game again, pressing the following keys:

* ``S`` - starts the game
* ``Q`` - hits your shot, score jumps to 100,
* ``Q`` - hits your shot, score jumps to 1100
* ``N`` - starts mode2. You should see a 1-second green message showing this
* ``Q`` - hits your shot, score jumps to 11,100
* ``Q`` - hits your shot, score jumps to 11,200
* ``Q`` - hits your shot, score jumps to 11,300
* ``M`` - stops mode2
* ``Q`` - hits your shot, no score change
* ``Q`` - hits your shot, score jumps to 11,400
* ``Q`` - hits your shot, score jumps to 12,400

Let's deconstruct the changes to the ``mode2.yaml`` config file too see what's
going on.

First, notice that we added a ``shots:`` section and then added "my_first_shot"
to it, like this:

.. code-block:: mpf-config

   ##! mode: mode2
   #! shot_profiles:
   #!   mode2:
   #!     states:
   #!       - name: flashing
   #!         show: flash
   #!         speed: 5
   #!       - name: lit
   #!         show: on
   #!     loop: false
   #!     block: true
   shots:
     my_first_shot:
       profile: mode2

However, unlike the "my_first_shot" entry in the base mode config, in the mode2
config we did NOT redefine the ``switch:`` or ``show_tokens:`` entries. Instead,
we just added the ``profile:`` setting and told it to use a profile called ``mode2``.

So what this means is that we're not creating a new shot or changing the configuration
of the shot, rather, we're just saying that when mode2 is active, we want to apply
a different shot profile to the shot. (Remember that settings from mode configuration
files are only active when that mode is active.)

Next, take a look at the ``shot_profiles:`` section:

.. code-block:: mpf-config

   ##! mode: mode2
   shot_profiles:
     mode2:
       states:
         - name: flashing
           show: flash
           speed: 5
         - name: lit
           show: on
       loop: false
       block: true

In this case, we defined a profile called ``mode2`` which has two states: "flashing" and "lit". (These
state names could be whatever you want, "incomplete" and "complete" or whatever.) Note also that we added
``speed: 5`` to the flashing step. That setting will be applied to the "flash" show when it's played, and
you can use any of the :doc:`/config/show_player` settings there. In this case that will play the show
at 5x speed, so we'll see a very fast flashing.

Also note that we added ``block: true`` to this profile. That means that when this profile is active, any
shot profiles from lower priority modes will be disabled. Since mode2 runs at priority 200, the profile
"my_first_profile" which we assigned in the base mode config (base.yaml) will be blocked.

And, since the variable_player events in the base mode are based on the shot being hit with the "my_first_profile"
applied, this is why when mode2 is running, we don't get the variable_player events from the base mode. Those
events are not posted because my_first_profile is not active because the higher priority profile attached
to the shot in mode2 is blocking it.

If you were to remove the ``block: true`` from the mode2 profile in the mode2 config, then when you hit the
shot while mode2 was active then you would get the scoring from both the base mode and mode2 mode applied.

(not done writing yet...)

Next steps to write

* Show tokens
* Shot groups
* advancing shots
* shot reset events

Check out the complete config.yaml file so far
----------------------------------------------

If you want to see a complete ``config.yaml`` file up to this point, it's in the ``mpf-examples/tutorial/step_18``
folder. You can run it be switching to that folder and running ``mpf both``:

.. code-block:: doscon

   C:\mpf-examples\tutorial_step_18>mpf both

Even if you have real hardware, it's probably worth running the MPF Monitor which will show you the events as they're
posted that correspond to the shot being hit and it changing profiles.
