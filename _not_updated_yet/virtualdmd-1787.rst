
The *Virtual DMD*`display element`_ is used to render a DMD display
into another display. In other words, it grabs the content of the DMD,
renders it to look nice, and makes it available for other displays.
This is how you get a DMD element in your on screen window. Virtual
DMDdisplay elements use the same `positioning & placement settings`_
as other display elements. There are also virtual DMD-specific
settings, including:



pixel_color:
~~~~~~~~~~~~

Hex color value of a fully bright pixel. Default is `ff5500` which is
an amber-orange color that looks like traditional DMDs. You can pick
any color you want. Here are some examples: ` `_



dark_color:
~~~~~~~~~~~

Hex color value of the pixels when they're off. Default is `221100`.



pixel_spacing:
~~~~~~~~~~~~~~

The space in pixels between each pixel that's rendered on the virtual
DMD. Here are some examples from a virtual DMD that's 512x128: ` `_



width:
~~~~~~

Width (in pixels) of the virtual DMD.



height:
~~~~~~~

Height(in pixels) of the virtual DMD.



Displaying a Color DMD
----------------------

Note thatif your DMD is configured to be color, then this Virtual DMD
element will display color pixels: ` `_` `_ No changes are needed in
this section to enable this.Since the virtual DMD just displays
whatever's on the DMD, then if your DMD is color, the virtual DMD will
be color too.

.. _display element: https://missionpinball.com/docs/displays/display-elements/
.. _ placement settings: https://missionpinball.com/docs/displays/display-elements/positioning/


