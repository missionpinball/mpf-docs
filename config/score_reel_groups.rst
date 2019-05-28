score_reel_groups:
==================

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``score_reel_groups:`` section of your config is where you configure groups of :doc:`score reels <score_reels>`.
Every reel only displays one digits so they have to be grouped to display longer scores.
See :doc:`/mechs/score_reels/index` for more details.


Required settings
-----------------

The following sections are required in the ``score_reel_groups:`` section of your config:

reels:
~~~~~~
List of one (or more) values, each is a type: string name of a ``score_reels:`` device.

List the :doc:`score reels <score_reels>` which make up this group.
Start with the highest digit. The last entry will be the right most digit.
You may use None if there is no reel for a digit.

Optional settings
-----------------

The following sections are optional in the ``score_reel_groups:`` section of your config. (If you don't include them, the default will be used).

chimes:
~~~~~~~
List of one (or more) values, each is a type: string name of a ``coils:`` device. Default: ``None``

List the :doc:`coils <coils>` driving the chime which are rung when the reel overflows.
Start with the highest digit. The last entry will be the right most digit.
You may use None if there is no chime for a digit.

lights_tag:
~~~~~~~~~~~
Single value, type: ``string``. Default: ``None``

Lights to turn on when this group is active.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

Tag groups with the player which uses it.
Add ``player1`` to use this reel for player 1. Use ``player2`` for player 2 and so on.
A reel can be used for more than one player.
