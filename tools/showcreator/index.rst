MPF Showcreator
===============

MPF supports playing :doc:`light shows </shows/index>` out of files in your config folder.
Those are human readable and can be created by hand.
But isn't that a bit cumbersome for larger shows?
Especially, if you want to swipe over all (or most) of your LEDs this might
take days.
Luckily, there is a tool for that.

The `light show generator for MPF <https://github.com/missionpinball/showcreator>`_
loads your LED positions from the :doc:`/tools/monitor/index`
config and lets you create show for transitions.

:doc:`Shows </shows/index>` in MPF are
written in YAML and can be used
:doc:`universally </config_players/index>`
to control all kinds of things (such as
:doc:`lights </config_players/coil_player>`,
:doc:`coils </config_players/coil_player>`,
:doc:`slides </config_players/slide_player>`,
:doc:`widgets </config_players/widget_player>`,
:doc:`sounds </config_players/sound_player>`
and :doc:`more </config_players/index>`).
Basically, shows are a list of actions combined with a duration after which
the next element in the list is played.
Here is an example of a light show with three lights which sequentially turn
blue over one second:

.. code-block:: mpf-config

    ##! show: my_show
    #show_version=5
    - duration: .25
      lights:
        l_arrow_1: off
        l_arrow_2: off
        l_arrow_3: off
    - duration: .25
      lights:
        l_arrow_1: blue
        l_arrow_2: off
        l_arrow_3: off
    - duration: .25
      lights:
        l_arrow_1: blue
        l_arrow_2: blue
        l_arrow_3: off
    - duration: .25
      lights:
        l_arrow_1: blue
        l_arrow_2: blue
        l_arrow_3: blue

In this simple example it totally makes sense to create the show by hand.
You could also throw in
:doc:`tokens </shows/tokens>`
for the lights and reuse the show all
over the machine for different light triples.

However, imagine you want to swipe over all lights in your machine.
That would be a lot of text and also hard to get right manually.
Luckily, Mark, the maker of the
`Nightmare before Christmas custom pinball machine <https://pinside.com/pinball/forum/topic/the-nightmare-before-christmas>`_,
created this awesome MPF Lightshow generator.

.. image:: /tools/images/showcreator.png

The tool allows you to set a shape (i.e. a star in the example), choose a start
and an end position and color.
Based on that it will create a light show for you which contains one section
per step (at a defined frame rate).
Neat right?
You might ask: How does it know where my lights are located on the playfield?

Luckily, you probably already have them set if you used the :doc:`MPF Monitor </tools/monitor/index>`.
It allows you to use drag an drop to position all your switches and lights on
a playfield image.
Those positions are then saved to the ``monitor/monitor.yaml`` file in your
machine folder.
All you have to do is to copy the lights to the ``ledsloc.txt`` file in the
show creator and your are good to go (this might become unnecessary in the
future).

This how a ``monitor/monitor.yaml`` looks:

.. code-block:: yaml

   drop_target:
     t_figure_front:
       x: 0.1598135527333567
       y: 0.2635487843024701
   flipper:
     flipper_left_back:
       x: 0.6544089443822798
       y: 0.8534547080449149
   light:
     gi_left_back_light_0:
       x: 0.5151063672560986
       y: 0.4518074675853541
     gi_left_back_light_1:
       x: 0.5228274477074748
       y: 0.4874764781841978
     gi_left_back_light_10:
       x: 0.5692904656319291
       y: 0.7657640987721404

And this is what your ``ledsloc.txt`` should look for the same machine (omit
everything except your lights):

.. code-block:: yaml

     gi_left_back_light_0:
       x: 0.5151063672560986
       y: 0.4518074675853541
     gi_left_back_light_1:
       x: 0.5228274477074748
       y: 0.4874764781841978
     gi_left_back_light_10:
       x: 0.5692904656319291
       y: 0.7657640987721404


Running the showcreator on Windows
----------------------------------

1. Checkout or download the `showcreator <https://github.com/missionpinball/showcreator.git>`_ repository.
2. Double click on led.exe


Compiling and running the showcreator on Ubuntu
-----------------------------------------------

Inside a new install folder:

.. code-block:: console

   # inside a new install folder
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

Afterwards you can run the showcreator using (from within your install folder):

.. code-block:: console

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

Dynamic Shows
-------------

It is great to render static shows which will not change during runtime.
If you want to render shows dynamically (using your GPU) you can also use
:doc:`your lights as display in MC </config_players/display_light_player>`
but that will cost much more resources during runtime than offline generated
shows.
