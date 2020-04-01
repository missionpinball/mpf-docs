mode_settings:
==============

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **NO**  |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

.. overview

The ``mode_settings:`` section of your config is a generic section that contains settings
that you might want to use in a specific mode. It's nice because it's pretty much ignored
by the general MPF config processing, meaning you can put whatever settings you want in
here for a specific mode.

In fact, several of the built-in MPF modes make use of the ``mode_settings:`` section,
including:

* :doc:`End of Ball Bonus mode <bonus>`

.. config


Related How To guides
---------------------

* :doc:`End of Ball Bonus mode <bonus>`
* :doc:`/game_design/mode_selection`
* :doc:`/game_design/game_modes/carousel`
* :doc:`/game_logic/bonus/index`
