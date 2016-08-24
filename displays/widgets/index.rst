Display widgets
===============

.. toctree::
   :hidden:
   :maxdepth: 2

   Creating reusable "named" widgets <reusable_widgets>
   Animating widgets <animate_widgets>
   Positioning widgets <widget_positioning>

Display widgets are where the real action takes place in MPF-MC's display system.
They're what you (as a game programmer) interact with most often. They're the
"stuff" that shows up on a display. (Well, technically, they're the stuff that
is added to a slide, and then that slide in turn is shown on a display.) MPF
includes the following types of display widgets:

+ Text
+ Image
+ Video
+ DMD
+ Character picker
+ Entered chars
+ Bezier
+ Ellipse
+ Line
+ Point
+ Quad
+ Rectangle
+ Triangle

These widgets plug-in to MPF-MC's display system in a standard way, so it's easy
for us (or for you) to write your own widgets if you need to be able to display
something that we don't include out-of-the-box. (We also have plans for more
types of display elements, including ones to render segmented displays to the on
screen window and ones that show the current status of lights, switches, and
coils.)




Colors in the MPF-MC can be specified by name (like "red") or by hex value ("ff0000"). Note that if you
specify a color by hex value, do NOT put a ``#`` in it, since YAML files use those for comments which
are ignored. RIGHT: ``color: ff0000``  WRONG: ``color: #ff0000``