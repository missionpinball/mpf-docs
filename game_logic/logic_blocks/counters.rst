Counter Logic Blocks
====================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/counters`                                                      |
+------------------------------------------------------------------------------+

"Counters" are :doc:`logic blocks </game_logic/logic_blocks/index>`
that track the number of times a certain event happens towards the
progress of a completion goal.

Examples include:

* Hit a target (or shot) X number of times to advance.
* Hit pop bumpers 75 times to start a Super Jets mode.
* Counting the number of combos made
* Keeping track of a bonus multiplier (maybe you use the shot group lane
  completion event to count progress towards the bonus multiplier, but you
  configure the max count to be 6, and then if it's hit again, you award
  an extra ball).

You can use optional parameters to specify whether multiple occurrences in
a very short time window should be grouped together and counted as one
hit, the counting interval, and whether this counter counts up or
down.

Here's an example of a counter you could use to track progress towards super
jets:

.. code-block:: yaml

  counters:
      super_jets:
          count_events: sw_pop
          events_when_hit: pop_hit
          starting_count: 75
          count_complete_value: 0
          direction: down
          events_when_complete: super_jets_start

And here's the logic block we use for the :doc:`Addams Family mansion awards </cookbook/TAF_mansion_awards>`
to make sure the mansions is initialized only once per game:

.. code-block:: yaml

  counters:
    initialize_mansion:
      count_events: mode_chair_lit_started
      events_when_complete: initialize_mansion
      count_complete_value: 1
      persist_state: true

