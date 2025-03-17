---
title: Widget Keys
---

# Widget Keys


Widget keys are used to uniquely identify instances of widgets which you
can later use to update or remove the widget.

Note that you can you can also identify widgets by name (which is almost
always more straightforward). You only need to use a key if you want to
put multiple instances of the same widget on the same slide, and then
you need a way to identify a individual ones to update or remove them.

## Adding the Same Widget Multiple Times

When adding the same widget to a slide or target simultaneously, keys
are used to differentiate the widgets from one another. An important
aspect to note is that only one instance of a specific widget can be
modified with a given event for the widget_player. This means that if
you want to add the same widget multiple times, you need to have unique
events to call each widget. This can be done in one of two ways, which
are shown below.

### Using the Same Event With Different Priorities

This is an example using priorities of the events, which will affect the
priority:

``` yaml
#! widgets:
#!   widget_1: []
widget_player:
  some_event.1:
    widget_1:
      key: widget_1_1
      slide: slide_2
      widget_settings:
         # <list of settings below go here>
  some_event.2:
    widget_1:
      key: widget_1_2
      slide: slide_2
      widget_settings:
         # <list of settings below go here>
```

It will add widget_1 to slide_2 two different times. In order to make
this meaningful, you would want to add additional `widget settings:`,
such as position, rotation, color, opacity, etc. This is important,
otherwise it will add the widget with the same settings twice, which
would overlap each other.

### Using the Same Event With Different Conditional Logic

An additional method would be to have unique events that call the same
widget multiple times. This could be done in one of two ways: completely
unique events (example: event_1 and event_2) or by using conditional
logic on the same event (example: event_1{param1} and event_1{param2}.

This is an example using unique conditional formatting for the same
event:

``` yaml
#! widgets:
#!   widget_1: []
widget_player:
  some_event{parameter_1 <10}:
    widget_1:
      key: widget_1_1
      slide: slide_2
      widget_settings:
         # <list of settings below go here>
  some_event{parameter_1 < 50}:
    widget_1:
      key: widget_1_2
      slide: slide_2
      widget_settings:
         # <list of settings below go here>
```

It will add widget_1 to slide_2 if the conditional criteria is met. If
the criteria is met for both of the events, they will both be played at
the same time. If they are both played at the same time, you would
likely want to add additional widget settings, such as position,
rotation, color, opacity, etc. This is important, otherwise it will add
the widget with the same settings twice, which would overlap each other.

## Remove or Update a Specific Widget Instance

To remove or update a specific instance of a widget from the page, you
need to refer to the key of that widget. This is done by the following
code, which has calls upon the generic widget and the key when an event
is posted.

``` yaml
#! widgets:
#!   widget_1: []
widget_player:
  some_event:
    widget_1:
      key: widget_1_1
      action: remove  #this could also be update
      widget_settings:
         # <list of settings below go here>
```

The above block of code would listen for some_event to occur, and then
remove the instance of widget_1 with the key widget_1_1. You can also
use the `action: update` and a set of `widget_settings:` to update the
widget with the new properties.
