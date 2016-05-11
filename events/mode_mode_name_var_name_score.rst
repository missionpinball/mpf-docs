mode_(mode_name)_(var_name)_score
=================================

*MPF Event*

A scoring event was just processed to add (or remove) value
from a player variable. (Remember that scoring events can affect
the value of *any* player variable, not just the *score* player
variable.

For example, if a scoring event in the "base" mode added to the
player variable called *ramps*, the event posted would be
*mode_base_ramps_score*.


Keyword arguments
-----------------

change
~~~~~~
The numeric value of the change. (*value* minus
*prev_value*).

prev_value
~~~~~~~~~~
The previous value of this player variable before the
new *value* was added.

value
~~~~~
The new value of the player variable.

