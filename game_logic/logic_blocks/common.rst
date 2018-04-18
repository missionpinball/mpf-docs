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
value: current count value for counters, steps accrued for accruals, and current
step number for sequences. In other words, when a logic block is just started or
reset, the player variable tracking it is set to ``0``. Then that increases by
one as each step/count is complete.

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

persist_state:
~~~~~~~~~~~~~~

Boolean setting (yes/no or true/false) which controls whether this logic block
remembers where it was from ball-to-ball. If ``False``, then this logic block will
reset itself whenever a new ball starts. If ``True``, then this logic block will
be saved to the player variable *<logic_block_name>_state*.


Note that logic block state is always maintained on a per-player basis,
regardless of what this setting is configured for.

Default is ``False``.

reset_on_complete:
~~~~~~~~~~~~~~~~~~

True/False (or Yes/No) which controls whether this logic block resets itself
once it completes. This just resets the current value or progress. It does
not change the enabled or disabled state.

Default is ``True``.

disable_on_complete:
~~~~~~~~~~~~~~~~~~~~

True/False (or Yes/No) which controls whether this logic block disables
itself once it completes. This does not reset the current value.

Default is ``True``.

Events posted by this logic block
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can enter a list of one (or more) events that will be posted when certain
things happen to this logic block. Enter multiple events in
:doc:`MPF list format </config/instructions/lists>`.

``events_when_hit:``
   Event(s) posted when this logic block is "hit", meaning that one of the
   sequence events, accrual events, or count events was just posted and
   advanced this logic block's state.

   Note that the event :doc:`/events/logicblock_name_hit` will always be
   posted, regardless of whether you have anything set here.

``events_when_complete:``
   List of one (or more) events which, when posted, will

   Note that the event :doc:`/events/logicblock_name_complete` will always be
   posted, regardless of whether you have anything set here.

Control Events
~~~~~~~~~~~~~~

The following settings are used to configure events that will change the state
of this logic block. Note that each of these can be one or more events.

You can list multiple events in the :doc:`events list format </config/instructions/device_control_events>`
which means you can specify delay times where the logic block will delay its
enabling until the time passes.

``enable_events:``
   Event(s) that will enable this logic block.

   A logic block must be enabled to track hits, progress, and to post events.

   If you don't have any enable_events listed, then the logic block will automatically
   be enabled when the player's ball starts.

   Default is ``None``.

``disable_events:``
   Event(s) that will disable this logic block.

   A logic block must be enabled to track hits, progress, and to post events.

   Default is ``None``.

``reset_events:``
   Event(s) that will reset this logic block back to its original value. This
   has no effect on the enabled/disabled state of the block.

   Note that there are also ``reset_on_complete:`` and ``persist_state:`` settings
   which also affect how and when the logic block is reset.

   You can reset a logic block regardless of whether it's enabled.

   Default is ``None``.

``restart_events:``
   List of one (or more) events which, when posted, will restart this logic
   block. A restart is a reset, then an enable, combined into a single action.

   Default is ``None``.





