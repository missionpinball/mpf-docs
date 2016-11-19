:orphan:

enable_events:
~~~~~~~~~~~~~~

List of one (or more) events which, when posted, will enable this logic block.

A logic block must be enabled to track hits, progress, and to post events.

You can list multiple events in the :doc:`events list format </config/instructions/device_control_events>`
which means you can specify delay times where the logic block will delay its
enabling until the time passes.

If you don't have any enable_events listed, then the logic block will automatically
be enabled when the player's ball starts.

Default is ``None``.

disable_events:
~~~~~~~~~~~~~~~

List of one (or more) events which, when posted, will disable this logic block.

A logic block must be enabled to track hits, progress, and to post events.

You can list multiple events in the :doc:`events list format </config/instructions/device_control_events>`
which means you can specify delay times where the logic block will delay its
disabling until the time passes.

Default is ``None``.

reset_events:
~~~~~~~~~~~~~

List of one (or more) events which, when posted, will reset this logic block back
to its original value.

Note that there are also ``reset_on_complete:`` and ``persist_state:`` settings
which also affect how and when the logic block is reset.

You can reset a logic block regardless of whether it's enabled.

Default is ``None``.

restart_events:
~~~~~~~~~~~~~~~

list|str|None

Default is ``None``.

reset_on_complete:
~~~~~~~~~~~~~~~~~~

single|bool|True

Default is ``True``.

disable_on_complete:
~~~~~~~~~~~~~~~~~~~~

single|bool|True

Default is ``True``.

persist_state:
~~~~~~~~~~~~~~

Boolean setting (yes/no or true/false) which controls whether this logic block
remembers where it was from ball-to-ball. If ``False``, then this logic block will
reset itself whenever a new ball starts.

Default is ``False``.

events_when_complete:
~~~~~~~~~~~~~~~~~~~~~

list|str|None

Default is ``None``.

events_when_hit:
~~~~~~~~~~~~~~~~

list|str|None

Default is ``None``.

player_variable:
~~~~~~~~~~~~~~~~

single|str|None
