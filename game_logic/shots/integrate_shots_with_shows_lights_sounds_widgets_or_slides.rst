How to integrate shots with shows, lights, sounds, widgets, slides and more
===========================================================================

Pinball games need to communicate with the player.
Regarding shots this includes two typical things:

1. Indicate the current state of the shot.
   This is usually implemented by toggling a light or show an image on screen.
   Normally, the state indication stays permanently until the state changes.
   It might also permanently play of shot (i.e. to flash an arrow).
   Additionally, it has to be restored after a player change and sometimes
   on more restart.

2. On state change (or hit of a shot) the machine needs to communicate success
   to the player.
   Usually, this is implemented using a some light show, sound and some
   animation on screen.
   Additionally, this often involves scoring and might load start another mode.

To implement (1) we recommend to use :doc:`shot_profiles <shot_profiles>` and
create a show per state.
This gives you maximum flexibility.
Additionally, it will automatically restore the previous state on player change
or mode restart (lights/screen will never be out of sync with your state).

To implement (2) we recommend to use :doc:`/config_players/show_player` on the
:doc:`/events/shot_hit` event.
This allows very flexible animations/scoring/video/sounds and will also
automate all cleanup for you.

Config Example
--------------

Let us look at a very typical example (from
:doc:`/mechs/switches/rollover_switches`)
for a typical inlane/outlane setup with rotation using flipper buttons.
Additionally, we want to show the state of the lanes on screen.
When shots are hit we want to play a sound, play a show on screen and flash
the light of the shot.

First, we will define some switches and lights for inlanes and outlanes.
In a mode we define all the shots and tie them to a light.
Furthermore, we define an widget name to display for each shot.
To color the light and display the widget we define a show and integrate it
to our shots using a shot_profile.
Eventually, we add a show_player to play animations and sounds when a shot
is hit.


.. code-block:: mpf-mc-config

   # this is in your machine-wide config
   # first we define some switches + lights
   switches:
     s_outlane_left:
       number: 0
     s_inlane_left:
       number: 1
     s_inlane_right:
       number: 6
     s_outlane_right:
       number: 7
   lights:
     l_outlane_left:
       number: 0
     l_inlane_left:
       number: 1
     l_inlane_right:
       number: 6
     l_outlane_right:
       number: 7
     gi_left_sling:
       number: 8
     gi_right_sling:
       number: 9
   ##! mode: my_mode
   # put this into a mode
   # shots each pass their led and widget to the show define in their shot_profile
   shots:
     shot_outlane_left:
       switches: s_outlane_left
       profile: lane_profile
       show_tokens:
         leds: l_outlane_left
         widget: outlane_left
     shot_inlane_left:
       switches: s_inlane_left
       profile: lane_profile
       show_tokens:
         leds: l_inlane_left
         widget: inlane_left
     shot_inlane_right:
       switches: s_inlane_right
       profile: lane_profile
       show_tokens:
         leds: l_inlane_right
         widget: inlane_right
     shot_outlane_right:
       switches: s_outlane_right
       profile: lane_profile
       show_tokens:
         leds: l_outlane_right
         widget: outlane_right
   # integrate shots with their show
   shot_profiles:
     lane_profile:
       states:
         - name: unlit
           show: "off"           # a default show to turn of the led. change if you want to do something on unlit shots
         - name: lit
           show: "shot_lit"      # our show to indicate an lit shot
             # you can add more states here
   # to rotate shots and reset them when they are all lit
   shot_groups:
     sg_lanes:
       shots: shot_outlane_left, shot_inlane_left, shot_inlane_right, shot_outlane_right
       rotate_left_events: s_flipper_left_active
       rotate_right_events: s_flipper_right_active
       reset_events:
         sg_lanes_lit_complete: 1s
   # define a few widgets which show on screen. you can also use images or videos here
   widgets:
     outlane_right:
       - type: text
         text: Outlane right lit
     outlane_left:
       - type: text
         text: Outlane left lit
     inlane_right:
       - type: text
         text: Inlane right lit
     inlane_left:
       - type: text
         text: Inlane left lit
   shows:
     shot_lit:    # define our show to indicate the state
       - duration: -1      # this show step will run permanently
         widgets:    # show the corresponding widget
           (widget):
             action: add
         lights:     # turn the light purple
           (leds): purple
     shot_hit:    # define our show to communicate success to the player
       - duration: 1s      # this show step lasts 1s
           # add sounds here or videos
           # add scoring here
         shows:      # run another (built-in) show to flash the light
           flash_color:
             show_tokens:
               color: red
               leds: (leds)
             speed: 4
     group_complete:    # define our show to communicate success on completing all shots
       - duration: 1s
           # add scoring, sounds and video
         shows:
           flash_color:
             priority: 10     # higher priority as the shots
             show_tokens:
               color: green
               leds: l_outlane_left, l_inlane_left, l_inlane_right, l_outlane_right, gi_left_sling, gi_right_sling
             speed: 4
   # on success flash the sling shot gi on the side of the lane hit and play a sound/video
   show_player:
      # play a show once a each shot is lit
     shot_outlane_left_hit{state=="unlit"}:
       shot_hit:
         key: left
         show_tokens:
           leds: gi_left_sling
         loops: 0
     shot_inlane_left_hit{state=="unlit"}:
       shot_hit:
         key: left
         show_tokens:
           leds: gi_left_sling
         loops: 0
     shot_outlane_right_hit{state=="unlit"}:
       shot_hit:
         key: right
         show_tokens:
           leds: gi_right_sling
         loops: 0
     shot_inlane_right_hit{state=="unlit"}:
       shot_hit:
         key: right
         show_tokens:
           leds: gi_right_sling
         loops: 0
      # play a show when the group completes
     sg_lanes_complete{state=="lit"}:
       group_complete:
         loops: 0
   ##! test
   #! start_game
   #! start_mode my_mode
   #! assert_light_color l_outlane_left off
   #! assert_light_color l_inlane_left off
   #! assert_light_color l_inlane_right off
   #! assert_light_color l_outlane_right off
   #! hit_and_release_switch s_outlane_left
   #! advance_time_and_run .1
   #! assert_light_flashing gi_left_sling red
   #! assert_light_color gi_right_sling off
   #! assert_light_color l_outlane_left purple
   #! assert_light_color l_inlane_left off
   #! assert_light_color l_inlane_right off
   #! assert_light_color l_outlane_right off
   #! assert_text_on_top_slide "Outlane left lit"
   #! advance_time_and_run 2
   #! assert_light_color gi_left_sling off
   #! hit_and_release_switch s_outlane_right
   #! hit_and_release_switch s_inlane_left
   #! advance_time_and_run .1
   #! assert_light_flashing gi_left_sling red .4
   #! assert_light_flashing gi_right_sling red .4
   #! assert_light_color l_outlane_left purple
   #! assert_light_color l_inlane_left purple
   #! assert_light_color l_inlane_right off
   #! assert_light_color l_outlane_right purple
   #! assert_text_on_top_slide "Outlane left lit"
   #! assert_text_on_top_slide "Inlane left lit"
   #! assert_text_on_top_slide "Outlane right lit"
   #! post s_flipper_left_active
   #! advance_time_and_run .1
   #! assert_light_color l_outlane_left purple
   #! assert_light_color l_inlane_left off
   #! assert_light_color l_inlane_right purple
   #! assert_light_color l_outlane_right purple
   #! assert_text_on_top_slide "Outlane left lit"
   #! assert_text_on_top_slide "Inlane right lit"
   #! assert_text_on_top_slide "Outlane right lit"
   #! hit_and_release_switch s_inlane_left
   #! advance_time_and_run .1
   #! assert_light_flashing l_outlane_left green .4
   #! assert_light_flashing l_inlane_left green .4
   #! advance_time_and_run 1
   #! assert_light_color l_outlane_left off
   #! assert_light_color l_inlane_left off
   #! assert_light_color l_inlane_right off
   #! assert_light_color l_outlane_right off
   #! assert_text_not_on_top_slide "Outlane left lit"
   #! assert_text_not_on_top_slide "Inlane right lit"
   #! assert_text_not_on_top_slide "Inlane left lit"
   #! assert_text_not_on_top_slide "Outlane right lit"

