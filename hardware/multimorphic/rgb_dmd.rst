How to configure an RGB DMD (P-ROC/P3_ROC)
==========================================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/physical_rgb_dmds`                                             |
+------------------------------------------------------------------------------+
| :doc:`/config/smartmatrix`                                                   |
+------------------------------------------------------------------------------+
| :doc:`/config/eli_dmd`                                                       |
+------------------------------------------------------------------------------+

Neither the P-ROC nor the P3-ROC has direct support for RGB DMDs. However you
can still use an RGB DMD with a P-ROC/P3-ROC by using one of the standalone
RGB DMD controllers. (Basically you buy the RGB DMD hardware and another small
controller, and then you have two USB connections from your computer—one to the
P-ROC/P3-ROC, and a second to the RGB DMD controller.)

Standalone RGB DMD options which you can use with a P-ROC/P3-ROC include:

* :doc:`SmartMatrix </hardware/smartmatrix/index>`
* :doc:`RGB.DMD </hardware/eli_dmd/index>`
