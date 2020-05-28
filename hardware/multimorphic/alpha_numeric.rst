How to configure alpha-numeric displays (P-ROC)
===============================================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/segment_displays`                                              |
+------------------------------------------------------------------------------+
| :doc:`/config/p_roc`                                                         |
+------------------------------------------------------------------------------+

The P-ROC includes support four alpha-numeric displays (0-3). You can configure them in MPF:

.. code-block:: mpf-config

  segment_displays:
    display1:
      number: 0
    display2:
      number: 1
    display3:
      number: 2
    display4:
      number: 3

Note that the :doc:`/displays/display/alpha_numeric` guide has more details
on using alpha numeric and segment displays.

What if it did not work?
------------------------

Have a look at our
:doc:`troubleshooting guide for the P/P3-Roc <troubleshooting>`.
