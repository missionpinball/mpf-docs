Playfields
==========

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/playfields`                                                    |
+------------------------------------------------------------------------------+
| :doc:`/config/playfield_transfers`                                           |
+------------------------------------------------------------------------------+

.. contents::
   :local:

Believe it or not, the playfield in MPF is technically a :doc:`ball device </mechs/ball_devices/index>`.
This is needed since MPF wants to know where all the balls are at all
times, so it needs to know which balls are "in" the playfield device.

:doc:`TODO: Add a picture of a playfield </about/help_us_to_write_it>`

The playfield is also responsible for tracking balls that
"disappeared" from it without going into other devices—-a process which
kicks off the :doc:`ball search </game_logic/ball_search/index>`.
The default playfield ball device (called
*playfield*) is created automatically based on settings in the
``mpfconfig.yaml`` default configuration file. Most machines only have
one playfield, though if you have a mini-playfield or a head-to-head
machine then you can configure additional playfield devices.

Playfields are configured in the :doc:`playfields: section </config/playfields>`
of the configuration file.

Monitorable Properties
----------------------

For :doc:`dynamic values </config/instructions/dynamic_values>` and
:doc:`conditional events </events/overview/conditional>`,
the prefix for playfields is ``device.playfields.<name>``.

*available_balls*
   Balls which will be available eventually. If a ball is requested it will be included
   in available_balls but not in balls until it arrives.

*balls*
   The number of balls on the playfield.

Related Events
--------------

.. include:: /events/include_playfields.rst

Other playfield concepts
------------------------

.. toctree::

   ball_tracking
   playfield_balls_vs_balls_in_play
   playfield_transfer
