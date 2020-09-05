

.. config


Optional settings
-----------------

The following sections are optional in the ``logic_blocks_common:`` section of your config. (If you don't include them, the default will be used).

disable_events:
~~~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`).

Event(s) that will disable this logic block.

A logic block must be enabled to track hits, progress, and to post events.

disable_on_complete:
~~~~~~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``true``

True/False (or Yes/No) which controls whether this logic block disables
itself once it completes. This does not reset the current value.

enable_events:
~~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`).

Event(s) that will enable this logic block.

A logic block must be enabled to track hits, progress, and to post events.

If you don't have any enable_events listed, then the logic block will automatically
be enabled when the player's ball starts.

events_when_complete:
~~~~~~~~~~~~~~~~~~~~~
List of one (or more) events.

Events that will be posted when this device is completed.

events_when_hit:
~~~~~~~~~~~~~~~~
List of one (or more) events.

Events that will be posted when this device is hit or advanced.

persist_state:
~~~~~~~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

Boolean setting (yes/no or true/false) which controls whether this logic block
remembers where it was from ball-to-ball. If ``False``, then this logic block will
reset itself whenever a new ball starts. If ``True``, then this logic block will
be saved to the player variable *<logic_block_name>_state*.

Note that logic block state is reset on mode end when this is ``False`` and, as
normal modes stop at the end of a ball, the state is always maintained on a
per-player basis, regardless of what this setting is configured for.

reset_events:
~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`).

Event(s) that will reset this logic block back to its original value. This
has no effect on the enabled/disabled state of the block.

Note that there are also ``reset_on_complete:`` and ``persist_state:`` settings
which also affect how and when the logic block is reset.

You can reset a logic block regardless of whether it's enabled.

reset_on_complete:
~~~~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``true``

True/False (or Yes/No) which controls whether this logic block resets itself
once it completes. This just resets the current value or progress. It does
not change the enabled or disabled state.

restart_events:
~~~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`).

List of one (or more) events which, when posted, will restart this logic
block. A restart is a reset, then an enable, combined into a single action.

start_enabled:
~~~~~~~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``).

If ``true`` this device will start enabled.
If ``false`` this device will start disabled.
If you omit this the device will start enabled unless you specify
``enable_events`` in which case the device will start disabled.
