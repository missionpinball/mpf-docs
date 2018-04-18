variable_player:
================

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **NO**  |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

The ``variable_player:`` section of your mode config lets you add, subtract, or replace player
variables based on events that are posted.

At the most basic level, you can use this to add to a player's score (which is technically
adding value to the player variable called *score*), but in reality you can affect any
player or machine variable.

Here's an example:

.. code-block:: mpf-config

   ##! config: mode1
   player_variable:
      target_1_hit:
         score: 1000   # adds 1000 to the player's "score" variable
      ramp_1_hit:
         score: 10000  # adds 10,000 to the player's "score" variable
         ramps: 1      # adds 1 to the player's "ramps" variable
      ramp_1_timeout:
         ramps:
           int: 0        # sets the player's "ramps" variable to 0.
           action: set   # means that this event will "set" (or reset) the variable to the value, rather than add to it
      ramp_2_hit:
         score:
            int: 25000 * current_player.ramps  # multiplies the value of the current player's "ramps" variable by 25,000 and adds the result to the player's "score" variable
            block: true   # "blocks" this event from being passed to variable player sections from lower-priority modes
      counter_treasure_value_complete:
         treasure_name:
            string: RUBY  # Sets the player's "treasure_name" variable to a string called "RUBY"

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

<any_player_variable>:
~~~~~~~~~~~~~~~~~~~~~~

You can include any player variable under an event to add numeric value to that variable. (If the variable doesn't
exist, it will set the player variable to that.) For example:

.. code-block:: yaml

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

action:
~~~~~~~

One of the following settings: ``add``, ``set``, ``add_machine``, ``set_machine``. Default is ``add``.

By default, the variable player entries will be added to the existing value of a player variable. If you want to replace
or reset the value of the player var, you can add ``action: set`` to the entry. However to do this, you have to
indent that setting under the player var name, and then specify the value in the "int:" section. For example, if you
want the example from the above section to reset the aliens player variable to 1 instead of adding 1 to the current
value, it would look like this:

.. code-block:: yaml

   variable_player:
      some_event:
         score: 1000
         aliens:         # the player var you want to reset
            int: 1       # the integer value you're resetting this player var to
            action: set  # means you're resetting it, rather than adding to it
         bonus: 10

Starting in MPF 0.33, you can also add and set machine variables, by specifying ``action: add_machine`` or
``action: set_machine``. In these cases the machine variable is specified just like the player variable in the "set" example above.

block:
~~~~~~

Adding ``block: True`` to a variable_player entry means that MPF will "block" this scoring entry from being sent down to
variable_player entries in lower priority modes.

This is useful if you have a shot in a base mode that scores 500 points, but then in some timed mode you want that shot
to be 5,000 points but you don't also want the base mode to score the 500 points on top of the 5,000 from the higher
mode.

Note that when you use block, you also have to include the ``int:``, ``float:``, or ``string:`` setting indented. For example:

.. code-block:: yaml

  variable_player:
    ramp_1_hit:
      score:
        int: 5000
        block: true

There is also a shorthand way:

.. code-block:: yaml

  variable_player:
    ramp_1_hit:
      score: 5000|block

int:
~~~~

Adds or sets a player or machine variable to the specified integer value (this is the most common use of the variable_player).
The ``int:`` setting takes priority over the ``float:`` setting so if both are present only the ``int:`` will be used.

float:
~~~~~~

Adds or sets a player or machine variable to the specified float value.  The ``int:`` setting takes priority over the ``float:``
setting so if both are present only the ``int:`` will be used.

string:
~~~~~~~

Lets you set a player or machine variable to a string value (text characters) rather than adding numeric value. This is useful
for when you want to make slides that show some value and you need to "translate" some numeric value to words.

Here's an example from *Brooks 'n Dunn* where there is a player variable (set via a counter) which tracks the
player's current album value. We ue the variable_player section tied to the events posted when the player variable changes
and conditional events to set the current name of the album value, like this:

.. code-block:: yaml

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

player:
~~~~~~~

Lets you specify which player (by number) this variable_player entry will affect. (Player 1 is would be ``player: 1`` etc. This lets you
effect the score or other player variables of players other than the current player.

If the ``player:`` setting is not used, then this variable_player entry will default to the current player.
