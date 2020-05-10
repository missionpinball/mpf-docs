Configuring Segment Displays in LISY
====================================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/segment_displays`                                              |
+------------------------------------------------------------------------------+
| :doc:`/config/segment_display_player`                                        |
+------------------------------------------------------------------------------+

MPF can control all segment displays on your machine with LISY.
Configure them like this:

.. code-block:: mpf-config

   segment_displays:
     info_display:
       number: 0
     player1_display:
       number: 1
     player2_display:
       number: 2
     player3_display:
       number: 3
     player4_display:
       number: 4

Note that the :doc:`/displays/display/alpha_numeric` guide has more details
on using alpha numeric and segment displays.

What if it did not work?
------------------------

Have a look at our :doc:`LISY troubleshooting guide <troubleshooting>`.
