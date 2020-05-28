Config file reference
=====================

This section contains details about every possible entry you can use in your
YAML config files. Each entry also has information about whether it's valid in
your machine-wide config, a mode-specific config, or both.


Instructions
------------

As you dig into the specific settings for individual config sections, it's important to understand how various
settings mentioned in the reference are used:

.. toctree::
   :maxdepth: 2

   Instructions <instructions/index>

Index of config sections
------------------------

Here's a list of every single config section from both MPF and the MPF-MC. Some of these are valid only in machine-wide
configs, and others only work in mode config files. (And some are valid in both.) The detail page for each setting
indicated which type of config file it's valid in.

.. toctree::
   :maxdepth: 1

   accelerometers: <accelerometers>
   accruals: <accruals>
   achievements: <achievements>
   achievement_groups: <achievement_groups>
   animations: <animations>
   assets: <assets>
   auditor: <auditor>
   autofire_coils: <autofire_coils>
   ball_devices: <ball_devices>
   ball_holds: <ball_holds>
   ball_locks: <ball_locks>
   ball_saves: <ball_saves>
   bcp: <bcp>
   bcp_connection: <bcp_connection>
   bcp_server: <bcp_server>
   bitmap_fonts: <bitmap_fonts>
   bonus (mode_settings:) <bonus>
   coil_overwrites: <coil_overwrites>
   coil_player: <coil_player>
   coils: <coils>
   color_correction_profile: <color_correction_profile>
   combo_switches: <combo_switches>
   config: <config>
   counters: <counters>
   counter_control_events: <counter_control_events>
   credits: <credits>
   custom_code: <custom_code>
   display_light_player: <display_light_player>
   displays: <displays>
   digital_outputs: <digital_outputs>
   diverters: <diverters>
   dmds: <dmds>
   drop_target_banks: <drop_target_banks>
   drop_targets: <drop_targets>
   dual_wound_coils: <dual_wound_coils>
   event_player: <event_player>
   extra_balls: <extra_balls>
   extra_ball_groups: <extra_ball_groups>
   fadecandy: <fadecandy>
   fast: <fast>
   fast_coils: <fast_coils>
   fast_firmware_update: <fast_firmware_update>
   fast_switches: <fast_switches>
   flasher_player: <flasher_player>
   flashers: <flashers>
   flippers: <flippers>
   game: <game>
   gi_player: <gi_player>
   gis: <gis>
   hardware: <hardware>
   hardware_sound_player: <hardware_sound_player>
   hardware_sound_systems: <hardware_sound_systems>
   high_score: <high_score>
   image_pools: <image_pools>
   images: <images>
   info_lights: <info_lights>
   keyboard: <keyboard>
   kickbacks: <kickbacks>
   kivy_config: <kivy_config>
   led_player: <led_player>
   light_stripes: <light_stripes>
   light_rings: <light_rings>
   lisy: <lisy>
   leds: <leds>
   lights: <lights>
   light_segment_displays: <light_segment_displays>
   light_settings: <light_settings>
   light_player: <light_player>
   logic_blocks: <logic_blocks>
   logging: <logging>
   machine: <machine>
   machine_vars: <machine_vars>
   magnets: <magnets>
   matrix_lights: <matrix_lights>
   mc_custom_code: <mc_custom_code>
   mc_scriptlets: <mc_scriptlets>
   mode: <mode>
   mode_settings: <mode_settings>
   modes: <modes>
   motors: <motors>
   mpf: <mpf>
   mpf-mc: <mpf-mc>
   multiball_locks: <multiball_locks>
   multiballs: <multiballs>
   mypinballs: <mypinballs>
   named_colors: <named_colors>
   open_pixel_control: <open_pixel_control>
   opp: <opp>
   opp_coils: <opp_coils>
   osc: <osc>
   p_roc: <p_roc>
   pd_led_boards <pd_led_boards>
   pin2dmd: <pin2dmd>
   player_vars: <player_vars>
   playfield_transfers: <playfield_transfers>
   playfields: <playfields>
   playlist_player: <playlist_player>
   playlists: <playlists>
   plugins: <plugins>
   pololu_maestro: <pololu_maestro>
   pololu_tic: <pololu_tic>
   psus: <psus>
   queue_event_player: <queue_event_player>
   queue_relay_player: <queue_relay_player>
   random_event_player: <random_event_player>
   raspberry_pi: <raspberry_pi>
   rgb_dmds: <rgb_dmds>
   rpi_dmd: <rpi_dmd>
   score_queue_player: <score_queue_player>
   score_queues: <score_queues>
   score_reel_groups: <score_reel_groups>
   score_reels: <score_reels>
   scriptlets: <scriptlets>
   segment_display_player: <segment_display_player>
   segment_displays: <segment_displays>
   servo_controllers: <servo_controllers>
   servos: <servos>
   settings: <settings>
   sequences: <sequences>
   sequence_shots: <sequence_shots>
   shot_groups: <shot_groups>
   shot_profiles: <shot_profiles>
   shots: <shots>
   show_player: <show_player>
   show_pools: <show_pools>
   shows: <shows>
   slide_player: <slide_player>
   slides: <slides>
   smart_virtual: <smart_virtual>
   smartmatrix: <smartmatrix>
   snux: <snux>
   sound_ducking: <sound_ducking>
   sound_loop_player: <sound_loop_player>
   sound_loop_sets: <sound_loop_sets>
   sound_marker: <sound_marker>
   sound_player: <sound_player>
   sound_pools: <sound_pools>
   sound_system_tracks: <sound_system_tracks>
   sound_system: <sound_system>
   sounds: <sounds>
   spi_bit_bang <spi_bit_bang>
   spike: <spike>
   spike_node: <spike_node>
   state_machines: <state_machines>
   steppers: <steppers>
   step_stick_stepper_settings: <step_stick_stepper_settings>
   switch_overwrites: <switch_overwrites>
   switch_player: <switch_player>
   switches: <switches>
   system11: <system11>
   text_strings: <text_strings>
   text_ui: <text_ui>
   tic_stepper_settings: <tic_stepper_settings>
   tilt: <tilt>
   timed_switches: <timed_switches>
   timers: <timers>
   track_player: <track_player>
   trinamics_steprocker: <trinamics_steprocker>
   variable_player: <variable_player>
   video_pools: <video_pools>
   videos: <videos>
   virtual_platform_start_active_switches: <virtual_platform_start_active_switches>
   widget_player: <widget_player>
   widget_styles: <widget_styles>
   widgets: <widgets>
   window: <window>
