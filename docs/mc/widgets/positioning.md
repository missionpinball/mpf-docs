---
title: How to position widgets on slides
---

# How to position widgets on slides


Probably the most important thing to know about putting widgets on
slides is how to position them.

## 1. Understanding MPF display coordinates

At the most basic level, every display slide has a resolution (always
conveyed in the order width, then height), and widgets have a position
on slide (horizontal, then vertical).

* The dimensions of the slide are always described *width* (x), then
    *height* (y). (So a 128x32 display is 128 pixels wide and 32 pixels
    tall.)
* The "zero" position is the lower-left corner. (Just like an x-y
    cartesian coordinate graph from school.)
* Since the `(0, 0)` position is the actual location of the lower-left
    corner pixel, the upper-right pixel is actually one less than the
    width and height of your slide. (e.g. a display that's 128 pixels
    wide has x positions 0 through 127.
* A widget's position is always described *horizontal* (x), then
    *vertical* (y). So a widget at position `(10, 20)` is 10 pixels in
    from the left edge and 20 pixels up from the bottom.

Here's a simple example that illustrates this:

![image](/docs/mc/images/widget_positioning_basics.png)

By the way, in MPF, the actual "pixel size" of the display as MPF sees
it is separate from actual pixels of the physical display. So you could
have a display in MPF that's 400x300 pixels, but you show that full
size on an LCD that's 1920x1200 pixels. MPF will automatically scale
the logical display to fit in the size of the window you configure on
the physical display. This is known as "resolution independence", and
is nice if you ever have to replace your LCD in the future and the new
one you buy doesn't have the same resolution as your old one.

## 2. Understanding widget "anchors"

In the diagram from the first step, the "position" of each widget is
set based on its lower-left corner. In real life, if you had to position
every widget based on its lower-left corner all the time, you'd go
crazy! For example, to "center" a widget, you'd have to calculate
what the x and y offsets were and then do some math, and then if you
animated the widget's size you'd have to recalculate it... it would
be a mess!

Fortunately MPF does all this math for you.

When you configure a widget in MPF, you can config its "anchor" point
(both `anchor_x` for the horizontal anchor and `anchor_y` for the
vertical anchor.)

A widget's anchor setting tells MPF what point on the widget is used to
position it on the slide. Here are some examples which show how various
anchor settings are applied to different widgets. The red bulls-eye
target represents the point that's used by MPF to position that widget
with each type of anchor settings.

![image](/docs/mc/images/widget_anchors.png)

## 3. Combing anchors and widget positioning

Now that you know how the coordinates and anchors work, let's look at
some examples that combine these two concepts:

![image](/docs/mc/images/widget_positioning_with_anchors_1.png)

In the diagram above, you can see how the bulls-eye anchor target is the
actual point of the widget that is positioned with each widget's `x:`
and `y:` settings.

You'll also notice that widgets can be fully or partially be positioned
outside the boundaries of a slide. (This is useful if you want to
animate a widget "entering" the slide from off screen--you'd
position the widget so it's outside the bounds of the visible window
and then animate it moving on.) Also note that positioning can be
negative. Negative x values are off the left edge of the slide, and
negative y values are off the bottom.

As you look at this example, you can probably start to see that
different anchors make sense for different types of positioning. For
example, if you have several widgets that you'd like to left-align,
then it makes sense to set their anchors to `anchor_x: left` and
positioning them based on their left edge.

By default, MPF uses the center of the widget for the anchor. This is
what you get if you do not include an `anchor_x:` or `anchor_y:`
setting. (Also the terms `middle` and `center` are interchangeable in
all widget anchor and positioning settings.)

## 4. Relative positioning

Even though anchors are powerful, it can still be kind of confusing to
position widgets based solely on `x:` and `y:` pixel values. After all,
you constantly have to think about how big your display is and do lots
of math to get your values set.

Fortunately MPF can use relative positions for a widget's `x:` and `y:`
values, as show here:

![image](/docs/mc/images/widget_positioning_with_anchors_2.png)

There are a lot of different options in this diagram, so let's go
through them one-by-one.

First, for `x:` values, you can use:

* `x: left` - Positions the anchor of the widget at the left edge of
    the slide
* `x: center` - Positions the anchor of the widget in the horizontal
    center
* `x: right` - Positions the anchor on the right edge

You can also use percentage values. The percentages are automatically
calculated based on the width of the slide. So if you set `x:50%` and
your slide is 800 pixels wide, the x value will be 400. (`x: 50%` is the
same as `x: center`.)

For `y:` values, you can use:

* `y: top` - Positions the anchor of the widget at the top of the
    slide.
* `y: middle` - Positions the anchor of the widget in the vertical
    middle.
* `y: bottom` - Positions the anchor on the bottom edge.

Again, you can also use percentages.

What's really cool is you can *also* combine relative words with pixels
and percentages. Some examples:

* `x: center+10` - Positions the x anchor of the widget 10 pixels to
    the right of the center position.
* `x: center-10` - Positions the anchor 10 pixels to the left of the
    center.
* `y: top-10%` - Positions the y anchor 10% below the top edge of the
    slide.

## 5. Try to use relative & percent positioning for everything

If you can manage to use relative (top/bottom/left/middle/etc.) and
percentage values for everything, then your display system will be
completely resolution independent!

Remember we said that the logical size of a display in MPF can be scaled
up to any size physical display. So if you build your configs for a
1024x768 display, and then a few years down the line, you install a
1600x1200 monitor, you can make one simple config change to tell MPF to
scale your 1024x768 up to the 1600x1200 display. That's fine, but you
won't have a display that's as crisp as it can be because the graphics
card will be scaling everything.

However, if you config all your widget positioning using only relative
positions and percentages, then if you get a new display in the future,
you can change the native logical resolution of your display in MPF and
then make full use of the full resolution. It would be like everything
instantly becoming high res!

## 6. Widget positioning offset adjustments

Another features of widget positioning in MPF is something known as an
"offset adjustment". So far we saw how anchors can be positioned in
the middle or an edge of the widget. The offset adjusts let you
fine-tune the position of the anchor so it can be anywhere--including
off the widget altogether!

Why would you want to do that? The main reason is that sometimes the
technical edge of your widget is not exactly in the position that makes
the most logical sense. A good example of this is text widgets. Many
fonts have bounding boxes that are a few pixels bigger than the actual
rendered text. For example, the text bounding box will allow for lower
case letters that hang down below the baseline, but most pinball
machines only use uppercase letters. This makes it hard to align the
baseline of your font because there is random space under it:

Consider the following example where you want to align the bottom of the
text with the bottom of the circle. The black areas represent the
visible pixels, and the gray area is the actual widget bounding box.
Even though this font is small (only 5 pixels tall, uses for small text
on a DMD), it still has two blank rows of pixels below every letter.
This means that if you set the `anchor_y: bottom` on both your text and
the circle, they will not actually be aligned:

![image](/docs/mc/images/widget_bad_offset.png)

What's even worst is that this font only has 1 extra row on top, so if
you want to center-align it with another widget you won't get the
actual center of the visible text.

Fortunately MPF has a way to deal with this in the form of anchor
adjustments. There are four adjustment values you can configure for a
widget:

* `adjust_top`
* `adjust_right`
* `adjust_left`
* `adjust_bottom`

All of these settings are optional. (They all default to `0`.)

You might think it's weird that there are top, right, left, and bottom
adjustments. Why not just have simple x and y adjustments? The reason is
because having four is easiest when you're actually laying out your
slides. For example, you might have a widget (like our text widget) with
different amount of extra space on the top versus the bottom. So letting
you specify an offset for the top and a separate offset for the bottom
means that you can anchor and position that widget by either the top or
the bottom and you don't have to mess with the adjusts each time. (It
also means that center anchors will actually be in the visual center of
the widget.) In other words, you set your adjustments once and never
have to worry about them again.

For all the adjustments, positive values move the edge of the widget
more towards the center (cutting off extra pixels), and negative values
move it more away from the center (adding padding)

Going back to the example from before, if we add `adjust_bottom: 2`,
that will move the adjustment point 2 pixels towards the middle, meaning
our bottom alignment now actually aligns:

![image](/docs/mc/images/widget_good_offset.png)

Negative values have the effect of adding padding to widgets, which can
also be nice as you're aligning and distributing things.

The only other thing to know about adjustments is that they only affect
the positioning of the widget. Adjustments are not cropping, and they
will not "cut off" or "trim" the widget.

## 7. Widget position rounding

Sometimes a center-anchored or percentage-based widget will end up at a
position with a fractional pixel. High-resolution displays have no
trouble smoothing out partial pixels, but low-resolution displays (like
DMDs) may render the widget blurry.

You can prevent MPF-MC from positioning widgets on pixel fractions with
the `round_anchor_x:` and `round_anchor_y:` setting, either locally on a
widget or globally on the display. When present, this setting will force
MPF-MC to round fractional anchor positions in the specified direction.

* `round_anchor_x: left` - Round the horizonal pixel position down
* `round_anchor_x: right` - Round the horizonal pixel position up
* `round_anchor_x: center` - Do not round the pixel position (default)
* `round_anchor_y: bottom` - Round the vertical pixel position down
* `round_anchor_y: top` - Round the vertical pixel position up
* `round_anchor_y: center` - Do not round the pixel position (default)

![image](/docs/mc/images/widget_anchor_rounding.png)

This setting is valid on `widgets` and `displays`. If you have a display
and a widget both configured for rounding, the widget's setting will
take priority.

## 8. Widget positioning can be done in styles

One of the powerful features of widgets in MPF is that you can configure
widget styles, which are like buckets of settings that are applied and
merged into widget settings. You can put any widget settings you want in
a style (and then specify the style to be applied to a widget in the
`style:` setting in a widget config, a slide config, a show, or a widget
player).

Styles can be used in several different ways. For example, you can
configure a style for text widgets which has the font name, font size,
and adjustments so you can simply add `style: big` to a widget and
everything will be there.

You can also put `x:` and `y:` settings in styles and use them to
position and size the widgets on different parts of your display. For
example, you might have an area of the screen that always shows some
kind of status message, and even though that might be used throughout
your game, you might always want the same font, alignment, size, and
positioning no matter what's there. So you can define a style called
`info_zone` and then any text widget that uses that style will always
show up in the right place. (You can also use styles for z-order and
animations, so you can use a style to define popups and other things
that you'll use over and over.)

See the How To guide on widget styles for details.

## 9. Putting it all together

So now you've seen all the options for positioning and placement of
widgets. But how do you actually use them? Simple. Everything discussed
here are just regular widget settings. So you can use them in slides:

``` mpf-mc-config
slides:
  slide1:
    widgets:
      - type: text
        text: MY WIDGET
        x: left+10%
        y: top-10%
        adjust_bottom: 2
#! slide_player:
#!   show_slide: slide1
##! test
#! post show_slide
#! advance_time_and_run .1
#! assert_text_on_top_slide "MY WIDGET"
```

You can use them in [named widgets](reusable_widgets.md):

``` mpf-mc-config
widgets:
  my_cool_widget:
    - type: text
      text: MY WIDGET
      x: left+10%
      y: top-10%
      adjust_bottom: 2
#! widget_player:
#!   show_widget: my_cool_widget
##! test
#! post show_widget
#! advance_time_and_run .1
#! assert_text_on_top_slide "MY WIDGET"
```

You can use them in the widget player:

``` mpf-mc-config
widgets:
  my_widget:
    - type: text
      text: "MY WIDGET"
widget_player:
  some_event:
    my_widget:
      widget_settings:
        x: left+10%
        y: top-10%
        adjust_bottom: 2
##! test
#! post some_event
#! advance_time_and_run .1
#! assert_text_on_top_slide "MY WIDGET"
```

And you can use them in shows:

``` mpf-mc-config
# in your machine config
widgets:
  my_widget:
    - type: text
      text: "MY WIDGET"
#! show_player:
#!   start_show: test_show
##! show: test_show
# in your show
- duration: 1
  widgets:
    my_widget:
      widget_settings:
        x: right-15.4%
        y: top
##! test
#! post start_show
#! advance_time_and_run .1
#! assert_text_on_top_slide "MY WIDGET"
```
