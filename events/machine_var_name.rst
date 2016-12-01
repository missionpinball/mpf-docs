machine_var_(name)
==================

*MPF Event*

Posted when a machine variable is added or changes value.
(Machine variables are like player variables, except they're
maintained machine-wide instead of per-player or per-game.)

Keyword arguments
-----------------

(See the :doc:`/events/overview/conditional` guide for details for how to
create entries in your config file that only respond to certain combinations of
the arguments below.)

``change``
  If the machine variable just changed, this will be the
amount of the change. If it's not possible to determine a numeric
change (for example, if this machine variable is a list), then this
*change* value will be set to the boolean *True*.

``prev_value``
  The previous value of this machine variable, e.g. what
it was before the current value.

``value``
  The new value of this machine variable.

