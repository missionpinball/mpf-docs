---
title: Widget player
---

# Widget player


The *widget player* is a [config player](index.md)
that's used to add or remove widgets to existing slides on a display.
(This player is part of the MPF media controller and only available if
you're using MPF-MC for your media controller.)

Note that the widget player is a [config_player](index.md),
so everything mentioned below is valid in the `widget_player:` section
of a config file *and* in the `widgets:` section of a
[show step](../shows/content.md).

Full instructions on how to use the slide_player are included in the
[Widgets](../mc/widgets/index.md) section of the
documentation. The stuff here in the config reference is for reference
later. You can test slides and widgets interactively using
[Interactive MC (iMC)](../tools/imc.md).

Generically-speaking, there are two formats you can use for
widget_player entries: "express" and "full" configs. Express configs
will look like this:

``` yaml
#! widgets:
#!   widget1: []
#!   widget2: []
#!   widget3: []
widget_player:
  event1: widget1
  event2: widget2
  event3: widget3
```

Full configs will look like this:

``` yaml
widget_player:
   event1:
      widget1:
         <settings>
   event2:
      widget2:
         <settings>
   event3:
      widget3:
         <settings>
```

In both cases, these configurations are saying, "When *event1* is
posted, add widget *widget1*. When *event2* is posted, add *widget2*.
Etc."

This "express" config is down-and-dirty, with no options, to just add
widgets to the current slide on the default display. The full config
lets you specify additional options (based on the settings detailed
below).

For example, the following config will add *widget_1* when *some_event*
is posted, but it will also override the default settings and add widget
to the slide called *slide_2*, even if that's not the current slide
that's showing.

``` yaml
#! widgets:
#!   widget_1: []
widget_player:
  some_event:
    widget_1:
      slide: slide_2
```

## Usage in config files

In config files, the widget player is used via the `widget_player:`
section.

## Usage in shows

In shows, the widget player is used via the `widgets:` section of a
step.

## Config Options

See [widget_player:](../config/widget_player.md) for config details.
