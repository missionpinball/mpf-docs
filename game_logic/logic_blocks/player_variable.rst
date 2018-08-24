player_variable:
~~~~~~~~~~~~~~~~

By default, the current "state" (or progress) of logic blocks
is stored in a :doc:`player variable </game_logic/players/index>` called
*<counter_name>_state*.
For example, a logic block called "logic_block_1" would store its state
in a player variable called *logic_block_1_state*.

However, you can use the ``player_variable:`` setting to change this to
any player variable you want. Making this change doesn't really affect anything
other than the name of the variable. It's just for convenience if you prefer a
different name.

Note that this player variable stores the state the logic block as a numerical
value: steps accrued for accruals, and current step number for sequences.
In other words, when a logic block is just started or reset, the player variable
tracking it is set to ``0``. Then that increases by one as each step/count is
complete.

You can easily use this numerical value in a text widget to show the number of
combos complete, or the number of pop bumper hits required for super jets, etc.
This player variable "state" is different than the state of the logic block itself,
which is an object with `enabled`, `completed`, and `value` attributes. Note the
difference in accessing the logic block state as a dynamic value vs. placeholder
text:

.. code-block:: mpf-config

  ##! mode: my_mode
  variable_player:
    counter_hit:
      score: 100 * device.counters.logic_block_1.value
                   # The logic block stores the count as the 'value' attribute

  widgets:
    counter_widget:
      - type: text
        text: (logic_block_1_state) Hits!
              # The player variable is the count value itself

.. note::
   The player variable is only saved if the logic block is configured
   with ``persist_state: True``. If ``persist_state`` is ``False``, the logic block
   value will _not_ be saved under any variable name (not even the default).

