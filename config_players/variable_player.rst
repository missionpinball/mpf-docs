Variable player
===============

The *variable player* is a :doc:`config player </config_players/index>` that's used to set the value of player
and machine variables. This is commonly used for scoring in your machine.
See :doc:`variable_player </config/variable_player>`
for more detailed information.

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

See our :doc:`player variables reference </player_vars/index>` and
:doc:`machine variables reference </machine_vars/index>`
to learn about existing variables.
You can also create player variables on the fly if they did not exist.
If you want to define defaults for variables you may define them in the
:doc:`/config/player_vars` or :doc:`/config/machine_vars` sections.

Usage in config files
---------------------

In config files, the variable player is used via the ``variable_player:`` section.

Usage in shows
--------------

In shows, the variable player is used via the ``variables:`` section of a step.

Config Options
--------------

See :doc:`/config/variable_player` for config details.
