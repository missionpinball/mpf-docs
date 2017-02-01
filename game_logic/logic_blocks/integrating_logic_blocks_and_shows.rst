Integrating Logic_Blocks and Shows
==================================

Logic_blocks can be flexibly integrated with shows using the (name)_updated event.
It is posted on every state change (i.e. when a counter is incremented) and when
logic_blocks are restored (on mode restart). This means that the event may be posted
more than once and all handlers should be idempotent (i.e. that you can execute them more
than once without changing state after the first time). Therefore, this event should
not be used for scoring. However, it works well to control shows, lights, slides and
restore them on the next ball.

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
      
