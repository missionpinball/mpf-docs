show_player:
============

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

.. note:: This section can also be used in a show file in the ``shows:`` section of a step.


The ``show_player:`` section of your config is where you start, stop, pause, (etc.) shows.

Here is an example:

.. code-block:: mpf-config

   show_player:
     some_event: your_show_name
     some_other_event: another_show

In the example above, when the event *some_event* is posted, the show called ``your_show_name`` will be played (started).
When the event *some_other_event* is posted, the show called ``another_show`` will be played.

See :doc:`/config_players/show_player` for details.

Settings
--------

The following settings can be added under a show name. If you don't include them, the default will be used.

action:
~~~~~~~
Single value of one of the following options: play, stop, pause, resume, advance, step_back, update. Default: ``play``

``play``
   Starts playing the show. This is the default action which will happen if you don't include an ``action:`` setting.

``stop``
   Stops the show. Removes and "undoes" anything the show did, and posts the show stop events.

``pause``
   Pauses the show by holding it at the current step. Posts the show pause events.

``resume``
   Resumes a previously paused show.

``advance``
   Manually advances a show to the next step. Posts the show advance events.

``step_back``
   Manually moves the show back to the previous step. Posts the show step_back events.

``update``
   Not yet implemented. In the future it will be used to change a setting of a running show,
   like changing the playback speed.

block_queue:
~~~~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``


You can use ``block_queue: yes`` if you want the show to block a queue event until the show is
done. Note that you can only use this if the event that starts the show is a
:doc:`queue event </events/overview/event_types>`.

For example, the mode stopping events are queue events. So take a look at the
following config:

.. code-block:: mpf-config

   show_player:
     mode_my_mode_stopping:
       show_1:
         block_queue: true

In the example above, when the mode called *my_mode* posts its stopping
event, show_1 will start playing. However because this show is set to block
the queue event, the mode stopping event will not finish until the show
finishes. In other words, the mode will not fully stop, and the
*mode_my_mode_stopped* event will not be posted until the show ends.

If you didn't use the block_queue setting, then the show would start and then
stop right away since the mode would end and be over (and shows started in modes
are stopped when those modes end).

If you used this setting, make sure that you don't have
``loops: -1``, or a ``duration: -1`` as the final step of the show, since those will mean the show
will never end, and then the queue event will never be unblocked, and your machine will hang.

key:
~~~~
Single value, type: ``string``. Default: ``None``

Used to set a unique identifier you can set when playing a show which can then be used later
to identify a show you want to perform an action on.

loops:
~~~~~~
Single value, type: ``integer``. Default: ``-1``

Controls the looping / repeating of the show. The default if you don't include this setting is
``loops: -1`` means that the show will repeat indefinitely until it's stopped.

If you just want a show to play once and then stop, use ``loops: 0``.

Since this setting is the number of times it loops, the value will be one less than the number
of times the show will play. (e.g. ``loops: 1`` means the show will loop once which means it will
play through twice.)

Note that if a show only has one step, *loops* will be set to 0, regardless of the actual loops setting.

manual_advance:
~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

If you set this to yes/true, then the show will not auto-advance based on time. Instead you will
have to manually advance the show step-by-step with additional show_player entries with
``action: advance`` entries.

This can be useful if you want to have some kind of slow progress based on
a series of events instead of a show that auto plays.

For example:

.. code-block:: mpf-config

   show_player:
     some_event:
       show_1:
         manual_advance: true
     some_advance_event:
       show_1:
         action: advance

In the example above, the event *some_event* will start show_1, but that show
will stay on its first step since it's set to manually advance. Then each
time the event *some_advance_event* is posted, show_1 will advance to its
next step.

priority:
~~~~~~~~~
Single value, type: ``integer``. Default: ``0``

Adjusts the priority of the show that's played.

By default, shows play at the priority of the mode where the show_player entry is. So this
setting merely adjusts the show's priority up or down. For example, if you have a mode
running at priority 300, and a show in a show_player with the setting ``priority: 10``, then that
show will run at priority 310. Priorities can also be negative.

The show's priority affects the priority of everything it does. Sounds, slides, LEDs, etc.

show_tokens:
~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``str``. Default: ``None``

Allows you to specify show token values that will be used to replace the show tokens in the show
when it's played.

Read what show tokens are :doc:`here </shows/tokens>`.

For example:

.. code-block:: mpf-config

   show_player:
     some_event:
       show1:
         show_tokens:
           led: right_inlane

In the example above, the show called "show1" will be played, but the show token called "led" in the
show will be replaced at runtime with the value "right_inlane".

speed:
~~~~~~
Single value, type: ``number`` (will be converted to floating point). Default: ``1``

Controls the playback speed of the show. The default value of 1 means the show plays back at 1x
speed. (In other words, it plays at the actual speed each step is configured for. In this case
you don't actually need to include the setting.)

If you want to play the show at 2x the speed, use ``speed: 2``. If you want to play it at half
speed, use ``speed: .5``. Etc.

start_running:
~~~~~~~~~~~~~~
Single value, type: ``boolean``. Default: ``True``

Whether the show starts running immediately when it is played.

By default, calling ``play`` on a show begins at the starting step and advances through the steps
according to the show config. If ``start_running`` is false, the show will play the starting step
and immediately pause. You can begin playing the show by calling show_player with ``action: resume``.

start_step:
~~~~~~~~~~~
Single value, type: ``integer``. Default: ``1``

Which step the show starts on when it's played.

Note that you can use a :doc:`dynamic value </config/instructions/dynamic_values>`
for this setting.

sync_ms:
~~~~~~~~
Single value, type: ``integer``. Default: ``None``

Sets the sync_ms value of this show which will delay the start to a certain millisecond multiple
to ensure that multiple shows started at different times all play in sync with each other.

See the :doc:`/shows/sync_ms` documentation for details.

Events posted by shows
----------------------

You can configure shows to post certain events when things happen. These are
useful (for example), to eject a ball when a show ends.

events_when_advanced:
~~~~~~~~~~~~~~~~~~~~~


:doc:`List </config/instructions/lists>` of one (or more) names of events.
Default: ``None``.

Event(s) that will be posted when this show has been manually advanced to the
next step.

events_when_completed:
~~~~~~~~~~~~~~~~~~~~~~


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


:doc:`List </config/instructions/lists>` of one (or more) names of events.
Default: ``None``.

Event(s) that will be posted when this show has looped (meaning it reached the
end and is jumping back to the first step).

events_when_paused:
~~~~~~~~~~~~~~~~~~~


:doc:`List </config/instructions/lists>` of one (or more) names of events.
Default: ``None``.

Event(s) that will be posted when this show has been paused.

events_when_played:
~~~~~~~~~~~~~~~~~~~


:doc:`List </config/instructions/lists>` of one (or more) names of events.
Default: ``None``.

Event(s) that will be posted when this show is played (started).

events_when_resumed:
~~~~~~~~~~~~~~~~~~~~


:doc:`List </config/instructions/lists>` of one (or more) names of events.
Default: ``None``.

Event(s) that will be posted when this show is resumed from a pause.

events_when_stepped_back:
~~~~~~~~~~~~~~~~~~~~~~~~~


:doc:`List </config/instructions/lists>` of one (or more) names of events.
Default: ``None``.

Event(s) that will be posted when this show has been manually stepped back to
the previous step.

events_when_stopped:
~~~~~~~~~~~~~~~~~~~~


:doc:`List </config/instructions/lists>` of one (or more) names of events.
Default: ``None``.

Event(s) that will be posted when this show has been stopped. Note that these
events are posted anytime the show has been stopped, regardless of whether it
made it to the end and stopped on its own, or whether it was stopped randomly
where it was.

events_when_updated:
~~~~~~~~~~~~~~~~~~~~


:doc:`List </config/instructions/lists>` of one (or more) names of events.
Default: ``None``.

Event(s) that will be posted when this show has been updated. Note that the
show "update" function has not been implemented yet, so this setting is more
of a placeholder at the moment.


.. toctree::
   :maxdepth: 1
   :hidden:

   show_config: <show_config>
