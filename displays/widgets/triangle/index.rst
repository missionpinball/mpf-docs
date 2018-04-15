Triangle widget
===============

The triangle widget is used to draw triangles on a :doc:`slide </displays/slides/index>`.

Here's an example:

.. code-block:: mpf-config

   #config_version=5

   slide_player:
     mc_ready:
        triangle_example:
         - type: triangle
           color: blue
           points: 0, 0, 100, 0, 100, 100
         - type: triangle
           points: 400, 400, 300, 200, 600, 500
           color: red
         - type: triangle
           points: 200, 500, 100, 400, 300, 400

The example above results in the following:

.. image:: /displays/images/triangle.png

Settings
--------

.. code-block:: yaml

   type: triangle
   points:

.. note:: Triangle widgets also have "common" widget settings for position, opacity,
   animations, color, style, etc. Those are not listed here, but are instead covered in
   :doc:`common widget settings </displays/widgets/common_settings>` page.

Also remember that all widget settings can be controlled via
:doc:`widget styles </displays/widgets/styles>`, rather than
you having to set every setting on every widget.

type: triangle
~~~~~~~~~~~~~~

Tells MPF that this is a triangle widget.

points:
~~~~~~~

A list of six numbers which are the the x,y coordinates for each of the three corners.
For example, ``points: 400, 300, 200, 300, 400, 200`` would be a triangle with one corner
at (400, 300), another corner at (200, 300), and the final corner at (400, 200).
