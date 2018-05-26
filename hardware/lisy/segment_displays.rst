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


See :doc:`/segment_displays/index` for details on how to use them.
