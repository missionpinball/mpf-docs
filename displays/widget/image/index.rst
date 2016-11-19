Image Widget
============

The image widget is used to display an image on a :doc:`slide </displays/slides/index>`.
It's also used to display animated images, which can either be animated GIFs or a folder
or zip file of sequentially-numbered images (of any type).

Image types that support alpha channels (like PNGs) are supported.

Settings
--------

::

   type: image
   image:
   width:
   height:
   allow_stretch:
   keep_ratio:

   fps:
   loops:
   auto_play:
   start_frame:

.. note:: Ellipse widgets also have "common" widget settings for position, opacity,
   animations, color, style, etc. Those are not listed here, but are instead covered in
   :doc:`common widget settings </displays/widget/common_settings>` page.

Also remember that all widget settings can be controlled via
:doc:`widget styles </displays/widgets/styles>`, rather than
you having to set every setting on every widget.


type: image
~~~~~~~~~~~

Tells MPF that this is an image widget

image:
~~~~~~

The name of the image asset this widget will show. Details on image
assets are :doc:`here </assets/images>`.

width:
~~~~~~
Net yet implemented. TODO

Default is 0

height:
~~~~~~~
Net yet implemented. TODO

Default is 0

allow_stretch:
~~~~~~~~~~~~~~
Net yet implemented. TODO

Default is False

keep_ratio:
~~~~~~~~~~~
Net yet implemented. TODO

Default is False

fps:
~~~~

For animated images, sets how fast it plays (frames per second).

Default is 10.

loops:
~~~~~~

The number of times an animated image will loop. Set to ``0`` for unlimited. (Note this is
different than other areas of MPF, which use ``-1`` to indicate unlimited loops.)

Default is 0.

auto_play:
~~~~~~~~~~

If the image is an animated image, configures whether it plays automatically when it's loaded.

Default is True.

This is good for looping images, but if you have an image you want to play at a specific point,
you probably want to set this to no and play it from specific events via the widget player.

start_frame:
~~~~~~~~~~~~

Net yet implemented. TODO

Default is 0.
