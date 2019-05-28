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
It allows you to use drag and drop to position all your switches and lights on
a playfield image.
Those positions are then saved to the ``monitor/monitor.yaml`` file in your
machine folder.
All you have to do is point the light show creator to the ``monitor/monitor.yaml`` file on startup.

You set the start and end positions, rotations, scales and colors of that shape
anywhere you want over the playfield.

Here we start with a gradient bar at the top of the playfield in a pink color.

.. image:: /tools/images/showcreator_start.png

We want the final position to be here at the bottom, in a darker red shade.

.. image:: /tools/images/showcreator_end.png

You can then adjust the length of the animation in milliseconds and hence the number of steps in the final show.
In this example, the shape will be moved from the start to finish in 24 steps.

Based on these settings, it will create a light show for you which contains all needed commands
per step for each of the lights the shape passes over. Lightshow playback speed can be adjusted in MPF.

You're not restricted to just the included shapes.  You can make your own shapes and drop them in the shapes folder.

.. image:: /tools/images/showcreator_shapes.png

Once you get the hang of animating a single shape, you can go further by adding in more shapes.
You can add a total of 256 shapes in animation segments.
Each segment can be set to ``concurrent`` (start and end same time as the previous segment)
or ``follow`` (start after previous segment)
This allows for more interesting multipart shows. For example you could have several color swipes coming from different directions
one after the other or effects like multiple spotlights moving across the playfield like a hollywood premiere.


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

The tool is handy to render static shows which will not change during runtime.
If you want to render shows dynamically (using your GPU) you can also use
:doc:`your lights as display in MC </config_players/display_light_player>`
but that will cost much more resources during runtime than offline generated
shows.
