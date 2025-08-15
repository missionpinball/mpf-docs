---
title: "slides: Config Reference"
---

# slides: Config Reference

--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**YES** :white_check_mark:|

The `slides:` section of your config is where you pre-define "named"
slides that you can then use later in shows and the slide_player section
of a config file. See the
[How to Show a Slide on a Display](../mc/slides/showing_slides.md) guide
for details on this. You can test slides and widgets interactively using
[Interactive MC (iMC)](../tools/imc.md).

Slide names are universal throughout MPF, so if you create two slides
with the same name---even in different modes---one of them will
overwrite the other and things will be confusing, so don't do that.

See the [How to create slides](../mc/slides/creating_slides.md)
documentation for full details on how to create slides. (You should
definitely "learn" about slides there. The settings here are mostly
used for reference later.)

There are several different ways you can enter slides. In all cases,
you'll have a `slides:` section of your config, and then under that,
you'll have sub-entries which are slide names. But what is entered
under each slide name varies.

**Option 1: Slide with a widget**

If you want to define a slide that only has a single widget, you can
just add the
[widget's properties](../mc/widgets/types.md) under the slide name. In the example below, we're defining
two slides, one called *my_slide_1* and the other called *my_slide_2*,
and they each only have a single widget.

``` yaml
slides:
  my_slide_1:
    type: text
    text: THIS IS MY SLIDE
  my_slide_2:
    type: text
    text: THIS IS ANOTHER SLIDE
    color: lime
    font_size: 25
```

**Option 2: List of widgets**

Of course many slides you'll define will have more than one widget. To
add multiple widgets to a slide, just enter them like you entered a
single widget, but use a dash (and a space) to dictate where a new
widget starts, like this:

``` yaml
slides:
  my_slide_1:
    - type: text
      text: THIS IS MY SLIDE
    - type: image
      image: johnny_5
  my_slide_2:
    - type: text
      text: THIS IS ANOTHER SLIDE
    - type: text
      y: 20%
      text: IT HAS MORE THAN 1 WIDGET
    - type: ellipse
      color: red
      width: 200
      height: 100
```

**Option 3: Widgets under "widgets:" section**

In addition to widgets, slides have other options (as described below),
and sometimes you might want to define a slide that has widgets and
slide settings. To do that, you need to move your widgets definition
into a sub-section called "widgets:", and then you can add the other
slide settings under the slide along with the widgets.

Here's an example. Note that the slide with multiple widgets is using
the dash in the widgets: section to separate the individual widgets.

``` yaml
slides:
  my_slide_1:
    background_color: red
    widgets:
      type: text
      text: THIS IS MY SLIDE
  my_slide_2:
    widgets:
      - type: text
        text: THIS IS ANOTHER SLIDE
      - type: text
        y: 20%
        text: IT HAS MORE THAN 1 WIDGET
      - type: ellipse
        color: red
        width: 200
        height: 100
    expire: 2s
    transition:
      type: move_in
      direction: right
```

You can mix-and-match the three options for entering widgets as needed
within the same slides: section of your config.

## Creating a blank slide

If you want to create a blank slide (perhaps an empty canvas that
you'll populate via the widget player later?), then you need to tell
the slides: section that you have an empty list. In YAML, that's done
with a \[ and \] next to each other (which is confusing because it looks
like a rectangle, but it's not, like this: `[]`.

You can use this format to create a blank slide with no options:

``` yaml
slides:
  my_blank_slide: []
```

Or you can use it to create a blank slide with options, but no widgets,
like this:

``` yaml
slides:
  my_blank_slide:
    background_color: red
    widgets: []
```

## Settings

The following sections provide additional options for your slide which
you can use if you move the widgets into their own `widgets:` section.
If you just include the widgets as top-level entries (like Options 1 and
2 above), then the default values for each of these settings below will
be used.

### background_color:

Single value, type: `color` (*color name*, *hex*, or list of values
*0*-*255*). Default: `000000ff`

The background color of the slide. Details on how to enter color values
are [here](instructions/colors.md).

### debug:

Single value, type: `boolean` (`true`/`false`). Default: `false`

Set to true/yes if you want to add addition debug information about this
slide to the log. (Note this requires a verbose log to see.)

### expire:

Single value, type: `time string (secs)`
([Instructions for entering time strings](instructions/time_strings.md)). Defaults to empty.

Sets an expiration time which will automatically remove this slide. If
it's showing when it's removed, the next-highest priority active slide
will be shown in its place.

Note that you can also configure expiration when the slide is shown (in
either a show or via the slide_player), so you don't need to define an
expire setting as part of the slide definition unless you want that
expire time to be used every time the slide is shown.

If you specify an expire time in both places, the expire time in the
slide_player or show will take precedence.

### opacity:

Single value, type: `number` (will be converted to floating point).
Default: `1.0`

Sets the overall opacity of the slide. A value of 1.0 is fully opaque. A
value of .5 means the slide is 50% transparent, and a value of 0 means
the slide will be invisible and you'll probably be confused about why
it's not showing up.

### transition_out:

Note that you can also configure a transition when the slide is shown
(in either a show or via the slide_player), so you don't need to define
a transition as part of the slide definition unless you want that
transition to be used every time the slide is shown.

If you specify a transition in both places, the transition in the
slide_player or show will take precedence.

## Related How To guides

* [Slides](../mc/slides/index.md)
