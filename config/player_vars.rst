player_vars:
============

*Config file section*


+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+


The ``player_vars:`` section of your machine-wide config file lets you
specify the initial state of player variables that are set for a player
when the game starts.

Example:

.. literalinclude:: /example_configs/player_vars/config/player_vars.yaml
   :language: yaml

Settings
--------

Each subsection in the ``player_vars:`` section is the name of a player
variable to set. Then there are two sub-settings under there:

initial_value: (required)
~~~~~~~~~~~~~~~~~~~~~~~~~

The initial value of this player variable that you're setting. This
is set when the player is created.

value_type:
~~~~~~~~~~~

Select one of the options from this list: ``int`` (integer), ``float``, or
``str`` (string). The default is "int", and there is no intelligence to
try to detect which type of value you have, so if you have a floating
point number or a string, you also need to set the value_type.



