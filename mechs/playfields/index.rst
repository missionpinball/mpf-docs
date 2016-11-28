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

Playfields are configured in the :doc:`playfields: section </config/playfields>`
of the configuration file.

playfield_active switch tags
============================

In MPF, it's important to add "playfield_active" tags to every switch that
can be hit by a ball when there's a ball on that playfield. This is how MPF
knows that a ball has been successfully ejected onto the playfield, and it's
used to reset ball search timer.

This setting is a tag property which you apply to the switches in the
``switches:`` section of your machine config file, like this:

::

   switches:

      s_trough1:
        number:
      s_trough2:
        number:
      s_plunger_lane:
        number:
      s_standup_1:
        number:
        tags: playfield_active
      s_upper_right_rollover:
        number:
        tags: playfield_active

.. important::

   Since the playfield_active tag is also used for ball search, it's important
   that you tag all the playfield switches with playfield_active, not just the
   ones that are first hit when a ball is launched.

If you have more than one playfield, then the "playfield_active" switch tag
name should be adjusted to match the name of your actual playfield. For example,
if you have a playfield called "upper_playfield", then the switches which are
hit by a ball on the upper playfield should be tagged ``upper_playfield_active``.

Multiple playfields
===================

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
