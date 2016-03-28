
The *Shape*`display element`_ is used fordrawing simple shapes onto
the display. Shapedisplay elements use the same `positioning &
placement settings`_ as other display elements. There are also shape-
specific settings, including:



shape: (required)
~~~~~~~~~~~~~~~~~

A string name of the shape. Options include:


+ box- Draws a boxof a certain size. Additional settings include width
  and height.
+ line - Draws a line from one point to another. Additional settings
  include width and height. The line is drawn from point (0,0) to the
  width and height specified.




thickness:
~~~~~~~~~~

The thickness of the line in pixels. Default is 1. If you set this to
zero, the shape will be filled in.



shade:
~~~~~~

For DMD displays, the shade (intensity) of the shape, from 0-15.
Default is 15.



color:
~~~~~~

For 24-bit displays, the hex color string of the shape.

.. _display element: https://missionpinball.com/docs/displays/display-elements/
.. _ placement settings: https://missionpinball.com/docs/displays/display-elements/positioning/


