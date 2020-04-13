mode:
=====

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **NO**  |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

.. overview

The ``mode:`` section of a mode config file is used to specify
settings for a that mode.

Note that this ``mode:`` section is different than the
``modes:`` section. (The ``modes:`` section is a machine-wide setting where
you list all the modes that are made available to MPF when it boots
up. The ``mode:`` section we're talking about here goes in a mode-specific
config and holds the settings for that specific mode.)

Let's take a look at an example ``mode:`` section from a multiball mode:

.. code-block:: mpf-config

    ##! mode: mode1
    mode:
      start_events: ball_starting
      stop_events: timer_mode_timer_complete, shot_right_ramp
      priority: 300

.. config


Optional settings
-----------------

The following sections are optional in the ``mode:`` section of your config. (If you don't include them, the default will be used).

code:
~~~~~
Single value, type: ``string``. Defaults to empty.

If you want to write some custom Python code for this mode, you can
specify the name of your file as well as the class (a child class of
Mode). This entry is completely optional. If you don't need to write
custom Python code for this mode (i.e. if you can do everything you
need to do with config files which will probably be the case 90% of
the time, then you can skip this setting.)

console_log:
~~~~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level for the console log for this mode.

events_when_started:
~~~~~~~~~~~~~~~~~~~~
List of one (or more) events. Those will be posted by the device. Defaults to empty.

Events which will be posted when this mode has been started.

events_when_stopped:
~~~~~~~~~~~~~~~~~~~~
List of one (or more) events. Those will be posted by the device. Defaults to empty.

Events which will be posted when this mode has been stopped.

file_log:
~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level for the file log for this mode.

game_mode:
~~~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``true``

A mode can only access player state if ``game_mode`` is set to ``True``.
You can set this to ``False`` to allow a mode to run outside of a game.
On example for such a mode is the attract mode.
Game modes are automatically stopped at the end of a game.

priority:
~~~~~~~~~
Single value, type: ``integer``. Default: ``100``

This is the numeric value that this mode will run at. (Note that this
cannot be changed once the mode is running.) This priority affects two
things:

+ The priority order of the modes which affects the order shots and
  other "blockable" events are processed.
+ The default priority that other things from this mode run at
  (shows, slides, sounds, etc.).

Our best practices are that you should have a 100-point separation
between modes. (i.e. run your base mode at 100, a game mode at 200,
maybe your extra ball awarded mode at 10,000, etc.) The reason for
this is that with big spacing between modes, you still have room to
adjust the relative priorities of things that happen within a mode
without the risk of those things affecting other modes.

.. warning::

   Keep your mode priorities between 100 and 1000000. MPF needs some built-in
   modes to run above and below your modes, so it has some things that run
   under 100 and over 1 million.

restart_on_next_ball:
~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

If you set this to *true*, a mode that was running when the ball ended
that was also configured to stop on ball end will automatically start
for the next ball this player has. This is managed on a per-player
basis via a player variable *_restart_modes_on_next_ball*
which maintains a list of the modes to be restarted.

start_events:
~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

Default: ``None``

Events in this list, when posted, cause this mode to start.

If the mode is already running when one of the start events is
posted, that's ok. (i.e. It won't start over or break.)

For modes that
you want to start when the player's ball starts (like for your base
mode, ball save, or skillshot, you'd enter `ball_starting` here. For
modes that should start when some progress has been made in the game,
enter the name of the event that represents when you want to start the
mode. This could be the event from a shot being made, the resultant
event from a logic block being completed, etc.

start_priority:
~~~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``0``

Allows you to fine-tune the order that modes are started in.

By default, modes register their start event handlers based on their
mode priority, meaning if two modes are both configured to start on the
``ball_starting`` event, the higher-priority one will start first.

This ``start_priority:`` setting allows you to specify a relative value
that will be added to the mode's ``priority:`` for the purpose of
controlling the start order. (You can specify positive or negative values
here.)

Note that the ``start_priority:`` setting only matters when you have multiple
modes that are set to start on the same event.

stop_events:
~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

Default: ``None``

Events in this list, when posted, cause the mode to stop which
will remove itself from the list of active modes. All of the things
you configured in this mode's config file will be unloaded. (i.e.
slides and shows won't play, scoring and shot events are removed,
etc.)

In the skillshot mode from the example above, there are two
``stop_events:``. The first entry is the event that's posted when a
timer called "mode_timer" is complete. (In this case this is a timed
mode, so when that timer expires, the mode ends.) The second event is
when the skillshot is made (the right ramp) in this case. (This is
because once the skillshot is made, you want to remove this mode.)

If a mode is stopped and another one of the stop_events is posted, that's
ok. The mode will remain stopped.

stop_on_ball_end:
~~~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``true``

The default behavior for modes in MPF is that they're automatically
stopped when the ball ends. Some modes (like the built-in *game* and
*credit* modes) need to stay running even when the ball ends, so to
support that you can add ``stop_on_ball_end: false``.

Another use of this option is to retain the mode's progress towards
completion after draining a ball; allowing the next player to start
their ball where the previous player left off in the mode. To enable
this behavior, you can add ``stop_on_ball_end: false``.

However, it is very likely that a mode will be left unfinished (open)
after the final ball, causing MPF to shutdown unexpectedly.  You will
get an error similar to this:

.. code-block:: python

   AssertionError('Mode terra_2 is not supposed to run outside of game.',)

To avoid this
unexpected crash of MPF, add ``game_ending`` to the ``stop_events:``

.. code-block:: mpf-config

   ##! mode: mode1
   mode:
     start_events: mode_terra_2_start
     stop_events: mode_complete, game_ending
     stop_on_ball_end: false
     game_mode: false

However, a mode with ``stop_on_ball_end: False`` set must be a non game mode
(i.e. ``game_mode: False`` is also set).
To prevent crashes you cannot use all player functionality (such as accessing
player variable) in this mode.

stop_priority:
~~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``0``

Control the order that modes stop.

By default, modes register their stop handlers at the level the mode
is operating plus one. (Why +1? Because if you have one mode set to
stop at an event and another mode set to start on the same event,
automatically adding +1 to the stop event handler guarantees that the
old mode will stop before the new mode starts.)

If you add stop
priority, it's relative and added on top of the priority of the mode
plus the +1. So if you have one mode you want to stop before another
mode, you can simply add ``stop_priority: 1`` to that mode, and if other
modes don't have a stop_priority set then they'll stop after it. (A
higher number means that mode stops first.)

If you have a mode you
want to stop last, then don't enter a *stop_priority* for it but enter
`stop_priority: 1` for all the other modes you want to stop first. You
can add different *stop_priority* values for different modes, and they
will all stop in order, highest numeric value to lowest. Note that the
*stop_priority* setting only matters when you have multiple modes that
are set to end on the same stop_event.

use_wait_queue:
~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

Specifies whether this mode should "pause"
the flow of MPF while this mode is running. This only works if the
mode is started via a "queue" event (something like ball_ending,
game_ending, etc.). When set to true, game flow will be halted as long
as this mode is running. Game flow proceeds when this mode ends.

This is useful for things like bonus modes where you want the mode to
finish before the game flow moves on with the next player's turn, or modes
like match or high score entry where you want those to finish before the
attract mode starts again.


Related How To guides
---------------------

* :doc:`/game_design/index`
* :doc:`/tutorial/14_add_a_mode`
* :doc:`/game_logic/modes/index`
