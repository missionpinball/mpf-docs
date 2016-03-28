
One of the big changes for MPF in version 0.30 is that we're changing
the MPF media controller (mpf-mc) architecture. Previous versions used
a multimedia library called `Pygame`_, and starting in 0.30, we're
removing Pygame and replacing it with a library called `Kivy`_. (Check
out the `release notes`_ for details about the other stuff that's new
in MPF 0.30, as well as our `migration guide`_ if you're migrating
from MPF 0.21 to 0.30.)



What's a multimedia library?
----------------------------

Python at its core is a console-based programming environment. In
other words, there's nothing built-in to Python that handles graphics
and sounds. Pretty much all it can do is write text to the console and
beep. So in order for a Python app to control graphical windows and
audio, you have write your Python app so that it can talk to the
computer's graphics and sound subsystem. Doing this directly would be
a huge pain, because the way that graphics and sounds work in Windows
is different than Mac which is different than Linux. To address this,
there are cross-platform multimedia libraries that expose OS-specific
multimedia commands in a generic way. For example, these cross-
platform libraries let a programmer write commands like "open a
graphical window that is 800x600 pixels", and then the cross-platform
library on Windows will translate that to the DirectX calls to make
that happen, on Mac it will translate it to the Core Graphics
commands, etc. The same is true for everything graphics- and sound-
related. We can simply say, "put this image in the window," or "put
this text here," or "play this sound," and it's done. So that's what
we used Pygame for up until this point.



Why change?
-----------

Pygame has served us well for MPF versions 0.9 - 0.21. But there are
many limitations in Pygame that, when taken together, caused us to
want to find a different multimedia library to use. The limitations in
Pygame that have been holding back MPF include:


+ Pygame is not maintained anymore. The last release was in 2009,
  which means it only works with the versions of Python that were
  current in 2009.
+ Bugs that have been found since 2009 have not been fixed. (For
  example, the Mac version of Pygame has a memory leak which is why we
  can't support MPF on a Mac.)
+ The audio system in Pygame is very basic. It only allows 2-channels
  (no surround sound), 8 simultaneous voices, and a single music track.
+ Pygame does all of its graphical processing in the CPU, meaning it
  does not leverage the GPUs in modern computers. This leads to both
  lower performance and higher CPU usage. (Things that a GPU can do
  almost instantly take a lot of processing power if they're done on a
  CPU.)
+ Pygame only supports video if it's encoded into MPEG-1 format with
  very obscure settings which does not lead to high quality videos. (And
  Pygame on the Mac doesn't support video at all!)
+ Pygame cannot precisely control where the graphical window pops up
  on the screen, which is a problem for machines that have an LCD in the
  backbox that is partially obscured.




Introducing Kivy
----------------

After looking at many different options, we've decided to use a Python
library called `Kivy`_. Kivy is modern, well-supported, and actively
maintained. It's licensed with the MIT license (which is what MPF
uses). Kivy leverages OpenGL, SDL2, and the GPU (if a system has it)
and is easy to use for us as developers. Kivy is also designed to be a
complete application framework (rather than just a multimedia
library), which means that Kivy has a lot of functions built-in that
we had to build from scratch in the previous version of our MPF media
controller. (As a side note, remember that MPF's architecture
separates the MPF core engine from the media controller. So everything
we're talking about here with Pygame and Kivy only applies to the
media controller. The MPF core engine remains the same.)



The MPF Kivy-based Media Controller architecture & concepts
-----------------------------------------------------------

Much of the general concepts of the media controller do not change in
MPF 0.30. However we are updating a few terms to make them more
logical. A display is (usually) a physical thing that shows content,
like an on screen window, a DMD, or an RGB LED color DMD. Each display
has a slide frame which is responsible for showing slides and running
transitions between slides. (A transition is just an animated effect
as the display flips from one slide to another, like push, move,
slide, fade, flip, etc.) The main concept in the new media controller
is the slide. A slide is like a container which holds widgets. Widgets
are the individual elements you put on the slide. (These were called
"display elements" in previous versions of MPF.) There are different
types of widgets for different types of content: text, image, video,
shape, etc. You can animate widgets over time by changing their
properties to make them change color, size, rotate, etc. Any mode can
put any widget on any slide. (Or you can put a widget on top of the
current slide, for example if you want the credits mode to show a
quick pop up message that plays an animation when a coin is inserted
on top of whatever slide is current.) You don't have to create a new
slide for a mode, but you have the option to if you want. When a mode
stops, its widgets and slides will be removed. The following diagram
shows how it all fits together. Most of the time in your game, you'll
be focused on slides and widgets. Widgets and slides are all tied back
to modes in MPF. One of the new features in the new mpf-mc is that you
can add "sub slides" to a slide. You do this by adding a second slide
frame as a widget (which you can size and position however you want),
and then that sub-slide frame can manage its own slides and
transitions, each with its own widgets. This is how you would do
something like the "4-up" screen in *The Wizard of Oz* or how you'd
let a game mode "own" a section of the slide. (In the WOZ example
you'd have 4 slide frame widgets, each controlling its little portion
of the screen.) You can also add a widget to a slide which shows the
content from another display. For example, this is how you can add a
"virtual DMD" to an on screen window. Here's the overall architectural
diagram:



Changes to terminology with Kivy
--------------------------------

As part of this move to Kivy, we're going to rename many of the
concepts and components in the media controller so they match the
names that Kivy calls things. The names we used previously were
essentially made-up, and since people may need to search for how to do
things in Kivy, it makes sense that MPF calls things by the same names
that Kivy uses.
Old name New name Display Display Slide Slide none Slide Frame Display
Element Widget Transition Transition Decoration Animation Movie Video
Animation Image (but an animated type, like GIF or zip file of image
frames


How display stuff was configured in the PRIOR version
-----------------------------------------------------

We want to minimize the impact of changes to config files in MPF. That
said, the new mpf-mc will address several shortcomings in the prior
version, and in doing so, we have to make some changes. As a reminder,
here is how display content was controlled in the PRIOR version of
MPF: (1) Via `slide_player:` entries, like this:


::

    
    slide_player:
      some_event:
        - type: text
          text: foo
        - type: shape
          shape: line
        - type image
          image: hello
          (etc)


(2) Via `show_player:` entries, like this:


::

    
    show_player:
      some_event:
        show_name:
          tps: 5
          repeat: true
          (etc)


And then show yaml files would include slide settings for each step in
the show, like this:


::

    
    - tocks: 1
      display:
        - type: text
          text: foo
        - type: shape
          shape: box
          (etc)




Limitations of the PRIOR version
--------------------------------

In the past year, we've realized there were several limitations with
the way MPF handled the display, including:


+ Slides were "owned" by a mode. If you wanted to use the same slide
  in multiple modes, you had to copy+paste the same slide settings in
  multiple areas. This was annoying and meant that you had to change
  things in lots of places.
+ There was no way for slides to be reused.
+ The slide_player concept meant that events could only trigger
  complete slides. You couldn't just add a display element to an
  existing slide.
+ It was just about impossible to make compound slides with various
  parts of the slide getting content from different modes.
+ In general, it was all "slide-centric"




Changes for the NEW version
---------------------------

The big change is that you'll be able to define named slides like a
pool of assets. So you end up with all these slides. You can define
them in machine-wide config or mode configs.. whatever is easiest.
Like this:


::

    
    slides:
      slide_name_1:
        - type: text
          text: foo
        - type: image
          image: banana
      single_player_score:
        - type: text
          text: %score%
      (etc)


At this point you're just defining slides. They're not even tied to
modes yet. It's just slide names and widgets (& positioning &
layering). Then you can show slides via events, like this:


::

    
    slide_player:
      event_name:
        slide: screen_name_1
        transition:
          type: slide
          direction: right
          duration: 1s


This gives the advantage of being able to reuse slides from any mode.
Then you can also define widgets where you give them names. Again this
can be in mode config for machine wide config:


::

    
    widgets:
      some_widget_name:
        - type: text
          text: foo


You can also define groups of widgets:


::

    
    widgets:
      common_bottom:
        - type: text
          text: BALL %ball%
        - type: text
          text: PLAYER %num%


The idea there is you can apply those widgets to any slide based on
any event, like this:


::

    
    widget_player:
      some_event:
        - widget: common_bottom
          slide: some_slide_name


Or you could apply those widgets to whatever screen was current


::

    
    widget_player:
      some_event:
        - widget: common_bottom
          slide: %current%


All of these ( *slide_player:* and *widget_player:*) can have
additional settings for expiration time, layer, etc. You have the
option of defining widgets as either part of a slide definition (in
the *slides:* section) or as standalone widgets (or groups of widgets)
in the *widgets:* section. It really doesn't matter which. The only
reason there are two options is if you want to define entire slides at
once or more standalone widgets you can reuse and add to any slide.
(And even if you define an entire screen, you still have the option to
dynamically add widgets later.) todo: Adding sub-slide frames Can you
just add screen/widget definitions in slide_player and widget_player
sections?

.. _Kivy: http://kivy.org
.. _release notes: https://missionpinball.com/docs/mpf-0-30-release-notes/
.. _migration guide: https://missionpinball.com/docs/howto/how-to-migrate-from-mpf-0-21-to-mpf-0-30/
.. _Pygame: http://pygame.org


