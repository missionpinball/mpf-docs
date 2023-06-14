---
title: Slide player
---

# Slide player


The *slide player* is a
[config player](index.md) in
the MPF media controller that is used to play slide content, including
showing slides, hiding slides, and removing slides. (This player is part
of the MPF media controller and only available if you're using MPF-MC
for your media controller.)

Note that the slide player is a
[config_player](index.md),
so everything mentioned below is valid in the `slide_player:` section of
a config file *and* in the `slides:` section of a show step. You can
test slides and widgets interactively using
[Interactive MC (iMC)](../tools/imc.md).

Full instructions on how to use the slide_player are included in the
[How to Show a Slide on a Display](../mc/slides/showing_slides.md) guide.
The documentation here is for reference later.

Generically-speaking, there are two formats you can use for slide_player
entries: "express" and "full" configs. Express configs will look
like this:

``` mpf-mc-config
#! slides:
#!   slide1: []
#!   slide2: []
#!   slide3: []
slide_player:
  event1: slide1
  event2: slide2
  event3: slide3
```

Full configs will look like this:

``` yaml
slide_player:
   event1:
      slide1:
         <settings>
   event2:
      slide2:
         <settings>
   event3:
      slide3:
         <settings>
```

In both cases, these configurations are saying, "When *event1* is
posted, show *slide1*. When *event2* is posted, show *slide2*. Etc."

This "express" config is down-and-dirty, with no options, to just show
slides. The full config lets you specify additional options (based on
the settings detailed below).

For example, the following config will show *slide_1* when *some_event*
is posted, but it will also override the default settings and show the
slide on the display target called *display1* and at a priority that's
200 higher than the base priority.

``` mpf-mc-config
#! slides:
#!   slide_1: []
#! displays:
#!   display1:
#!     width: 1366
#!     height: 768
#!     default: true
slide_player:
  some_event:
    slide_1:
      target: display1
      priority: 200
```

## Showing dynamically-created slides

Both of the examples so far assumed that you were using the slide player
to show a slide that had already been defined in the
[slides:](../config/slides.md) section if your config.
However you can also define slides right in-line in your slide player.

The following config will show a slide called *slide_1* when the
*some_event* is posted, but it assumes that *slide_1* does not yet
exist, and it contains a list of widgets (one text widget and one
rectangle widget) which will be added to that slide.

Note that slide names are global in MPF, so if you already had a slide
defined called *slide_1* and you redefine it in your slide player like
the example below, this new slide will become *slide_1* and the old one
will be gone.

``` mpf-mc-config
slide_player:
  some_event:
    slide_1:
      widgets:
        - type: text
          text: I AM A TEXT WIDGET
        - type: rectangle
          width: 200
          height: 100
          color: red
```

You can also mix-and-match defining a slide in the slide player as well
as adjusting properties of how the slide is shown. Just add multiple
settings, like this:

``` mpf-mc-config
slide_player:
  some_event:
    slide_1:
      widgets:
        - type: text
          text: I AM A TEXT WIDGET
        - type: rectangle
          width: 200
          height: 100
          color: red
      transition: wipe
```

Remember that these slide player settings can also be used in show steps
(in a `slides:` section). Any of the examples above apply, you just
don't include the event name, like this:

``` mpf-mc-config
##! show: show1
#show_version=5
- time: 0
  slides: slide1
- time: +3
  slides: slide2
- time: +3
  slides:
    slide3:          # newly-defined slide here
      widgets:
      - type: text
        text: I AM SLIDE 3 IN THIS SHOW
        color: lime
- time: +3
  slides:
    slide4:
      transition:
        type: move_out
        duration: 1s
        direction: up
```

Here's a list of all the valid settings for individual slides in the
`slide_player:` section of your config file or the `slides:` section of
a show. Note that all of these are optional. Any that you do not include
will be automatically added with the default values applied.

## Usage in config files

In config files, the slide player is used via the `slide_player:`
section.

## Usage in shows

In shows, the slide player is used via the `slides:` section of a step.

## List of settings and options

Refer to the [slide_player](../config/slide_player.md) section of the config file reference for a full explanation
of how to use the slide player in both config and show files.

## Config Options

See [slide_player:](../config/slide_player.md) for config
details.
