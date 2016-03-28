
All `display elements`_ in MPFare positioned on a slide in the same
way, using the same settings, with the same results—regardless of what
*type* of display element it is. Here's what you need to know:


+ All display elements are rectangular in shape . Even if the image or
  shape is a circle or irregular, the bounding box that makes up the
  display element is rectangular. (Remember that individual pixels in a
  display element can be transparent, so it's possible for a shapeto
  look like a circle even though it's really a square.)
+ All display elements have a width and height which defines the size
  of the rectangle that makes them up.
+ All display elements have an (x, y) position which represents the x,
  y position on the display of their upper-left corner.


Let's look at an example slide for a 128x32 display with four display
elements on it. The light gray boxes represent the bounding rectangles
of each display element.


+ The 123,456,789 text element is positioned at (2, 2), meaning its
  upper left corner is 2 pixels over from the left edge and 2 pixels
  down from the top edge. This element's size is 40x8, which means the
  coordinates of its lower right corner are (42, 10). (Not that that
  really matters, since all positioning in MPF is done off the upper
  left corner.
+ The shape element with the circle on it is positioned at (2, 12),
  meaning its upper left corner is 2 pixels over from the right and 12
  pixels down from the top. This is an example of where the positioning
  can seem confusing, because the pixel at (2, 12) is actually
  transparent, and to the viewer it wouldn't even appear like that
  circle has a pixel there. Since the size of the circle's bounding
  rectangle is 16x16, the lower right corner is at (18, 28).
+ Etc.


` `_



Elements can be positioned so they're off the slide, even using
negative numbers
----------------

It's possible for individual display elements to be positioned in such
a way that they are partially (or completely) off the side. That's
perfectly fine. In the diagram below:


+ We moved the "y" coordinate of the 123,456,789 text element from 2
  to -2, so now the top part of that element is off the slide. If you
  view this slide then it willstill show the parts of the element that
  are in bounds.
+ The "Free Play" text element is positioned at (25, 35), meaning it's
  completely off the slide. This is fully valid, and this element is
  still considered to be an element that's part of this slide. It's just
  that it doesn't happened to be positioned where anyone can see it.
  (Why would you want to do that? Several reasons, like if you wanted to
  create a really big slide and scroll it. More on that later.)
+ The circle shape element is positioned at (128, 32). At first you
  might think, "Hey, this display is 128x32, so if I want to put an
  element in the lower right corner, then I just position it at the
  max." Obviously this is wrong, as the diagram below shows, since the
  positions are based on the upper-left corners of elements. And to add
  insult to injury, if you position an element at (128, 32) on a display
  that's 128x32, you won't even see a single pixel! (Since the display
  coordinates start at (0, 0) instead of (1, 0), the lowest rightmost
  pixel on a 128x32 display is at position (127, 31). So your element
  positioned at (128, 32) is the first pixel off the edge in both
  directions. :)






Applying this Knowledge to your Game
------------------------------------

Ok, so now you've got the theory behind how elements are placed, how
do *you* actually go about placing display elements on a slide. Really
there are four settings you need to know about: `h_pos`, `v_pos`, `x`,
and `y`.



h_pos:
~~~~~~

This is "horizontal position", and it describeshow this element will
be placed on the slide horizontally. Valid options are `left`,
`center`, and `right`. The names are probably pretty self-explanatory.
If you set h_pos to `left`, then the element will be positioned on the
left edge of the slide. If you set it to center, then it will be
centered, and if you set it to right then it will be positioned on the
right. If you read the theory part above, you know that positioning
display elements in the center orthe right is actually kind of complex
since all the positional coordinates are based on the upper left
corner of an element. So even when we center an element, we still have
to figure out what the left position will be. Fortunately MPF does
this for you, so if you just say "center" then it will figure it out.
(The formula for centering, in case you're curious, is `(slide_width -
element_width) / 2`, and the formula for "right" positioning is
`slide_width - element_width`).



v_pos:
~~~~~~

This is "vertical position", and it's just like `h_pos` except it's
for `top`, `center`, or `bottom`.



x:
~~

This is the position for the "x" (horizontal) coordinate of your
display element. `x: 0` is the left edge of your slide. Increasing `x`
values move the display element to the right, and decreasing `x`
values move it to the left. The exact behavior of how your `x` value
effects the horizontal positioning of your element depends on a few
things:


+ If you specify an `x` value and you do *not* specify a `h_pos`
  value, then the `x` value is the actual "x" pixel position on your
  slide. (Remember this can be negative or it can be higher than your
  slide is wide.)
+ If you specify an `x` value and you also specify an `h_pos` value,
  then the `x` value represents the number of pixels of offset from that
  `h_pos`.
+ If you you specify an `x` value that is a decimal in-between 0 and
  1, then it will be treated as a percentage value. You can also use
  this with or without an `h_pos` setting.


Let's look at some examples since this can seem tricky until you
understand it.


::

    
    h_pos: center
    x: 2


Theelement will be positioned 2 pixels to the right of center.


::

    
    h_pos: right
    x: 2


Theelement will be positioned 2 pixels to the right of the right,
which means it will be extendingoff the right edge of the slide by two
pixels.


::

    
    h_pos: right
    x: -2


Theelement will be positioned 2 pixels to the leftof the right edge,
meaning there will be a 2-pixel gap between this element and the right
edge of the slide.


::

    
    h_pos: right
    x: -.1


Theelement will be positioned10% in from the right edge. Exactly how
far 10% is depends on the dimensions of your element. (These decimal
percentage values are really only useful for resizable on screen
windows when you want things to stay relative to each other. If you
have a fixed-resolution display in your machine, you can probably use
absolute pixels for everything.)


::

    
    x: 2


Theelement will be positioned 2 pixels to the leftof the left edge.
Note that if you do not include an `h_pos` value, it has the same
effect as including `h_pos: left` since the left edge is the "zero"
position for x.


::

    


If you don't specify an `x` or an `h_pos` value, then MPF will use the
default setting (as specified in the `dsplaydefaults:` section of your
config file. The out-of-the-box setting is `center`.



y:
~~

The `y` valueis just like `x`, except it relates to the vertical
position, and it bases its anchor on the `v_pos` value. We probably
don't have to go through an example here. Just remember that `y: 0` is
the top of the slide, and the negative `y` values move the
elementhigher up, and positive `y` values move the element down.



"Z-Ordering" (Layering) values
------------------------------

MPF also lets you specify what happens when you position two (or more)
display elements so that part (or all) of them overlap. In this case
you can specify layerswhich control which element is drawn on top of
the other elements. You can also control transparency settings
fordisplay elements, including whether the entire element should be
partially transparent, and/or whether specific pixels should be
transparent. (See the documentation for each display element for
details.)



layer:
~~~~~~

This is a numeric value of the layerof this element. Higher values
equal higher layers, so an element with a layerof 1 will be drawn on
top of an element with a layerof zero. There's no limit to the numbers
you can use here. You can use 0, 1, 2 or 100, 1000, 10000, or -2, -1,
0—it really doesn't matter. All that matters is the relative values
when the slide it being put together. The default layer(if you don't
specify one) is zero. It's totally fine for you not to specify a
layerfor 99% of your elements. You really only need it in the rare
cases where things are on top of each other.



opacity:
~~~~~~~~

This is a decimal value (between 0 and 1) which affects the overall
transparency of this display element. A value of zero means it's
totally clear (i.e. invisible), and a value of 1 means it's totally
opaque. The key here is that this opacity setting only affects the
overall opacity of the pixels which are not already transparent. Some
elements might have individual pixels which are already transparent,
and in those cases even if you have an opacity value of 1 here then
the transparent pixels will still be transparent. The default value is
1.



Where do you specify these positioning values?
----------------------------------------------

So now that you know all the details about how to position and
controldisplay elements, you're probably wonderinghow do you actually
do this? Where do you enter these values? Well, in a nutshell, you do
this in lots of places. Whereveryou create and/or configure a
displayelement, you also have the option of specifying `h_pos`,
`v_pos`, `x`, `y`, and `layer` values. (Or any combination of none,
some, or all of them.) For example:


+ In the ` `slideplayer:` section`_ of your config file, you create
  entries for different display elements you want to show on the display
  based on MPF events.
+ When you `create shows`_, you can add display elements into the
  `display:` section of astep, and those elements include these
  positional options.
+ If you're manually adding display elements to a slide (either via a
  `scriptlet`_or any other actual code you're writing), you can specify
  these positional values as arguments when you add a display element to
  a slide via the slide's `add_element()` method.


Here's an example of a Text element(from a show file) which has
several elements with positioning values: ` `_



These positional settingscombine with the display element's "other"
settings
--------

The last thing to keep in mind is that each type of display element
has its own settings you need to specify. For example, the `Text
element`_has settings for the text string, font, size, antialias,
etc., the `Animation element`_ has settings for the name of the
animation, frames per second, whether it repeats, etc. So in all
cases, you can mix and match these positional `h_pos`, `v_pos`, `x`,
`y`, and `layer` settings with the other settings that each element
needs.

.. _create shows: https://missionpinball.com/docs/shows/creating-shows/
.. _scriptlet: https://missionpinball.com/docs/programming-guide/scriptlets/
.. _display elements: https://missionpinball.com/docs/displays/display-elements/
.. _Text element: https://missionpinball.com/docs/displays/display-elements/text/
.. _Animation element: https://missionpinball.com/docs/displays/display-elements/animation/
.. _ section: https://missionpinball.com/docs/configuration-file-reference/slideplayer/


