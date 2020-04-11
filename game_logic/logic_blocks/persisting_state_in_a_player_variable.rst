Persisting the State of a Logic Block in a Player Variable
==========================================================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/counters`                                                      |
+------------------------------------------------------------------------------+
| :doc:`/config/variable_player`                                               |
+------------------------------------------------------------------------------+

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

.. code-block:: mpf-mc-config

   ##! mode: my_mode
   counters:
     logic_block_1:
       count_events: count_up_event

   variable_player:
     counter_logic_block_1_hit:  # this is triggered when the counter changes
       my_widget_placeholder: 100 * device.counters.logic_block_1.value
      # The logic block stores the count as the 'value' attribute
   widgets:
     counter_widget:
       - type: text
         text: (my_widget_placeholder) Hits!
     # This placeholder is set by variable_player when the counter changes
   #! widget_player:
   #!   show_widget_event: counter_widget
   ##! test
   #! start_game
   #! start_mode my_mode
   #! post show_widget_event
   #! post count_up_event
   #! advance_time_and_run .1
   #! assert_text_on_top_slide "100 Hits!"

In this example we persist the value of the counter in the player variable
``counter_hit`` to use it in a slide.

.. note::
   The player variable is only saved if the logic block is configured
   with ``persist_state: True``. If ``persist_state`` is ``False``, the logic block
   value will _not_ be saved under any variable name (not even the default).

