---
title: Config File Reference Index
---

# Config File Reference Index

This section contains details about every possible entry you can use in
your YAML config files. Each entry also has information about whether
it's valid in your machine-wide config, a mode-specific config, or
both.

## Instructions

As you dig into the specific settings for individual config sections,
it's important to understand how various settings mentioned in the
reference are used:

* [Instructions](instructions/index.md)

## Index of config sections

Here's a list of every single config section from both MPF and the
MPF-MC. Some of these are valid only in machine-wide configs, and others
only work in mode config files. (And some are valid in both.) The detail
page for each setting indicated which type of config file it's valid
in.


### Config Players:

For more info, see: ["Config Players" Reference Index](config_players/index.md)

These are a special type of MPF device that allow you to listen for events
and perform actions in response. Each config player is named for the type
of device that you control with it. For example, `light_player` is a config
player that lets you set light colors in response to events.

* [blinkenlight_player:](blinkenlight_player.md)
* [coil_player:](coil_player.md)
* [display_light_player:](display_light_player.md)
* [event_player:](event_player.md)
* [flasher_player:](flasher_player.md)
* [light_player:](light_player.md)
* [queue_event_player:](queue_event_player.md)
* [queue_relay_player:](queue_relay_player.md)
* [random_event_player:](random_event_player.md)
* [score_queue_player:](score_queue_player.md)
* [segment_display_player:](segment_display_player.md)
* [show_player:](show_player.md)
* [slide_player:](slide_player.md)
* [sound_player:](sound_player.md)
* [variable_player:](variable_player.md)
* [widget_player:](widget_player.md)

### Devices:

These are generally MPF device configs, or other very general settings.

* [accelerometers:](accelerometers.md)
* [accruals:](accruals.md)
* [achievements:](achievements.md)
* [achievement_groups:](achievement_groups.md)
* [assets:](assets.md)
* [autofire_coils:](autofire_coils.md)
* [ball_devices:](ball_devices.md)
* [ball_holds:](ball_holds.md)
* [ball_locks:](ball_locks.md)
* [ball_saves:](ball_saves.md)
* [bcp:](bcp.md)
* [bcp_connection:](bcp_connection.md)
* [bcp_server:](bcp_server.md)
* [blinkenlights:](blinkenlights.md)
* [coil_overwrites:](coil_overwrites.md)
* [coils:](coils.md)
* [color_correction_profile:](color_correction_profile.md)
* [combo_switches:](combo_switches.md)
* [config:](config.md)
* [counters:](counters.md)
* [counter_control_events:](counter_control_events.md)
* [custom_code:](custom_code.md)
* [displays:](displays.md)
* [digital_outputs:](digital_outputs.md)
* [diverters:](diverters.md)
* [dmds:](dmds.md)
* [drop_target_banks:](drop_target_banks.md)
* [drop_targets:](drop_targets.md)
* [dual_wound_coils:](dual_wound_coils.md)
* [extra_balls:](extra_balls.md)
* [extra_ball_groups:](extra_ball_groups.md)
* [flippers:](flippers.md)
* [game:](game.md)
* [hardware:](hardware.md)
* [info_lights:](info_lights.md)
* [kickbacks:](kickbacks.md)
* [light_stripes:](light_stripes.md)
* [light_rings:](light_rings.md)
* [lights:](lights.md)
* [light_segment_displays:](light_segment_displays.md)
* [light_settings:](light_settings.md)
* [logic_blocks:](logic_blocks.md)
* [machine:](machine.md)
* [machine_vars:](machine_vars.md)
* [magnets:](magnets.md)
* [mode:](mode.md)
* [mode_settings:](mode_settings.md)
* [modes:](modes.md)
* [motors:](motors.md)
* [multiball_locks:](multiball_locks.md)
* [multiballs:](multiballs.md)
* [mpf:](mpf.md)
* [named_colors:](named_colors.md)
* [player_vars:](player_vars.md)
* [playfield_transfers:](playfield_transfers.md)
* [playfields:](playfields.md)
* [plugins:](plugins.md)
* [psus:](psus.md)
* [rgb_dmds:](rgb_dmds.md)
* [score_queues:](score_queues.md)
* [score_reel_groups:](score_reel_groups.md)
* [score_reels:](score_reels.md)
* [segment_displays:](segment_displays.md)
* [servos:](servos.md)
* [sequences:](sequences.md)
* [sequence_shots:](sequence_shots.md)
* [shakers:](shakers.md)
* [shot_control_events:](shot_control_events.md)
* [shot_groups:](shot_groups.md)
* [shot_profiles:](shot_profiles.md)
* [shots:](shots.md)
* [show_pools:](show_pools.md)
* [shows:](shows.md)
* [spinners:](spinners.md)
* [speedometers:](speedometers.md)
* [state_machines:](state_machines.md)
* [steppers:](steppers.md)
* [switch_overwrites:](switch_overwrites.md)
* [switches:](switches.md)
* [text_ui:](text_ui.md)
* [timed_switches:](timed_switches.md)
* [timers:](timers.md)

### MPF Built-in configs

These configs relate to the optional modes that MPF provides that allow you to
have standard features you would expect from a pinball machine with minimal configuration,
such as attract mode, tilt handling, and credit management. Many of these features
depend on `tags` set on related devices, such as `start` on the start button switch.

* [auditor:](auditor.md)
* [bonus (mode_settings:)](bonus.md)
* [credits:](credits.md)
* [high_score:](high_score.md)
* [logging:](logging.md)
* [settings:](settings.md)
* [switch_player:](switch_player.md)
* [tilt:](tilt.md)

### Platform-specific Configs

While the previous configs listed are generic across the many platforms
provided by MPF, all of these platforms need their own configurations,
and some offer additional features on top of the standard devices already listed.

* [fadecandy:](fadecandy.md)
* [fast:](fast.md)
* [fast_coils:](fast_coils.md)
* [fast_switches:](fast_switches.md)
* [hardware_sound_player:](hardware_sound_player.md)
* [hardware_sound_systems:](hardware_sound_systems.md)
* [kivy_config:](kivy_config.md)
* [lisy:](lisy.md)
* [mypinballs:](mypinballs.md)
* [open_pixel_control:](open_pixel_control.md)
* [opp:](opp.md)
* [opp_coils:](opp_coils.md)
* [osc:](osc.md)
* [p_roc:](p_roc.md)
* [pd_led_boards:](pd_led_boards.md)
* [pin2dmd:](pin2dmd.md)
* [pkone:](pkone.md)
* [pololu_maestro:](pololu_maestro.md)
* [pololu_tic:](pololu_tic.md)
* [raspberry_pi:](raspberry_pi.md)
* [rpi_dmd:](rpi_dmd.md)
* [servo_controllers:](servo_controllers.md)
* [smart_virtual:](smart_virtual.md)
* [smartmatrix:](smartmatrix.md)
* [snux:](snux.md)
* [spi_bit_bang:](spi_bit_bang.md)
* [spike:](spike.md)
* [spike_node:](spike_node.md)
* [step_stick_stepper_settings:](step_stick_stepper_settings.md)
* [system11:](system11.md)
* [tic_stepper_settings:](tic_stepper_settings.md)
* [trinamics_steprocker:](trinamics_steprocker.md)
* [twitch_client:](twitch_client.md)
* [virtual_platform_start_active_switches:](virtual_platform_start_active_switches.md)
* [virtual_segment_display_connector:](virtual_segment_display_connector.md)

### Legacy MPF-MC Configs

Prior to MPF 0.80, the standard media controller was "mpf-mc". The
MPF config files were used to configure the various audio and video
effects played on the machine alongside the pinball device and mode
configs listed above. Developers upgrading from pre-0.80 to GMC will
need to replace the features implemented in these configs with
equivalents in Godot or a custom media controller.

`slide_player`, `sound_player`, and `widget_player` are listed in the
"Config Players" section above, and they are very similar between pre-GMC
and GMC eras of media controller.

* [animations:](animations.md)
* [bitmap_fonts:](bitmap_fonts.md)
* [image_pools:](image_pools.md)
* [images:](images.md)
* [keyboard:](keyboard.md)
* [mc_custom_code:](mc_custom_code.md)
* [mc_scriptlets:](mc_scriptlets.md)
* [mpf-mc:](mpf-mc.md)
* [playlist_player:](playlist_player.md)
* [playlists:](playlists.md)
* [slides:](slides.md)
* [sound_ducking:](sound_ducking.md)
* [sound_loop_player:](sound_loop_player.md)
* [sound_loop_sets:](sound_loop_sets.md)
* [sound_marker:](sound_marker.md)
* [sound_pools:](sound_pools.md)
* [sound_system_tracks:](sound_system_tracks.md)
* [sound_system:](sound_system.md)
* [sounds:](sounds.md)
* [text_strings:](text_strings.md)
* [track_player:](track_player.md)
* [videos:](videos.md)
* [video_pools:](video_pools.md)
* [widget_styles:](widget_styles.md)
* [widgets:](widgets.md)
* [window:](window.md)

### Deprecated Config Reference

These configs were available in earlier versions of MPF (generally pre-0.56), but are no longer supported.
See the individual pages for information on their replacements.

* [flashers:](flashers.md)
* [gi_player:](gi_player.md)
* [gis:](gis.md)
* [led_player:](led_player.md)
* [leds:](leds.md)
* [matrix_lights:](matrix_lights.md)
* [scriptlets:](scriptlets.md)
