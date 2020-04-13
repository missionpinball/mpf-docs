variable_player:
================

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **NO**  |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

.. overview

The ``variable_player:`` section of your mode config lets you add, subtract, or replace player
variables based on events that are posted.

At the most basic level, you can use this to add to a player's score (which is technically
adding value to the player variable called *score*), but in reality you can affect any
player or machine variable.

Here's an example:

.. code-block:: mpf-config

   ##! mode: mode1
   variable_player:
     target_1_hit:
       score: 1000     # adds 1000 to the player's "score" variable
     ramp_1_hit:
       score: 10000    # adds 10,000 to the player's "score" variable
       ramps: 1        # adds 1 to the player's "ramps" variable
     ramp_1_timeout:
       ramps:
         int: 0          # sets the player's "ramps" variable to 0.
         action: set     # means that this event will "set" (or reset) the variable to the value, rather than add to it
     ramp_2_hit:
       score:
         int: 25000 * current_player.ramps     # multiplies the value of the current player's "ramps" variable by 25,000 and adds the result to the player's "score" variable
         block: true      # "blocks" this event from being passed to variable player sections from lower-priority modes
     counter_treasure_value_complete:
       treasure_name:
         string: RUBY     # Sets the player's "treasure_name" variable to a string called "RUBY"

See :doc:`/config_players/variable_player` for details.

Settings
--------

Like many sections of MPF configs, the ``variable_player:`` section format is generically setup like this:

.. code-block:: yaml

   variable_player:
      some_event:
         <settings>
      some_other_event:
         <settings>
      another_event:
         <settings>

The following settings can be used with each event section listed in your variable_player section:

Example
~~~~~~~

You can include any player variable under an event to add numeric value to that variable. (If the variable doesn't
exist, it will set the player variable to that.) For example:

.. code-block:: mpf-config

   ##! mode: mode1
   variable_player:
     some_event:
       score: 1000
       aliens: 1
       bonus: 10

The above config will add 1000 to the "score" player variable, 1 to the "aliens" player variable, and 20 to the "bonus"
player variable when the event called *some_event* is posted. Note that you don't even need to include a "score" if you
just want to add to other player vars.

Note that you can use a :doc:`dynamic value </config/instructions/dynamic_values>` for this setting too, which means
you can pull in values from other player variables, device states, etc. and do math on them.

.. config


Optional settings
-----------------

The following sections are optional in the ``variable_player:`` section of your config. (If you don't include them, the default will be used).

action:
~~~~~~~
Single value, type: one of the following options: add, set, add_machine, set_machine. Default: ``add``

By default, the variable player entries will be added to the existing value of a player variable. If you want to replace
or reset the value of the player var, you can add ``action: set`` to the entry. However to do this, you have to
indent that setting under the player var name, and then specify the value in the "int:" section. For example, if you
want the example from the above section to reset the aliens player variable to 1 instead of adding 1 to the current
value, it would look like this:

.. code-block:: mpf-config

   ##! mode: mode1
   variable_player:
     some_event:
       score: 1000
       aliens:           # the player var you want to reset
         int: 1          # the integer value you're resetting this player var to
         action: set     # means you're resetting it, rather than adding to it
       bonus: 10

Starting in MPF 0.33, you can also add and set machine variables, by specifying ``action: add_machine`` or
``action: set_machine``. In these cases the machine variable is specified just like the player variable in the "set" example above.

block:
~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

This is useful if you have a shot in a base mode that scores 500 points, but then in some timed mode you want that shot
to be 5,000 points but you don't also want the base mode to score the 500 points on top of the 5,000 from the higher
mode.

Note that when you use block, you also have to include the ``int:``, ``float:``, or ``string:`` setting indented. For example:

.. code-block:: mpf-config

   ##! mode: mode1
   variable_player:
     ramp_1_hit:
       score:
         int: 5000
         block: true

There is also a shorthand way:

.. code-block:: mpf-config

   ##! mode: mode1
   variable_player:
     ramp_1_hit:
       score: 5000|block

float:
~~~~~~
Single value, type: ``number`` or ``template`` (will be converted to floating point; :doc:`Instructions for entering templates </config/instructions/dynamic_values>`). Defaults to empty.

Adds or sets a player or machine variable to the specified float value.  The ``int:`` setting takes priority over the ``float:``
setting so if both are present only the ``int:`` will be used.
You can use :doc:`placeholders </config/instructions/dynamic_values>` which evalute to float as well.

int:
~~~~
Single value, type: ``integer`` or ``template`` (:doc:`Instructions for entering templates </config/instructions/dynamic_values>`). Defaults to empty.

Adds or sets a player or machine variable to the specified integer value (this is the most common use of the variable_player).
The ``int:`` setting takes priority over the ``float:`` setting so if both are present only the ``int:`` will be used.
You can use :doc:`placeholders </config/instructions/dynamic_values>` which evalute to int as well.

player:
~~~~~~~
Single value, type: ``integer``. Defaults to empty.

.. code-block:: mpf-config

   ##! mode: mode1
   variable_player:
     add_score_to_player_2:
       score:
         int: 1000
         player: 2
   ##! test
   #! start_two_player_game
   #! start_mode mode1
   #! assert_player_variable 0 score
   #! post add_score_to_player_2
   #! assert_player_variable 0 score
   #! drain_all_balls
   #! assert_player_variable 1000 score

If the ``player:`` setting is not used, then this variable_player entry will default to the current player.

string:
~~~~~~~
Single value, type: ``string``. Defaults to empty.

Here's an example from *Brooks 'n Dunn* where there is a player variable (set via a counter) which tracks the
player's current album value. We use the variable_player section tied to the events posted when the player variable changes
and conditional events to set the current name of the album value, like this:

.. code-block:: mpf-config

   ##! mode: mode1
   variable_player:
     player_album_value{value==1}:
       album_name:
         string: SILVER
     player_album_value{value==2}:
       album_name:
         string: GOLD
     player_album_value{value==3}:
       album_name:
         string: PLATINUM
     player_album_value{value==4}:
       album_name:
         string: DOUBLE PLATINUM
     player_album_value{value==5}:
       album_name:
         string: QUINTUPLE PLATINUM
     player_album_value{value>5}:
       album_name:
         string: OFF THE CHARTS!

The above config lets us always have a player var called "album_name" we can use in slides and widgets which matches
the value of the album, and it's automatically updated whenever the player var "album_value" changes.


Related How To guides
---------------------

* :doc:`/config_players/variable_player`
* :doc:`/game_logic/scoring/index`
* :doc:`/tutorial/15_scoring`
* :doc:`/game_logic/logic_blocks/persisting_state_in_a_player_variable`
