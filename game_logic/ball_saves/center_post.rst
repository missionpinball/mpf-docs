Center Post Ball Save
=====================

Some machines have a mechanical ball save called center post.
It pops up between the flippers and prevents the ball from draining.

.. image:: /game_logic/images/center_post.jpg

To use it in MPF we reuse a diverter.
A simple :doc:`/config/coil_player` would work as well but then we would have
to reimplement ball search and service mode logic.
The diverter will already implement all that for us.

This is an example:

.. code-block:: mpf-config

   # in your machine config
   coils:
     c_ball_save_post_up:
       number: 1-10  # yours might be different
       default_pulse_ms: 15
     c_ball_save_post_down:
       number: 1-15  # yours might be different
       default_pulse_ms: 15

   lights:
     ball_saver:
       number:

   diverters:
     ball_save_post:
       activation_coil: c_ball_save_post_up
       deactivation_coil: c_ball_save_post_down
       activate_events: ball_save_post_up
       deactivate_events: ball_save_post_down
       enable_events: ball_started
       type: pulse

   ##! mode: base
   # in base mode

   event_player:
     ball_save_default_timer_start:
       - ball_save_post_up
     ball_save_default_disabled:
       - ball_save_post_down

   ball_saves:
     default:
       active_time: 10s
       grace_period: 2s
       hurry_up_time: 5s
       enable_events: mode_base_started
       timer_start_events: balldevice_bd_plunger_ball_eject_success
       disable_events: ball_will_end
       auto_launch: true
       balls_to_save: 1
       early_ball_save_events: s_right_outlane_active, s_left_outlane_active

   show_player:
     ball_save_default_timer_start:
       ball_save_show:
         action: play
         speed: 5
     ball_save_default_hurry_up:
       ball_save_show:
         action: play
         speed: 10
     ball_save_default_disabled:
       ball_save_show:
         action: stop

   shows:
     ball_save_show:
       - time: 0
         lights:
           ball_saver:
             color: black
       - time: '+1'
         lights:
           ball_saver:
             color: red
