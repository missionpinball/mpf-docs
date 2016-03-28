
This How To guide explains how to configure a tilt in MPF. The MPF
package contains a the code for a tilt mode which runs at all times to
watch for tilts, so all you have to do to use add some configs to your
machine’s *modes* folder and you’re all set. Features of the tilt mode
include:


+ Separate processing of tilt warning, tilt, and slam tilt events.
+ Specify that several tilt warnings coming close together only count
  as one warning.
+ Specify "settle time" that the tilt warning switch has to not
  activate in order to let it "settle" between players (so the next
  player after a super hard tilt doesn't get a tilt also because the
  plumb bob was still swinging).
+ Configurable options for when a player's tilt warnings are reset
  (per game, per ball, etc.).
+ Flexible events you can use to trigger display, sound, and lighting
  effects when tilt warnings occur.


Let's dig in to the process of actually getting the tilt setup.



(A) Create your 'tilt' mode folder
----------------------------------

The tilt mode works like any other mode in MPF. You’ll create a folder
called *tilt* in your machine’s *modes* folder, and that folder will
contain subfolders config files, images, etc. So to begin, create a
folder called *<your_machine>/modes/tilt*. Then inside there, create
another folder called *config*. Then inside there, create a file
called *tilt.yaml*. (So that file should be at
*<your_machine>/modes/tilt/config/tilt.yaml*.) Your folder structure
should look something like this:



(B) Configure options for the tilt mode
---------------------------------------

Open up the tilt mode's config file that you just copied into your
machine folder. It should be at
*<your_machine>/modes/tilt/config/tilt.yaml*. Since this file is
totally blank, add the required ` *#config_version=3*`_ to the top
line. Next, add a section called *tilt:*, and then under there, indent
a few spaces (it doesn't matter how many, 2 or 4 or whatever you
prefer) and add a section called *categories:*. Your *tilt.yaml* file
should now look like this:


::

    
    #config_version=3
    
    tilt:


Next you need to add the settings for the tilt behavior in your
machine. Here's a sample you can use as a starting point:


::

    
    tilt:
      tilt_warning_switch_tag: tilt_warning
      tilt_switch_tag: tilt
      slam_tilt_switch_tag: slam_tilt
      warnings_to_tilt: 3
      reset_warnings_events: ball_ended
      multiple_hit_window: 300ms
      settle_time: 5s
      tilt_warnings_player_var: tilt_warnings


Full details of what each of these settings does is outlined in the `
*tilt:* section`_ of the configuration file reference, so check that
out for details on anything not covered here. It's all fairly self-
explanatory. First, notice that the switches to activate the *tilt*,
*tilt warning*, and *slam tilt* are controlled by switch tags rather
than by switch names themselves. (We'll add those in the next step.)
*Warnings_to_tilt* is how many warning switch activations lead to a
tilt. The default value of 3 means that the player will have 2
warnings, since on the third activation the tilt will occur. The
*multiple_hit_window* means that multiple tilt warning events within
this time window will only count as a single warning. This is a non-
sliding window, meaning that if the window is 300ms and a tilt warning
comes in at 0 (the first one), then 250ms after that, then 60ms after
that—that will actually count as 2 warnings. (The second hit at 250ms
is within the 300ms window, but the third hit 60ms later is actually
310ms after the first one which started the window, so it counts.) The
*settle_time* is the amount of time that must pass after the last
warning before the tilt will be cleared and the next ball can start.
This is to prevent the situation where a player tilts in an aggressive
way and the plumb bob is bouncing around so much that it causes the
next player's ball to tilt too. So when a tilt occurs, if a ball
drains before the *settle_time* is up, MPF will hold the machine in
the tilt state until it settles, then proceed on to the next player
and/or the next ball. The *reset_warnings_events* is the event in MPF
that resets the tilt warnings to 0. The sample config from above means
that the tilt warnings are reset when the ball ends. In other words
with a *warnings_to_tilt* of 3, the player gets three warnings per
ball. If you want to make the warnings carry over from ball-to-ball,
you could change the *reset_warnings_events* to *game_ended*.



(C) Add switch tags
-------------------

Since the tilt mode uses switch tags instead of switch names, you need
to go into your machine-wide configuration and add the tags to the
various switches you want to do tilt-related things. In most modern
games, you'll just use the tilt_warning and slam_tilt tags, like this
(from your machine-wide config):


::

    
    switches:
      s_plumb_bob:
        number: s14
        label:
        tags: tilt
      s_slam_tilt:
        number: s21
        label:
        tags: slam_tilt




(D) Add the tilt mode to your list of modes
-------------------------------------------

Now that you have the tilt settings configured, you can add the tilt
mode to the list of modes that are used in your machine. To do this,
add `- tilt` to the *modes:* section in your machine-wide config, like
this:


::

    
    modes:
      - base
      - some_existing_mode
      - another_mode_you_might_have
      - credits
      - bonus
      - tilt


The order doesn’t matter here since the priority each mode runs at is
configured in its own mode configuration file. All you’re doing now is
configuring the tilt mode as a mode that your machine will use. You
might be wondering why your new *tilt.yaml* mode configuration file
doesn't have a *mode:* section? That's because the *tilt* mode is
built-in to MPF (in the *mpf/modes/tilt*) folder, so when you add a
*tilt* folder to your own machine's modes folder, MPF merges together
the settings from the MPF modes folder and your modes folder. (It
loads the MPF mode config first with baseline settings, and then it
merges in your machine's mode config which can override them.) If you
look at the built-in *tilt* mode's config (at
*mpf/modes/tilt/config/tilt.yaml*), you'll see it has the following
*mode:* section:


::

    
    mode:
      code: tilt.Tilt
      priority: 10000
      start_events: machine_reset_phase_3
      stop_on_ball_end: False


First is that the priority of this mode is really high, 10000 by
default. That's because we want this mode to run "on top" of any other
mode so any slides it puts on the display (like the tilt warnings) are
displayed on top of the slides from any other mode that might be
running. Also note that the tilt mode starts when the
*machine_reset_phase_3* event is posted (which is done as part of the
MPF startup process), and that there are no stop events. Basically we
want the tilt mode to start and never stop. (We even want it to run
during attract mode so it can look for slam tilts.)



(E) Add slides and lighting effects
-----------------------------------

There are several events posted by the tilt mode, including:


+ * tilt_warning * – a switch with the tilt warning tag was activated
  outside of the multiple hit window, and the player’s tilt warnings has
  just increased.
+ * tilt_warning_<x> * – Same as tilt warning, but the “x” is the
  number of the warning. This lets you put different slides on the
  display for tilt_warning_1 versus tilt_warning_2, etc.
+ * tilt * – The machine has tilted.
+ * tilt_clear * – The tilt is cleared, meaning all the balls have
  drained and the settle_time has passed.
+ * slam_tilt * – The machine has slam tilted.


You can use this events to tell the player what's going on. For
example, the configuration from the tilt mode template includes the
following:


::

    
    slide_player:
      tilt_warning_1:
        type: text
        text: WARNING
        expire: 1s
      tilt_warning_2:
        - type: text
          text: WARNING
          y: 2
        - type: text
          text: WARNING
          y: 18
          expire: 1s
      tilt:
        type: text
        text: TILT
      tilt_clear:
        clear_slides: yes


These slide player settings put a slide that says *WARNING* on the
display for 1 second on the first warning, and a slide that says
*WARNING WARNING* for the second warning. They also display a slide
that says *TILT* when the player tilts. Also note the *tilt_clear:*
entry which clears out all the slides from the tilt mode when the tilt
clears. Since the tilt mode is running at priority 10,000, these
slides should play on top of any other slides from other active modes.
You can change the fonts, placement, text, etc. of these slides or add
other display elements as you see fit. You could also add
*sound_player* or *light_player* sections if you wanted to plays
sounds or blink all the playfield lights. (To blink the playfield
lights, create a light show with 1 step that turns off all the lights
for a half-second or so.)



(F) Check out this complete tilt config file
--------------------------------------------

Here's the complete tilt config file from the Demo Man sample game. (
*demo_man/modes/tilt/config/tilt.yaml*):


::

    
    #config_version=3
    
    tilt:
      tilt_warning_switch_tag: tilt_warning
      tilt_switch_tag: tilt
      slam_tilt_switch_tag: slam_tilt
      warnings_to_tilt: 3
      reset_warnings_events: ball_ended
      multiple_hit_window: 300ms
      settle_time: 5s
      tilt_warnings_player_var: tilt_warnings
    
    slide_player:
      tilt_warning_1:
        type: text
        text: WARNING
        expire: 1s
      tilt_warning_2:
        - type: text
          text: WARNING
          y: 2
        - type: text
          text: WARNING
          y: 18
          expire: 1s
      tilt:
        type: text
        text: TILT
      tilt_clear:
        clear_slides: yes


.. _#config_version=3: https://missionpinball.com/docs/configuration-file-reference/important-config-file-concepts/config_version/
.. _ section: https://missionpinball.com/docs/configuration-file-reference/tilt/


