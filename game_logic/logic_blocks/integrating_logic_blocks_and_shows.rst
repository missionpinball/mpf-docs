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

.. code-block:: mpf-config

  ##! mode: my_mode
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

Another way to achieve the same thing is this:


You can even achieve this a bit simpler than in the example. Like this:

.. code-block:: mpf-config

  ##! mode: my_mode
  counters:
      my_counter:
          count_events: my_count_event
          starting_count: 0
          count_complete_value: 3

  show_player:
    logicblock_my_counter_updated{enabled}:
      my_show:
        key: my_counter_show
        start_step: value + 1
        show_tokens:
          led1: l_led1
          led2: l_led2
          led3: l_led3
          color: magenta
    logicblock_my_counter_updated{not enabled}:
      my_counter_show: stop

This will start the show ``my_show`` at the value of the counter ``my_counter``.
For instance when the counter is 0 it will start step 1, counter 1 will run step 2 and so on.
Once the counter is disabled the show it stopped (but other behaviours are possible).

``my_show`` could look like this:

.. code-block:: mpf-config

   ##! show: my_show
   #show_version=5
   - duration: -1
     lights:
       (led1): off
       (led2): off
       (led3): off
   - duration: -1
     lights:
       (led1): (color)
       (led2): off
       (led3): off
   - duration: -1
     lights:
       (led1): (color)
       (led2): (color)
       (led3): off
   - duration: -1
     lights:
       (led1): (color)
       (led2): (color)
       (led3): (color)


Actions which should only happen once
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want something to happen only once when the logic_block advances (and
not on mode restart) you should use the ``_hit`` event.
E.g. for a callout use this:

.. code-block:: mpf-config

  ##! mode: my_mode
  counters:
      my_counter:
          count_events: my_count_event
          starting_count: 0
          count_complete_value: 10

  sound_player:
   logicblock_my_counter_hit{remaining == 5}:
     sound_just_5_remaining:
      action: play
   logicblock_my_counter_hit{remaining == 2}:
     sound_just_2_remaining:
      action: play
   logicblock_my_counter_hit{remaining == 1}:
     sound_just_1_remaining:
      action: play


Other Triggered Events
~~~~~~~~~~~~~~~~~~~~~~

You can also have a show depend on the state of a logic block while being triggered
by another event, using :doc:`Conditional Events </events/overview/conditional>`.

You can access the value directly from the device variable using ``devices.counters.my_counter.value``:

.. code-block:: mpf-config

  ##! mode: my_mode
  show_player:
    some_other_event{devices.counters.my_counter.value==0}: my_show_initial
    some_other_event{devices.counters.my_counter.value==1}: my_show_once_hit
    some_other_event{devices.counters.my_counter.value==2}: my_show_twice_hit

+------------------------------------------------------------------------------+
| Related Events                                                               |
+==============================================================================+
| :doc:`/events/logicblock_name_updated`                                       |
+------------------------------------------------------------------------------+
| :doc:`/events/logicblock_name_hit`                                           |
+------------------------------------------------------------------------------+
