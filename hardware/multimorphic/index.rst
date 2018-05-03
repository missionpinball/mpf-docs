How to configure Multimorphic (P-ROC & P3-ROC) hardware
=======================================================

Here's a list of all the How To guides which explain how to use MPF with
`Multimorphic P-ROC and P3-ROC control systems <http://pinballcontrollers.com/>`_.
These guides include the numbering format (how you map specific entries in your
config files to board and connector locations) as well as overall settings that
affect how your hardware performs.

This page is about the software side of things.
Hardware and electrical engineering stuff is documented at the
`P-Roc section in the pinballmakers.com Wiki <http://pinballmakers.com/wiki/index.php/P-ROC_Main_Page>`_.

3 steps to using a P-ROC/P3-ROC
-------------------------------

1. :doc:`Install the hardware drivers to support the P-ROC/P3-ROC <hardware_drivers>`.
2. :doc:`Configure your platform <platform>`.
3. Configure the individual pinball mechanisms from the list below.

P-ROC/P3-ROC pinball mech configuration
---------------------------------------

The following pinball mechanisms are supported by the P-ROC and/or P3-ROC.
Click each one for details on how to configure these types of mechanisms for
the P-ROC or P3-ROC.

.. toctree::
   :titlesonly:
   :hidden:

   Installing Hardware Drivers <hardware_drivers>
   Setting the platform for P-ROC/P3-ROC <platform>

.. toctree::
   :titlesonly:

   Switches (P-ROC) <switches_p_roc>
   Switches (P3-ROC) <switches_p3_roc>
   Coils/Drivers/Magnets/Motors (P-ROC & P3-ROC) <drivers>
   LEDs (P-ROC & P3-ROC)<leds>
   Matrix Lights (P-ROC & P3-ROC)<lights>
   Traditional single-color DMD (P-ROC) <dmd>
   RGB DMD (P-ROC & P3-ROC) <rgb_dmd>
   Alpha-numeric displays (P-ROC) <alpha_numeric>
   Accelerometer (P3-ROC) <accelerometer>
   Servos (P3-ROC) <servos>
