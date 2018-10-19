How to enable "weak flippers" (novelty mode)
============================================

Some machines have modes which reduce the flipper power.
This can be implemented in two ways.
Either by reducing ``pulse_power`` or by reducing ``pulse_ms`` (some platforms
only support the latter).

This is an example:

.. code-block:: mpf-config

   switches:
        s_left_flipper:
            number: 1
        s_right_flipper:
            number: 2

   coils:
        c_flipper_left:
            number: 0
            default_pulse_ms: 30
            default_pulse_power: 0.5
            default_hold_power: 0.125
        c_flipper_right:
            number: 1
            default_pulse_ms: 30
            default_pulse_power: 0.5
            default_hold_power: 0.125

   flippers:
     left:
       main_coil: c_flipper_left
       activation_switch: s_left_flipper
       enable_events: normal_flippers_enable, ball_started
       disable_events: weak_flipper_enable, ball_will_end, service_mode_entered
     right:
       main_coil: c_flipper_right
       activation_switch: s_right_flipper
       enable_events: normal_flippers_enable, ball_started
       disable_events: weak_flipper_enable, ball_will_end, service_mode_entered
     left_weak:
       main_coil: c_flipper_left
       main_coil_overwrite:
         pulse_power: 0.3     # alternatively you can use pulse_ms: 20 here
       activation_switch: s_left_flipper
       enable_events: weak_flipper_enable
       disable_events: normal_flippers_enable
     right_weak:
       main_coil: c_flipper_right
       main_coil_overwrite:
         pulse_power: 0.3     # alternatively you can use pulse_ms: 20 here
       activation_switch: s_right_flipper
       enable_events: weak_flipper_enable
       disable_events: normal_flippers_enable

   ##! test
   #! start_game
   #! assert_bool_condition True device.flippers.left.enabled
   #! assert_bool_condition False device.flippers.left_weak.enabled
   #! post weak_flipper_enable
   #! assert_bool_condition False device.flippers.left.enabled
   #! assert_bool_condition True device.flippers.left_weak.enabled
   #! post normal_flippers_enable
   #! assert_bool_condition True device.flippers.left.enabled
   #! assert_bool_condition False device.flippers.left_weak.enabled

We define two sets of flippers: Normal and weak flippers.
Post ``weak_flipper_enable`` in your mode to enable weak flippers.
Later post ``normal_flippers_enable`` to reenable normal flippers.
You can also use your mode start/stop events here.
