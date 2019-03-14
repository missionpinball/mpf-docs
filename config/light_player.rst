light_player:
=============

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`shows </shows/index>`                                       | **YES** |
+----------------------------------------------------------------------------+---------+

.. note:: This section can also be used in a show file in the ``lights:`` section of a step.

.. overview

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

.. code-block:: mpf-config

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


Optional settings
-----------------

The following sections are optional in the ``light_player:`` section of your config. (If you don't include them, the default will be used).

brightness:
~~~~~~~~~~~
Single value, type: 2-byte hex value (``00`` to ``ff``). Default: ``ff``

Set a brightness to a light. If you use brightness on an RGB light MPF will
use the brightness for every channel. For instance brigness ``AA`` will
result in color ``AAAAAA``.

color:
~~~~~~
Single value, type: ``string``. Default: ``white``

Set a color to this light. Color values may be a hex string (e.g. `22FFCC`), a list of RGB values 
(e.g. `[50, 128, 206]`),or a color name (e.g. `turquoise`). MPF knows 140+ standard web color names, 
and you can define your own custom colors in the :doc:`/config/named_colors` section of your config. 

If you apply a color to a non-RGB light it will use the maximum brightness of any channel.

fade:
~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings) </config/instructions/time_strings>` . Default: ``0``

Time to fade this light in ms. Use this to achieve smooth transitions between colors.

