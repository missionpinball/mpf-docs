(combo_switch)_(state)
======================

*MPF Event*

Combo switch (name) changed to state (state).

Note that these events can be overridden in a combo switch's
config.

Valid states are: *inactive*, *both*, or *one*.

..rubric:: both

A switch from group 1 and group 2 are both active at the
same time, having been pressed within the ``max_offset_time:`` and
being active for at least the ``hold_time:``.

..rubric:: one

Either switch 1 or switch 2 has been released for at
least the ``release_time:`` but the other switch is still active.

..rubric:: inactive

Both switches are inactive.

*This event does not have any keyword arguments*
