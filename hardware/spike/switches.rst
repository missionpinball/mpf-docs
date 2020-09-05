How to configure switches (Stern SPIKE)
=======================================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/spike`                                                         |
+------------------------------------------------------------------------------+
| :doc:`/config/switches`                                                      |
+------------------------------------------------------------------------------+

To configure switches on Stern SPIKE machines, you can follow the guides
and instructions in the :doc:`/mechs/switches/index` docs.

The only special thing to know is how the number works.

number:
-------

The number of a switch on a Stern SPIKE machine is a combination of the
address of the node its plugged into, and then its individual ID.

You can find the switch numbers are in the manual. Omit the "SW" and letters for
extension boards. Here's an example from Wrestlemania Pro:

.. image:: /hardware/images/spike_switch_table.jpg

This would result in the following switch entries:

.. code-block:: mpf-config

   switches:
     s_left_inlane:
       number: 11-0
     s_right_inlane:
       number: 11-8
     s_left_outlane:
       number: 11-1
     s_right_outlane:
       number: 11-9
     s_left_sling:
       number: 8-7
     s_right_sling:
       number: 8-6
     s_center_drops_right:
       number: 9-6
       type: false
     s_center_drops_middle:
       number: 9-5
       type: false
     s_center_drops_left:
       number: 9-4
       type: false
     s_left_flipper:
       number: 8-2
     s_right_flipper:
       number: 8-3
     s_left_lane:
       number: 11-3
     s_left_orbit:
       number: 9-11
     s_tourney_start:
       number: 1-12
     s_trough_6:
       number: 9-17
       type: false
     s_trough_5:
       number: 9-18
       type: false

Note that optos (highlighted in green) need to have the ``type: NO`` added
to them.

What if it did not work?
------------------------

Have a look at our :doc:`SPIKE troubleshooting guide <troubleshooting>`.
