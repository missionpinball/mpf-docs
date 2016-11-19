Ellipse Widget
==============

The ellipse widget is used to draw a solid ellipse (including circles) on a :doc:`slide </displays/slides/index>`.

It can also be used to draw "wedges" (pie slices) or ellipses with sections missing (like Pac Man).

Note that ellipses are always solid. If you want an elliptical outline,
use the :doc:`/displays/widget/bezier/index`.

Settings
--------

::

   width:
   height:
   segments:
   angle_start:
   angle_end:

.. note:: Ellipse widgets also have "common" widget settings for position, opacity,
   animations, color, style, etc. Those are not listed here, but are instead covered in
   :doc:`common widget settings </displays/widget/common_settings>` page.

Also remember that all widget settings can be controlled via
:doc:`widget styles </displays/widgets/styles>`, rather than
you having to set every setting on every widget.

type: ellipse
~~~~~~~~~~~~~

Tells MPF that this is an ellipse widget. This setting is required when using ellipse widgets.

width:
~~~~~~

The width (in pixels) of this ellipse. This setting is required.

The ``width:`` and ``height:`` settings set the bounding box that the
ellipse will be drawn in. If you want a circle, set the width and height
to be the same.

height:
~~~~~~~

The height (in pixels) of this ellipse. This setting is required.

segments:
~~~~~~~~~

The number of segments that will make up the ellipse. More segments will
create a smoother edge, but depending on the size of your display and the
size of the ellipse, you might not see much of a difference.

The default is ``180``.

angle_start:
~~~~~~~~~~~~

The angle, between 0-360, where the ellipse will start. The default is ``0``.

angle_end:
~~~~~~~~~~

The angle, between 0-360, where the ellipse will start. The default is ``360``.

Note that a start angle of 0 and an end angle of 360 will create a complete
solid ellipse.

Examples
--------

The example config files section of the documentation contains
:doc:`examples of bezier widgets </examples/shapes/index>`.
