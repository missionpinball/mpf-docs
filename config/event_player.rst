event_player:
=============

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`shows </shows/index>`                                       | **YES** |
+----------------------------------------------------------------------------+---------+

.. note:: This section can also be used in a show file in the ``events:`` section of a step.

You can use the ``event_player:`` section of your config files to cause
additional events to be automatically posted when a specific event is
posted. The event_player can be thought of as a really simple way to
implement game logic. (e.g. "When this happens, do this.")

If you add
this section to your machine-wide config file, the entries here will
always be active. If you enter it into a mode-specific config file,
entries will only be active while that mode is active. 

Basic Event Playing
-------------------

::

    event_player:
        ball_starting:
            cmd_flippers_enable
            cmd_autofire_coils_enable
            cmd_drop_targets_reset
        ball_ending:
            cmd_flippers_disable
            cmd_autofire_coils_disable
        tilt:
            cmd_flippers_disable
            cmd_autofire_coils_disable
        slam_tilt:
            cmd_flippers_disable
            cmd_autofire_coils_disable

The event player settings above will post the events
*cmd_flippers_enable*, *cmd_autofire_coils_enable*, and
*cmd_drop_targets_reset* when the *ball_starting* event is posted.
Similarly they will post events to disable the flippers and autofire
coils when ball end and tilt events are posted.

To use this, simply
create an ``event_player:`` entry in your config file. Then create sub-
entries for each event you want to trigger other events, and add a
list of one or more events that should be posted automatically under
each trigger event.

Remember that you can create this event_player:
section in either your machine-wide or in mode-specific config files.
For example, if you want a target called "upper" to reset when a mode
called "shoot_here" starts, you could create an entry like this in the
shoot here mode's shoot_here.yaml mode configuration file:

::

    event_player:
      mode_shoot_here_started:
        cmd_upper_target_reset

Conditional Event Playing
-------------------------

Events in the event player can be conditional, to allow precise control over
when an event is played:

::

   event_player:
       mode_base_started{current_player.score>10000}:
         start_mode_superbonusround
         play_show_richy_rich
       start_mode_battle{device.achievements.ironthrone.state!="completed"}:
         start_mode_choose_battle
       start_mode_battle{device.achievements.ironthrone.state=="completed"}:
         start_mode_victory_lap

In the above example, both "start_mode_superbonusround" and "play_show_richy_rich" will
only be posted if the player's score is over 10,000 when base mode starts. And if the
battle mode is started, either "start_mode_choose_battle" or "start_mode_victory_lap"
will be posted depending on whether the *ironthrone* achievement has been completed.

Conditions can also be applied to events within a list, to allow one event to
trigger a variable number of handlers:

::

   event_player:
      reenable_nonrecruit_modes:
         - start_mode_shadowbroker_base
         - start_mode_n7_assignments
         - start_mode_overlordlight{device.achievements.collectorship.state!="complete"}
         - start_mode_arrival{device.achievements.collectorship.state=="complete"}
         - start_mode_shopping{current_player.cash>=1000}

In the above example, both "start_mode_shadowbroker_base" and "start_mode_n7_assignments" will
be posted every time. One of either "start_mode_overlord" or "start_mode_arrival" will be posted,
depending on whether the player has completed the collectorship achievement. And if the player_var
"cash" is high enough, "start_mode_shopping" will also be posted. 

In many cases, conditions can be applied to either the triggering event or the handling event.
For more information and examples of conditions, see :doc:`conditional events </events/overview/conditional>`.
