How to create reusable widgets
==============================

This guide explains how you can create reusable "named" widgets that you can use again and again on multiple display
slides. This saves you from having to copy-and-paste the same widget (or sets of widgets) into multiple slide
configurations, it makes it easy to update and fine-tune your widget config since you only have to change it in one
place, and it lets you add individual widgets to the display that will show up regardless of what slide is currently
showing.

1. Understanding widgets
------------------------

Before we look at how to create reusable widgets, let's look at how regular widgets work in MPF.

You probably know that you can have a ``slides:`` section of your config (either machine-wide or mode-specific configs),
and when you define a slide, you can specify what widgets are on that slide, like this:

.. code-block:: mpf-config

   slides:
      my_slide:
         widgets:
            - type: text
              text: HELLO!
            - type: text
              x: 0
              font_size: 5
              text: YAY PINBALL
            - type: image
              image: background1

In the example above, the slide called *my_slide* has three widgets--two text widgets and a background image. (Remember
that the "z order" or "layer" of widgets is top-to-bottom, so the *HELLO!* widget is on top, then *YAY PINBALL* is next,
and they're both on top of the *background1* image.

These three widgets are permanently attached to the slide called *my_slide*. There's no way to reuse them on any other
slides.

2. Creating reusable widgets
----------------------------

But what if you had a widget you wanted to use on multiple slides? For example, maybe you have a widget with some
animations that comes on the display when a certain shot is made, and you want that widget to appear on any slide
(whichever slide happens to be showing at that time).

The way to do that is to create a "named" widget that's reusable. You do that in the ``widgets:`` section of your
config. (This can be either a machine-wide or a mode config file.)

For example:

.. code-block:: mpf-config

   widgets:
      laughing_jackal:
        - type: image
          image: jackal

Now you have a widget defined called *laughing_jackal* that you can add to any slide. (Note that this example is
simple, but any widget type with any widget settings can be defined here, including positioning, colors, animations, etc.

The only "catch" is that the list of widget names is global across MPF. So even though you can define widgets in both
the machine-wide or the mode config files, named widgets are processed when MPF starts up, so don't use the same name
twice since whichever one loads second will overwrite the first one.

3. Using your named widget
--------------------------

Now that you have a widget defined, how do you add it to a slide? That's done via the "widget" config player, which
means you can add a ``widget_player:`` section to a config file to trigger it based on an event, or you can add it
via the ``widgets:`` section of a show step. (All the examples in this guide will be based on the ``widget_player:``
section of a config file, but you can use them all in show steps too. Just use them in a ``widgets:`` section of a
show step and do not include the event name.

There are several options you can use in the widget player, depending on how you and where you want to show your
widget (which display, which slide, etc.)

"Express" config
~~~~~~~~~~~~~~~~

If you just want to add your widget to whichever slide is current on the default display, you can use the "express"
config, like this:

.. code-block:: mpf-config

   widget_player:
      some_event: laughing_jackal
      some_other_event: another_widget

With the config above, when the event *some_event* is posted, the widget called *laughing_jackal* will be added to
the current slide on the default display. Notice that you can add multiple entries here for different widgets and
different events.

This widget is added with whatever settings you defined for it in the ``widgets:`` section of your config. It's all
pretty straightforward, though you might have to play with the ``z:`` setting (the layer) to get it to show up. (For
example, if your current slide has a full size background, you'd want to configure your widget with a ``z:`` setting
that's a higher priority so it shows up on top of the background image.)

Adding a widget to a specific slide
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to add your widget to a particular slide (versus whatever slide happens to be showing at the moment), you
can do so by specifying that slide name in the ``widget_player:``. For example:

.. code-block:: mpf-config

   widget_player:
      some_event:              # event that will trigger this widget to show
         laughing_jackal:      # widget you want to show
            slide: my_slide

In the example above, when the event *some_event* is posted, the widget *laughing_jackal* will be added to the slide
called *my_slide*. If *my_slide* is the current active slide on the display, you'll see the widget appear. If that
slide is not being shown, the widget will still be added, and it will be there the next time that slide is shown.

Remember you can add as many events and widgets as you want to the ``widget_player:`` section of your config, and you
can even mix-and-match formats, like this:

.. code-block:: mpf-config

   widget_player:
      some_event:
         laughing_jackal:
            slide: my_slide
      some_other_event: another_widget

Adding a widget to a specific display target
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Rather than specifying a particular slide to add your widget to, you can target a display, and the
widget will be added "on top" of whatever slide is currently being shown:

.. code-block:: mpf-config

   widget_player:
      some_event:
         laughing_jackal:
            target: display1

Remember in MPF, display targets are the names of a display (dmd, window, etc.).

More details about this are in the :doc:`layers` guide.

Overriding named widget settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When you create your named widget, it contains a bunch of settings that are used to add it to a slide. (That's sort of
the whole point.)

However sometimes it's useful to be able to override or add additional settings at play time. You can do this in the
``widget_settings:`` section of the ``widget_player:`` in a config file or the ``widgets:`` section of a show step.

For example, if you use a
widget for the tilt warning like in the previous example, you'd probably want that widget to be removed after a few
seconds, which you could do like this:

.. code-block:: mpf-config

   widget_player:
      tilt_warning:             # event
         tilt_warning:          # widget name
            widget_settings:    # additional settings to be added / updated
              expire: 2s

(Technically speaking, if you were going to show a tilt warning widget, you'd probably also want to play a sound and
maybe flash all the lights on the playfield, so in your real game you're probably actually create a show to do this
and then play it via the ``show_player:`` section of your config and include the widget in the ``widgets:`` section
of the show, but you get the idea.)

You can also set the expiration time of a widget when you define the widget in the ``widgets:`` section of the config.
See the config file reference for details.

You can add/update any setting for the widget (color, text, position, animations, widget_styles, z (layer), etc.)

Removing widgets
~~~~~~~~~~~~~~~~

You can also use the widget player to remove named widgets from a slide that had been previous added. To do this,
just add an ``action: remove`` setting to the widget player, like this:

.. code-block:: mpf-config

   widget_player:
      show_jackal: laughing_jackal
      hide_jackal:
         laughing_jackal:
            action: remove

The config above will add the *laughing_jackal* to the current slide on the default display when the event *show_jackal*
is posted, and then it will remove it when the event *hide_jackal* is posted.

Creating named groups of widgets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All of the examples in this guide showed using a single widget as named widget. But you can actually define multiple
widgets in a named widget (essentially meaning that your named widget is really a named group of widgets. For example:

.. code-block:: mpf-config

   widgets:
     widget3:
     - type: text
       text: HI
       color: ff0000
       font_size: 100
     - type: text
       text: THERE
       color: 00ff66
       font_size: 100
     - type: text
       text: EVERYONE!
       color: ff00ff
       font_size: 100

You play, show, or hide this "widget" in the same way as every other example in this guide, except in this case, playing
*widget3* will actually add all three widgets to the slide. (Again you can play with z-order / layering, and
remember that each widget (even in a multi-widget group) can have its own z-order settings.

Putting it all together, these are the basics of using named widgets in MPF. The important takeaways are:

+ Widget names are global, so don't use the same name twice.
+ Everything here can be done in either the ``widget_player:`` section of a config file or the ``widgets:`` section of
  a show step.
+ All widget options are valid, including keys, animations, expiration, styles, positioning, z-ordering, colors,
  transparencies, padding, etc.
+ When "playing" a widget, you can target a display or a slide.
+ Once a widget is "played" and added to a slide, it becomes just another widget on that slide. The fact that it was
  put there by the widget player doesn't matter.

Adding multiple named widgets in one event
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can also add multiple named widgets from a single event. This is nice if you want to add widgets to
multiple displays or slides at the same time. For example:

.. code-block:: mpf-config

   widget_player:
      some_event:
         widget1:
            target: dmd
         widget2:
            target: lcd

Note that if you do this, the structure of YAML requires that you have at least
one setting under each widget name, so you can just add a ``target:`` or ``action: add``
if you don't want to change or set anything else in the widget.
