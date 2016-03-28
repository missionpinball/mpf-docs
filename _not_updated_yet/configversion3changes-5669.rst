
MPF 0.20 introduces *#config_version=3*. Here are the changes:



Renamed Sections:
-----------------
Old name New name targets: shots: target_groups: shot_groups:
_remove_profile_events _remove_active_profile_events autofire:
switch_activity autofire:reverse_switch led: log_color_changes led:
debug Events that started with *shot_* Events now start with *target_*
attract_start mode_attract_started min balls min_balls balls per game
balls_per_game max players per game max_players shot_profiles: steps
shot_profiles: states step_names_to_rotate state_names_to_rotate
state_names_to_not_rotate step_names_to_not_rotate Events that ended
with *_remove_profile* Events now end with *_remove_active_profile*
max balls (removed)


Targets have been renamed to "shots"
------------------------------------

Pretty much everywhere that you had the word "target" in your old
config, that will now be "shot" in v3. This includes:


+ The `targets:` section
+ The `target_groups`: section
+ The `target_profiles:` section
+ Any events that began with *target_**


You'll need to find-and-replace and change these from *target* to
*shot*. Note that you *cannot* simply do a global "find and replace"
for every instance of `target` to `shot` because there are a lot of
places where the word target is used. For example, you can't change
*drop_targets* to *drop_shots*, or a ball device's *eject_targets* to
*eject_shots*.



Convert existing "shots" to new-style shots
-------------------------------------------

Previous versions of MPF config files did have functionality for
shots. That functionality has been rolled into the new *shots*
sections. (Which is awesome, because that means that what use to be
your old shots can now be combined into groups, control lights and
LEDs with different profiles, track states when they're hit, etc. And
it means that what used to be called targets now can have sequences of
switches to hit them instead of only one switch.) Because of this
change, you'll have to manually go through your existing config files
and convert & combine any of your old `shots:` sections with the new
shots. Fortunately that's pretty simple. For an old shot with one
switch, there are no changes:


::

    
    shots:
        right_ramp:
            switch: right_ramp_exit


If you had a section called "targets:" in your old file that's renamed
to shots, make sure you combine what was the old shots section into
the new shots section so your file only has a single section called
shots. For an old sequence shot:


::

    
        left_ramp:
            type: sequence
            switches: left_ramp_enter, left_ramp_exit
            time: 3s


Remove the `type:` entry and change `switches:` to `switch_sequence:`:


::

    
        left_ramp:
            switch_sequence: left_ramp_enter, left_ramp_exit
            time: 3s


Note that you can apply all the benefits of what used to be called
"targets" to your sequence shots now, including grouping them,
rotation, light scripts with steps, hit events, etc.



The Configuration File Migration Tool has been updated
------------------------------------------------------

You can use the `config file migration tool`_ to scan your machine
folder for all your YAML files and update them from v2 to v3. It can
do pretty much everything except for dealing with your existing
`shots:` sections, which it will mark for you to change. (So it will
change everything *target*-related to shots and that should all work,
but your existing *shots* entries will have to be manually converted
to the new shots format. In general that shouldn't be too difficult.)



Drop targets are now separate from shots
----------------------------------------

In prior versions of the config, drop_targets could have profiles
attached to them, and drop_target_banks were like target_groups with
profiles. In the new config, drop_targets are now "just" drop targets.
They're a switch, a coil to reset them, and (optionally) a coil to
knock them down. drop_target_banks are just a group of drop_targets as
well as (optional) bank-wide reset or knockdown coils. So any of the
profile-related settings (like *profile*, *advance_events*,
*enable_events*, *disable_events*, etc.) are now removed from the
`drop_targets:` and `drop_target_banks:` sections of your config
files. (Note that *reset* and *knockdown* events still apply.) Of
course you might want to still have the shot-like functionality with
your drop targets, and that's still possible. The way you do that in
the new config is you would just setup a shot based on the drop
target's switch (and optionally its light or LED). So you can still
manage shot profiles, states, advance them, get hit events, etc., but
that all comes from shots you have assigned to the drop target
switches, rather than to the drop target itself.



"Attract" and "Game" are now regular modes
------------------------------------------

Prior to config_version=3, there were two types of modes in MPF. Game
modes were what you would think of as regular modes. They were only
active while a game was in progress, and you configured them in your
`modes` folder and created them for base, skillshot, multiball, etc.
MPF also had what we called "machine modes" which was what the overall
state that the machine was in, such as *attract* or *game*. Now we
have gotten rid of machine modes and changed the regular game modes so
that they can also run when a game is not in progress. As part of
this, we have converted the attract and game machine modes into
regular modes. We also made a change to MPF to add a `modes` folder to
the `mpf` folder. So this means that there are now two modes folders,
one at `mpf/modes` and one in `your_machine/modes`. When MPF runs, it
will combine all the modes from both locations to apply to your game.
At this point, we only have game and attract modes in the mpf/modes
folder, but in the future we envision creating "default" modes for
tilt, volume_control, coin & credits, service menu, coin_door_open,
etc. You can customize the built-in modes by creating a folder for
that mode with the same name in your own machine's mode folder, then
you can add a mode config yaml file there which will be merged in with
the mode's default yaml file. We'll write more information about this
in the future, but for now it's important to know that you will see
attract and game modes running with this new version of MPF. (Attract
runs at priority 1, and game runs at priority 2. Your own game modes
should start at priority 100.)



Mode-specific code changes
--------------------------

If you have custom mode code in your game, you will have to make a few
changes. The name of the module that holds the parent `Mode` class has
been renamed from "mode" to "modes, meaning you need to change this:


::

    
    from mpf.system.modes import Mode


To this:


::

    
    from mpf.system.mode import Mode


Also any keyword arguments that were attached to an event that's used
to start or stop a mode will now be passed to that mode's mode_start()
and mode_stop() events, meaning you need (potentially) change your
mode code so those methods can accept keywords. If you add **kwargs to
those method definitions, that will act as a catch-all for any
keywords that are passed that you might not be expecting. You can
change it like this: Old:


::

    
    def mode_start(self):


New:


::

    
    def mode_start(self, **kwargs)


Old:


::

    
    def mode_start(self):


New


::

    
    def mode_start(self, **kwargs)




.. _config file migration tool: https://missionpinball.com/docs/tools/config-file-migrator/


