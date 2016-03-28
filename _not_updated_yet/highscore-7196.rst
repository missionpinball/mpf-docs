
The *high_score:* section of the config file contains settings for the
high score mode. This section *cannot* be used in your machine-wide
config files. This section *can* be used in mode-specific config
files. There's a full `How To guide`_ which walks you through setting
up the high score mode, so be sure to read that for the details. This
page just contains the settings which control how the high score mode
behaves. Here's an example config:


::

    
    high_score:
      shift_left_tag: left_flipper
      shift_right_tag: right_flipper
      select_tag: start
      award_slide_display_time: 4s
      categories:
      - score:
          - GRAND CHAMPION
          - HIGH SCORE 1
          - HIGH SCORE 2
          - HIGH SCORE 3
          - HIGH SCORE 4




shift_left_tag:
~~~~~~~~~~~~~~~

This is the name of a tag applied to a switch which causes the
character picker to shift the highlighted character to the left when a
switch with this tag is activated. The default is left_flipper, which
means in order for this to work, you'd add left_flipper to your left
flipper button. For example:


::

    
    switches:
      s_lower_left_flipper:
        number: 0A
        tags: left_flipper




shift_right_tag:
~~~~~~~~~~~~~~~~

Just like the shit_left_tag, but the name of the tag for the switch
that will shift the selected character to the right.



select_tag:
~~~~~~~~~~~

The tag of the switch that, when activated, will select the currently-
highlighted character. (Usually this will add the highlighted letter
to the list of entered characters, but there are also characters for
*back* and *end*, so when this switch is hit, it will do whatever
action is highlighted.)



award_slide_display_time:
~~~~~~~~~~~~~~~~~~~~~~~~~

The amount of time (entered in MPF time string format) which controls
how long the award slide is shown on the display after the player
enters their name or initials. Once this time passes, the high score
mode will move on to collecting the initials for the next player
and/or finish the game ending process and move on to the attract mode.



categories:
~~~~~~~~~~~

The list of player variables you want to track for each high score
category, with sub-entries under each for the award names (labels) for
each position.

.. _How To guide: https://missionpinball.com/docs/howto/high-scores/


