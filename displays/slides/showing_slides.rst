How to Show a Slide on a Display
================================

Once you have your :doc:`slides created <creating_slides>`, you need to decide
which slides you show when.

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

::

    slide_player:
        left_lane_hit: good_job

You can have as many event/slide combinations as you want, like this:

::

    slide_player:
        left_lane_hit: good_job
        right_lane_hit: good_job
        left_ramp_hit: ramp_champ

The above examples are what we call the "express" config option since each
event specifies a slide name, but no other options. (It just uses the default
options for showing each slide. But instead of putting the
slide name after the event name, you can also create a sub-entry with the
slide name, then *another* sub-entry with additional options, like this:

::

    slide_player:
        right_ramp_hit:
            ramp_hit_slide:
                expire: 2s
                target: dmd

You can mix-and-match all of these in a single config, like this:

::

    slide_player:
         left_lane_hit: good_job
         right_lane_hit: good_job
         left_ramp_hit: ramp_champ
         slide_player:
            right_ramp_hit:
                ramp_hit_slide:
                    expire: 2s
                    target: dmd

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

::

    - duration: 3s
      slide: happy_face

Again, you can use the sub-entry format to specify additional options:

::

    - duration: 3s
      slide:
        happy_face:
          target: playfield_screen

Creating new slides in the slide_player
---------------------------------------

Both of the options we've show so far (using the :doc:`/config/slide_player` section of
a config file and using the :doc:`/config/slides` section of a show) have used existing
named slides that you would have already defined in the :doc:`/config/slides` section of
a config. You also have the option to define new slides directly in each of
these sections. See the :doc:`creating_slides` section of the documentation
for instructions on how to do that.

