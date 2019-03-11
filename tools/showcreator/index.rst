MPF Showcreator
===============


The `light show generator for MPF <https://github.com/missionpinball/showcreator>`_
loads your LED positions from the :doc:`/tools/monitor/index`
config and lets you create show for transitions.


Running the showcreator on Windows
----------------------------------

1. Checkout or download the `showcreator <https://github.com/missionpinball/showcreator.git>`_ repository.
2. Double click on led.exe


Compiling and running the showcreator on Ubuntu
-----------------------------------------------

.. code-block:: console

   # inside a new src folder
   apt install linux-libc-dev:i386 libxft2:i386 g++-multilib gcc-multilib libxpm-dev:i386 libxxf86vm-dev:i386 libgl1-mesa-dev:i386 libglu1-mesa-dev:i386
   git clone https://github.com/blitz-research/blitzmax.git
   cd blitzmax
   cd _src_/linux
   ./install.bat  # yes its .bat
   cd ../../../   # back to your src folder

   git clone https://github.com/missionpinball/showcreator.git
   cd showcreator
   ../blitzmax/bin/bmk makeapp led.bmx

   # run it
   ./led

Afterwards you can run the showcreator using (from within your new folder):

   ./showcreator/led

Key bindings
------------

 * A - adjust rotation
 * S - adjust x scale
 * X - adjust y scale
 * C - adjust both x and y scales
 * HOLD SHIFT to reverse above functions
 * HOLD CTRL to increase functions by 10X
 * I - flash between START and FINISH end points
 * L - toggle between viewing SHAPES or affected LEDs
 * B - toggle between BW and full colour output
 * B+SHIFT - change the B/W Threshold (16-240)/256
 * SPC - toggle between START and FINISH end points
 * U - play segment
 * P - play complete set
 * M - HOLD for slow motion during segment/set play
 * P+SHIFT - play set and create script file
 * ESC - quit - Y/N confirm quit
 * Left Mouse Button Down over playfield adjusts position of current end (START or FINISH) +SHIFT adjusts both START AND FINISH positions
