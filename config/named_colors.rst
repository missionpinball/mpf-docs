named_colors:
=============

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``named_colors:`` section of your config is where you define color names that
can be used for RGB lights throughout your machine code. Anywhere in lights: or light_player: where a color can be specified, named colors can be used.

Your named colors can be an array of R/G/B values or a hex string of hex values (which can also include a brightness percentage, like all hex color strings).

This is an example:

.. code-block:: mpf-config

  named_colors:
    custom_blue: [24, 65, 226]
    troll_green: 4a9b22
    troll_green_dark: 4a9b22%50
  lights:
    troll_target:
      number: 10
      default_on_color: troll_green
    l_jackpot:
      number: 20
  light_player:
    trolls_disabled:
      troll_target: troll_green_dark
    jackpot_lit:
      l_jackpot:
        color: custom_blue
        fade: 10

.. config


Related How To guides
---------------------

.. todo:: :doc:`/about/help_us_to_write_it`
