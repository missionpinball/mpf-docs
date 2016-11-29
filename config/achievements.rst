achievements:
=============

*Config file section*

.. versionchanged:: 0.32

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **NO**  |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

The ``achievements:`` section of your config is where you configure
:doc:`player-based "achievement" tracking </game_logic/achievements/index>`.

Like most things in MPF configs, the highest-level entries in the
``achievements:`` section of your config are the names of the individual
achievements, and then indented under each of those are the settings for that
individual achievement.

Here's an example achievements section from Brooks & Dunn:

::

   achievements:
     world_tour:
       show_tokens:
         leds: l_world_tour
       show_when_selected: flash
       show_when_started: flash
       show_when_completed: on
       events_when_started: start_world_tour_mode
       restart_after_stop_possible: true
       start_enabled: True
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
       start_enabled: True
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
       start_enabled: True
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
       start_enabled: True
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
       start_enabled: True
       events_when_completed: rotate_mission_rotator, light_mission_select
       complete_events: play_poker_success
       enable_events: play_poker_fail, ball_will_end

General Settings
----------------

The following settings are used to configure each achievement. Since
achievements are so flexible, these are all optional, though you need to use
some of them or your achievement won't do anything. :)

show_tokens:
~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``str``. Default: ``None``

This is an indented list of key/value pairs for the
:doc:`show tokens </shows/tokens>` that will be sent to the shows that are
played when this achievement changes state. (See the settings called
"show_when_XXX" further down in this documentation.)

start_enabled:
~~~~~~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

Controls whether this achievement will be initially set to the "enabled" state.
If this setting is false/no, then this achievement will be set to the "disabled"
state initially.

This setting controls the initial state of the achievement when the mode
containing this achievement is started, as well as the state the achievement
switches to when its reset.

restart_after_stop_possible:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``True``

Is it possible to restart this achievement after it's been stopped?

restart_on_next_ball_when_started:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``True``

If True/Yes, then this achievement is set to the "started" state when the
player's next ball starts if it was in the "started" state when the previous
ball ended. This is useful if you want to restart a mode that was running when
the ball ended.

Note that this restart will also play the ``show_when_started:`` show, and it
will also post the ``events_when_started:`` events.

enable_on_next_ball_when_enabled:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``True``

If a ball ends when this achievement is enabled, should it automatically enable itself again
when the next ball starts? This is similar to the
``restart_on_next_ball_when_started:`` event from above, except it applies to
the "enabled" state instead of the "started" state.

This setting will also play the ``show_when_enabled:`` show, and it
will also post the ``events_when_enabled:`` events.

debug:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

Enables debug logging.

Control Events
--------------

The following settings specify which MPF events cause this achievement to move
to a new state.

enable_events:
~~~~~~~~~~~~~~
One or more sub-entries, either as a list of events, or key/value pairs of
event names and delay times. (See the
:doc:`/config/instructions/device_control_events` documentation for details
on how to enter settings here.

Default: ``None``

Events in this list, when posted, cause this achievement to switch to its
"enabled" state. These events will also cause the achievement to play the
show defined in the ``show_when_enabled:`` setting and to emit (post) events
in the ``events_when_enabled:`` setting.

select_events:
~~~~~~~~~~~~~~

.. versionadded:: 0.32

One or more sub-entries, either as a list of events, or key/value pairs of
event names and delay times. (See the
:doc:`/config/instructions/device_control_events` documentation for details
on how to enter settings here.

Default: ``None``

Events in this list, when posted, cause this achievement to switch to its
"selected" state. These events will also cause the achievement to play the
show defined in the ``show_when_selected:`` setting and to emit (post) events
in the ``events_when_selected:`` setting.

Note that the "selected" state, in MPF, is used to describe an achievement
that is currently selected ("highlighted" or "lit") and available to be
started. This would typically be tied to a show (via the
``show_when_selected:`` setting) that causes a light or LED to flash.

start_events:
~~~~~~~~~~~~~
One or more sub-entries, either as a list of events, or key/value pairs of
event names and delay times. (See the
:doc:`/config/instructions/device_control_events` documentation for details
on how to enter settings here.

Default: ``None``

Events in this list, when posted, cause this achievement to switch to its
"started" state. These events will also cause the achievement to play the
show defined in the ``show_when_started:`` setting and to emit (post) events
in the ``events_when_started:`` setting.

complete_events:
~~~~~~~~~~~~~~~~
One or more sub-entries, either as a list of events, or key/value pairs of
event names and delay times. (See the
:doc:`/config/instructions/device_control_events` documentation for details
on how to enter settings here.

Default: ``None``

Events in this list, when posted, cause this achievement to switch to its
"completed" state. These events will also cause the achievement to play the
show defined in the ``show_when_completed:`` setting and to emit (post) events
in the ``events_when_completed:`` setting.

disable_events:
~~~~~~~~~~~~~~~
One or more sub-entries, either as a list of events, or key/value pairs of
event names and delay times. (See the
:doc:`/config/instructions/device_control_events` documentation for details
on how to enter settings here.

Default: ``None``

Events in this list, when posted, cause this achievement to switch to its
"disabled" state. These events will also cause the achievement to play the
show defined in the ``show_when_disabled:`` setting and to emit (post) events
in the ``events_when_disabled:`` setting.

stop_events:
~~~~~~~~~~~~
One or more sub-entries, either as a list of events, or key/value pairs of
event names and delay times. (See the
:doc:`/config/instructions/device_control_events` documentation for details
on how to enter settings here.

Default: ``None``

Events in this list, when posted, cause this achievement to switch to its
"stopped" state. These events will also cause the achievement to play the
show defined in the ``show_when_stopped:`` setting and to emit (post) events
in the ``events_when_stopped:`` setting.

reset_events:
~~~~~~~~~~~~~
One or more sub-entries, either as a list of events, or key/value pairs of
event names and delay times. (See the
:doc:`/config/instructions/device_control_events` documentation for details
on how to enter settings here.

Default: ``None``

Events in this list, when posted, cause this achievement to reset back to its
default state (which will either be "disabled" or, if you have
``start_enabled: true``, "enabled")

Events posted by achievements
-----------------------------

You can configure achievements to post certain events when they change state.

Note that all achievements will always post events in the form
:doc:`/events/achievement_name_state_state` when they change state. The events
listed below are in additional to that event.

events_when_enabled:
~~~~~~~~~~~~~~~~~~~~
:doc:`List </config/instructions/lists>` of one (or more) names of events.
Default: ``None``.

A single event, or a list of events, that will be posted when this achievement
is enabled.

events_when_selected:
~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 0.32

:doc:`List </config/instructions/lists>` of one (or more) names of events.
Default: ``None``.

A single event, or a list of events, that will be posted when this
achievement is selected.

events_when_started:
~~~~~~~~~~~~~~~~~~~~
:doc:`List </config/instructions/lists>` of one (or more) names of events.
Default: ``None``.

A single event, or a list of events, that will be posted when this achievement is started.

events_when_completed:
~~~~~~~~~~~~~~~~~~~~~~
:doc:`List </config/instructions/lists>` of one (or more) names of events.
Default: ``None``.

A single event, or a list of events, that will be posted when this achievement is complete.

events_when_disabled:
~~~~~~~~~~~~~~~~~~~~~
:doc:`List </config/instructions/lists>` of one (or more) names of events.
Default: ``None``.

A single event, or a list of events, that will be posted when this achievement is disabled.

events_when_stopped:
~~~~~~~~~~~~~~~~~~~~
:doc:`List </config/instructions/lists>` of one (or more) names of events.
Default: ``None``.

A single event, or a list of events, that will be posted when this achievement is stopped.

Shows
-----

The following settings control which show is played when this achievement
switches to a new state.

Note that whatever show was playing from the previous state will be stopped.

Also, any tokens configured in the ``show_tokens:`` section will be passed to
the show here.

show_when_enabled:
~~~~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``None``

Name of the show that will be started when this achievement has been enabled.

show_when_selected:
~~~~~~~~~~~~~~~~~~~

.. versionadded:: 0.32

Single value, type: ``string``. Default: ``None``

Name of the show that will be started when this achievement has been selected.

show_when_started:
~~~~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``None``

Name of the show that will be started when this achievement has been started.

show_when_completed:
~~~~~~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``None``

Name of the show that will be started when this achievement has been completed.

show_when_disabled:
~~~~~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``None``

Name of the show that will be started when this achievement has been disabled.

show_when_stopped:
~~~~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``None``

Name of the show that will be started when this achievement has been stopped.
