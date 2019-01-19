player_variable:
~~~~~~~~~~~~~~~~

Prior to MPF 0.50 the state of logic blocks has been persisted to player
variables.
This only longer holds true for player specific blocks (e.g. if you set
``persist_state`` to ``True``).
In that case the variable will be called ``(logic_block)_state``.
For example, a logic block called "logic_block_1" would store its state
in a player variable called *logic_block_1_state*.
When you do not want to persist the value you can reference it using
``device.counters.logic_block_1.value`` (also if you set it).

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

In this example we persist the value of the counter in the player variable
``counter_hit`` to use it in a slide.

.. note::
   The player variable is only saved if the logic block is configured
   with ``persist_state: True``. If ``persist_state`` is ``False``, the logic block
   value will _not_ be saved under any variable name (not even the default).

