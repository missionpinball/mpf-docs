
Pretty much every pinball machine has some type of display, whether
it's a set of 1980s-style 7-segment numeric displays, an early 90s-
style alphanumeric display, a dot matrix displays (DMD), or a modern
LCD (which itself can either by a small LCD, like a "color DMD", or a
huge one like what Jersey Jack has in the backbox of The Wizard of Oz
and The Hobbit). The `MPF media controller`_ is designed so that it
can support all types of these displays, including multiple different
types of displays at the same time. It supports text, drawing shapes,
images, and animations. You can position any combination of these on
the display at any time, and you can set layering and transparencies.
You can use standard TrueType fonts, and you can configure alternate
translations for text in multi-language environments. You can also
apply decorations and transitions to your displays and their elements.
And, like just everything else inMPF, you can do most of your display
configuration via the machine configuration files. Here are a few
photosof the MPF Media Controller's display system in action. These
were all created with the configuration files and without manual
programming. The first photo shows a traditional DMD with a single
text element. The second is on-screen window displaymade up of an
image element (the background), a virtual DMD element, a drawing
element (the thin white box around the DMD), and a text element (the
"Judge Dredd" words in the lower right corner). The third image
"color" DMD on an LCD monitor that you could install in your backbox,
and the fourth image is a full-color RGB LED matrix (so it's like a
color DMD, but a matrix of LEDs and not an LCD). ` `_` `_` `_` `_
Before we go into the details of all the various display components,
let's start with an overview of how the MPF display architecture
works. (If you don't care about the details and just want to start
using your display, you can jump directly into our `step-by-step
tutorial`_ which covers how to get your display running.) The MPF
Media Controller uses the same core architecture to power all kinds of
displays, regardless of whether it's a DMD (physical or virtual,
monochrome or color), an LCD (on screen window displays), or a
combination of both. The MPF Media Controller's display system is
based on `SDL`_1.2 (which it interfaces via `Pygame`_). Pygame & SDL
are prerequisites for the MPF Media Controller, and it won't run
without them. We put together an architecture diagram which details
how the MPF Media Controller's display system works. It's kind of
complex to look at, but we'll to step through it piece-by-piece. The
good news is that you don't have to understand all of itto use MPF.
(You can follow our `step-by-step tutorial`_ to get your display up
and running just with a few config file entries.)But as you start to
create more advanced display effects, it will be helpful to understand
how everything fits together. ` `_ The major components ofThe MPF
Media Controller's display system are:


+ Your game logic which is responsible for generating the content that
  will be displayed. This could come from `settings in your machine
  configuration file`_, entries in show files, or game code you write
  manually.
+ Every objectyou put on a display is called a ` Display Element `_.
  MPF supports several different types of display elements, each with
  their own settings and properties.

    + ` Text elements `_ let you display text.You can pick the font, the
      color, etc. The actual text strings in Text elements can be run
      through the Language module before they're sent to the display so you
      can do on-the-fly text replacements. This is used for multi-language
      translation and for installing alternate (i.e. "family friendly") text
      strings.
    + ` Image elements `_ let you show images.
    + ` Animation elements `_ let you play animations (i.e. videos). You
      can start and stop them, specify whether they should repeat, specify
      the playback rate, etc.
    + ` Shape elements `_ let you draw simple shapes onto the display.
      Boxes, lines, circles, etc.

+ Every display element lets you `specify its position on the
  display`_, either via pixel-level accuracy, or with positional
  keywords like "top", "center", "left", etc. You can also specify the
  layer(z-order) of elements to control which ones are drawn on top of
  each other if they overlap, and you can control alpha transparencies
  which affect how they blend with elements below them.
+ Next, you can apply ` Decorators `_ to elements which can cause them
  to sparkle, blink, pulse, etc. It's really easy to write your own
  custom decorators too.
+ You arrange all of your elements on a ` Slide `_. A slide is the
  same size of the display, so arranging various display elements on a
  slide is how you arrange them on the display. Every display has an
  "active" slide which is the slide that's currently being shown. It can
  also have one or more inactive slides that are waiting in the
  background to be shown later.
+ A ` Transition Manager `_ lets you use cool effects to transition
  from one slide to another. MPF ships with several different types of
  transitions (push, fade, reveal, flip, etc.), and it's really easy to
  write your own transitions if you'd like to make custom ones.
+ An ` MPF Display `_is a physical displayin your game. For example,
  the DMD is an MPF display, as is the on-screen window. MPF actually
  supports multiple simultaneous displays (each with their own unique
  sets of slides), so you can have an on screen window and a physical
  DMD at the same time, and they don't have to show the same content,
  (though they can if you want). You can even use the contents of one
  display as an "display element" that's part of another display. (For
  example you can have the DMD display show up in a portion of your on
  screen window while still showing other display elements around it.)
  We current have MPF Displays for the on screen window and the DMD, and
  we'll add a segmented display soon.




All these concepts come from PowerPoint. :)
-------------------------------------------

The creators of MPF (Brian Madden and Gabe Knuth) both have day jobs
as IT industry analysts, and we both give dozens of presentations per
year. In other words, we spend a lot of time with PowerPoint! If
you've ever used PowerPoint, you should notice that we used PowerPoint
(or Keynote or whatever presentation software you like) as the
conceptual model for MPF's display system. In PowerPoint, your content
is a series of " slides ." Each slide contains one or more " elements
." Those elements can be text , images , animations /videos, drawing
shapes , etc. Each element has a "size" (length & width), a "position"
on the slide (x, y coordinates), a "layer"which controls how it
overlaps with other elements, alpha transparencies, and
decorationeffects (blink, sparkle, spangly, etc). And even though your
entire PowerPoint presentation ismade of of lots of slides, only one
slide is active on your " display " at a time. Then when you changeto
another slide, you can have nice animated " transitions " from one
slide to the next. So if the MPF display system seems kind of complex,
just think of it like a giant PowerPoint presentation and it should
all hopefully make sense. Now let's start digging into some of the
details of each of the parts of the display system.

.. _Transition Manager: https://missionpinball.com/docs/displays/transitions/
.. _specify its position on the display: https://missionpinball.com/docs/displays/display-elements/positioning/
.. _Decorators: https://missionpinball.com/docs/displays/decorators/
.. _MPF media controller: https://missionpinball.com/docs/mpf-core-architecture/media-controllers/mpf-media-controller/
.. _MPF Display: https://missionpinball.com/docs/displays/displays/
.. _SDL: https://www.libsdl.org/
.. _Animation elements: https://missionpinball.com/docs/displays/display-elements/animation/
.. _Pygame: http://pygame.org/
.. _Display Element: https://missionpinball.com/docs/displays/display-elements/
.. _settings in your machine configuration file: https://missionpinball.com/docs/configuration-file-reference/slide_player/
.. _Image elements: https://missionpinball.com/docs/displays/display-elements/image/
.. _Text elements: https://missionpinball.com/docs/displays/display-elements/text/
.. _Slide: https://missionpinball.com/docs/displays/slides/
.. _Shape elements: https://missionpinball.com/docs/displays/display-elements/shape/
.. _step-by-step tutorial: /docs/tutorial
.. _step-by-step tutorial: https://missionpinball.com/docs/tutorial/


