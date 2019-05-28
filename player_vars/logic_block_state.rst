(logic_block)_state
===================

*MPF player variable*

A dictionary that stores the internal state of the logic block
with the name (logic_block). (In other words, a logic block called
*mode1_hit_counter* will store its state in a player variable called
``mode1_hit_counter_state``).

The state that's stored in this variable includes whether the logic
block is enabled and whether it's complete. However when this variable is
referenced in a placeholder for :doc:`/displays/widgets/text/text_dynamic`,
only the _value_ of the logic block's counter will be rendered.

Note that a logic block will only store this player variable if it is
configured with ``persist_state: True``.

