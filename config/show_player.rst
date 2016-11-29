show_player:
============

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

.. note:: This section can also be used in a show file in the ``shows:`` section of a step.

.. overview

The ``show_player:`` section of your config is where you...

.. todo::
   Add description.

Optional settings
-----------------

The following sections are optional in the ``show_player:`` section of your config. (If you don't include them, the default will be used).

action:
~~~~~~~
Single value, type: one of the following options: play, stop, pause, resume, advance, step_back, update. Default: ``play``

.. versionchanged:: 0.31 (Added "step_back" state)

.. todo::
   Add description.

block_queue:
~~~~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

.. versionadded:: 0.32

.. todo::
   Add description.

key:
~~~~
Single value, type: ``string``. Default: ``None``

.. todo::
   Add description.

loops:
~~~~~~
Single value, type: ``integer``. Default: ``-1``

.. todo::
   Add description.

manual_advance:
~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

.. todo::
   Add description.

priority:
~~~~~~~~~
Single value, type: ``integer``. Default: ``0``

.. todo::
   Add description.

reset:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``True``

.. todo::
   Add description.

show_tokens:
~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``str``. Default: ``None``

.. todo::
   Add description.

speed:
~~~~~~
Single value, type: ``number`` (will be converted to floating point). Default: ``1``

.. todo::
   Add description.

start_step:
~~~~~~~~~~~
Single value, type: ``integer``. Default: ``1``

.. todo::
   Add description.

sync_ms:
~~~~~~~~

.. versionchanged:: 0.32

Single value, type: ``integer``. Default: ``None``

.. todo::
   Add description.

.. note:: The ``show_player:`` section of your config may contain additional settings not mentioned here. Read the introductory text for details of what those might be.

Events posted by achievements
-----------------------------

You can configure shows to post certain events when things happen. These are
useful (for example), to eject a ball when a show ends.

events_when_advanced:
~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 0.32

:doc:`List </config/instructions/lists>` of one (or more) names of events.
Default: ``None``.

Event(s) that will be posted when this show has been manually advanced to the
next step.

events_when_completed:
~~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 0.32

:doc:`List </config/instructions/lists>` of one (or more) names of events.
Default: ``None``.

Event(s) that will be posted when this show has completed, meaning it ran
through to the last step and ended naturally.

Note that if a show loops, these events are *not* posted when the loop happens.
(You can use the *events_when_looped* for that.) However if a show is set to
loop a specific number of times and then ends, these events will be posted at
the end.

Note that if you want an event to post whenever the show stops, even if it
didn't make it all the way to the end, you can use *events_when_stopped*.

events_when_looped:
~~~~~~~~~~~~~~~~~~~

.. versionadded:: 0.32

:doc:`List </config/instructions/lists>` of one (or more) names of events.
Default: ``None``.

Event(s) that will be posted when this show has looped (meaning it reached the
end and is jumping back to the first step).

events_when_paused:
~~~~~~~~~~~~~~~~~~~

.. versionadded:: 0.32

:doc:`List </config/instructions/lists>` of one (or more) names of events.
Default: ``None``.

Event(s) that will be posted when this show has been paused.

events_when_played:
~~~~~~~~~~~~~~~~~~~

.. versionadded:: 0.32

:doc:`List </config/instructions/lists>` of one (or more) names of events.
Default: ``None``.

Event(s) that will be posted when this show is played (started).

events_when_resumed:
~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 0.32

:doc:`List </config/instructions/lists>` of one (or more) names of events.
Default: ``None``.

Event(s) that will be posted when this show is resumed from a pause.

events_when_stepped_back:
~~~~~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 0.32

:doc:`List </config/instructions/lists>` of one (or more) names of events.
Default: ``None``.

Event(s) that will be posted when this show has been manually stepped back to
the previous step.

events_when_stopped:
~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 0.32

:doc:`List </config/instructions/lists>` of one (or more) names of events.
Default: ``None``.

Event(s) that will be posted when this show has been stopped. Note that these
events are posted anytime the show has been stopped, regardless of whether it
made it to the end and stopped on its own, or whether it was stopped randomly
where it was.

events_when_updated:
~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 0.32

:doc:`List </config/instructions/lists>` of one (or more) names of events.
Default: ``None``.

Event(s) that will be posted when this show has been updated. Note that the
show "update" function has not been implemented yet, so this setting is more
of a placeholder at the moment.
