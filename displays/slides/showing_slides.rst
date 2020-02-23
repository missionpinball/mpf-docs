How to Show a Slide on a Display
================================

Once you have your :doc:`slides created <creating_slides>`, you need to decide
which slides you show when. (Just remember you can test slides and widgets
interactively using :doc:`Interactive MC (iMC) </tools/imc/index>`.)

Using the slide_player
----------------------

The most common option is to use the :doc:`/config/slide_player` section of a config
file. This can be in either your machine-wide or in mode-specific config files.
(Like all mode settings, slides in a mode-based config file will only play
when that mode is active.)

The slide player is based on MPF's :doc:`events system </events/index>`,
meaning that you basically say, "play THIS slide when THAT event happens".

For example, if you want to play a slide named "good_job" when the event
"left_lane_hit" is posted, you would set your config like this:

.. code-block:: mpf-mc-config

   #! slides:
   #!   good_job:
   #!     - type: text
   #!       text: "GOOD JOB"
   slide_player:
     left_lane_hit: good_job
   ##! test
   #! post left_lane_hit
   #! advance_time_and_run .1
   #! assert_text_on_top_slide "GOOD JOB"

You can have as many event/slide combinations as you want, like this:

.. code-block:: mpf-mc-config

   #! slides:
   #!   good_job:
   #!     - type: text
   #!       text: "GOOD JOB"
   #!   ramp_champ:
   #!     - type: text
   #!       text: "RAMP CHAMP"
   slide_player:
     left_lane_hit: good_job
     right_lane_hit: good_job
     left_ramp_hit: ramp_champ
   ##! test
   #! post left_lane_hit
   #! advance_time_and_run .1
   #! assert_text_on_top_slide "GOOD JOB"

The above examples are what we call the "express" config option since each
event specifies a slide name, but no other options. (It just uses the default
options for showing each slide. But instead of putting the
slide name after the event name, you can also create a sub-entry with the
slide name, then *another* sub-entry with additional options, like this:

.. code-block:: mpf-mc-config

   #! displays:
   #!   dmd:
   #!     width: 128
   #!     height: 32
   #! slides:
   #!   ramp_hit_slide:
   #!     - type: text
   #!       text: Ramp has been hit
   slide_player:
     right_ramp_hit:
       ramp_hit_slide:
         expire: 2s
         target: dmd
   ##! test
   #! post right_ramp_hit
   #! advance_time_and_run .1
   #! assert_text_on_top_slide "Ramp has been hit" dmd

You can mix-and-match all of these in a single config, like this:

.. code-block:: mpf-mc-config

   #! displays:
   #!   dmd:
   #!     width: 128
   #!     height: 32
   #! slides:
   #!   ramp_hit_slide:
   #!     - type: text
   #!       text: Ramp has been hit
   #!   good_job:
   #!     - type: text
   #!       text: "GOOD JOB"
   #!   ramp_champ:
   #!     - type: text
   #!       text: "RAMP CHAMP"
   slide_player:
     left_lane_hit: good_job
     right_lane_hit: good_job
     left_ramp_hit: ramp_champ
     right_ramp_hit:
       ramp_hit_slide:
         expire: 2s
         target: dmd
   ##! test
   #! post right_ramp_hit
   #! advance_time_and_run .1
   #! assert_text_on_top_slide "Ramp has been hit" dmd
   #! advance_time_and_run 3
   #! assert_text_not_on_top_slide "Ramp has been hit" dmd

In the example above, when the event "left_ramp_hit" happens, the slide
"ramp_champ" is shown. When the event "right_ramp_hit" happens, the slide
"ramp_hit_slide" is shown, but with the additional options of setting the slide
to expire (to be removed) after 2 seconds, and for that slide to show on the
"dmd" display target instead of the default display.

There are many options for the slide_player in addition to the "expire" and
"target" options shown above. Refer to the :doc:`/config/slide_player` section
of the config file reference for full details.

Adding slides to a show
-----------------------

The slide_player is one of MPF's many :doc:`/config_players/index` (so called
because they use a "config" section to "play" things). Config players can be
used in a config file (as shown above) and also in a show step. To use the slide
player in a show, you add a :doc:`/config/slides` section to a show step.

For example, if you want a slide called "happy_face" to play in a step in a
show, you can do it like this (this is a snippet of a single step in a show):

.. code-block:: mpf-mc-config

   #! slides:
   #!   happy_face:
   #!     - type: text
   #!       text: "Happy Face"
   #! show_player:
   #!   play_show: my_show
   ##! show: my_show
   - duration: 3s
     slides: happy_face
   ##! test
   #! post play_show
   #! advance_time_and_run .1
   #! assert_text_on_top_slide "Happy Face"

Again, you can use the sub-entry format to specify additional options:

.. code-block:: mpf-mc-config

   #! displays:
   #!   playfield_screen:
   #!     width: 200
   #!     height: 300
   #! slides:
   #!   happy_face:
   #!     - type: text
   #!       text: "Happy Face"
   #! show_player:
   #!   play_show: my_show
   ##! show: my_show
   - duration: 3s
     slides:
       happy_face:
         target: playfield_screen
   ##! test
   #! post play_show
   #! advance_time_and_run .1
   #! assert_text_on_top_slide "Happy Face"

Creating new slides in the slide_player
---------------------------------------

Both of the options we've show so far (using the :doc:`/config/slide_player` section of
a config file and using the :doc:`/config/slides` section of a show) have used existing
named slides that you would have already defined in the :doc:`/config/slides` section of
a config. You also have the option to define new slides directly in each of
these sections. See the :doc:`creating_slides` section of the documentation
for instructions on how to do that.

