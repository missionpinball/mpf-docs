Raspberry PI DMD (rpi-rgb-led-matrix)
=====================================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/hardware`                                                      |
+------------------------------------------------------------------------------+
| :doc:`/config/rpi_dmd`                                                       |
+------------------------------------------------------------------------------+
| :doc:`/config/rgb_dmds`                                                      |
+------------------------------------------------------------------------------+
| :doc:`/config/displays`                                                      |
+------------------------------------------------------------------------------+


The rpi dmd platform can be used to control a RGB LED matrix on your Raspberry
Pi (any model).

1. Connect the hardware
-----------------------

We suggest that you follow the tutorial in the
`rpi-rgb-led-matrix library <https://github.com/hzeller/rpi-rgb-led-matrix>`_.


2. Install the extension
------------------------

You need to install the ``rgbmatrix`` extension on your RPi using the following
command:

.. code-block:: console

   git clone https://github.com/hzeller/rpi-rgb-led-matrix.git
   cd rpi-rgb-led-matrix
   sudo apt-get update && sudo apt-get install python3-dev python3-pillow -y
   make build-python PYTHON=$(which python3)
   sudo make install-python PYTHON=$(which python3)


3. Configure your DMD
---------------------

This is an example config:

.. code-block:: mpf-mc-config

   hardware:
     platform: rpi_dmd
   rpi_dmd:
     cols: 32
     rows: 32
     gpio_slowdown: 2
     pwm_lsb_nanoseconds: 300
   window:
     width: 600
     height: 200
     title: Mission Pinball Framework
   displays:
     window:   # on screen window
       width: 600
       height: 200
     dmd:   # source display for the DMD
       width: 32
       height: 32
       default: true
       round_anchor_x: left
   rgb_dmds:
     rpi_dmd:
       source_display: dmd
   slides:
     window_slide_1:   # slide we'll show in the on-screen window
       - type: display   # this widget shows the DMD content in this slide too
         effects:
           - type: color_dmd
         width: 512
         height: 128
       - type: text
         text: MISSION PINBALL FRAMEWORK
         anchor_y: top
         y: top-3
         font_size: 30
         color: white
       - type: rectangle
         width: 514
         height: 130
         color: 444444
     dmd_slide_1:   # slide we'll show on the physical DMD
       - type: text
         text: IT WORKS!
         font_size: 30
         color: red
   slide_player:
     init_done:
       window_slide_1:
         target: window
       dmd_slide_1:
         target: dmd
   ##! test
   #! assert_text_on_top_slide "IT WORKS!" dmd
   #! assert_text_on_top_slide "MISSION PINBALL FRAMEWORK" window

The size of your dmd (32x32 pixel in the example) should match your physical
matrix.
Also make sure to configure the :doc:`/config/rpi_dmd` section accordingly.

Note that the :doc:`/displays/display/rgb_dmd` guide has more details
on the window and slide settings used in this machine config.

4. Start MPF as root
--------------------

For this library to work you need to start MPF as root like this:

.. code-block:: console

   sudo mpf game

This is needed for the matrix to access the hardware and it will drop
privileges after it started.

What if it did not work?
------------------------

Have a look at our :doc:`hardware troubleshooting guide </hardware/troubleshooting_hardware>`.
