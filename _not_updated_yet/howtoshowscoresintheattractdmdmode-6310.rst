
One of the things "real" pinball machines do is show the scores from
the last game on the DMD during the attract mode. So that's what we're
going to cover in this tutorial. Also note that this tutorial is just
for showing the old scores of the last game in the attract mode. You
can also show the live scores of other players while a game is in
progress, but that's a different tutorial which we'll write soon. To
do this, you need to add "machine variables" into your attract mode
DMD show file.



(A) What are machine variables?
-------------------------------

You might already be familiar with the concept of player variables.
Player variables are variables that are stored on a per-player basis
in MPF. A complete game might have hundreds variables per player,
ranging from simple things like score and ball number, to modes
complete, shot status, logic blocks, timers, etc. Machine variables
are similar in concept to player variables, except instead of being
stored on a per-player basis, they're stored for the whole machine. So
what kinds of variables are properties of the machine? Things like the
number of credits, the high scores, and (in this case), the scores
from the last game that was played.



(B) Using machine variables in slides
-------------------------------------

You might know that you can use the `%variable_name%` format in a
`slide_show:` or `slide_player:` configuration to access player
variables from that slide. Machine variables are pretty much the same,
except you add `machine|` in front of the variable name. So if you
want a slide to display the value of a machine variable called
player1_score, then you would add an entry `text:
"%machine|player1_score%"` to your slide config. It's that simple! In
fact that's all you really need to know. Check out this slide that we
added to the *Demo Man* `attract_dmd_loop.yaml` display show: (How do
you create this attract mode DMD show? `We have a tutorial for
that!`_)


::

    
    - tocks: 3
      display:
        - type: text
          text: "%machine|player1_score%"
          number_grouping: true
          min_digits: 2
          font: small
          v_pos: top
          h_pos: right
          x: -80
          y: 1
        - type: text
          text: "%machine|player2_score%"
          number_grouping: true
          min_digits: 2
          font: small
          v_pos: top
          h_pos: right
          x: -1
          y: 1
        - type: text
          text: "%machine|player3_score%"
          number_grouping: true
          min_digits: 2
          font: small
          v_pos: bottom
          h_pos: right
          x: -80
          y: -10
        - type: text
          text: "%machine|player4_score%"
          number_grouping: true
          min_digits: 2
          font: small
          v_pos: bottom
          h_pos: right
          x: -1
          y: -10
        - type: text
          text: FREE PLAY
          font: small
          h_pos: center
          v_pos: bottom


We use the display element positioning (h_pos, v_pos, x, and y) to get
everything set how we like it. (Details on how to do that are
`here`_.) Note that we use `h_pos: right` for everything and then set
the because we want all the score to be right-aligned (even the ones
on the left where we just have a high negative y value). Here are the
results: ` `_ (Note that there are periods instead of commas. That's
because the font we're using doesn't have a comma. :( We'll find a new
font at some point, or `you can add your own`_.) One of the cool
things with the way machine variables work is that if the machine
variable doesn't exist, then MPF will not render it to the display. In
other words if the last game you played only had three players, then
you would only see three scores. Another cool thing about machine
variables is they have the option to be persisted to disk. That means
they can stick around even when MPF is turned off! (This again is
something that "real" pinball machines do. When you turn them on, they
show the scores from the last game even if the machine was off for a
week.) Not all machine variables are persisted to disk, but scores
from the last game played are. When machine variables are persisted to
disk, MPF them in a file in your machine folder:
`<your_machine_root>/data/machine_vars.yaml`. (Note that in MPF 0.21,
we moved `audits.yaml` to that folder also.) ` `_ If you take a look
at the `machine_vars.yaml` file, you'll see that it looks pretty
similar to your YAML config files:


::

    
    player1_score: !!python/object/new:mpf.system.config.CaseInsensitiveDict
      dictitems:
        value: 56473820
    player2_score: !!python/object/new:mpf.system.config.CaseInsensitiveDict
      dictitems:
        value: 34586740
    player3_score: !!python/object/new:mpf.system.config.CaseInsensitiveDict
      dictitems:
        value: 1209800
    player4_score: !!python/object/new:mpf.system.config.CaseInsensitiveDict
      dictitems:
        value: 88759490


When MPF boots, it loads the machine variables from disk into memory.
When a game starts, MPF erases all the player score entries from the
file on disk, so if your last game was a four-person game and then you
play a one-player game, the machine_vars.yaml file will only contain
the score for the first player. Then when you start a game (and when
you add a player), MPF writes the new score value (of 0) to disk. It
also updates the file on disk each time a player's turn ends.

.. _We have a tutorial for that!: https://missionpinball.com/docs/tutorial/attract-mode-display-show/
.. _you can add your own: https://missionpinball.com/docs/howto/how-to-adding-truetype-fonts/
.. _here: https://missionpinball.com/docs/mpf-core-architecture/displays-dmd/display-elements/positioning/


