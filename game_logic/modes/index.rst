Modes
=====

Game modes are a big part of pinball programming and a big part of MPF, so it's
worth taking an in-depth look at what they are and how they work.

+---------------------------------------------------------------------------+
| Related Config File Sections                                              |
+===========================================================================+
| :doc:`/config/mode`                                                       |
+---------------------------------------------------------------------------+
| :doc:`/config/modes`                                                      |
+---------------------------------------------------------------------------+

As a pinball player, you're probably familiar with the concept of "modes." Most
modern machines have lots of different modes, and typically you complete various
modes throughout a game on your way to the wizard mode. Many machines have
lights on the playfield that show what modes have been completed so far. The
player might need to do something to light a "start mode" shot, and then when
that shot is made, the mode starts. Then the mode runs for awhile, and while
it's running there's typically some kind of sub-goal. (Hit as many standups as
you can, shoot both ramps, get as many pop bumper hits as possible, etc.) Some
modes run for a predetermined amount of time (e.g. 30 seconds or until the ball
drains), some modes are multiball and stop when there's only one ball left, some
modes run until the ball ends, some modes run until you complete the mode's
objectives, and some modes just sort of run forever.

MPF takes a slightly different approach to modes. In MPF, modes are used for
almost everything—a lot more than just "in game" modes. For example, the attract
mode is a "mode" in MPF, as is the bonus processing, the high score name entry,
and lots of other things that you wouldn't think of as a traditional game mode.
In fact even the "game" itself is a mode in MPF! MPF includes many built-in
modes (that you can use outright or customize), and you can create your own
modes as needed.

How modes work in MPF
---------------------

To add a mode to your MPF machine configuration, you create a folder called
*modes* in your machine's folder. Then inside there, you create subfolders for
each mode in your machine, like this.

.. todo:
   Add image

In your game, you might have dozens (or even
hundreds) of mode folders. Each of your modes folders is almost like a mini-MPF
configuration that's only active during that mode. You can have subfolders in
each mode folder for game assets, config files, and code that only apply to that
mode, like this:

Each of a mode's subfolders follows the same structure as your machine folder in
general. The *config* folder holds YAML configuration files, the *shows* folder
holds show files, the *sounds* folder contains audio files, the *animations*
folder contains animations, etc. (Note that not every type of folder will be in
every mode. If a mode doesn't have a specific type of content, then you don't
need to include the folder for it.) The idea is that each subfolder holds
everything that mode needs, and everything in a mode's folder only applies to
that specific mode. For example, in a mode's config file, you can add several
types of configuration entries (as detailed in the configuration file
reference), that only apply when that mode is active, including:

+ shows
+ slides
+ multiballs
+ ball locks
+ sounds
+ shows
+ scoring
+ etc.

Again, anything that's specified in a mode's configuration file is only active
while that mode is active. So if you have a mode called "multiball" with the
following entry in that mode's config file:

::

    scoring:
        right_ramp_hit:
            score: 50000

In that case the *right_ramp_hit* shot event will only award the points when
that multiball mode is running. When it stops, that scoring configuration is
removed. (You can also configure certain events to be "blocked" from propagating
down to lower-priority modes. More on that in a bit.)

Machine-wide versus mode-specific folders and configurations
------------------------------------------------------------

You might have noticed that many of the settings you add to mode- specific
configuration files are also valid settings for the machine- wide configuration
files which can exist in ``your_machine_folder/config/config.yaml`` file. So
what's the difference between the two? If you configure a setting in a machine-
wide configuration file, then that setting will be available at all times in
your machine. If you configure a setting in a mode-specific configuration file,
then that setting will only apply when that mode is active. The same is true for
asset files (in your images, animations, movies, sounds, or shows folder). For
example, if you put a sound file in ``your_machine_folder/sounds`` folder, then
that sound will be available to any mode in your machine. If you put it in the
*sounds* folder under a specific mode, then that sound file will only be
available to that mode. You can even configure assets to automatically load when
a mode starts and unload when a mode ends—a feature that is necessary on
memory-limited hardware platforms like the BeagleBone Black. The reason MPF's
mode system was built this way is so that each mode is self-contained. This is
especially useful in situations where more than one person is working on a
particular game. You can think of each mode's folder as a mini self-contained
MPF environment, as each mode will have its own files and configuration. This
also makes it easier to keep track of which modes use which files.

When to use modes
-----------------

As you read this, it's natural to think of MPF's modes like game modes, and
certainly that's a big part of how they're used. But there is no limit to the
number of modes that can be active at any one time (and it doesn't negative
affect performance to have dozens of modes running at once), so when you start
programming your game you'll probably end up breaking your game logic into lots
of little modes.

For example, skill shot should be implemented as a mode. You could create a mode
called *skill_shot* that loads when a new player is up, and while it's active it
can light certain shots and award points and play light shows and animations
associated with the skill shot. You can also setup a timer that automatically
starts running when the ball is plunged, and then when the timer ends, you can
configure it to unload the skill shot mode. (You would also configure the skill
shot mode to stop and unload as soon as the skill shot is made.) You might also
have modes which track combos, progress towards ball locks, or really anything
else you want.

The key with modes in MPF is to understand that they're more than game modes.
You'll create lots and lots of them for all sorts of things. (Basically anything
you want which temporarily changes switches, rules, scoring, or any type of
device behavior will be a mode in MPF.)

Adding your modes to your machine configuration
-----------------------------------------------

If you want to add a mode to your game, you need to add a ``modes:`` section to
your machine configuration file and then create an entry for each mode (by
listing the folder), like this: (It's important to have the dash in front of
each line.)

::

    modes:
      - skillshot
      - base
      - both_ramps_made
      - gun_fight
      - multiball
      - skillshot
      - watch_tower

The reason for this is that you might have some modes in your *modes* folder
that you're working on that aren't complete yet, or you might want to build
different sets of configuration files that use different modes. So you have to
list all the modes that you want to use in your machine config file for MPF to
read in those modes.

Working with mode-specific config files
---------------------------------------

We already mentioned that each mode in MPF is really like a full "mini" instance
of MPF with settings and assets that only apply to that specific mode. So just
like the root MPF config, you create a ``config`` subfolder in each mode's
folder, and then you put a YAML configuration file in that mode's *config*
folder that holds all the config settings for that mode. Recall that the default
config file name for your machine-wide configuration is a file called
``config.yaml``. When you setup a mode's specific config file, you do so by
naming the file ``<mode_name>.yaml``. (So this file would be
``<your_machine_file>/modes/<mode_name>/config/<mode_name>.yaml`` file.)

For example, the configuration file for a skill shot mode might be
``<your_machine_file>/modes/skillshot/config/skillshot.yaml``. The reason each
mode's config file is based on the mode name rather than just being called
``config.yaml`` is simply for the convenience of the programmer. Our experience
is that when we're working on a game, we typically have lots of tabs open in our
file editor, and it's really confusing if all the tabs are named *config.yaml*!
So we made it so each mode's config file is based on the mode name instead. In
each mode's config file, you can add an entry called ``mode:`` which holds
settings for the mode itself. Typically this is just a list of MPF events that
will cause the mode to start and stop, as well as the priority the mode runs at,
the name of the mode, and whether the mode has any custom Python code that goes
with it. (Full details of this are in the ``mode:`` section of the configuration
file reference.)

Starting and stopping modes
---------------------------

Modes stop and start based on standard MPF events. For example, if you want a
mode to run whenever a ball is in play, you'd add ``ball_starting`` to the
mode's start events list, and you wouldn't specific a stop event. If you want a
mode to automatically stop when a timer expires, you'd add the name of the event
that's posted when the timer ends to the mode's stop events list.

Mode priorities
---------------

When you set up the configuration for a mode (via the ``mode:`` section of that
mode's ``config/<mode_name>.yaml`` file, you can optionally specify a priority
for that mode. Specifying a priority for a mode is useful when you have more
than one mode running and you want to control how all the running modes interact
with each other.

For example, you can configure scoring events so they "block" lower level modes
which have score configured for the same event. So you might have a base game
mode which scores 10k points for a ramp shot, but then in one particular mode
you might want to make the ramps worth 100l points. To do this you would add the
scoring setting for 100k to your special mode, and then you'd run that mode at a
higher priority than your base game mode and configure the scoring for that
event to block the scoring from the lower mode. (Otherwise you'd get both
scoring events and a ramp shot would grant 110k points.) Whether you configure a
scoring event to block or not is optional, and you can specify it on an
individual basis per scoring event. (And in many case you very well might want
to score both events from both modes.)

The mode priorities also affect the priorities of things like all display
widgets and slides. For example, your base mode might play an animation and a
light show when a ramp shot is made in the base game mode, but when your special
higher mode is running you might want to play a different slide and a different
light show. So be specifying the special mode to run at a higher priority, it
will get priority access to the display and lights. (Again you can configure
this on a setting-by-setting basis, because there are plenty of times where you
might actually want the lower-priority shows to play even when a higher priority
mode is running.)

.. note:: In MPF prior to v0.20, there was the concept of "machine" modes and
   "game" modes. Starting with MPF v0.20, those have been combined, and
   they're just called *modes*. MPF comes with its own built-in modes
   that will be mixed together with your own machine-specific modes. For
   example, MPF includes modes for *attract* (priority 10) and *game*
   (priority 20) which are responsible for the fundamentals of running
   the attract and game modes.

Using modes as game logic
-------------------------

.. toctree::

   modes_as_game_logic

+------------------------------------------------------------------------------+
| Related How To Guides                                                        |
+==============================================================================+
| :doc:`Creating your first game mode </tutorial/14_add_a_mode>`               |
+------------------------------------------------------------------------------+

+------------------------------------------------------------------------------+
| Related Events                                                               |
+==============================================================================+
| :doc:`/events/mode_name_started`                                             |
+------------------------------------------------------------------------------+
| :doc:`/events/mode_name_starting`                                            |
+------------------------------------------------------------------------------+
| :doc:`/events/mode_name_stopped`                                             |
+------------------------------------------------------------------------------+
| :doc:`/events/mode_name_stopping`                                            |
+------------------------------------------------------------------------------+
| :doc:`/events/clear`                                                         |
+------------------------------------------------------------------------------+

Built-in Modes
--------------

MPF includes several "built-in" modes which are ready to use in your game. Some
of them are used automatically, and some require that you add some config
sections and options to your machine. Click on each for details:

.. toctree::

   Creating your own modes <custom_modes>
   Attract <attract>
   Game <game>
   Credits <credits>
   High score <high_score>
   Tilt <tilt>


