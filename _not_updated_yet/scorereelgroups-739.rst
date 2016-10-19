
The *score_reel_groups:* section in the machine configuration files
holds settings for groupings of mechanical score reels for EM-style
pinball machines. Details about how score reel groups work can be
found in the `Score Reel Groups device section`_ of this
documentation.

This sectioncan be used in your machine-wide config files. This
sectioncanbe used in mode-specific config files.

Here's an example:


::

    
        score_reel_groups:
            player1:
                reels: score_1p_10k, score_1p_1k, score_1p_100, score_1p_10, None
                tags: player1
                max_simultaneous_coils: 2
                chimes: None, chime1, chime2, chime3, None
                confirm: lazy
            player2:
                reels: score_2p_10k, score_2p_1k, score_2p_100, score_2p_10, None
                tags: player2
                max_simultaneous_coils: 2
                chimes: None, chime1, chime2, chime3, None
                confirm: lazy


Each section is headed with the name you’d like to refer to this score
reel group as in your game code. In the above example, the score reel
groups are named *player1*and *player2*, which obviously refer to the
Player 1 and Player 2 score reel groupings in the machine's backbox.
There are several subsections for each `score_reel_group`:



reels:
~~~~~~

This is a comma-separated list of individual `score reels (based on
the names you gave them)`_that are grouped together to show the entire
value displayed in this group.The number of items in this list equals
the number of digits in your score, and the position of each
individual reel represents its position in the group, starting with
the left-most digit. Note that if your score reel group has one of
those fake plastic insertsa given position, then you need to enter the
word `None`in this list. The configuration sample above is for a
5-digit score reel group with a fake 0 in the ones column, so that's
why there are four reels defined in the ten thousands, thousands,
hundreds, and tens position, with *None* as the placeholder in the
ones position.



max_simultaneous_coils:
~~~~~~~~~~~~~~~~~~~~~~~

This is the maximum number of coils you want to fire at the same time
in the score reel group. This is needed because most machines don't
have enough power to fire too many coils at once. This usually comes
into play when the score reel group is resetting itself to zero. The
default value is 2 which should work fine in most situations and is a
fairly accurate representation of how classic EM games operated. You
can experiment with different values to see how well your specific
machine can handle them.



chimes:
~~~~~~~

This is a list of coils that are pulsed each time a score reel
advances when its performing a scoring action. This list should have
the same number of items as your `reels:`configuration, and the
position of each chime coil corresponds to the score reel group coil
that will cause it to fire. In the example above, the line `chimes:
None, chime1, chime2, chime3, None`means there is no chime for the ten
thousands reel, *chime1*is used for the thousands, *chime2*is used for
the hundreds, *chime3*is used for the tens, and no chime is used for
the ones. Note the actual chime coil pulse times are controlled by
each coil's setting in the `Coils section of the machine configuration
file`_. (`See our note`_ for how you can enter lists into the MPF
config files for proper formatting.)



Device Control Events
---------------------

None



Settings that apply to all device types
---------------------------------------

There are some settings that apply to all types of devices that also
apply here.



tags:
~~~~~

Tags for score reel groups work like tags for other devices. You can
use them to group and address score reel groups together. Certain tags
also have special meanings.


+ player *X* - Used to tell the machine that you want to map this
  score reel group to the player "X" in the tag name. You can add
  multiple player tags to a single score reel group and then the game
  will use that group for both players. For example, if you have a
  machine with two score reel groups but you want to have 4 player
  games, you can give one group the tags `player1, player3`and the other
  `player2, player4`, and the game will automatically reset each reel
  group to each player's score when it becomes their turn.




label:
~~~~~~

The plain-English name for this device that will show up in operator
menus and trouble reports.



debug:
~~~~~~

Set this to *true* to add lots of logging information about this shot
to the debug log. This is helpful when you’re trying to troubleshoot
problems with this shot. Default is *False*.

.. _Score Reel Groups device section: https://missionpinball.com/docs/mpf-core-architecture/mechs/logical-mechs/score-reel-group/
.. _score reels (based on the names you gave them): https://missionpinball.com/docs/configuration-file-reference/score-reels/
.. _See our note: /docs/configuration-file-reference/adding-lists-and-lists-of-lists-to-config-files/
.. _Coils section of the machine configuration file: /docs/configuration-file-reference/coils/


