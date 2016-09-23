Hovering widgets "above" slides
===============================

It's possible play widgets so that they ride "on top" of a slide instead of being attached to the slide itself.
This is useful for things like tilt warnings that you might want to pop up on top of whatever slide is current,
but you want the widget to stay on the display even if the slide transitions to another slide behind it.

So in this case, the widget is attached to a display target rather than being attached to a slide.

In versions of MPF prior to 0.30.3, this was done be specifying a negative ``z:`` setting for a widget. In MPF 0.30.3
and newer, this is done by adding a ``target:`` setting to the widget player.

For example:

::

   widgets:
      tilt_widget:
         - type: text
           text: TILT WARNING
           expire: 2s

   widget_player:
      tilt_warning:
         tilt_widget:
           target: dmd

In the above example, when the event *tilt_warning* is posted, the widget *tilt_widget* will be shown on the display
called "dmd" on top of whatever slide happens to be showing. And if the slide changes while the widget is showing, the
widget will stay there since the widget is attached to the display instead of the slide.

You can use any display target for the ``target:`` setting, which can be a display from the ``displays:`` section of
your machine config, or a ``slide_frame:`` that's on another slide.

.. note::

   In older versions of MPF where you attached a widget to a parent display with a negative z-value, you could specify
   that value as part of the widget's properties setting. That's no longer possible though since it didn't make sense
   in a lot of cases and caused bugs. Now you can only specify the target of a widget in the ``widget_player:``.