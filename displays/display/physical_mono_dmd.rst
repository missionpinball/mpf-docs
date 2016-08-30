Using a traditional (single color) physical DMD
===============================================

This guide will show you how to use an traditional, physical DMD with MPF, like
this:

.. image::  /displays/images/display_mono_dmd.jpg

It will also show you how to create an on-screen popup window which will show
the contents of the DMD, like this (with a blank DMD):

.. image:: /displays/images/on_screen_basic_dmd_window.png

If you want to use a physical DMD without the on-screen equivalent, we'll show
you how to do that at the end.

If you want to only have an on-screen DMD without the physical one, like if
you want to replace the DMD with an LCD screen but still have it look like a
DMD, then read :doc:`this guide <adding_dot_look_to_lcd>` instead.

The final version of the relevant sections of your machine config for a
physical DMD with an on screen window too will look like
this:

::

    displays:
      window:
        width: 600
        height: 200
      dmd:
        width: 128
        height: 32
        default: true

    window:
      width: 600
      height: 200
      title: Mission Pinball Framework

    physical_dmd:
      shades: 16

    slides:
      window_slide_1:
      - type: dmd
        width: 512
        height: 128
        pixel_color: ff5500
        dark_color: 220000
      - type: text
        style: tall title
        text: MISSION PINBALL FRAMEWORK
        anchor_y: top
        y: top-3
        font_size: 30
        color: white
      - type: rectangle
        width: 514
        height: 130
        color: 444444

    slide_player:
      mc_ready:
        window_slide_1:
          target: window

1. Understand how physical, mono DMDs work
------------------------------------------

This guide explains how to config physical single-color (mono) DMDs. These are
DMDs that are connected to your FAST Pinball or P-ROC controller via the 14-pin
ribbon cable, like this:

.. image:: /displays/images/physical_dmd_in_backbox.jpg

It makes no difference whether you're using an LED or an original plasma gas
DMD. (Also it doesn't matter what color it is.)

2. Add your displays
--------------------

The first part of the config file above is where you create your logical
displays like we covered in the :doc:`index` section.

::

    displays:
      window:
        width: 600
        height: 200
      dmd:
        width: 128
        height: 32
        default: true

We're creating two displays here. The first is called "window" and
has a size of 600x200. This will be the display that shows up on the computer
screen.

The second display, which we're calling "dmd", will be the display that provides
the content for the physical DMD. This display is 128x32, which is the pixel
size of the DMD.

Notice that we set ``default: true`` for the dmd display. This is because as
we're creating display content in our game, we want it (by default) to show up
in the DMD (since that will be the primary display in our game).

Note that you don't set colors or anything here—this is just setting up the
logical displays which we'll use next.

3. Add your window configuration
--------------------------------

Next, we have a ``window:`` section which holds the settings for the actual
on screen window itself. In this case we're just configuring it to be 800x600,
with a window title of "Mission Pinball Framework".

::

    window:
      width: 600
      height: 200
      title: Mission Pinball Framework

Check out :doc:`Step 2. of the LCD guide <lcd>` for more details on this
window section, and be sure to check out all the window options in the
:doc:`/config/window` section of the config file reference.

Notice that in this case, we did not add the ``source_display: window``
setting to this section. That's because we have a logical display called
"window", and when you have that, the on-screen window will automatically use
that display as its source.

4. Configure the physical DMD
-----------------------------

Next, we'll make an entry to the config that let's MPF know that it should
connect to a physical DMD. This entry is pretty simple:

::

    physical_dmd:
      shades: 16

Again, this will only work if you're using a P-ROC (not a P3-ROC) or a FAST
Pinball WPC or Core controller, so you need to have the corresponding
``platform:`` entry for a hardware platform that supports physical DMDs.

The "shades" option is how many brightness shades you want. 1990s WPC machines
supported 4 shades, and mode Stern DMD machines support 16. Both the P-ROC and
FAST controllers support 16 shades (even on older 1990s plasma DMDs). Most
modern games will probably be 16 shades, but you can do 4 (or even 2) if you
want an old school look.

There are lots more options for the physical_dmd: section than just the
"shades" option listed here. Check the :doc:`/config/physical_dmd` for a list
of all the options.

Note that one option you do NOT have for pysical DMDs is the color. That's
because the color of the DMD is determined by the DMD itself. You don't actually
send it color values, rather, you just send it brightness levels, and the DMD
shows those brightness levels with whatever color the DMD is.

One final note, both the P-ROC and FAST Controllers support additional
platform configuration options for the physical DMDs to control
millisecond-level timing of how the image is displayed. Refer to the relevant
platform documentation for details.

5. Configure a window slide to show the on screen DMD
-----------------------------------------------------

Now we have a working on-screen window and a working physical. But if you run
``mpf both`` now, your on screen window will be blank because we haven't
built any slides to show up.

So in this step, we're going to build a slide for the on-screen window that will
be shown when MPF starts. We'll add some widgets to that slide to make it look
like the screen shot at the beginning of this guide.

First, create a ``slides:`` section in your machine config (if you don't have
one already), and then create an entry for the slide that we want to show. In
this case, we've decided to name that slide "window_slide_1". (Of course you can
call this slide whatever you want.

::

    slides:
      window_slide_1:

Next we have to add some widgets to that slide. (Refer to the
:doc:`documentation on widgets </displays/widgets/index> if your not familiar
with widgets yet.)

The first widget will be a :doc:`DMD widget </displays/widgets/widget/dmd>`
which is a widget which renders a logical display onto a slide in a way that
makes it look like a DMD:

::

      - type: dmd
        width: 512
        height: 128
        pixel_color: ff5500
        dark_color: 220000

Again, there are lots of options here. Note that we're adding a ``height:`` and
``width:`` of 512x128. This is the on-screen pixel size of the DMD as it will
be drawn in the window. In this case we chose an even multiple of the source
display for the DMD (which is 128x32), meaning that each pixel of the original
DMD will be rendered on screen as 4 pixels by 4 pixels. This is big enough
to get the circular "dot look" filter to look good, and being an even multiple
means that we won't have any weird moire patterns.

For the on screen DMD, we *are* able to select the pixel color, because this
is how the DMD will be drawn on the computer screen, and MPF has no idea what
color the actual DMD is. So you can pick any color you want here. We chose
``ff5500`` which is a classic DMD orange color.

The dark color is a light gray which will be the color of the pixels that are
off. This means that we'll be able to see
the "off" pixels in our on screen DMD, but if you don't want that, then just
pick a dark color that's the same as your background color.

There are other options listed in the
:doc:`DMD widget </displays/widgets/widget/dmd>` documentation to control
settings like how big the circles are versus the space in between them, the
ability to not have the "dot" filter, and the ability to set the "glow" radius
of each dot.

Note that in this case, we did not have to add the ``source_display:`` option
because we have a display called "dmd" which will automatically be used as the
source for the DMD widget.

Next, we also added two more widgets to this slide—a text widget with the
title of the machine, and a gray rectangle that's slightly larger than the DMD
to give it a nice border.

::

      - type: text
        text: MISSION PINBALL FRAMEWORK
        anchor_y: top
        y: top-3
        font_size: 30
        color: white
      - type: rectangle
        width: 514
        height: 130
        color: 444444

6. Configure the slide to show when MPF starts
----------------------------------------------

Now we have a nice slide with the virtual DMD on it, but if you run MPF, you
still won't see it because we didn't tell MPF to show that slide in the window.
So that's what we're doing here:

::

    slide_player:
      mc_ready:
        window_slide_1:
          target: window

If you don't have a slide_player: entry in your machine-wide config, go ahead
and add it now. Then create an entry for the :doc:`/config/mc_ready` event.
This is the event that the media controller posts when it's ready to be used,
so it's a good event for our use case.

Then under that event, create an entry to show the slide you just created in the
previous step. Notice that we also have to add the ``target: window`` entry to
tell the slide player that we want this slide to show on the "window" target.
We need to do this because the default display (from Step 2) is the DMD, so if
we don't specify a target, this slide will show on the default, which would be
the DMD, instead of being shown on the window. (In this case, we would show a
slide on the DMD which contains a DMD widget whose source is the DMD, and we'd
probably open up some kind of wormhole and destroy the universe. So don't do
that.)

And this point, you're all set! Of course there's no content on the DMD yet
because we haven't set up any slide_player entries to add content to it, but
that's something you can do by following the tutorial or looking at the guides
for the slides and widgets here.

7. What if you don't want the on-screen window?
-----------------------------------------------

There might be some scenarios where you just want the physical DMD with no
on-screen DMD. (For example, maybe you're using a low-power single board
computer and you don't have enough horsepower to run a graphical environment.)

This is fine. To do it, just remove the window-related components from the
config, resulting in something like this:

::

    displays:
      dmd:
        width: 128
        height: 32

    physical_dmd:
      shades: 16

In this case, you don't need the ``default: true`` entry for the dmd in the
displays: section because you only have one display, so it will automatically
be the default.

.. todo::

   We need more explanation of how to run with no window here.
