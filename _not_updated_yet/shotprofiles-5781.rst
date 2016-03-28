
You can use the `shot_profiles:` section of your config files to
configure the settings for various *shot profiles* that you can then
apply to your shots and drop targets. This sectioncan be used in your
machine-wide config files. This sectioncan be used in your mode-
specificconfig files.


::

    
    shot_profiles:
        hit_me:
            states:
                - name: active
                  light_script: flash
                  repeat: yes
                  tocks_per_sec: 5
                - name: complete
                  light_script: "off"
            player_variable: laser
        default:
            states:
              - name: unlit
                light_script: "off"
              - name: lit
                light_script: "on"
        drop_shot:
            states:
              - name: up
                light_script: "off"
              - name: down
                light_script: "on"




<name>:
~~~~~~~

This is the name of the shot profile, which is how you'll refer to it
elsewhere in your config files when you apply it to shots. The sample
*shot_profiles:* section of the config file above contains three
profiles, called *hit_me*, *default*, and *drop_shot*. (All three of
these profiles are contained in the system-wide `mpfconfig.yaml` file,
so you don't actually have to create these exact ones in your game.)



player_variable:
~~~~~~~~~~~~~~~~

This is a profile setting that lets you specify the name of the player
variable that will be used to track the status of this shot when this
profile is applied. If you don't specify the name of a player
variable, it will automatically use *<shot_name>_<profile_name>* as
the player variable.



loop:
~~~~~

Controls whether the states of this profile "loop" when they reach the
end. If true, then the shot being hit when the profile is in the last
state causes the profile to "loop" around back to the first state.
This is useful if you want to create a "toggle" shot where you could
create a profile with two steps (lit and unlit) and then set loop to
be true. (If you have more than two steps in the shot profile, then
the looping will go from the last one back to the first one.) The
default is false, meaning when the profile reaches its last state, it
will just stay there even if it's hit again.



state_names_to_rotate:
~~~~~~~~~~~~~~~~~~~~~~

This is a list of state names that will be used to determine which
shots in a shot group will be rotated. By default, all states are
included. But this can be nice if you only want to rotate a subset of
the states. For example, if you have a shot group with a bunch of
lights that represent modes, you might have a shot profile with states
called *unlit*, *active* (flashing), and *complete* (lit). You'd use
these shots (and their lights) to track the game modes you've
completed, so at any time, you'd have a bunch of unlit shots
representing modes you haven't completed yet, solidly lit shots for
modes you've completed, and a single flashing shot representing the
mode that will be started next. Then in your game if you wanted to
rotate among the incomplete targets, you would set your shot profile
so it only rotated those state names, like this:


::

    
    shot_profiles:
      mode_tracker:
        rotation_events: pop_bumper_active
        state_names_to_rotate: unlit, active
        states:
          - name: unlit
            light_script: unlit
          - name: lit
            light_script: flash
            tocks_per_second: 5
          - name: complete
            light_script: "on"




state_names_to_not_rotate:
~~~~~~~~~~~~~~~~~~~~~~~~~~

This works like *state_names_to_rotate*, except it's the opposite
where you can enter the names of states to not rotate. You don't need
to use both—the options are here just for convenience.



rotation_pattern:
~~~~~~~~~~~~~~~~~

This setting lets you specify a custom rotation pattern that's used
when an event from this profile's rotation_events: section is posted.
You enter it as a list of Ls and Rs, for example:


::

    
    rotation_pattern: L, L, L, L, R, R, R, R


In the above example, the first four times a rotation_event is posted,
this shot group will rotate to the left, then the next four to the
right, then the next four to the left, etc. The pattern will loop.
This is how you could specify a single lit target that "sweeps" back
and forth across a group of five targets, for example. This only
impacts *rotation_events*, not *rotate_left_events* and
*rotate_right_events* since those events imply a direction.



advance_on_hit:
~~~~~~~~~~~~~~~

This setting controls whether the active shot profile advances to its
next state when the shot is hit. The default is true, but you can set
this to false if you want to manually advance the shot some other way.
(If this is false, you can still advance the shot with
*advance_events*, for example.)



lights_when_disabled:
~~~~~~~~~~~~~~~~~~~~~

Controls whether the lights or LEDs for shots which have this profile
applied will be active when this shot is disabled. By default this is
*true*, so if the shot profile associated with this shot has the light
turning on, then when you disable the shot the light will stay on. Set
it to *false* if you want the lights or LEDs to turn off when the shot
is disabled. (Note that even when this is false, the lights or LEDs
can still be controlled by other light scripts, light shows, manual
commands, etc.)



block:
~~~~~~

True or false value which lets you control whether hits to this shot
are propagated down to lower priority modes. The default value is true
if you don't specify this, meaning that blocking is enabled. If you
have `block: true` in a shot profile, then hits to that shot when that
profile is applied only are registered in the highest mode where that
shot is enabled. If you set `block: false`, then when a shot is hit in
one mode it will also look down to lower priority modes where that
shot is enabled. If that lower priority mode has a different profile
applied then it will also register a hit event based on that profile.
This will continue until it reaches a level with `block: true` or
until it reaches the end of the mode list. This is better explained
with an example. Imagine you have four lanes at the top of your
machine which you use in your base mode in a normal lane-change
fashion. (Lanes are unlit by default, hit a lane and they light,
complete all four lanes for an award.) Now imagine you also use those
lanes for a skillshot where one of the lanes is flashing and you try
to hit it while the skillshot is enabled. In this case, you'd have
different shot profiles for each mode, perhaps the default profile in
your base mode (with unlit->lit states) and a skillshot profile in
your skill shot mode (with flashing->complete states). By default, if
the player hits the a lane when the skill shot mode is running, the
skillshot profile is the active profile so it's the shot that gets the
hit. But then when the skill shot mode ends, the lane the player just
hit is not lit, since that shot profile was not active when it was
hit. (In other words, the skillshot blocked the hit event.) So if you
add `block: false` to your skillshot shot profile, then when the shot
is hit when the skill shot mode is running, it will receive the hit
and advance the shot from flashing to complete. Then the lower base
mode will also get the shot, and it will advance its state from unlit
to lit. The lights for the shot will only reflect the skillshot lights
since it's the higher priority, however, you will get
*yourshot_skillshot_flashing_hit* and *yourshot_default_unlit_hit*
events since both the hits registered because you set the skillshot
profile not to block the hit.



states:
~~~~~~~

Under each shot profile name, a setting called *states:* lets you
specify various properties for the target in different states. You can
configure multiple states in the order that you want them to be
stepped through. (You use a dash, then a space, then a setting to
indicate that items should be a list. See our reference about `how to
create list items in config files`_.) The following sections explain
the settings for each state:



(state)name:
~~~~~~~~~~~~

This is the name of the step. In other words, it's what "state" the
shot is in when this profile step is active.



(state)light_script:
~~~~~~~~~~~~~~~~~~~~

This is the name of the light script that will be run on any lights or
LEDs that are configured for the shot or drop shot that has this
profile applied when the shot is hit and advances to this step. This
light script should be a `script that you've created`_ somewhere else
in your config files.



(state) hold:
~~~~~~~~~~~~~

Whether the light or LED should "hold" its final state if your light
script ends. Default is true.



(state) reset:
~~~~~~~~~~~~~~

Whether the light or LED should reset itself if your light script
ends. Default is false.



(state) repeat:
~~~~~~~~~~~~~~~

Whether the light script should repeat. Control the number of times it
repeats with the num_repeats: setting. Default is true.



(state) blend:
~~~~~~~~~~~~~~

Whether the light script should blend with whatever else that light is
doing at a lower priority. Default is false.



(state) tocks_per_sec:
~~~~~~~~~~~~~~~~~~~~~~

How fast in terms of "tocks per second" the light script should run.
Default is 10.



(state) num_repeats:
~~~~~~~~~~~~~~~~~~~~

How many times the light script should repeat. A value of 0 means it
loops forever. Note that repeat must be true in order for this to have
an effect.



(state) sync_ms:
~~~~~~~~~~~~~~~~

A sync_ms value you can use to synchronize this light script with
other scripts that might be running. (This is how you can ensure that
all the lights in your machine are flashing together.) See the
documentation on light shows for details about how this works.

.. _script that you've created: https://missionpinball.com/docs/configuration-file-reference/lightscripts/
.. _how to create list items in config files: https://missionpinball.com/docs/configuration-file-reference/adding-lists-and-lists-of-lists-to-config-files/


