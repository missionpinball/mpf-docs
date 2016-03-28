
The `logic_blocks:` section of your config file contains subsections
for each type of *`logic block`_* in your game, including
*`accruals`_*, *`counters`_*, and *`sequences`_*. This section
*cannot* be used in your machine-wide config files. This sectioncan be
used in your mode-specific config files. You can read about the
configuration details for each type of logic block from the links
above. However, there are several types of settings that apply to all
logic blocks, so we're including them once here instead of copying-
and-pasting them into the sections on each logic block.



Settings that apply to all types of Logic Blocks
------------------------------------------------



<name>:
~~~~~~~

You configure your individual Logic Blocks in the `logic_blocks:`
section of your config files. The actual name you pick for each Logic
Block doesn’t matter. It’s just a friendly name that will make sense
to you.



events_when_complete:
~~~~~~~~~~~~~~~~~~~~~

This is a `list of events`_ (or a single event) which are posted when
this logic block is complete. If you don't have a configuration entry
here, then MPF will automatically post an event with the name
*logicblock_<your_logic_block>_complete* when the logic block is
complete.



enable_events:
~~~~~~~~~~~~~~

This is a `list of events`_ (or a single event) which, when posted,
causes this logic block tostart watching for events to trackprogress
towards completion. If your logic blockis not active, then any events
that fire won't count towards progress. Default for this is *None*
(meaning you'd have to manually enable this logic block in code).



disable_events:
~~~~~~~~~~~~~~~

This is a `list of events`_ (or a single event) which, when posted,
causes this logic blockto stop watching for events and to stop
tracking progress towards completion. If any one of the events is
posted while this logic blockis disabled, it will be ignored. Default
for this is *None* (meaning you'd have to manually disable this logic
block in code), or that it will be disabled when the mode this logic
block's config is in stops.



reset_events:
~~~~~~~~~~~~~

This is a `list of events`_ (or a single event) which, when posted,
resets this logic blockback to to its default state. Default is
*None*.



restart_on_complete:
~~~~~~~~~~~~~~~~~~~~

Yes/No (or True/False) which controls whether this logic block should
reset and restart itself when it completes. Default is *false*.



disable_on_complete:
~~~~~~~~~~~~~~~~~~~~

Yes/No (or True/False) which controls whether this logic block should
disableitself when it completes. Default is *true*.



persist_state:
~~~~~~~~~~~~~~

If this is set to *true*, then this logic block will not reset its
state each time it's loaded. This means that you have have "long
running" logic blocks that persist across balls. (Remember though that
logic blocks are still tracked on a per-player basis.) Default is
*false*.

.. _list of events: https://missionpinball.com/docs/configuration-file-reference/important-config-file-concepts/adding-lists-and-lists-of-lists-to-config-files/
.. _accruals: https://missionpinball.com/docs/configuration-file-reference/accruals/
.. _logic block: https://missionpinball.com/docs/mpf-core-architecture/system-modules/logic-blocks-manager/
.. _sequences: /docs/configuration-file-reference/sequences
.. _counters: https://missionpinball.com/docs/configuration-file-reference/counters


