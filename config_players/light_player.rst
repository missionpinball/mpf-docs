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
     l_light:
       number:
   shows:
     red_color:
       - lights:
           l_light: red
   show_player:
     turn_light_red_event: red_color
   ##! test
   #! post turn_light_red_event
   #! advance_time_and_run .1
   #! assert_light_color l_light red

Setting multiple lights
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: mpf-config

   lights:
     l_target1:
       number:
     l_target2:
       number:
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
   ##! test
   #! post play_rainbow_show_on_targets
   #! advance_time_and_run .1
   #! assert_light_color l_target1 red
   #! assert_light_color l_target2 red
   #! advance_time_and_run 1
   #! assert_light_color l_target1 orange
   #! assert_light_color l_target2 orange

The show ``rainbow`` will turn your LED(s) in the placeholder ``(leds)``
to a different color every second (because 1s is the default duration of a step).
The last step (purple) will stay for 3s.
When you post ``play_rainbow_show_on_targets`` the show is played on two
lights which are referenced directly.

Setting lights via tags
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: mpf-config

   lights:
     l_drop1:
       number:
       tags: drops
     l_drop2:
       number:
       tags: drops
   shows:
     rainbow:
       - lights:
           (tag): red
         duration: 1s
       - lights:
           (tag): orange
         duration: 1s
       - lights:
           (tag): yellow
         duration: 1s
       - lights:
           (tag): green
         duration: 1s
       - lights:
           (tag): blue
         duration: 1s
       - lights:
           (tag): purple
         duration: 1s
   show_player:
     play_rainbow_show_via_tag:
       rainbow:
         show_tokens:
           tag: drops
   ##! test
   #! post play_rainbow_show_via_tag
   #! advance_time_and_run .1
   #! assert_light_color l_drop1 red
   #! assert_light_color l_drop2 red
   #! advance_time_and_run 1
   #! assert_light_color l_drop1 orange
   #! assert_light_color l_drop2 orange

In ``play_rainbow_show_via_tag`` we reference (two) lights via the tag
``drops``.

Fade lights between steps
^^^^^^^^^^^^^^^^^^^^^^^^^

There are two syntax to express fades.
Short syntax which is ``(color)-f(time)(unit)`` (i.e. ``red-f200ms``) or
extended syntax which is a dict with two entrie for ``color`` and ``fade``.
Here is an example for the short syntax:

.. code-block:: mpf-config

   #! lights:
   #!   l_rgb:
   #!     number:
   shows:
     rainbow_with_fade_f_syntax:
       - lights:
           l_rgb: red-f1s
         duration: 1s
       - lights:
           l_rgb: orange-f1s
         duration: 1s
       - lights:
           l_rgb: yellow-f1s
         duration: 1s
       - lights:
           l_rgb: green-f1s
         duration: 1s
       - lights:
           l_rgb: blue-f1s
         duration: 1s
       - lights:
           l_rgb: purple-f1s
         duration: 1s

   show_player:
     play_rainbow_show: rainbow_with_fade_f_syntax

   ##! test
   #! post play_rainbow_show
   #! advance_time_and_run 1
   #! assert_light_color l_rgb red
   #! advance_time_and_run 1
   #! assert_light_color l_rgb orange

And an example with extended syntax:

.. code-block:: mpf-config

   #! lights:
   #!   l_rgb:
   #!     number:
   shows:
     rainbow_with_fade_extended_syntax:
       - lights:
           l_rgb:
             color: red
             fade: 1s
         duration: 1s
       - lights:
           l_rgb:
             color: orange
             fade: 1s
         duration: 1s
       - lights:
           l_rgb:
             color: yellow
             fade: 1s
         duration: 1s
       - lights:
           l_rgb:
             color: green
             fade: 1s
         duration: 1s
       - lights:
           l_rgb:
             color: blue
             fade: 1s
         duration: 1s
       - lights:
           l_rgb:
             color: purple
             fade: 1s
         duration: 1s

   show_player:
     play_rainbow_show: rainbow_with_fade_extended_syntax

   ##! test
   #! post play_rainbow_show
   #! advance_time_and_run 1
   #! assert_light_color l_rgb red
   #! advance_time_and_run 1
   #! assert_light_color l_rgb orange

In most cases simple syntax is sufficient.
Extended syntax is easier to use with placeholders.

Config Options
--------------

See :doc:`/config/light_player` for config details.
