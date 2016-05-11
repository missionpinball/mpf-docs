counter_(name)_hit
==================

*MPF Event*

The counter logic block "name" was just hit.

Note that this is the default hit event for counter logic blocks,
but this can be changed in a logic block's "events_when_hit:"
setting, so this might not be the actual event that's posted for
all counter logic blocks in your machine.


Keyword arguments
-----------------

count
~~~~~
The new count value for this logic block. (It may be
counting up or down, depending on its config.)

