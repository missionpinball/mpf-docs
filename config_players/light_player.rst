Light player
============

The *light player* is a :doc:`config player </config_players/index>` that's used to set the brightness and
color of lights (including turning them on and off).

Usage in config files
---------------------

In config files, the light player is used via the ``light_player:`` section.

The ``light_player:`` section of your config is where you can control lights
in config or shows. Example in config:

.. code-block:: mpf-config

   light_player:
     some_event:
       led1:
         color: red
         fade: 200ms
       led2:
         color: ff0000
         fade: 2000ms

Usage in shows
--------------

In shows, the light player is used via the ``lights:`` section of a step.

.. code-block:: mpf-config

   lights:
      l_target1:
         number:
      l_target2:
         number:
      l_drop1:
         number:
         tags: drops
      l_drop2:
         number:
         tags: drops

   shows:
      rainbow:
         - lights:
             (leds): red
         - lights:
             (leds): orange
         - lights:
             (leds): yellow
         - lights:
             (leds): green
         - lights:
             (leds): blue
         - lights:
             (leds): purple
           duration: 3s

   show_player:
      play_rainbow_show_on_targets:
         rainbow:
            show_tokens:
               leds: l_target1, l_target2
      play_rainbow_show_via_tag:
         rainbow:
            show_tokens:
               leds: drops

   ##! test
   #! post play_rainbow_show_on_targets
   #! advance_time_and_run .1
   #! assert_light_color l_target1 red
   #! assert_light_color l_target2 red
   #! advance_time_and_run 1
   #! assert_light_color l_target1 orange
   #! assert_light_color l_target2 orange
   #! post play_rainbow_show_via_tag
   #! advance_time_and_run .1
   #! assert_light_color l_drop1 red
   #! assert_light_color l_drop2 red
   #! advance_time_and_run 1
   #! assert_light_color l_drop1 orange
   #! assert_light_color l_drop2 orange

The show ``rainbow`` will turn your LED(s) in the placeholder ``(leds)``
to a different color every second (because 1s is the default duration of a step).
The last step (purple) will stay for 3s.
When you post ``play_rainbow_show_on_targets`` the show is played on two
lights which are referenced directly.
In ``play_rainbow_show_via_tag`` we reference (two) lights via the tag
``drops``.

Config Options
--------------

See :doc:`/config/light_player` for config details.
