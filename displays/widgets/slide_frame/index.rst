Slide Frame Widget
==================

The slide frame widget is used to create a "frame" on a :doc:`slide </displays/slides/index>`
that is used to hold other slides. (Think of this like a picture-in-picture kind of thing.)

Here's an example:

.. code-block:: yaml

   #config_version=4

   slides:
     base_slide:
       - type: slide_frame
         name: my_frame
         width: 400
         height: 300
         x: 300
         y: 200
       - type: text
         text: this is the base slide
         x: 600
         y: 400
     frame_slide:
       widgets:
         - type: text
           text: this is a slide in the frame
       background_color: red

   slide_player:
     mc_ready.1: base_slide
     mc_ready.2:
       frame_slide:
         target: my_frame

And the result:

.. image:: /displays/images/slide_frame.png

Settings
--------

.. code-block:: yaml

   type: slide_frame
   name:
   width:
   height:

.. note:: Slide frame widgets also have "common" widget settings for position, opacity,
   animations, color, style, etc. Those are not listed here, but are instead covered in
   :doc:`common widget settings </displays/widgets/common_settings>` page.

Also remember that all widget settings can be controlled via
:doc:`widget styles </displays/widgets/styles>`, rather than
you having to set every setting on every widget.

name:
-----

The name of your frame. This name will be available as a ``target:`` name is other areas
of your configs (just like displays) when you want to target a slide to this frame.

More information on display targets is :doc:`here </displays/slides/display_targets>`.

width:
------

The width of the frame in pixels.

height:
-------

The height of the frame in pixels.
