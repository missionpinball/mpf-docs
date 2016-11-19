Playfields
==========

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/playfields`                                                    |
+------------------------------------------------------------------------------+
| :doc:`/config/playfield_transfers`                                           |
+------------------------------------------------------------------------------+

Believe it or not, the playfield in MPF is technically a :doc:`ball device </mechs/ball_devices/index>`.
This is needed since MPF wants to know where all the balls are at all
times, so it needs to know which balls are "in" the playfield device.

The playfield is also responsible for tracking balls that
"disappeared" from it without going into other devices—-a process which
kicks off the :doc:`ball search </game_logic/ball_search/index>`.
The default playfield ball device (called
*playfield*) is created automatically based on settings in the
``mpfconfig.yaml`` default configuration file. Most machines only have
one playfield, though if you have a mini-playfield or a head-to-head
machine then you can configure additional playfield devices.

Playfields are configured in the :doc:`playfields: section </config/playfields>` of the
configuration file.

.. toctree::
   playfield_transfer

+------------------------------------------------------------------------------+
| Related How To Guides                                                        |
+==============================================================================+
| TODO                                                                         |
+------------------------------------------------------------------------------+

+------------------------------------------------------------------------------+
| Related Events                                                               |
+==============================================================================+
| :doc:`/events/sw_playfield_active`                                           |
+------------------------------------------------------------------------------+
| :doc:`/events/unexpected_ball_on_playfield`                                  |
+------------------------------------------------------------------------------+
