player_(var_name)
=================

*MPF Event*

Posted when simpler types of player variables are added or
change value.

The actual event has (var_name) replaced with the name of the
player variable that changed. Some examples:

* player_score
* player_shot_upper_lit_hit

Lots of things are stored in player variables, so there's no way to
build a complete list of what all the options are here. Elsewhere
in the documentation, if you see something that says it's stored in
a player variable, that means you'll get this event when that
player variable is created or is changed.

Note that this event is only posted for simpler types of player
variables, including player variables that are integers, floating
point numbers, or strings. More complex player variables (lists,
dicts, etc.) do not get this event posted.

This event is posted for a single player variable changing, meaning
if multiple player variables change at the same time, multiple
events will be posted, one for each change.

Keyword arguments
-----------------

(See the :doc:`/events/overview/conditional` guide for details for how to
create entries in your config file that only respond to certain combinations of
the arguments below.)

``change``
  If the player variable just changed, this will be the amount of the change. If it's not possible to determine a numeric change (for example, if this player variable is a string), then this *change* value will be set to the boolean *True*.

``player_num``
  The player number this variable just changed for, starting with 1. (e.g. Player 1 will have *player_num=1*, Player 4 will have *player_num=4*, etc.)

``prev_value``
  The previous value of this player variable, e.g. what it was before the current value.

``value``
  The new value of this player variable.

