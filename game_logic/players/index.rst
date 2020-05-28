Player Variables
================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/player_vars`                                                   |
+------------------------------------------------------------------------------+

MPF contains lots of features which make working with players easy including
variables.  If you are not a programmer, variables are just locations inside
the computer's memory to store bits of information like numbers and text
(aka strings).  Programmers create variables to store and retrieve these bit
of information for use in their programs. For example, You may want to create
a player variable to store the number of times a bumper has been hit to award
a bumper bonus.

Each player has "player variables" which are key/value pairs that are stored
separately for each player.

Some simple examples of player variables include things like:

* ``number``: The player's number (1, 2, etc.)
* ``score``: The player's current score

There are two types of player variables that you can use; the default player
variables provided by MPF and custom variables that you can create, update and reference.

========================
Default Player Variables
========================

There's a :doc:`/player_vars/index` which lists the default player variables
that MPF creates and uses.

MPF also uses player variables to keep track of all the built-in game logic
elements that are tracked on a per-player basis, including achievement status,
logic block states, extra balls, bonus, etc.

========================
Custom Player Variables
========================

You can also create your own custom player variables which can be called anything you want
and can store anything you want. You can use them to track player's progress
through the game, how many loops they've made, how many pop bumper hits they
have, etc. See the :doc:`/config/player_vars` documentation for details and
examples.

----------
Data types
----------

If you are a programmer, you likely know what datatypes are.  If you are not a
programmer but want to create your own player variables, you'll need to know
a little bit about datatypes.  To make this really simple, you may want to store
the name of the current mode so that you can display the mode name on the display.
Since the name of the mode is a piece of text, you'll need to create a player variable
of type "str" to denote a string of characters.  Here are the data types available in MPF.

+------------+-----------------------------+
| Datatype   | Description                 |
+============+=============================+
| str        | a string of textual         |
|            | characters                  |
+------------+-----------------------------+
| int        | an integer, a basic number  |
|            | with no decimal point       |
+------------+-----------------------------+
| float      | floating point, a more      |
|            | precise number with         |
|            | decimal point               |
+------------+-----------------------------+

**Examples:**

.. code-block:: mpf-config

  player_vars:
    current_mode:
      initial_value: Trees Attack
      value_type: str
    bumper_hits:
      initial_value: 0
      value_type: int
    super_bonus_multipler:
      initial_value: 1.25
      value_type: float

Player varaibles are essentially global in MPF, meaning that you can define them
in config files and they are available to use in any location in your files.  This
makes them easy to use but also easy to introduce bugs or unintended consequences
so be aware of every place that you use them if you are getting unanticipated
results.  A best practice would be to define all of your player variables in a common
location such as the machine configuration file.

--------------------
Setting Variables
--------------------

MPF configuration files do not work with variables as easily as "real" programming languages. The primary
method of changing a variable is by configuring the change you would like to make.
In the current version of MPF, this is primarily done in the ``variable_player:`` section of your mode.

.. code-block:: mpf-config

  ##! mode: my_mode
  variable_player:
    # add 1 to bumper_hits
    bumper_1_active:
      bumper_hits: 1

The example below shows a player variable of type string being updated.  A mode carousel (mode selection by the player)
was used by the player to select a mode ladder (a set of modes played in a sequence similar to scenes in GhostBusters).
The apostrophes are not required but allowed.

.. code-block:: mpf-config

  ##! mode: my_mode
  variable_player:
    carousel_left_scoop_scene_selected:
      current_ladder:
        action: set
        string: 'Scene 1'

The example below shows a player variable being updated after a conditional event.  In this case, the base
mode has received an event indicated that a mode has been complete.  The conditional event checks to see
which mode ladder was in play and increments the custom player variable ladder_scene_1 to indicate the
progress towards completing the mode.

.. code-block:: mpf-config

  ##! mode: my_mode
  variable_player:
    mode_is_complete{current_player.current_ladder=="Scene 1"}:
      ladder_scene_1: 1

---------------------------
Displaying Custom Variables
---------------------------
Displaying your custom player variables on a slide can be confusing in the current version of MPF. The example below
shows a text widget that is displaying 3 variables on the main scoring screen of the base mode.  The first
two variables are of type "str" and the last variable is of type "int".

.. code-block:: mpf-mc-config

   player_vars:
     current_ladder:
       initial_value: "Initial Ladder"
       value_type: str
     current_mode:
       initial_value: "No Mode"
       value_type: str
     ladder_scene_1:
       initial_value: 1
       value_type: int

   ##! mode: base
   slide_player:
     mode_base_started:
       widgets:
         - type: text
           text: (current_ladder) > (current_mode) > (ladder_scene_1)
   ##! test
   #! start_game
   #! start_mode base
   #! advance_time_and_run .1
   #! assert_text_on_top_slide "Initial Ladder > No Mode > 1"




+------------------------------------------------------------------------------+
| Related How To Guides                                                        |
+==============================================================================+
| :doc:`/about/help_us_to_write_it`                                            |
+------------------------------------------------------------------------------+

+------------------------------------------------------------------------------+
| Related Events                                                               |
+==============================================================================+
| :doc:`/events/player_add_request`                                            |
+------------------------------------------------------------------------------+
| :doc:`/events/player_added`                                                  |
+------------------------------------------------------------------------------+
| :doc:`/events/player_turn_will_start`                                        |
+------------------------------------------------------------------------------+
| :doc:`/events/player_turn_starting`                                          |
+------------------------------------------------------------------------------+
| :doc:`/events/player_turn_started`                                           |
+------------------------------------------------------------------------------+
| :doc:`/events/ball_save_ball_save_saving_ball`                               |
+------------------------------------------------------------------------------+
| :doc:`/events/player_turn_will_end`                                          |
+------------------------------------------------------------------------------+
| :doc:`/events/player_turn_ending`                                            |
+------------------------------------------------------------------------------+
| :doc:`/events/player_turn_ended`                                             |
+------------------------------------------------------------------------------+
| :doc:`/events/multi_player_ball_started`                                     |
+------------------------------------------------------------------------------+
| :doc:`/events/single_player_ball_started`                                    |
+------------------------------------------------------------------------------+
