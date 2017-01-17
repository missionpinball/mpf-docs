Common Settings that Apply to All Widget Types
==============================================

The following settings are "common" settings that apply to all :doc:`types of widgets </displays/widgets/index>`:

::

   type:
   x:
   y:
   anchor_x:
   anchor_y:
   opacity:
   z:
   animations:
   reset_animations_events:
   color:
   style:
   adjust_top:
   adjust_bottom:
   adjust_left:
   adjust_right:
   expire:
   key:

type:
~~~~~
Specifies the type of widget, such as ``type: text`` or ``type: image``. This setting
is required (since MPF needs to know what kind of widget it is).

x:
~~

The horizontal position of the widget on the slide. This setting can be entered
in several ways:

* Absolute position: a number like ``0``, ``200``, or ``-50``
* Relative position entered as a percent: ``20%`` or ``-12%``
* A positional keyword: ``left``, ``center``, or ``right``
* A combination of positional keyword and a value: ``left+10%``, ``right-5``

The default value is ``center``.

See the :doc:`widget positioning </displays/widgets/positioning>`
documentation for full details on how to position a widget on a slide.

y:
~~

The vertical position of the widget on a slide. This setting can be entered
in several ways:

* Absolute position: ``0``, ``200``
* Relative position entered as a percent: ``20%``
* A positional keyword: ``top``, ``middle``, or ``bottom``
* A combination of positional keyword and a value: ``bottom+10%``, ``top-5``

The default value is ``middle``.

See the :doc:`widget positioning </displays/widgets/positioning>`
documentation for full details on how to position a widget on a slide.

anchor_x:
~~~~~~~~~

The horizontal "anchor" point of the widget which specifies what point on the
widget is used for the horizontal positioning. Valid options are
``left``, ``center``, and ``right``.

The default value is ``center``.

See the :doc:`widget positioning </displays/widgets/positioning>`
documentation for full details on how to position a widget on a slide.

anchor_x:
~~~~~~~~~

The vertical "anchor" point of the widget which specifies what point on the
widget is used for the vertical positioning. Valid options are
``left``, ``center``, and ``right``.

The default value is ``center``.

See the :doc:`widget positioning </displays/widgets/positioning>`
documentation for full details on how to position a widget on a slide.

opacity:
~~~~~~~~

A value from 0 to 1 which controls the opacity (or transparency) of the widget.
You can use decimal values between 0 and 1 for partial transparency.

* Completely transparent (e.g. invisible): ``0``
* Completely opaque (e.g. normal): ``1``
* 50% transparent: ``0.5``

The default value is ``1``.

Note that some widget types allow you to set values greater than 1, which will
have the effect of making the "glow" of the widget brighter. This isn't a great
effect, but it could be useful in some cases.

.. caution::

   Note that opacity values are 0 to 1, not 0 to 100. If you set
   ``opacity: 100`` then that's really like 10,000% opacity and your widget will
   probably look really weird.

z:
~~

Specifies the "layer" or "z-order" of the widget. Higher z values mean that if
parts of two widgets overlap on the slide, the one with the higher value will
be drawn on top of the one with the lower value. (e.g. ``z: 100`` will be drawn
on top of ``z: 99``.)

The default drawing order of widgets is controlled by the order the widgets
are listed in the slide, widget group, or widget_player config entry. So usually
you don't need to manually set the z value, instead just put them in the
order you want in your config.

However, being able to manually set the z value is nice if you want to add a
widget to an existing slide and have it appear above and below certain widgets.

The default z value is ``0``.

If you do want to add a widget with a particular z order to an existing slide,
you'll probably have to set those existing widgets to a z value other than 0.

animations:
~~~~~~~~~~~

Contains a list of events and the animated widget properties and steps for each
of those events. See the
:doc:`widget animation documentation </displays/widgets/animation>` for
details.

reset_animations_events:
~~~~~~~~~~~~~~~~~~~~~~~~

A list of events which are used to reset the widget to its original settings and
stop all running animations. See the
:doc:`widget animation documentation </displays/widgets/animation>` for
details.

Note that this seems like a grammatical error, since it's "animations events", but
it's correct in this case because this setting is for a list of events that resets
the widget animations (since animations themselves are a list of separate animations).

color:
~~~~~~

Sets the color (and opacity) of the widget. This is pretty straightforward for
most widget types (like text and the various shape widgets). If you set this for
an image or video widget, it will have the effect of "tinting" the widget with
the color you specified.

You can enter this as a hex color string or a color name. See the
:doc:`color instructions </config/instructions/colors>` for details.

If you're entering hex strings, you can enter either 6 or 8 characters. The
first six characters are RGB values (``00``-``ff`` each), and the final is the
opacity (``00``-``ff``). If you don't enter an opacity, ``ff`` (fully
opaque) is used.

The default value is ``ffffffff`` which is white at 100% opacity.

style:
~~~~~~

The name of the style you want to apply to this widget. Note that styles must
be previously defined someone in your config in order to use them. Also you can
override any setting from the style by also manually including it in the
widget config. See the :doc:`style documentation </displays/widgets/styles>`
for details.

The default value is ``None`` which means no style is used.

adjust_top:
~~~~~~~~~~~

Redefines the top point of the widget when used in positioning to compensate for
widgets that have visual top points that don't align with their technical top
points.

The default value is ``None``.

See the :doc:`widget positioning </displays/widgets/positioning>`
documentation for full details on how widget positioning offset adjustments
work.

adjust_bottom:
~~~~~~~~~~~~~~

Redefines the bottom point of the widget when used in positioning to compensate
for widgets that have visual bottom points that don't align with their technical
bottom points.

The default value is ``None``.

See the :doc:`widget positioning </displays/widgets/positioning>`
documentation for full details on how widget positioning offset adjustments
work.

adjust_left:
~~~~~~~~~~~~

Redefines the left point of the widget when used in positioning to compensate
for widgets that have visual left points that don't align with their technical
left points.

The default value is ``None``.

See the :doc:`widget positioning </displays/widgets/positioning>`
documentation for full details on how widget positioning offset adjustments
work.

adjust_right:
~~~~~~~~~~~~~

Redefines the right point of the widget when used in positioning to compensate
for widgets that have visual right points that don't align with their technical
right points.

The default value is ``None``.

See the :doc:`widget positioning </displays/widgets/positioning>`
documentation for full details on how widget positioning offset adjustments
work.

expire:
~~~~~~~

Sets a time (such as ``expire: 2s``) for this widget to be removed from the
slide once it's added to it. This is useful with the widget_player when you want
to add a widget to an existing slide and then remove it again.

The default value is ``None``.

key:
~~~~

Specifies a "key" name which is assigned to the widget which you can later use
to target this widget if you want to do something to do (change a property,
remove it, etc.) You don't need to specify keys for every widget—only for the
ones that you want to target later.

See the :doc:`documentation on widget keys </displays/widgets/keys>` for
details.
