
At this point you have a machine you can turn on, lights flash, the
DMD show plays, you can hit start, you have a base mode with some
simple scoring, and you can play complete games. Not bad! In this step
we're going to introduce you to a key MPF concept called "shots", and
you're going to create your first shot.



(A) What's a shot?
------------------

Broadly speaking, a shot is anything the player shoots at during a
game. It could be a standup target, a lane, a ramp, a loop, a drop
target, a pop bumper, a toy, etc. Many shots in MPF have lights or
LEDs associated with them that indicate what "state" the shot is in.
(e.g. "shoot the flashing targets" or "hit the lit ramp" could mean
"hit the target that's in the *flashing* state", or "hit the ramp
that's in the *lit* state".) Shots in MPF are similar to other devices
we've worked with (like autofires and ball devices) where you group
together switches, lights, and/or LEDs into the things we call
*shots*. (Not every shot has a light or LED associated with it.) You
can even configure shots that are based on series of switches that
must be hit in the right order within a certain time frame. For
example, you might have an orbit shot with three switches:
*orbit_left*, *orbit_top*, and *orbit_right*. You could configure one
shot called *left_orbit* that's triggered when the switches
*orbit_left*, *orbit_center*, and *orbit_right* are hit (in that
order) within 3 seconds, and you could configure a second shot called
*right_orbit* that's triggered when the switches *orbit_right*,
*orbit_center*, and *orbit_left* are hit within 3 seconds. (So, same
switches, but two different shots depending on the order they're hit.)
You can also group multiple shots together into a shot group. For
example, you might have three lanes at the top of your playfield, each
with a rollover switch and a light. In that case you'd configure each
of them as a separate shot. Then you could create a shot group that
grouped all three of the shots together into a logical group. A shot
group lets you do cool things, like trigger an event when all of the
member shots are in the same state (increase Bonus X when all three
shots are "lit"), and you can setup things like "shot rotation" that
rotates the state of the member shots left or right (lane change via
the flipper buttons, for example). We'll get to that soon. For now,
let's create our first shot.



(B) Create your first shot
--------------------------

You define your shots by adding a `shots:` section to your config
file. Simple enough. At this point you're probably aware that there
are two different types of config files in your machine. There are
your machine-wide config files which live in `<your machine
root>/config` folder, and then there are mode-specific config files
which live in `<your machine root>/modes/<mode name>/config`. You can
configure shots in either your machine-wide config or in a mode-
specific config. Shots you configure in your machine-wide config exist
for the entire game, and shots configured in a mode config only exist
while that mode is active. What's kind of confusing is that you can
also configure the same shot in both your machine-wide config and in a
mode-specific config. When you do this, the machine-wide configuration
for that shot is available always and acts as the default settings for
that shot, and then you can further customize the behavior of a shot
in a particular mode by adding settings for it in a mode config. Our
preference is to add all the physical shots on your playfield to your
machine-wide config since they never change. (A ramp is a ramp is a
ramp, regardless of what modes are active.) Then we customize the
shots in the mode configs for the specific modes that need to do
something special with them. As you'll see as we dig deeper into
shots, shots and modes are tightly integrated in MPF, and in fact a
single shot can be configured in multiple modes at the same time. (The
shot knows which modes it's configured for, and when it's hit it can
track multiple states from multiple modes at the same time!) You can
even configure shots in a mode config so that shot is "blocked" while
the mode is active. (For example, maybe your pop bumpers count up
towards super jets in your base game mode, but you might have a
special game mode where you want the bumpers to only be used by that
mode.) We're getting ahead of ourselves a bit. Let's start by creating
our first shot in the machine-wide config file. Pick a switch that has
a light or LED near it to begin with. This can be a standup target, a
rollover lane, or something like that. If you have matrix lights in
your machine, setup the shot like this:


::

    
    shots:
      my_first_shot:
        switch: s_standup_1
        light: l_right_middle_triangle


If you have LEDs, you'd setup your shot like this:


::

    
    shots:
      my_first_shot:
        switch: s_standup_1
        led: l_right_middle_triangle


Notice that the configuration for the shot is the same. The only
difference is whether you specific a `light:` or `led:`.



(C) Test your shot
------------------

At this point you can start a game and test your shot. When the game
starts, you should notice that the light associated with your shot is
off. If you hit the switch associated with your shot, the light will
come on. Congrats! You now have a shot! The "state" of the shot
(whether it's *unlit* or *lit*, in this case), is saved on a per-
player basis. If you start a game, launch a ball, and hit your shot,
you'll notice that when the ball drains the shot is still lit. (Later
we'll show you how to add scoring and how to control when the shot
resets.) Also notice that if you start a multiplayer game, if the
first player hits the shot and lights it, then when the second
player's ball starts the shot will go back to the *unlit* state since
the second player hasn't lit it yet. Shots are only active while a
ball is in play, so you have to start a game in order for your shots
to work. (Note that the ball counts as "in play" once it's sitting in
the plunger lane waiting to be plunged, so as soon as you hit start
and the trough ejects a ball, you should be able to hit the switch
associated with your shot and see the light come on.)



(D) Change the shot profile
---------------------------

Right now your shot has two states. It starts unlit, then you hit it,
then it becomes lit. Shots in MPF can have *profiles* applied to them
that control how they behave, including what the lights do and what
happens when you hit them. When you build your config for your
machine, you can create different profiles (each profile has a name),
and then you can apply those profiles to your shots. MPF has a built-
in profile called "default," and this default profile is automatically
applied to shots where you don't specify that another profile should
be used. The default profile has two states. The first is called
"unlit" and it sets the light to be off. The second is called "lit"
and it sets the light to be on. So what's happening behind the scenes
is you setup your shot, you did not specify a profile so MPF applied
the profile called default, the first step in that default profile is
called unlit and has the light set to be off which is why the light
starts off, then when you hit the switch for the shot, the profile is
advanced to the next step which is called "lit" and which is
configured to turn on the light. Hopefully that all makes sense? :)
Let's create a new profile and apply it to this shot so you can see it
in action.



(1) Create a new profile
~~~~~~~~~~~~~~~~~~~~~~~~

You create your shot profiles in the shot_profiles: section of your
config file. Like the other shot-related settings, you can add your
profiles to either your machine-wide or to a mode-specific config. It
really doesn't matter. We prefer to add profiles that we'll use
throughout our game to the machine-wide config, and then if there's
some special profile that we'll just use for one mode then we'll add
that to the mode-specific config. (Profiles end up being available
across the entire machine regardless of where they're configured, so
don't create two different profiles with the same name.) For now,
let's create a new profile in the machine-wide config.yaml file. Start
by adding a section called shot_profiles:


::

    
    shot_profiles:


(You can read about all the profile settings in the ` `shot_profiles:`
section`_ of the configuration file reference.) Let's create a new
profile called "hit_me" which will start with the light in a flashing
state, and then when the shot is hit, it will change to a solid "on"
state. We would set it up like this:


::

    
    shot_profiles:
        hit_me:
            states:
              - name: lit
                light_script: flash
              - name: complete
                light_script: "on"


Looking at what we just entered above, you see the profile entry for
the profile named "hit_me", then you see an entry for "states", and
under there you see the steps for the states. (Note that each step
starts with a dash, then a space, then a "name:" entry. The name is
the name of that state (or step), and under it you see the
light_script that will be played when that state is active for that
shot. In this case, we created two states. The first we decided to
call "lit" and we play a light_script called "flash", and the second
state we're calling "complete" and we play a light_script called
"off". (We haven't talked about light_scripts yet. We'll get to those
later, though they're configured via the config files too. You can
read more about them `here`_.) MPF includes some built-in light
scripts called *on*, *off*, and *flash* which is why we can use them
here without defining them elsewhere in our config file. Also note
that we put the "on" script in quotes. This is an annoying YAML thing.
Python's YAML processor tries to be smart about values it finds in
yaml files. If it sees a value of *on*, it interprets it as a boolean
"True" entry. The YAML processor converts several words to boolean
True, including *true*, *yes*, and *on*. In this case we don't want
our entry to be converted to `light_script: True`, rather, we want it
to be `light_script: on`, so that's why we put quotes around it. It's
like we're saying, "Dude, just read this as "on", don't try to be all
smart and convert it to True." Anyway, so now we have a profile
defined called hit_me that has two states: *lit* (flashing) and
*complete* (on).



(2) Apply this profile to your shot
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now go back into the config file for your base mode (
`/modes/base/config/base.yaml`) and go back to the shots section we
setup before. Then add a setting to that shot called `profile:` and
add your *hit_me* profile, like this:


::

    
    shots:
      my_first_shot:
        switch: s_standup_1
        led: l_right_middle_triangle
        profile: hit_me




(3) Test it out
~~~~~~~~~~~~~~~

Be sure to save both of your config files, and then start a game. You
should see that the light for your shot is flashing (since the "flash"
script is applied in that's the light_script for the first step in the
*hit_me* profile). Then when you hit the switch for this shot, the
light should turn on solid.



(E) Add some scoring
--------------------

Remember from one of the `earlier steps`_ in the tutorial that we
added a `scoring:` section to your base mode's config file. Also
remember that the scoring section has entries for events that you tie
scores to. So in order to add scoring to your new shot, we need to
know (not done yet... work in progress....)

.. _ section: https://missionpinball.com/docs/configuration-file-reference/shot_profiles/
.. _earlier steps: https://missionpinball.com/docs/tutorial/add-scoring-to-your-base-mode/
.. _here: https://missionpinball.com/docs/configuration-file-reference/lightscripts/


