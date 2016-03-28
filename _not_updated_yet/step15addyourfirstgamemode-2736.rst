
By this point in the tutorial you should have a "playable" game,
though it's pretty boring because there's no scoring, no modes, and
the display just shows *PLAYER X BALL X* the whole time. So in this
step the real fun will begin as we configure our first game mode! So
far all of the configuration we've been doing has been machine-wide
configuration which was stored in the
`machine_files/your_machine/config` folder. Now we're going to add a
`modes` folder and then a sub-folder for each mode. Then in each
mode's folder, we can create mode-specific configurations. What's cool
about MPF's modes system is that all of the configuration you do for a
mode is only active when that mode is active. In fact from here on
out, almost everything you configure will be at the *mode*-level
rather than the *machine-wide* level. As we go deeper into the
tutorial and the How To guides, you'll start to get a feel for what
types of things should be in the machine-wide configuration versus the
types of things that should be in mode-specific configurations. Pretty
much all the hardware (coils, switches, lights, leds, ball devices,
platform, DMD, etc.) are configured as machine-wide settings, and then
game logic-type things (scoring, shots, sound effects, animations,
light shows, etc.) are configured as mode-specific settings. In MPF
you can have as many modes running at once as you want. In fact you'll
probably use this to your advantage, breaking up your game into lots
of little modes to make the programming easier. (Many of these modes
will not be "in your face" modes that the player is aware of. Things
like skill shot, combo timers, super jet counters, etc., will all be
configuredas modes even though the player wouldn't think of them as
modes.)



(A) Read the documentation about modes
--------------------------------------

The first step to setting up a game mode is to understand how game
modes work in MPF. So `read that documentation now`_ to get an
overview, and then come back here for the step-by-step walk-through of
doing your first mode.



(B) Set up the folders & files for your "base"mode
--------------------------------------------------

The first mode we're going to create is a mode called "base." (Don't
call it "game" because MPF has a built in mode called "game" that you
don't want to overwrite.) This base game mode will be running at all
times (while a game is in play) and can be thought of as the "default"
game mode. We'll set up default shots, scoring, configure the DMD to
show the score, etc. Everything in the base game mode will be
available if no other higher-priority modes arerunning. To create the
base game mode:


#. Create a folder called `modes` in your machine's folder.
#. Create an empty file in that folder called `__init__.py`. That's
   two underscores, then `init`, then two more underscores, then `.py`.
   That file can literally be blank, but it just has to have that name.
   (What is `__init__.py`?It's a marker file to tell Python that a folder
   might contain code it has to run. MPF needs it to allow you to add
   custom code to your modes folder. Just add it now and forget about it
   and all is well. `More info here`_.)
#. Create a subfolder your `modes` folder called `base`. (You will
   ultimately createone subfolder for each mode you have, and the name of
   the folder controls the name of the mode.)
#. Inside your `base` folder, create a folder called `config`. (This
   folder will hold your mode-specific config files.)
#. Inside your `config` folder, create a file called `base.yaml`.
   (This is the default config file for your base mode. We use the naming
   scheme `<mode_name>.yaml` instead of `config.yaml` for these to make
   it easier to keep track of which files are which if you open a bunch
   of them at once in your editor.)


At this pointyour machine's folder & file structure should look like
this: ` `_



(C) Add your base game mode's settings to its config file
---------------------------------------------------------

The settings that control a mode are configured the mode's own
configuration file. We do this because itallows modes to be completely
self-contained. In other words, as long as you have a mode's folder
and all its content, then you have everything you need for that mode.
To do this, open your new mode's `base.yaml` in your code editor. Add
your config_version, then create a top-level configuration section
called `mode:`. On the next line, indent four spaces and add the entry
`start_events: ball_starting`. On the following line, also indent four
spaces and type `priority: 100`. Your `base.yaml` file should now look
like this:


::

    
    #config_version=3
    mode:
        start_events: ball_starting
        priority: 100


The varioussettings options for your `mode:` section are detailed in
the `configuration file reference`_. The two settings we added here
should be pretty obvious. The `start_events: ball_starting` means that
this mode will automatically start when the `MPF event`_
*ball_starting* is posted. (In other words, this mode will start
whenever a ball starts.) You can also enter a list of *stop_events* to
control how the mode ends, though if you don't enter one here then the
mode will automatically stop when the ball ends, so you don't have to
specify a stop event now. The `priority: 100` means that everything
this mode does will have a base priority of 100. We'll create future
modes at higher priorities so they can take over the display, control
lights, filter and block scoring, etc.



(D) Add your mode to your machine-wide config file
--------------------------------------------------

Now that you have a mode set up, you need to go back to your machine-
wide configuration file to add this new mode to the list of modes that
your game will use. At first you might think this is a bit confusing.
After all, you just created a folder and a config file for your new
mode, so why do you have to specify that mode in another location too?
The reason is wedon't want to automatically include a mode in a game
just because that mode has a folder in the modes folder. (After all,
what if you're testing something out, or if you have multiple versions
of a mode you're playing with? It would be dangerous if MPF just
automatically loaded every mode it found.) So instead we built it so
that you have to add all the modes you want to be availablein a game
to a list in the machine-wide config file. To do this, go back to your
machine-wide `config.yaml` file (in `your_machine/config/config.yaml`)
and add a top-level section called `modes:`. (Like all the sections in
your config file, you can put this section anywhere you want in your
file. Maybe up towards the top so it's easy to find later?) Then on
the next line, type two spaces, then a dash, then another space, then
type `base`. So now that section of your `config.yaml` should look
like this:


::

    
    modes:
      - base


Note that it's very important that you put dashes in front of each
mode in this list? Why? Because with dashes, MPF will be able to
combine settings together in this list from different config files.
For modes that important, because MPF has several built-in modes it
uses for its own things. (For example, attract and game are both
modes, and we'll be creating future ones that you might want to use
too for tilt, volume control, game statistics, high score entry,
credits, etc.)



(E) Run your game to verify your new mode works
-----------------------------------------------

Be sure to save the changes to `base.yaml` and `config.yaml`, and then
run your game again. For this test, you do not need to use verbose
logging since mode information is reported in the basic level of
logging. Once MPFis running, start a game and you should see something
likeon the console and/or the log file:


::

    
    INFO : Mode.base : Mode Started. Priority: 100
    INFO : ModeController : +=============== ACTIVE MODES ===================+
    INFO : ModeController : | base : 100                                     |
    INFO : ModeController : | game : 20                                      |
    INFO : ModeController : +------------------------------------------------+


As you can probably imagine, the *ACTIVE MODES*section liststhe game
that are currently active, as well as their priorities. This list will
automatically reprint in the log any time a mode starts or stops.



(F) Make your base mode do something useful
-------------------------------------------

We already mentioned that there are lots of different things you could
add to your base mode. For now, let's configure the DMDso that it
shows the player's score. To do this, go back to your base mode's
config file ( `your_machine/modes/base/config/base.yaml`) and add a
section called `slide_player:`. Then add the following subsections so
your complete `base.yaml` looks like this:


::

    
    mode:
        start_events: ball_starting
        priority: 100
    
    slide_player:
      mode_base_started:
        - type: text
          text: "%score%"
          number_grouping: true
          min_digits: 2
          v_pos: center
          transition:
              type: move_in
        - type: text
          text: PLAYER %number%
          v_pos: bottom
          h_pos: left
          font: small
        - type: text
          text: BALL %ball%
          v_pos: bottom
          h_pos: right
          font: small


We briefly touched on the `slide_player:` functionality earlier in
this tutorial.(Remember that each sub-entry here will listen for an
MPF event with that name and then show its content on the display.) So
what's happening here is two things: MPF's mode controller posts an
event called *mode_<mode name>_started* and *mode_<mode_name>_stopped*
whenever a mode starts or stops. So in this case, we set our slide
player entry to play when it sees the event *mode_base_started* which
means it will play that slide as soon as the base mode starts. (And
since you configured your base mode to start based on the
*ball_starting* event, this means this text will print whenever you
start a ball.) You may be wondering why we don't set that slide to
play on the *ball_starting* event? The key to remember with game modes
is thatall the settings in your mode-specific config file are only
active when the mode itself is active. In the case of our base mode,
the *ball_starting* event is what actually causes the mode to start.
When *ball_starting*is posted, the base mode starts and loads its
configuration. At that point that *ball_starting* event has already
happened, so if you set a slide to play within that mode then it will
never play because it doesn't start watching for that event until
after it happened. (Hopefully that makes sense?) Anyway, if you look
at the `slide_player:` entries under `mode_base_started:`, you'll see
that it shows the player's score, the player number, and the ball
number. Note that those entries have words between percentage signs.
Words between percentage signs are variables that are replaced in real
time when they're updated. In this case these are "player variables"
because they are values that belong to the current player. (We'll dig
into this more later.) Also note that the text: "%score%" entry has
quotes around it. That's a YAML thing because YAML values can't start
with a percent sign. So we wrap it in quotes. Finally, notice that
there's a ` *move in* transition`_ which will move this slide in from
the top of the display. (Check out the configuration file reference
for `full details about how the s `lide_player:` configuration
works`_.) Now run your game and press start and look at what happens:
https://www.youtube.com/watch?v=v1DGd8exQIs



(G) Remove the old slide_player ball_started entry
--------------------------------------------------

Now that you have this cool score display from your new base mode, you
can go into your machine-wide config.yaml and remove the slide_player:
entry for ball_started:. So now the slide_player: in your machine-wide
config.yaml should just look like this:


::

    
    slide_player:
        mode_attract_started:
            type: text
            text: PRESS START
            slide_priority: 10




(H) Troubleshooting if it didn't work
-------------------------------------


+ Make sure you actually start a game. Remember that this new base
  mode is only active when a ball starts from a game that's in progress,
  so you won't see the mode until a game starts. (If you're not able to
  start a game, check the troubleshooting tips in the previous step.)
+ If you get some kind of crash or error, specifically any errors that
  mention anything about"config" or "path," double-check that you put
  all the files in the proper locations back in Step (B). (A common
  mistake is to put `base.yaml` in the `base` folder rather than the
  `base/config` folder.)


.. _MPF event: https://missionpinball.com/docs/events/
.. _configuration file reference: https://missionpinball.com/docs/configuration-file-reference/mode/
.. _read that documentation now: https://missionpinball.com/docs/mpf-core-architecture/modes/
.. _ transition: https://missionpinball.com/docs/displays/transitions/move-in/
.. _More info here: http://stackoverflow.com/questions/448271/what-is-init-py-for
.. _ configuration works: https://missionpinball.com/docs/configuration-file-reference/slideplayer/


