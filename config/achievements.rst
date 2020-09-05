achievements:
=============

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **NO**  |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

.. overview

The ``achievements:`` section of your config is where you configure
:doc:`player-based "achievement" tracking </game_logic/achievements/index>`.

Like most things in MPF configs, the highest-level entries in the
``achievements:`` section of your config are the names of the individual
achievements, and then indented under each of those are the settings for that
individual achievement.

Here's an example achievements section from Brooks & Dunn:

.. code-block:: mpf-config

   ##! mode: mode1
   achievements:
     world_tour:
       show_tokens:
         leds: l_world_tour
       show_when_selected: flash
       show_when_started: flash
       show_when_completed: on
       events_when_started: start_world_tour_mode
       restart_after_stop_possible: true
       events_when_completed: rotate_mission_rotator, light_mission_select
       complete_events: world_tour_success
       enable_events: world_tour_fail, ball_will_end
     money_bags:
       show_tokens:
         leds: l_money_bags
       show_when_selected: flash
       show_when_started: flash
       show_when_completed: on
       events_when_started: start_money_bags_mode
       restart_after_stop_possible: true
       events_when_completed: rotate_mission_rotator, light_mission_select
       complete_events: money_bags_success
       enable_events: money_bags_fail, ball_will_end
     music_awards:
       show_tokens:
         leds: l_music_awards
       show_when_selected: flash
       show_when_started: flash
       show_when_completed: on
       events_when_started: start_music_awards_mode
       restart_after_stop_possible: true
       complete_events: music_awards_success
       events_when_completed: rotate_mission_rotator, light_mission_select
       enable_events: music_awards_fail, ball_will_end
     jukebox:
       show_tokens:
         leds: l_jukebox_insert
       show_when_selected: flash
       show_when_started: flash
       show_when_completed: on
       events_when_started: start_jukebox_mode
       restart_after_stop_possible: true
       events_when_completed: rotate_mission_rotator, light_mission_select
       complete_events: jukebox_success
       enable_events: jukebox_fail, ball_will_end
     play_poker:
       show_tokens:
         leds: l_play_poker
       show_when_selected: flash
       show_when_started: flash
       show_when_completed: on
       events_when_started: start_play_poker_mode
       restart_after_stop_possible: true
       events_when_completed: rotate_mission_rotator, light_mission_select
       complete_events: play_poker_success
       enable_events: play_poker_fail, ball_will_end

More examples:

* :doc:`/cookbook/TAF_mansion_awards`
* :doc:`/examples/achievement/index`

Shows
-----

The ``show_when_xxx`` settings control which show is played when this achievement
switches to a new state.

Note that whatever show was playing from the previous state will be stopped.

Also, any tokens configured in the ``show_tokens:`` section will be passed to
the show here.

Events posted by achievements
-----------------------------

You can configure achievements to post certain events when they change state.

Note that all achievements will by default post events in the form
:doc:`/events/achievement_achievement_state_state` when they change state. The events
listed below as ``events_when_xxx``, if defined, will replace the default event.

Control Events
--------------

The following ``xxx_events`` settings specify which MPF events cause this
achievement to move to a new state.

.. config


Optional settings
-----------------

The following sections are optional in the ``achievements:`` section of your config. (If you don't include them, the default will be used).

complete_events:
~~~~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

Events in this list, when posted, cause this achievement to switch to its
"completed" state. This must be in the "started" state in order to be moved
to the "completed" state when these events post.   These events will also
cause the achievement to play the show defined in the ``show_when_completed:``
setting and to emit (post) events in the ``events_when_completed:`` setting.

disable_events:
~~~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

Events in this list, when posted, cause this achievement to switch to its
"disabled" state. These events will also cause the achievement to play the
show defined in the ``show_when_disabled:`` setting and to emit (post) events
in the ``events_when_disabled:`` setting.

enable_events:
~~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

Events in this list, when posted, cause this achievement to switch to its
"enabled" state. These events will also cause the achievement to play the
show defined in the ``show_when_enabled:`` setting and to emit (post) events
in the ``events_when_enabled:`` setting.

enable_on_next_ball_when_enabled:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``true``

If True/Yes, this achievement will stay "enabled" when the next ball starts if
it was enabled when the last ball ended. If False/No, this achivement will be
changed to "disabled" when the next ball starts.

This is similar to the ``restart_on_next_ball_when_started:`` event from above,
except it applies to the "enabled" state instead of the "started" state.

This setting will also play the ``show_when_enabled:`` show and post the
``events_when_enabled:`` events when re-enabling, but will not play or post
anything when disabling.

events_when_completed:
~~~~~~~~~~~~~~~~~~~~~~
List of one (or more) events. Those will be posted by the device. Defaults to empty.

A single event, or a list of events, that will be posted when this achievement is complete.

events_when_disabled:
~~~~~~~~~~~~~~~~~~~~~
List of one (or more) events. Those will be posted by the device. Defaults to empty.

A single event, or a list of events, that will be posted when this achievement is disabled.

events_when_enabled:
~~~~~~~~~~~~~~~~~~~~
List of one (or more) events. Those will be posted by the device. Defaults to empty.

A single event, or a list of events, that will be posted when this achievement
is enabled.

events_when_selected:
~~~~~~~~~~~~~~~~~~~~~
List of one (or more) events. Those will be posted by the device. Defaults to empty.

A single event, or a list of events, that will be posted when this
achievement is selected.

events_when_started:
~~~~~~~~~~~~~~~~~~~~
List of one (or more) events. Those will be posted by the device. Defaults to empty.

A single event, or a list of events, that will be posted when this achievement is started.

events_when_stopped:
~~~~~~~~~~~~~~~~~~~~
List of one (or more) events. Those will be posted by the device. Defaults to empty.

A single event, or a list of events, that will be posted when this achievement is stopped.

reset_events:
~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

Events in this list, when posted, cause this achievement to reset back to its
default state (which will either be "disabled" or, if you have
``start_enabled: true``, "enabled")

restart_after_stop_possible:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``true``

Is it possible to restart this achievement after it's been stopped?

restart_on_next_ball_when_started:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

If True/Yes, then this achievement will stay in the "started" state when the
player's next ball starts if it was in the "started" state when the previous
ball ended. This is useful if you want to restart a mode that was running when
the ball ended.

Note that this restart will also play the ``show_when_started:`` show, and it
will also post the ``events_when_started:`` events.

If False/No, this achievement's state will change from "started" to "stopped"
when the next ball starts. This will *not* play the ``show_when_stopped:`` show and
it will *not* post the ``events_when_stopped:`` events.

select_events:
~~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

Events in this list, when posted, cause this achievement to switch to its
"selected" state. These events will also cause the achievement to play the
show defined in the ``show_when_selected:`` setting and to emit (post) events
in the ``events_when_selected:`` setting.

Note that the "selected" state, in MPF, is used to describe an achievement
that is currently selected ("highlighted" or "lit") and available to be
started. This would typically be tied to a show (via the
``show_when_selected:`` setting) that causes a light or LED to flash.

show_tokens:
~~~~~~~~~~~~
One or more sub-entries. Each in the format of ``string`` : ``string``

This is an indented list of key/value pairs for the
:doc:`show tokens </shows/tokens>` that will be sent to the shows that are
played when this achievement changes state. (See the settings called
"show_when_XXX" further down in this documentation.)

show_when_completed:
~~~~~~~~~~~~~~~~~~~~
Single value, type: string name of a :doc:`shows <shows>` device. Defaults to empty.

Name of the show that will be started when this achievement has been completed.

show_when_disabled:
~~~~~~~~~~~~~~~~~~~
Single value, type: string name of a :doc:`shows <shows>` device. Defaults to empty.

Name of the show that will be started when this achievement has been disabled.

show_when_enabled:
~~~~~~~~~~~~~~~~~~
Single value, type: string name of a :doc:`shows <shows>` device. Defaults to empty.

Name of the show that will be started when this achievement has been enabled.

show_when_selected:
~~~~~~~~~~~~~~~~~~~
Single value, type: string name of a :doc:`shows <shows>` device. Defaults to empty.

Name of the show that will be started when this achievement has been selected.

show_when_started:
~~~~~~~~~~~~~~~~~~
Single value, type: string name of a :doc:`shows <shows>` device. Defaults to empty.

Name of the show that will be started when this achievement has been started.

show_when_stopped:
~~~~~~~~~~~~~~~~~~
Single value, type: string name of a :doc:`shows <shows>` device. Defaults to empty.

Name of the show that will be started when this achievement has been stopped.

start_enabled:
~~~~~~~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Defaults to empty.

Whether this achievment is enabled or disabled when it is first loaded.

start_events:
~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

Default: ``None``

Events in this list, when posted, cause this achievement to switch to its
"started" state. These events will also cause the achievement to play the
show defined in the ``show_when_started:`` setting and to emit (post) events
in the ``events_when_started:`` setting.

stop_events:
~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

Default: ``None``

Events in this list, when posted, cause this achievement to switch to its
"stopped" state. These events will also cause the achievement to play the
show defined in the ``show_when_stopped:`` setting and to emit (post) events
in the ``events_when_stopped:`` setting.

sync_ms:
~~~~~~~~
Single value, type: ``integer``. Defaults to empty.

A sync_ms value used for any shows which are started by this achievement. See the
:doc:`full sync_ms documentation for details </shows/sync_ms>`.

unselect_events:
~~~~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

.. todo:: :doc:`/about/help_us_to_write_it`

console_log:
~~~~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level for the console log for this device.

debug:
~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

Enables debug logging.

file_log:
~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level for the file log for this device.

label:
~~~~~~
Single value, type: ``string``. Default: ``%``

Name of this device in service mode.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Defaults to empty.

Not used.


Related How To guides
---------------------

* :doc:`/game_logic/achievements/achievement_groups`
* :doc:`/game_logic/achievements/index`
