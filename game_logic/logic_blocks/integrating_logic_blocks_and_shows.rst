Integrating Logic_Blocks and Shows
==================================

Logic_Block-Triggered Events
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Logic_blocks can be flexibly integrated with shows using the *(name)_updated* event.
It is posted on every state change (i.e. when a counter is incremented) and when
logic_blocks are restored (on mode restart). This means that the event may be posted
more than once and all handlers should be idempotent (i.e. that you can execute them more
than once without changing state after the first time). This event works well to control
shows, lights, slides, and to restore them on the next ball. However it should not be used
for scoring (to handle an event when the counter changes, consider the *(name)_hit* event instead).

.. code-block:: yaml

    logic_blocks:
        counters:
            my_counter:
                count_events: my_count_event
                starting_count: 0
                count_complete_value: 3

    show_player:
      logicblock_my_counter_updated{value == 0}:
        my_show_initial:
          key: my_counter_show  # this is to remove the previous show from the same player
      logicblock_my_counter_updated{value == 1}:
        my_show_first_hit:
          key: my_counter_show  # this is to remove the previous show from the same player
      logicblock_my_counter_updated{value >= 2}:
        my_show_final:
          key: my_counter_show  # this is to remove the previous show from the same player


Every time ``my_counter`` is updated (or restored) it will post
``logicblock_my_counter_updated``. Depending on the value of ``my_counter``
either ``my_show_initial`` (value is 0), ``my_show_first_hit`` (value is 1) or
``my_show_final`` (value is 2 or 3) are shown. All show_players have the same key so
they will stop any other show playing with the same key.

Other Triggered Events
~~~~~~~~~~~~~~~~~~~~~~

You can also have a show depend on the state of a logic block while being triggered
by another event, using :docs:`Conditional Events </events/overview/conditional>`.

If the logic_block has a persistent state (``persist_state: true``), you can make
a condition based on the player variable for the block:

.. code-block:: yaml

  show_player:
    some_other_event{current_player.my_counter_state==0}: my_show_initial
    some_other_event{current_player.my_counter_state==1}: my_show_once_hit
    some_other_event{current_player.my_counter_state==2}: my_show_twice_hit

If the logic_block is not persistent (``persist_state: false``), you can access the
value directly from the block device:

.. code-block:: yaml

  show_player:
    some_other_event{devices.counters.my_counter.value==0}: my_show_initial
    some_other_event{devices.counters.my_counter.value==1}: my_show_once_hit
    some_other_event{devices.counters.my_counter.value==2}: my_show_twice_hit
