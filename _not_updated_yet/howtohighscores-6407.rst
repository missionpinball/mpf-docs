
This How To guide explains how to setup a high score mode in MPF. The
MPF package contains a the code for a high score mode, so all you have
to do to use add some configs to your machine's *modes* folder and
you're all set. Features of the high score mode include:


+ Set any player variable as a high score option. So in addition to
  score you could set high score entries for loops, ramps, aliens
  destroyed, etc.
+ Set how many of each high score type are tracked (Top 5 for high
  scores, Top 3 for loops, Top 1 for aliens, etc.)
+ Set what each “award name” is called. (The highest score is “GRAND
  CHAMPION,” the second highest score is “HIGH SCORE 1”, the highest
  loop score is “MAJOR LOOPER”, etc.)
+ How many characters a player can enter for their name.
+ A list of valid characters the player can choose from
+ The layout of the display for entering their names and show their
  rewards. (This is done with regular events you can use with the
  slide_player, and two new display elements have been created—a
  character picker and a text field that shows the characters entered.)
  You can set up slides like any slide in MPF.
+ BCP events for high score awards and entry, so you can configure
  high score entry screens for the built-in MPF media controller or the
  Unity backbox controller.


Here are a few examples of the high score mode in action. These
examples are with a traditional single-color DMD, but they're
generated with standard events and display elements, so you can make a
color DMD, a high-def LCD display, etc. ` `_` `_ Now lets dig in to
actually getting this setup:



(A) Create your high_score mode folder
--------------------------------------

The high score mode works like any other mode in MPF. You'll create a
folder called *high_score* in your machine's *modes* folder, and that
folder will contain subfolders config files, images, etc. So to begin,
create a folder called *<your_machine>/modes/high_score*. Then inside
there, create another folder called *config*. Then inside there,
create a file called *high_score.yaml*. (So that file should be at
*<your_machine>/modes/high_score/config/high_score.yaml*.) Your folder
structure should look something like this:



(B) Decide what things you want to track high scores from
---------------------------------------------------------

MPF uses the concept of *player variables* (`more info here`_) to keep
track of various things on a per-player basis. The most obvious
example of this is the score. Each player has a *score* variable since
obviously you need to track the score separately for each player.
There are also player variables for things like the player number,
current ball number, how many extra balls the player has, etc. As you
build-out your game config, you can leverage player variables to track
anything you want on a per-player basis. You can access and update
player variables via logic blocks, the scoring settings, or directly
via custom code you write. The concept of player variables is tightly-
coupled with MPF's high score mode. When you decide how high scores
will work in your machine, what you're actually doing is mapping
player variable names to high score categories and names. So the first
thing you need to decide is what player variables you want to track as
high score achievements. For example, you probably want to track the
score variable and maybe keep the top 5 highest scores in your list.
You might also track loops for a "loops champion". You could set it so
that every time a loop shot was created, a player variable called
loops was incremented by one, and then you could use the high score
system to track whichever player had the most loops in a game. Again,
you can base your high scores on any player variable you want, and you
can track as many entries for each as you want. So the first step to
implementing high scores is to decide what you want to track.



(C) Add settings to your high_score.yaml config file
----------------------------------------------------

Once you decide what you want to track, the next step is to actually
build-out the config file for it. Open up the high score mode's config
file that you just copied into your machine folder. It should be at
*<your_machine>/modes/high_score/config/high_score.yaml*. Since this
file is totally blank, add the required ` *#config_version=3*`_ to the
top line. Next, add a section called *high_score:*, and then under
there, indent a few spaces (it doesn't matter how many, 2 or 4 or
whatever you prefer) and add a section called *categories:*. Your
*high_score.yaml* file should now look like this:


::

    
    #config_version=3
    
    high_score:
      categories:


Now you need to add sub-entries in the categories section for each
player variable you'd like to track high scores for, and then under
those, the names (or "labels") you want to use to refer to each
position. If you want to track the player variable called *score*
(which is the score, so that makes sense), add a score: section, and
then under there create an entry for what you want to call each score
position. For example:


::

    
      categories:
      - score:
        - GRAND CHAMPION
        - HIGH SCORE 1
        - HIGH SCORE 2
        - HIGH SCORE 3
        - HIGH SCORE 4


The sub entry labels correspond to the ranking order of them, so the
player with the highest *score* player variable will get an award
named *GRAND CHAMPION*, the second-highest *score* player variable
will be assigned *HIGH SCORE 1*, and so on. Feel free to call these
whatever you want or to add as many or as few as you want. The number
of entries in the list is how many of each of the top values will be
saved. This is also where you configure the high score system to track
the highest results of other player variables. For example, if you
want to track the player variable called loops with a single award
called *LOOP CHAMP*, you'd enter that here too, like this:


::

    
    #config_version=3
    
    high_score:
      categories:
      - score:
        - GRAND CHAMPION
        - HIGH SCORE 1
        - HIGH SCORE 2
        - HIGH SCORE 3
        - HIGH SCORE 4
      - loops:
        - LOOP CHAMP


Notice that all of these have dashes in front of them (with a space
between the dash and the word). This is a YAML formatting thing which
tells the YAML processor that these items are in a list that should be
processed in order. (Not only does the order of the individual
placement labels correspond to the name of the position on the list,
but the order of the player variables in the categories list
corresponds to the order they'll be processed when your high score
mode is running and collecting the players' names or initials.) The
keys to remember are:


+ The name of the section in the categories entry corresponds to a
  player variable of the same name.
+ The sub-entries under a player variable are the labels for each
  slot.
+ The order of the sub-entries correspond to the order the labels will
  be applied to each position.
+ The number of sub-entries you have controls how many positions will
  be saved for each category.


Note that at this point, you are not configuring settings like how
many characters a player can enter, how many of these entries are
shown in your attract mode, or whether the player wins free credits
for an entry. All you're doing now is deciding what player variables
you'll track, how many positions of each variable you'll track, and
what those positions are called.



(D) Add the high score mode to your list of modes
-------------------------------------------------

Now that you have some basic high score settings configured, you can
add the high score mode to the list of modes that are used in your
machine. To do this, add `- high_score` to the *modes:* section in
your machine-wide config, like this:


::

    
    modes:
      - base
      - some_existing_mode
      - another_mode_you_might_have
      - tilt
      - bonus
      - high_score


The order doesn't matter here since the priority each mode runs at is
configured in its own mode configuration file. All you're doing now is
configuring the high score mode as a mode that your machine will use.
You might be wondering why your new *high_score.yaml* mode
configuration file doesn't have a *mode:* section? That's because the
*high_score* mode is built-in to MPF (in the *mpf/modes/high_score*)
folder, so when you add a *high_score* folder to your own machine's
modes folder, MPF merges together the settings from the MPF modes
folder and your modes folder. (It loads the MPF mode config first with
baseline settings, and then it merges in your machine's mode config
which can override them.) If you look at the built-in *high_score*
mode's config (at *mpf/modes/high_score/config/high_score.yaml*),
you'll see it has the following *mode:* section:


::

    
    mode:
      code: high_score.HighScore
      priority: 500
      start_events: game_ending, start_high_score
      use_wait_queue: true


So those are the base settings for the *high_score* mode which will be
applied unless you override them in your own machine's *high_score*
config file. Notice that this configuration has the high score mode
configured to automatically start when the *game_ending* event is
posted. When the high score mode starts, it will look at all the
values of the player variables for the high score categories you
configured and compare them to the existing high scores. If any
players from the current game have achieved a high score in any
category, the high score mode will kick off events to collect the
player's initials and display the high score screens. If no players in
that game have achieved a high score, the high score mode will stop
and the game ending process will continue. In other words, the high
score mode always starts whenever a game ends, but if no player has
achieved a high score, then the high score mode stops again. This
whole process only takes a few milliseconds.



(E) Configure your display slides to allow high score entry
-----------------------------------------------------------

After your high score mode is added, you need to add a *slide_player:*
entry in your high score config file so that it displays the high
score slides in the format that you like. If you have a 128x32 DMD-
based game, you can probably use the sample configuration pretty much
as it is. If you're using an HD display or an LCD window, you can
still use the default config as a starting point, but you'll most like
want to tweak some things. We'll go through the *slide_player:*
sections one-by-one here. There's a complete *high_score.yaml* file at
the end of this How To guide which you can copy to use as your
starting point.



Understanding the high score slides
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When the high score mode detects that a player has achieved a high
score, it will post an event called *high_score*. (If the player has
achieved multiple awards, or multiple players have achieved awards,
these will be sent one-by-one. More on that in a bit.) This high_score
event will have several parameters, including:


+ * award * - The name (label) of the award that the player got, like
  GRAND CHAMPION or ALIEN KING or whatever you have configured in the
  *categories:* section of your *high_score:* config.
+ * player_num * - The number of the player who earned that award.
+ * value * - The value of player variable for the award. (e.g. their
  score or the number of aliens they got or the total loops or whatever)


At the most basic level, you can add the *high_score* event to your
*slide_player:* configuration which means you can use the parameters
it passed to build the display slide the player will use to enter
their initials. This is no different than any other slide which shows
dynamic data (like your score display). The "magic" in the high score
slide is that you'll use two interactive types of display elements:
the *character_picker* element and the *entered_chars* element.
(Remember that `display elements`_ are the "things" you put on a
slide, like *text*, *image*, *animation*, etc. *Character_picker* and
*entered_chars* are just two more types of display elements that you
can add to any slide, and in this case you'll use them for the high
score.) Here's how the template *high_score* slide is built: ` `_
There are four display elements on this slide (and in the high_score
slide from the template you're basing your mode on), so let's look at
each of these one-by-one:



The player number text element
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The first display element on the slide is just a regular `text
element`_ like any other text element. It uses the *player_num* event
parameter to dynamically show the player number for the player who's
entering their name. You can set the size, position, font, decorators,
and anything else you want just like any other text display element.
Here's what the template includes. This is the red section in the
image above. Feel free to change it as you wish.


::

    
    - type: text
      text: PLAYER %player_num%
      font: medium
      v_pos: bottom
      h_pos: center
      x: -27
      y: -21




The award name text element
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The award name (the green box in the image above) is also just a
regular text display element that basis its text on the award
parameter passed along with the *high_score* event:


::

    
    - type: text
      text: "%award%"
      font: small
      v_pos: bottom
      h_pos: center
      x: -27
      y: -12




The character picker element
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The *character picker* display element (the blue box in the image) is
what shows the list of characters the player can chose from to enter
their name or initials. It also has settings for the spacing, the list
of characters, and related settings. Here's what the template
configuration contains. See the documentation for the `character
picker display element`_ for details on what all these settings do.


::

    
    - type: character_picker
      name: high_score
      slide_name: high_score
      clear_slide: true
      persist: no
      height: 9
      font: medium
      v_pos: bottom
      selected_char_color: 0
      selected_char_bg: 15
      char_x_offset: 1
      char_y_offset: 1
      char_width: 7
      char_list: "ABCDEFGHIJKLMNOPQRSTUVWXYZ_- "
      back_char: back_arrow_7x7
      end_char: end_11x7
      back_char_selected: back_arrow_7x7_selected
      end_char_selected: end_11x7_selected
      image_padding: 1
      shift_left_tag: left_flipper
      shift_right_tag: right_flipper
      select_tag: start
      max_chars: 3
      timeout: 30s
      return_param: award




The entered chars element
~~~~~~~~~~~~~~~~~~~~~~~~~

The *entered chars* (short for "entered characters) display element
(the purplish-pink box in the image above) is used to show the
characters that the player has selected so far. It also includes a
flashing cursor character showing the current spot they're picking a
character for. Like the other display elements, you can make this
whatever font you want, and set its size and position like any display
element. Note that in the config snippet below, the *h_pos:* is *left*
(even though the element itself is towards the right side of the
display). That's so that the text in the element is left-justified, so
we position the display element *left* and then use the *x:* setting
to move the element where we want it (at the 90th pixel from the left
edge of the display). The only other important thing about the entered
chars display element is that it has a setting for *character_picker*
which is where you specify the name of the character picker display
element which is the "source" for the entered chars. So notice that
`character_picker: high_score` matches `name: high_score` from the
*character_picker* settings above. See the documentation on the `
*entered chars* display element`_ for full details.


::

    
    - type: entered_chars
      character_picker: high_score
      cursor_char: _
      v_pos: bottom
      h_pos: left
      x: 90
      y: -12
      cursor_offset_x: 0
      cursor_offset_y: 0
      cursor_decorators:
        type: blink




(F) Configure your high score award slide
-----------------------------------------

Once the player enters their name or initials, MPF will then post two
events you can use for the high score award display slide. The high
score award display is the slide that is shown for a few seconds after
the player enters their initials. For example: " *GRAND CHAMPION:
BRI*" (or whatever you want). Two events are posted. One is always
called *high_score_award_display*, and the other is dynamically
created based on the award name itself in the form
*<award_name>_award_display* (e.g. *grand champion_award_display*).
The reason there are two is in case you want to have custom award
display slides for each kind of award. Otherwise you can just create a
single award display slide based on the generic
*high_score_award_display* event. Both of these events have the same
parameters which you can use in your award slide:


+ * player_name * - The name (or initials) the player just entered in
  the high score entry screen.
+ * award * - The name (label) of the award that the player got, like
  GRAND CHAMPION or ALIEN KING or whatever you have configured in the
  categories section of your high_score config.
+ * value * - The value of player variable for the award. (e.g. their
  score or the number of aliens they got or the total loops or whatever)


The high score mode template config file contains a single entry in
the slide_player for award slides:


::

    
    high_score_award_display:
      - type: text
        text: "%player_name%"
        color: 0
        bg_color: 15
        v_pos: center
        y: 2
        decorators:
          type: blink
          on_secs: .05
          off_secs: .05
      - type: text
        text: "%award%"
        font: medium
        v_pos: top
        y: 2


This slide will show the award in the top row with the player's name
under it. You can customize this however you want. Note that the time
this slide is shown is controlled in the *high_score:* settings, via
the *award_slide_display_time:* setting. The template mode sets this
to 4 seconds. This is a setting of the high score mode, rather than a
slide expiration setting, because the high score mode needs to know
how long to delay itself before moving on to the next award entry or
finishing the game ending process.



(G) Add tags to your switches
-----------------------------

The high score mode requires three switches to be configured. One is
to move the cursor to the left, another to move the cursor to the
right, and a third to select the highlighted character. MPF uses
switch tags for this. By default, it's configured to look for tags
called *left_flipper*, *right_flipper*, and *start*. Chances are you
already have these switches tagged with these names, but if not, go
into your machine-wide config (not your high_score config) and into
the *switches:* section and add those tags, like this:


::

    
    switches:
        s_flipper_lower_right:
            number: sf2
            tags: right_flipper
        s_flipper_lower_left:
            number: sf4
            tags: left_flipper
        s_start:
            number: s13
            tags: start




(H) Copy or create images for the 'back' and 'end' characters
-------------------------------------------------------------

Notice in the character_picker display element that there are four
image files referenced:


::

    
      back_char: back_arrow_7x7
      end_char: end_11x7
      back_char_selected: back_arrow_7x7_selected
      end_char_selected: end_11x7_selected


The full descriptions of these are in the character_picker config file
reference, but the quick overview is these are the images used for the
"back" and "end" characters in both their selected and unselected
states. (Since the character picker uses font characters, most fonts
don't have appropriate entries for back and end, so you have to draw
your own.) If you're using a DMD, then you can copy the images folder
from the built-in *high_score* mode folder into your own *high_score*
mode folder. Source folder to copy: `mpf/modes/high_score/images`
Where to put it: `<your_machine>/modes/high_score/images` If you have
an HD display or your using some other font, then you can create these
four images on your own, add them to your *high_score/images* folder,
and then add the names of the files to your character_picker
configuration.



(I) Check out this complete config file
---------------------------------------

Here's a complete *high_score.yaml* config file. This is what's used
in the demo_man sample game.


::

    
    #config_version=3
    
    high_score:
      categories:
      - score:
          - GRAND CHAMPION
          - HIGH SCORE 1
          - HIGH SCORE 2
          - HIGH SCORE 3
          - HIGH SCORE 4
    
    slide_player:
      high_score:
        - type: text
          text: PLAYER %player_num%
          font: medium
          v_pos: bottom
          h_pos: center
          x: -27
          y: -21
        - type: text
          text: "%award%"
          font: small
          v_pos: bottom
          h_pos: center
          x: -27
          y: -12
        - type: character_picker
          #width: 50
          name: high_score
          slide_name: high_score
          clear_slide: true
          persist: no
          height: 9
          font: medium
          v_pos: bottom
          selected_char_color: 0
          selected_char_bg: 15
          char_x_offset: 1
          char_y_offset: 1
          char_width: 7
          char_list: "ABCDEFGHIJKLMNOPQRSTUVWXYZ_- "
          back_char: back_arrow_7x7
          end_char: end_11x7
          back_char_selected: back_arrow_7x7_selected
          end_char_selected: end_11x7_selected
          image_padding: 1
          shift_left_tag: left_flipper
          shift_right_tag: right_flipper
          select_tag: start
          max_chars: 3
          timeout: 30s
          return_param: award
        - type: entered_chars
          character_picker: high_score
          cursor_char: _
          v_pos: bottom
          h_pos: left
          x: 90
          y: -12
          cursor_offset_x: 0
          cursor_offset_y: 0
          cursor_decorators:
            type: blink
    
      high_score_award_display:
        - type: text
          text: "%player_name%"
          color: 0
          bg_color: 15
          v_pos: center
          y: 2
          decorators:
            type: blink
            on_secs: .05
            off_secs: .05
        - type: text
          text: "%award%"
          font: medium
          v_pos: top
          y: 2


Note that there are additional settings you can configure in the
*high_score:* section of your config. Refer to the ` *high_score:*
page`_ in the config file reference for details.



(J) Add high scores to your attract mode display show
-----------------------------------------------------

The final thing you'll probably want to do if you're adding high
scores to your machine is to configure your attract mode display show
to include the various high scores. (Creating an attract mode display
show is `one of the steps`_ in the getting started tutorial.) Creating
slides for your attract mode slide show with high scores is pretty
straightforward. High scores are saved as machine variables, so you
access them via text display elements showing machine variables just
like any machine variable. (The how to guide which shows you `how to
add the scores from the last-played game`_ has more details on this.)
The exact names of the machine variables you'll use are dynamically
created based on the player variable of the award as well as position
in the list. They have the format like this:


+ *<player_variable_name><position_in_list>_name*
+ *<player_variable_name><position_in_list>_value*
+ *<player_variable_name><position_in_list>_label*


For example, for the high score based on the player variable "score",
if the highest score in the machine is "BRI" with a value of 7050550,
then the machine variables will be *score1_name* = `BRI`,
*score1_value* = `7050550`, and *score1_label* = `GRAND CHAMPION`. The
second-highest "score" will be *score2_name*, *score2_value*, with
*score2_label* = `HIGH SCORE 1`. If you also tracked a high score
entry for "ramps" then the highest scoring "ramps" will be
*ramps1_name* and *ramps1_value*, etc. Since these machine variables
are just accessed in a slide like any regular display element, you can
set the font, size, position, number grouping, etc. like any `text
display element`_. Here are some examples from the *demo_man* sample
game you can use as a starting point for your own machine: ` `_ The
entry for this slide in the attract mode YAML file looks like this:


::

    
    - tocks: 2
      display:
        - type: text
          text: "%machine|score1_label%"
          v_pos: top
          y: 4
        - type: text
          text: "%machine|score1_name% %machine|score1_value%"
          v_pos: bottom
          number_grouping: true
          y: -3
        - type: shape
          shape: box
          width: 128
          height: 32
        - type: shape
          shape: box
          width: 126
          height: 30
          shade: 8


Note that the value of the score is *7050550*, so in order for it to
include commas, we add *number_grouping: true*. (Again, just like any
other text display element.) Here's an example showing high scores 1
and 2: ` `_ And the related entry for the show YAML file:


::

    
    - tocks: 2
      display:
        - type: text
          text: "1. %machine|score2_name% %machine|score2_value%"
          v_pos: top
          h_pos: left
          number_grouping: true
          y: 3
          x: 12
        - type: text
          text: "2. %machine|score3_name% %machine|score3_value%"
          v_pos: bottom
          h_pos: left
          number_grouping: true
          y: -3
          x: 10
          transition:
            type: move_out
            duration: 1s
            direction: top


Notice in this case that we don't use the *score3_label* machine
variable. That's because the label value is *HIGH SCORE 1*, but in
this case that would be too long for the slide. We don't want the
slide to show *HIGH SCORE 1: BRI 93,060*, rather, we want it to show
*1. BRI 93,060*. So we just manually enter the "1. " in the text field
and use the machine variables to dynamically provide the content for
the player's name and their score. Of course you can add any high
score result to your attract mode. Here's an example slide showing the
loops champion: ` `_ And here's the config you'd add for that in your
attract mode display show:


::

    
    - tocks: 2
      display:
       - type: text
         text: MASTER LOOPER
         v_pos: top
         font: medium
       - type: text
         text: "%machine|loops1_name%"
         font: tall title
       - type: text
         text: "%machine|loops1_value% LOOPS"
         v_pos: bottom
         font: medium
         number_grouping: true
         transition:
           type: move_in
           duration: 1s
           direction: bottom


.. _text display element: https://missionpinball.com/docs/mpf-core-architecture/displays-dmd/display-elements/text/
.. _display elements: https://missionpinball.com/docs/mpf-core-architecture/displays-dmd/display-elements/
.. _character picker display element: https://missionpinball.com/docs/mpf-core-architecture/displays-dmd/display-elements/character-picker/
.. _#config_version=3: https://missionpinball.com/docs/configuration-file-reference/important-config-file-concepts/config_version/
.. _how to add the scores from the last-played game: https://missionpinball.com/docs/howto/show-scores-in-the-attract-dmd-mode/
.. _one of the steps: https://missionpinball.com/docs/tutorial/attract-mode-display-show/
.. _ page: https://missionpinball.com/docs/configuration-file-reference/high_score/
.. _ display element: https://missionpinball.com/docs/mpf-core-architecture/displays-dmd/display-elements/entered-chars/
.. _more info here: https://missionpinball.com/docs/mpf-core-architecture/player-management/


