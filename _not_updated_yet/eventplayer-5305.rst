
You can use the `event_player:` section of your config files to cause
additional events to be automatically posted when a specific event is
posted. The event_player can be thought of as a really simple way to
implement game logic. (e.g. "When this happens, do this.")If you add
this section to yourmachine-wide config file, the entries herewill
always be active. If you enter it into a mode-specific config file,
entrieswill only be active while that mode is active. This sectioncan
be used in your machine-wide config files. This sectioncanbe used in
mode-specific config files. Here's an example:


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
coils when ball end and tilt events are posted. To use this, simply
create an `event_player:` entry in your config file. Then create sub-
entries for each event you want to trigger other events, and add a
list of one or more events that should be posted automatically under
each trigger event. Remember that you can create this event_player:
section in either your machine-wide or in mode-specific config files.
For example, if you want a target called "upper" to reset when a mode
called "shoot_here" starts, you could create an entry like this in the
shoot here mode's shoot_here.yaml mode configuration file:


::

    
    event_player:
      mode_shoot_here_started:
        cmd_upper_target_reset




