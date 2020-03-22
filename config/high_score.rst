high_score:
===========

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **NO**  |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

.. overview

The ``high_score:`` section of your config is where you configure the built-in
high score mode.
See :doc:`/game_logic/high_scores/index` for details.

.. config


Required settings
-----------------

The following sections are required in the ``high_score:`` section of your config:

categories:
~~~~~~~~~~~
Ordered list for one (or more) sub-settings. Each in the format of ``string`` : ``list`` (:doc:`Instructions </config/instructions/lists>` for entering lists)

An ordered map of categories which contain a list of awards.
See :doc:`/game_logic/high_scores/index` for an example.


Optional settings
-----------------

The following sections are optional in the ``high_score:`` section of your config. (If you don't include them, the default will be used).

award_slide_display_time:
~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings) </config/instructions/time_strings>` . Default: ``4s``

How long should the award slide be displayed?

defaults:
~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``dict``.

A map of categories with a list of player/score tuples.
See :doc:`/game_logic/high_scores/index` for an example.
