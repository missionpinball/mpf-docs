Image Widget
============

The image widget is used to display an image on a :doc:`slide </displays/slides/index>`.
It's also used to display animated images, which can either be animated GIFs or a folder
or zip file of sequentially-numbered images (of any type).  The zipped folder must not 
contain any hidden files in it.  The popular Windows app 7-Zip appears to insert hidden
files that will cause MC to fail.  Uploading the folder to Google Drive and downloading
it appears to make zipped files with no hidden files in them.

Image types that support alpha channels (like PNGs) are supported.

Settings
--------

.. note:: Image widgets also have "common" widget settings for position, opacity,
   animations, color, style, etc. Those are not listed here, but are instead covered in
   :doc:`common widget settings </displays/widgets/common_settings>` page.

Also remember that all widget settings can be controlled via
:doc:`widget styles </displays/widgets/styles>`, rather than
you having to set every setting on every widget.

The following image widget settings may be :doc:`animated </displays/widgets/animation>`: ``x:``, ``y:``,
``color:``, ``rotation:``, ``scale:``, ``fps:``, ``current_frame:``, and ``opacity:``.


type: image
~~~~~~~~~~~
Single value, type: ``string``.

Tells MPF that this is an image widget

image:
~~~~~~
Single value, type: string name of a :doc:`image </assets/images>`.

The name of the image asset this widget will show. Details on image
assets are :doc:`here </assets/images>`.

fps:
~~~~
Single value, type: ``integer``. Default: ``10``.

For animated images, sets how fast it plays (frames per second).

loops:
~~~~~~
Single value, type: ``integer``. Default: ``-1``.

The number of times an animated image will loop. Set to ``-1`` for unlimited. Note this is
now consistent in 0.50 with other areas of MPF. In earlier versions of MPF this setting used
``0`` to specify unlimited loops.

auto_play:
~~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``True``

If the image is an animated image, configures whether it plays automatically when it's loaded.

This is good for looping images, but if you have an image you want to play at a specific point,
you probably want to set this to no and play it from specific events via the widget player.

start_frame:
~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``0``.

Which start frame to use for animated images.
