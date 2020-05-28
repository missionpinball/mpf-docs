achievement_groups:
===================

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **NO**  |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

.. overview

The ``achievements_groups:`` section of your config is where you configure
grouping of multiple
:doc:`player-based "achievement" tracking </game_logic/achievements/index>`.

Like most things in MPF configs, the highest-level entries in the
``achievement_groups:`` section of your config are the names of the individual
achievement group, and then indented under each of those are the settings for
that group.

Here's an example achievement_groups section from Brooks & Dunn. (This is
related to the example in the achievements config documentation.)

.. code-block:: mpf-config

    ##! mode: mode1
    #! # create some empty achievements for the group
    #! achievements:
    #!   world_tour:
    #!     enable_events: world_tour_fail, ball_will_end
    #!   money_bags:
    #!     enable_events: money_bags_fail, ball_will_end
    #!   music_awards:
    #!     enable_events: music_awards_fail, ball_will_end
    #!   jukebox:
    #!     enable_events: jukebox_fail, ball_will_end
    #!   play_poker:
    #!     enable_events: play_poker_fail, ball_will_end
    achievement_groups:
      my_group:
        achievements: world_tour, money_bags, music_awards, jukebox, play_poker
        enable_events: enable_mission_selection
        start_selected_events: shot_lower_vuk_from_playfield_hit
        select_random_achievement_events: rotate_mission_rotator
        events_when_enabled: mission_rotator_ready
        rotate_right_events: sw_toggle
        show_tokens:
          leds: l_begin_round
        show_when_enabled: flash

More examples:

* :doc:`/cookbook/TAF_mansion_awards`
* :doc:`/examples/achievement/index`

.. config


Required settings
-----------------

The following sections are required in the ``achievement_groups:`` section of your config:

achievements:
~~~~~~~~~~~~~
List of one (or more) values, each is a type: string name of a :doc:`achievements <achievements>` device. Defaults to empty.

This is a list of the achievements (from the ``achievements:`` section of your
mode config) that make up this group. The order here defines the order
individual achievements are rotated in via the ``rotate_right_events:`` and/or
``rotate_left_events:`` settings.


Optional settings
-----------------

The following sections are optional in the ``achievement_groups:`` section of your config. (If you don't include them, the default will be used).

allow_selection_change_while_disabled:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

Controls whether the currently selected achievement can be changed when the
achievement group is disabled. If False/No, then the rotate and select
random events will have no effect when the group is disabled.

auto_select:
~~~~~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

If True, this achievement group will automatically ensure that one of its member
achievements is always selected. The selected achievement will be chosen at random
from all the achievements in the "enabled" states (and the "stopped" states if
``restart_after_stop_possible:`` is set to True).

disable_events:
~~~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

Events in this list, when posted, disable this achievement group.
These events will also cause the
achievements to play the show defined in their ``show_when_disabled:`` setting
and to emit (post) events in their ``events_when_disabled:`` settings.

disable_while_achievement_started:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``true``

If True, this achievement will automatically disable itself when any of its
member achievements are in the "started" states. This is the default behavior
because an achievement group is typically used to select an achievement to run,
and while an achievement is running, you usually want to disable the selection
process for the next achievement.

enable_events:
~~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

Events in this list, when posted, will enable this achievement group. This
will play the ``show_when_enabled:`` and will post events in the
``events_when_enabled:`` settings.

This will also check to see if all the member achievements are complete,
it will check to see if there are no more enabled achievements, and it will
update the selected achievement.

Starting the selected achievement only works if the group is enabled. In
other words, if something has to be "lit" before an achievement can start,
then that is done via the group's "enable" functionality.

enable_while_no_achievement_started:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``true``

If True, this achievement will automatically enable itself when none of its
member achievements are in the "started" states. This is the default behavior
because an achievement group is typically used to select an achievement to run,
so when none are running, you want to enable the group so that the next
achievement can be selected.

events_when_all_completed:
~~~~~~~~~~~~~~~~~~~~~~~~~~
List of one (or more) events. Those will be posted by the device. Defaults to empty.

A single event, or a list of events, that will be posted when all the
achievements in this group are in the "completed" state. This is useful for
posting events to start a wizard mode, for example.

events_when_enabled:
~~~~~~~~~~~~~~~~~~~~
List of one (or more) events. Those will be posted by the device. Defaults to empty.

A single event, or a list of events, that will be posted when this achievement
group is enabled.

events_when_no_more_enabled:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
List of one (or more) events. Those will be posted by the device. Defaults to empty.

A single event, or a list of events, that will be posted when one of the events
in the ``select_random_achievement:`` is posted but there are no more available
achievements to be selected.

rotate_left_events:
~~~~~~~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

Default: ``None``

Same as ``rotate_right_events:``, but it rotates the selected achievement in the
opposite direction.

rotate_right_events:
~~~~~~~~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

Default: ``None``

Causes the states of the available achievements in this group to be rotated
to the right.

Note that the ``allow_selection_change_while_disabled:`` controls whether
these events will work when the achievement group is disabled.

This is used to "switch" the current selected achievement. For example, many
games have main achievements you need to complete to get to wizard mode.
Completed achievements have a light that's solid on, available (enabled)
achievements have a light that's off (since they're not yet complete but
available to be played), and the current selected achievement has a light that's
flashing (indicating that it's the next one to be played).

Then when you hit a slingshot or pop bumper, the currently selected (flashing)
achievement changes, but you only want to rotate with other achievements that
are enabled (available but not yet complete).

So if this is the current state:

* Mission 1: completed
* Mission 2: selected
* Mission 3: enabled
* Mission 4: enabled
* Mission 5: enabled

And then one of the ``rotate_right_events:`` is posted (like from a pop bumper
hit), the new list would look like this:

* Mission 1: completed
* Mission 2: enabled
* Mission 3: selected
* Mission 4: enabled
* Mission 5: enabled

Notice that the "selected" state moved from Mission 2 to Mission 3, and the
completed state of Mission 1 did not change.

Even though these are called "rotate" events, what really happens is that when
this rotation occurs, the previously selected achievement changes from
"selected" to "enabled", and the newly selected achievement changes from
"enabled" to "selected". Both achievements will stop their current shows and
play the shows associated with their new states, and both will post the events
associted with their new states.

Note that if you want to select a random achievement instead of the next one
on the list, you can use a ``select_random_achievement_events:`` event instead.

select_random_achievement_events:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

Events in this list, when posted, will randomly pick one of the available
achievements and change it to its "selected" state. This is useful when a game
is starting and you want one of the available achievements to start in a selected
state. (e.g. pick a random mission to be highlighted.)

Note that the ``allow_selection_change_while_disabled:`` controls whether
these events will work when the achievement group is disabled.

The "available" achievements which could be chosen here include achievements
that are one of the following:

* enabled
* selected
* stopped (if the achievement's ``restart_after_stop_possible:`` is true/yes

An example of this would be in Attack From Mars, where the next country is
randomly chosen (selected) after you default the saucer for the previous
country.

If there are no more available events to be selected, then the events in
``events_when_no_more_enabled:`` are posted.

Note that if you want to always select a certain achievement (instead of
randomly picking one), then you can just set that particular achievement's
``select_events:`` entry rather than using this random selecting setting.

show_tokens:
~~~~~~~~~~~~
One or more sub-entries. Each in the format of ``string`` : ``string``

This is an indented list of key/value pairs for the
:doc:`show tokens </shows/tokens>` that will be sent to the shows that are
played when this achievement changes state.

Note that you can configure ``show_tokens:`` at the group level (here) or the
individual achievement level. That's done for convenience, and in practical use,
you'd just configure the show tokens in one place.

show_when_enabled:
~~~~~~~~~~~~~~~~~~
Single value, type: string name of a :doc:`shows <shows>` device. Defaults to empty.

Name of the show that will be started when this achievement group has been
enabled.
Also, any tokens configured in the ``show_tokens:`` section will be passed to
the show here.

start_selected_events:
~~~~~~~~~~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

Default: ``None``

Events in this list, when posted, cause any achievements in this group that are
in the "selected" state to switch to their "started" state. (Typically there
would only be a single achievement in the group that's "selected" at any time,
but you could have more than one.)

These events only work if the achievement group is enabled.

When the individual achievements change from "selected" to "started", they will
play their ``show_when_started:`` shows and post their
``events_when_started:`` events.

console_log:
~~~~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level for the console log for this device.

debug:
~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

Set this to true to see additional debug output. This might impact the performance of MPF.

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

Not used


Related How To guides
---------------------

* :doc:`/game_logic/achievements/achievement_groups`
* :doc:`/game_logic/achievements/index`
