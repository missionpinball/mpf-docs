(logic_block)_state
config_section: counters, accruals, sequences
=================================================================

*MPF player variable*

A dictionary that stores the internal state of the logic block
with the name (logic_block). (In other words, a logic block called
*mode1_hit_counter* will store its state in a player variable called
``mode1_hit_counter_state``).

The state that's stored in this variable include whether the logic
block is enabled and whether it's complete.

