Display Concepts
================

.. toctree::
   :hidden:



   physical_mono_dmd
   physical_rgb_dmd
   lcd
   adding_dot_look_to_lcd
   alpha_numeric


Anyway, in this example, the display is called "window". You can name your display whatever you want. For example,
here's a display called "potato" which is 100x100:

::

   displays:
      potato:
         width: 100
         height: 100

Even though you can name your displays whatever you want, some names are magic and have special properties. For example,
when the on-screen window is created, it will "attach" itself (to show content from) one of the displays you have
defined here in the ``displays:`` section of your machine config. So to us, it's just more convenient to name the
display in a way that describes where it will actually be shown.

One final note about displays that you specify in your ``displays:`` section. The size (height and width) of your
displays here are independent from the actual physical displays (windows and DMDs). For example, the size of the
on-screen window is specified in the ``window:`` section of the machine config (which is 800x600 by default). So if you
change the size of your display here (perhaps to 320x240), then the on-screen window will still be 800x600, and the
content of the display canvas will be 320x240 (but scaled up to the 800x600 window). This means that MPF is
"resolution independent", in that you can build your game for a certain display size and then scale it up or down to
fit on whatever physical display is there later.

For now, though, you don't have to worry about any of that. Just create a display called "window" at 800x600 to get
through the tutorial, and then we'll show you how to change it via the How To guides later.