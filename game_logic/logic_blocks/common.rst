persist_state:
~~~~~~~~~~~~~~

Boolean setting (yes/no or true/false) which controls whether this logic block
remembers where it was from ball-to-ball. If ``False``, then this logic block will
reset itself whenever a new ball starts. If ``True``, then this logic block will
be saved to the player variable *<logic_block_name>_state*.

Note that logic block state is reset on mode end when this is ``False`` and, as
normal modes stop at the end of a ball, the state is always maintained on a
per-player basis, regardless of what this setting is configured for.

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





