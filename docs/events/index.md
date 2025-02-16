---
title: Events
---

# Events


The concept of *events* is one of the most important concepts in MPF.
MPF is an event-driven framework, and just about everything is either
posting and event or responding to an event that was posted.

There are several important concepts about events in MPF that you should
understand:

* [Overview of the MPF event system](overview/index.md)
* [Conditional Events (only trigger if certain conditions are true, e.g. last ball, score > 1000, etc.)](overview/conditional.md)
* [Event priorities (control the order that handlers fire)](overview/priorities.md)
* [Types of events](overview/event_types.md)

## Event Reference

Here's a list of all the "built in" events that are included in MPF
and the MPF MC. Of course your own machine will include many events
that aren't on the list here.

Every event in MPF is just a string of text. You'll see that in many
cases, the actual event that's posted has a slight variation of the
event text, typically incorporating something about which mechanism or
logic device posted the event.

For example, the switch event called
[(name)_active](switch_active.md) will
replace the "(name)" part of the event text with the actual switch
name. So the when a switch called `s_left_slingshot` is activated, it
will posted an event called *switch_s_left_slingshot_active*.

* [Events Overview](overview/index.md)
    * [Handler Priorities](overview/priorities.md)
    * [Types of events](overview/event_types.md)
    * [Conditional Events](overview/conditional.md)

* Device Events
    * [Achievement Events](index_achievements.md)
        * [achievement_(name)\_changed_state](achievement_achievement_changed_state.md)
        * [achievement_(name)\_state_(state)](achievement_achievement_state_state.md)

    * [Ball Device Events](index_ball_devices.md)
        * [balldevice_(name)\_ball_count_changed](balldevice_ball_device_ball_count_changed.md)
        * [balldevice_(name)\_ball_eject_attempt](balldevice_ball_device_ball_eject_attempt.md)
        * [balldevice_(name)\_ball_eject_failed](balldevice_ball_device_ball_eject_failed.md)
        * [balldevice_(name)\_ball_eject_success](balldevice_ball_device_ball_eject_success.md)
        * [balldevice_(name)\_ball_enter](balldevice_ball_device_ball_enter.md)
        * [balldevice_(name)\_ball_entered](balldevice_ball_device_ball_entered.md)
        * [balldevice_(name)\_ball_missing](balldevice_ball_device_ball_missing.md)
        * [balldevice_(name)_broken](balldevice_ball_device_broken.md)
        * [balldevice_(name)\_ejecting_ball](balldevice_ball_device_ejecting_ball.md)
        * [balldevice_ball_missing](balldevice_ball_missing.md)
        * [balldevice_balls_available](balldevice_balls_available.md)
        * [balldevice_captured_from_(captures_from)](balldevice_captured_from_captures_from.md)

    * [Ball Hold Events](index_ball_holds.md)
        * [ball_hold_(name)\_balls_released](ball_hold_ball_hold_balls_released.md)
        * [ball_hold_(name)\_full](ball_hold_ball_hold_full.md)
        * [ball_hold_(name)\_held_ball](ball_hold_ball_hold_held_ball.md)

    * [Ball Save Events](index_ball_saves.md)
        * [ball_save_(name)_disabled](ball_save_ball_save_disabled.md)
        * [ball_save_(name)_enabled](ball_save_ball_save_enabled.md)
        * [ball_save_(name)\_grace_period](ball_save_ball_save_grace_period.md)
        * [ball_save_(name)\_hurry_up](ball_save_ball_save_hurry_up.md)
        * [ball_save_(name)\_saving_ball](ball_save_ball_save_saving_ball.md)
        * [ball_save_(name)\_timer_start](ball_save_ball_save_timer_start.md)
        * [ball_save_(name)\_add_a_ball_timer_start](ball_save_multiball_add_a_ball_timer_start.md)
        * [ball_save_(name)\_timer_start](ball_save_multiball_timer_start.md)

    * [Combo Switch Events](index_combo_switches.md)
        * [(name)_both](combo_switch_both.md)
        * [(name)_inactive](combo_switch_inactive.md)
        * [(name)_one](combo_switch_one.md)
        * [(name)\_switches_1](combo_switch_switches_1.md)
        * [(name)\_switches_2](combo_switch_switches_2.md)
        * [flipper_cancel](flipper_cancel.md)

    * [Display Events](index_displays.md)
        * [display_(name)_initialized](display_display_initialized.md)
        * [display_(name)_ready](display_display_ready.md)
        * [displays_initialized](displays_initialized.md)

    * [Diverter Events](index_diverters.md)
        * [diverter_(name)_activating](diverter_diverter_activating.md)
        * [diverter_(name)_deactivating](diverter_diverter_deactivating.md)
        * [diverter_(name)_disabling](diverter_diverter_disabling.md)
        * [diverter_(name)_enabling](diverter_diverter_enabling.md)

    * [Drop Target Events](index_drop_targets.md)
        * [drop_target_(name)_down](drop_target_drop_target_down.md)
        * [drop_target_(name)_up](drop_target_drop_target_up.md)

    * [Drop Target Bank Events](index_drop_target_banks.md)
        * [drop_target_bank_(name)_down](drop_target_bank_drop_target_bank_down.md)
        * [drop_target_bank_(name)_mixed](drop_target_bank_drop_target_bank_mixed.md)
        * [drop_target_bank_(name)_up](drop_target_bank_drop_target_bank_up.md)

    * [Extra Ball Events](index_extra_balls.md)
        * [extra_ball_award_disabled](extra_ball_award_disabled.md)
        * [extra_ball_awarded](extra_ball_awarded.md)
        * [extra_ball_(name)\_award_disabled](extra_ball_extra_ball_award_disabled.md)
        * [extra_ball_(name)_awarded](extra_ball_extra_ball_awarded.md)
        * [extra_ball_(name)_lit](extra_ball_extra_ball_lit.md)

    * [Extra Ball Group Events](index_extra_ball_groups.md)
        * [extra_ball_group_(name)\_award_disabled](extra_ball_group_extra_ball_group_award_disabled.md)
        * [extra_ball_group_(name)_awarded](extra_ball_group_extra_ball_group_awarded.md)
        * [extra_ball_group_(name)_lit](extra_ball_group_extra_ball_group_lit.md)
        * [extra_ball_group_(name)\_lit_awarded](extra_ball_group_extra_ball_group_lit_awarded.md)
        * [extra_ball_group_(name)_unlit](extra_ball_group_extra_ball_group_unlit.md)

    * [Kickback Events](index_kickbacks.md)
        * [kickback_(name)_fired](kickback_kickback_fired.md)

    * [Machine Var Events](index_machine_vars.md)
        * [machine_var_(name)](machine_var_machine_var.md)

    * [Magnet Events](index_magnets.md)
        * [magnet_(name)\_flinged_ball](magnet_magnet_flinged_ball.md)
        * [magnet_(name)\_flinging_ball](magnet_magnet_flinging_ball.md)
        * [magnet_(name)\_grabbed_ball](magnet_magnet_grabbed_ball.md)
        * [magnet_(name)\_grabbing_ball](magnet_magnet_grabbing_ball.md)
        * [magnet_(name)\_released_ball](magnet_magnet_released_ball.md)
        * [magnet_(name)\_releasing_ball](magnet_magnet_releasing_ball.md)

    * [Motor Events](index_motors.md)
        * [motor_(name)\_reached_(position)](motor_motor_reached_position.md)

    * [Multiball Events](index_multiballs.md)
        * [multiball_(name)_ended](multiball_multiball_ended.md)
        * [multiball_(name)\_grace_period](multiball_multiball_grace_period.md)
        * [multiball_(name)\_hurry_up](multiball_multiball_hurry_up.md)
        * [multiball_(name)\_lost_ball](multiball_multiball_lost_ball.md)
        * [multiball_(name)\_shoot_again](multiball_multiball_shoot_again.md)
        * [multiball_(name)\_shoot_again_ended](multiball_multiball_shoot_again_ended.md)
        * [multiball_(name)_started](multiball_multiball_started.md)

    * [Multiball Lock Events](index_multiball_locks.md)
        * [multiball_lock_(name)_full](multiball_lock_multiball_lock_full.md)
        * [multiball_lock_(name)\_locked_ball](multiball_lock_multiball_lock_locked_ball.md)

    * [Player Var Events](index_player_vars.md)
        * [player_(name)](player_player_var.md)
        * [player_score](player_score.md)

    * [Playfield Events](index_playfields.md)
        * [(name)\_ball_count_change](playfield_ball_count_change.md)
        * [(name)_active](playfield_active.md)
        * [unexpected_ball_on_(name)](unexpected_ball_on_playfield.md)

    * [Playfield Transfer Events](index_playfield_transfers.md)
        * [playfield_transfer_(playfield_transfer)\_ball_transferred](playfield_transfer_playfield_transfer_ball_transferred.md)

    * [Score Reel Events](index_score_reels.md)
        * [reel_(name)_advanced](reel_score_reel_advanced.md)

    * [Sequence Shot Events](index_sequence_shots.md)
        * [(name)_hit](sequence_shot_hit.md)

    * [Shot Events](index_shots.md)
        * [(name)_hit](shot_hit.md)
        * [(name)\_(profile)_hit](shot_profile_hit.md)
        * [(name)\_(profile)\_(state)_hit](shot_profile_state_hit.md)
        * [(name)\_(state)_hit](shot_state_hit.md)

    * [Shot Group Events](index_shot_groups.md)
        * [(name)_complete](shot_group_complete.md)
        * [(name)_hit](shot_group_hit.md)
        * [(name)\_(state)_complete](shot_group_state_complete.md)
        * [(name)\_(state)_hit](shot_group_state_hit.md)


    * [Slide Events](index_slides.md)
        * [slide_(name)_active](slide_slide_active.md)
        * [slide_(name)_created](slide_slide_created.md)
        * [slide_(name)_removed](slide_slide_removed.md)

    * [Spinner Events](index_spinners.md)
        * [spinner_(name)_active](spinner_spinner_active.md)
        * [spinner_(name)_hit](spinner_spinner_hit.md)
        * [spinner_(name)_idle](spinner_spinner_idle.md)
        * [spinner_(name)_inactive](spinner_spinner_inactive.md)
        * [spinner_(name)\_(label)_active](spinner_spinner_label_active.md)
        * [spinner_(name)\_(label)_hit](spinner_spinner_label_hit.md)

    * [Switch Events](index_switches.md)
        * [sw_(name)_active](sw_playfield_active.md)
        * [sw_(tag)](sw_tag.md)
        * [sw_(tag)_active](sw_tag_active.md)
        * [sw_(tag)_inactive](sw_tag_inactive.md)
        * [(name)_active](switch_active.md)
        * [(name)_inactive](switch_inactive.md)
        * [switch_(name)_active](switch_switch_active.md)
        * [switch_(name)_inactive](switch_switch_inactive.md)

    * [Timed Switch Events](index_timed_switches.md)
        * [(name)_active](timed_switch_active.md)
        * [(name)_released](timed_switch_released.md)
        * [flipper_cradle](flipper_cradle.md)
        * [flipper_cradle_release](flipper_cradle_release.md)

    * [Timer Events](index_timers.md)
        * [timer_(name)_complete](timer_timer_complete.md)
        * [timer_(name)_paused](timer_timer_paused.md)
        * [timer_(name)_started](timer_timer_started.md)
        * [timer_(name)_stopped](timer_timer_stopped.md)
        * [timer_(name)_tick](timer_timer_tick.md)
        * [timer_(name)\_time_added](timer_timer_time_added.md)
        * [timer_(name)\_time_subtracted](timer_timer_time_subtracted.md)


* Other Event Groups
    * Audio Management Events
        * [master_volume_decrease](master_volume_decrease.md)
        * [master_volume_increase](master_volume_increase.md)

    * Ball Lifecycle Events
        * [ball_drain](ball_drain.md)
        * [ball_ended](ball_ended.md)
        * [ball_ending](ball_ending.md)
        * [ball_start_target](ball_start_target.md)
        * [ball_started](ball_started.md)
        * [ball_starting](ball_starting.md)
        * [ball_will_end](ball_will_end.md)
        * [ball_will_start](ball_will_start.md)
        * [balls_in_play](balls_in_play.md)
        * [collecting_balls](collecting_balls.md)
        * [collecting_balls_complete](collecting_balls_complete.md)
        * [multi_player_ball_started](multi_player_ball_started.md)
        * [single_player_ball_started](single_player_ball_started.md)

    * Ball Search Events
        * [ball_search_failed](ball_search_failed.md)
        * [ball_search_phase_(num)](ball_search_phase_num.md)
        * [ball_search_prevents_game_start](ball_search_prevents_game_start.md)
        * [ball_search_started](ball_search_started.md)
        * [ball_search_stopped](ball_search_stopped.md)
        * [cancel_ball_search](cancel_ball_search.md)

    * BCP Events
        * [bcp_clients_connected](bcp_clients_connected.md)
        * [bcp_connection_attempt](bcp_connection_attempt.md)
        * [client_connected](client_connected.md)
        * [client_disconnected](client_disconnected.md)

    * Bonus (End of Ball) Events
        * [bonus_multiplier](bonus_multiplier.md)
        * [bonus_start](bonus_start.md)
        * [bonus_subtotal](bonus_subtotal.md)

    * Config Player Events
        * [clear](clear.md)

    * Credit Events
        * [credits_added](credits_added.md)
        * [enabling_credit_play](enabling_credit_play.md)
        * [enabling_free_play](enabling_free_play.md)
        * [max_credits_reached](max_credits_reached.md)
        * [not_enough_credits](not_enough_credits.md)

    * Game Lifecycle Events
        * [game_ended](game_ended.md)
        * [game_ending](game_ending.md)
        * [game_start](game_start.md)
        * [game_started](game_started.md)
        * [game_starting](game_starting.md)
        * [game_will_end](game_will_end.md)
        * [game_will_start](game_will_start.md)
        * [request_to_start_game](request_to_start_game.md)
        * [shutdown](shutdown.md)

    * Logicblock Events (Counters, Accruals, Sequences)
        * [logicblock_(name)_complete](logicblock_name_complete.md)
        * [logicblock_(name)_hit](logicblock_name_hit.md)
        * [logicblock_(name)_updated](logicblock_name_updated.md)
        * [(logicblock_name)_timeout](name_timeout.md)

    * Machine Reset Events
        * [machine_reset_phase_1](machine_reset_phase_1.md)
        * [machine_reset_phase_2](machine_reset_phase_2.md)
        * [machine_reset_phase_3](machine_reset_phase_3.md)
        * [reset_complete](reset_complete.md)

    * MPF Initialization Events
        * [init_done](init_done.md)
        * [init_phase_1](init_phase_1.md)
        * [init_phase_2](init_phase_2.md)
        * [init_phase_3](init_phase_3.md)
        * [init_phase_4](init_phase_4.md)
        * [init_phase_5](init_phase_5.md)
        * [loading_assets](loading_assets.md)
        * [asset_loading_complete](asset_loading_complete.md)

    * Match Events
        * [match_has_match](match_has_match.md)
        * [match_no_match](match_no_match.md)

    * MC (Pre 0.80.x) Events
        * [mc_ready](mc_ready.md)
        * [mc_reset_complete](mc_reset_complete.md)
        * [mc_reset_phase_1](mc_reset_phase_1.md)
        * [mc_reset_phase_2](mc_reset_phase_2.md)
        * [mc_reset_phase_3](mc_reset_phase_3.md)

    * Mode Lifecycle Events
        * [mode_(name)_started](mode_name_started.md)
        * [mode_(name)_starting](mode_name_starting.md)
        * [mode_(name)_stopped](mode_name_stopped.md)
        * [mode_(name)_stopping](mode_name_stopping.md)
        * [mode_(name)\_will_start](mode_name_will_start.md)
        * [mode_(name)\_will_stop](mode_name_will_stop.md)

    * Multiplayer Management Events
        * [multiplayer_game](multiplayer_game.md)
        * [player_add_request](player_add_request.md)
        * [player_added](player_added.md)
        * [player_adding](player_adding.md)
        * [player_turn_ended](player_turn_ended.md)
        * [player_turn_ending](player_turn_ending.md)
        * [player_turn_started](player_turn_started.md)
        * [player_turn_starting](player_turn_starting.md)
        * [player_turn_will_end](player_turn_will_end.md)
        * [player_turn_will_start](player_turn_will_start.md)
        * [player_will_add](player_will_add.md)

    * Text Input Events
        * [text_input_(key)_abort](text_input_key_abort.md)
        * [text_input_(key)_complete](text_input_key_complete.md)

    * Tilt Events
        * [slam_tilt](slam_tilt.md)
        * [tilt](tilt.md)
        * [tilt_clear](tilt_clear.md)
        * [tilt_warning](tilt_warning.md)
        * [tilt_warning_(number)](tilt_warning_number.md)

    * Twitch Integration Events
        * [twitch_bit_donation](twitch_bit_donation.md)
        * [twitch_chat_message](twitch_chat_message.md)
        * [twitch_command](twitch_command.md)
        * [twitch_raid](twitch_raid.md)
        * [twitch_subscription](twitch_subscription.md)
