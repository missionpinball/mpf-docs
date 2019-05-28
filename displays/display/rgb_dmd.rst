Using an RGB full-color LED DMD
===============================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/displays`                                                      |
+------------------------------------------------------------------------------+

MPF supports RGB full-color LED DMDs. There are several hardware options you
can use for this: :doc:`/hardware/dmd_platforms`.

This guide shows you how to configure MPF to use one of these displays.

By the way, these RGB LED DMDs have been called "real" Color DMDs in the forums
since the displays are arrays of RGB LEDs rather than an LCD monitor running a
display that is made to look like a DMD. Many people like these better
than LCD-based displays because they're brighter and more vibrant, and
the blacks are actually black since the LEDs are off versus LCD
displays which have blacks are are actually dark gray.

.. image:: /displays/images/display_rgb_dmd.jpg

We will also show you how to create an on-screen popup window which will show
the contents of the DMD, like this (with a blank DMD):

.. image:: /displays/images/on_screen_basic_dmd_window.png

If you want to use a physical RGB DMD without the on-screen equivalent, we'll
show you how to do that at the end of this guide.

If you want to only have an on-screen DMD without the physical one, like if
you want to replace the DMD with an LCD screen but still have it look like a
color DMD, then read :doc:`this guide <adding_dot_look_to_lcd>` instead.

The final version of the relevant sections of your machine config for a
physical RGB DMD with an on screen window too will look like
this:


1. Add your displays to your MPF config
---------------------------------------

Next, add the DMD display to your list of displays in your machine-wide config
file:

.. code-block:: mpf-config

    displays:
      window:
        width: 600
        height: 200
      dmd:
        width: 128
        height: 32
        default: true

The example above contains two displays. The first is named "window" and
has a size of 600x200. This will be the display that shows up on the computer
screen. (Again, if you just want the DMD without an on-screen window, we'll
show you how to do that later, but for now it's probably easiest to create a
screen window so you can see what's happening with the display if you're working
on your game without a physical machine attached.)

The second display, which we're calling "dmd", will be the display that provides
the content for the physical RGB DMD. This display is 128x32, which is the pixel
size of the DMD. If you have a different size DMD, enter the size (in pixels)
here.

Notice that we set ``default: true`` for the DMD display. This is because as
we're creating display content in our game, we want it (by default) to show up
in the DMD (since that will be the primary display in our game).

2. Add your window configuration
--------------------------------

The ``window:`` section of the machine-wide config holds the settings for the
on-screen display window. If you don't have this section, add it now.

You can make the width and height anything you want. In this case we're just
configuring it to be 600x200 with a window title of "Mission Pinball
Framework".

.. code-block:: mpf-config

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

3. Configure a window slide to show the on screen DMD
-----------------------------------------------------

Now we have a working on-screen window and a working physical RGB DMD. But if
you run ``mpf both`` now, your on screen window will be blank because we haven't
built any slides to show up.

So in this step, we're going to build a slide for the on-screen window that will
be shown when MPF starts. We'll add some widgets to that slide to make it look
like the screen shot at the beginning of this guide.

First, create a ``slides:`` section in your machine config (if you don't have
one already), and then create an entry for the slide that we want to show. In
this case, we've decided to name that slide "window_slide_1". (Of course you can
call this slide whatever you want.)

.. code-block:: mpf-config

    slides:
      window_slide_1:

Next we have to add some widgets to that slide. (Refer to the
:doc:`documentation on widgets </displays/widgets/index>` if you're not familiar
with widgets yet.)

The first widget will be a :doc:`display widget </displays/widgets/display/index>`
with a :doc:`color_dmd effect </displays/widgets/display/effects>`
which is a widget which renders a logical display onto a slide in a way that
makes it look like a DMD:

.. code-block:: mpf-config

   slides:
      window_slide_1:
         - type: display
           effects:
            - type: color_dmd
           width: 512
           height: 128

Again, there are lots of options here. Note that we're adding a ``height:`` and
``width:`` of 512x128. This is the on-screen pixel size of the DMD as it will
be drawn in the window. In this case we chose an even multiple of the source
display for the DMD (which is 128x32), meaning that each pixel of the original
DMD will be rendered on screen as 4 pixels by 4 pixels. This is big enough
to get the circular "dot look" filter to look good, and being an even multiple
means that we won't have any weird moire patterns.

There are other options listed in the
:doc:`color_dmd effect </displays/widgets/display/effects>` documentation to control
settings like how big the circles are versus the space in between them, the
ability to not have the "dot" filter, and the ability to set the "glow" radius
of each dot, color tint, limiting the color palette, etc.

Note that in this case, we did not have to add the ``source_display:`` option
because we have a display called "dmd" which will automatically be used as the
source for the color DMD widget.

Next, we also added two more widgets to this slide—a text widget with the
title of the machine, and a gray rectangle that's slightly larger than the DMD
to give it a nice border.

.. code-block:: mpf-config

   slides:
      window_slide_1:
         - type: display
           effects:
            - type: color_dmd
           width: 512
           height: 128
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

4. Configure the slide to show when MPF starts
----------------------------------------------

Now we have a nice slide with the virtual DMD on it, but if you run MPF, you
still won't see it because we didn't tell MPF to show that slide in the window.
So that's what we're doing here:

.. code-block:: mpf-config

    slide_player:
      init_done:
        window_slide_1:
          target: window

If you don't have a slide_player: entry in your machine-wide config, go ahead
and add it now. Then create an entry for the :doc:`/events/init_done` event.
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

5. What if you don't want the on-screen window?
-----------------------------------------------

There might be some scenarios where you just want the physical DMD with no
on-screen DMD. (For example, maybe you're using a low-power single board
computer and you don't have enough horsepower to run a graphical environment.)

This is fine. To do it, just remove the window-related components from the
config.

In this case, you wouldn't need the ``default: true`` entry for the dmd in the
``displays:`` section because you only have one display, so it will automatically
be the default.

6. Configure your RGB DMD Hardware
----------------------------------

At this point you have two displays configured, and you have default content
showing up in both of them. The final step is to add the configuration for your
physical RGB DMD so that MPF can talk to your hardware.

The exact steps to do that vary depending on which DMD hardware platform you've
chosen, so click on the one you have from the list below and follow the final
instructions there to get everything set up.

* :doc:`SmartMatrix </hardware/smartmatrix/index>`
* :doc:`RGB.DMD </hardware/eli_dmd/index>`
* :doc:`FAST Pinball RGB DMD </hardware/fast/rgb_dmd>`
