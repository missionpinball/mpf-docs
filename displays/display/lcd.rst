Using an LCD for a display
==========================

This guide will show you how to use an on-screen LCD window for your main
display. This would be like what Jersey Jack does in Wizard of Oz or The Hobbit.

Here's what the final version of the relevant sections of your machine config
file will look like. We'll step through everything one-by-one.

.. code-block:: mpf-mc-config

    displays:
      window:
        height: 600
        width: 800
    window:
      height: 600
      width: 800
      title: Mission Pinball Framework
      resizable: true
      fullscreen: false
      borderless: false
      exit_on_escape: true
      source_display: window

1. Add your display
-------------------

The first part of the config file is where you create your display called
"window" and set its size:

.. code-block:: mpf-mc-config

    displays:
      window:
        width: 800
        height: 600

This is just like we covered in the :doc:`index` section.

2. Add your window configuration
--------------------------------

Next you need to add a section to your machine config file which
has the settings for the actual on-screen popup window. This is configured in
the ``window:`` section.

Most of the settings here are pretty self-explanatory. The most important thing
is the ``source_display: window`` section which is where you specify which
display (from the ``displays:`` section of your config) will provide the
actual source content for your on-screen window.

(That said, if you only have one display, or if you have a display called
"window", then the on-screen window will automatically use that display for
its source, but we're just including it here for completeness.)

The other important thing to point out is that you have to specify the size
of your display and your window separately. In the example above, we have an
800x600 window showing the content from an 800x600 display. But we could, for
example, set the display to 400x300 while keeping the window at 800x600. In that
case, the display content would be "scaled up" to fit the window, meaning that
each source pixel would be 2x2. This would be how you'd do a low-res old-school
look on a modern high-def window.

You can play with the other settings to see how they affect things.
The full list of window options is in the :doc:`/config/window` section of
the config file reference. (Just be sure that you add them to the
``window:`` section of your config, not the "window" entry in the ``displays:``
section.) Check that out to see what else you can do.

.. note::
   At this time, the MPF Media Controller only supports a single LCD window
   at a time. If you want more than one LCD window, MPF 0.31 will let you run
   multiple instances of the MPF-MC at the same time—one for each window.

Now you have a working config, so you can read through the rest of the display
documentation to see how you can add slides and widgets to your display.

Also, if you want to make the content on your window look like dots, or if you
want to show a "virtual" DMD in your window, check out the other guides in this
section.

See :doc:`multiple_screens` for informations about using two or more LCDs.
