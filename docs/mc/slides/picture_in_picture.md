---
title: How to do "Picture in Picture" display
---

# How to do "Picture in Picture" display


MPF uses a [window](../../config/window.md) to
define the area on a screen that can be used to display graphics. This
window and be further subdivided into
[displays](../displays/index.md) that
define areas of the window onto which slides and their widgets can be
projected.

Here is an example of setting up a window and four displays in a config
file.

``` yaml
window:
  width: 1080
  height: 1300
  title: CupheadWindow
  resizable: true
  fullscreen: false
  borderless: true
  exit_on_escape: true
  top: 0
  left: 0

displays:
  insert:
    width: 100
    height: 100
  upper:
    width: 1040
    height: 280
  middle:
    width: 1040
    height: 580
  lower:
    width: 1040
    height: 320
```

A layout slide can then be made that sets the locations of each of these
displays on a window. The x and y locations are relative to the lower
left corner of the window. The order in which you define each widget
determines which widget has priority over the other widgets. In this
example the "insert"display is defined before the "lower" display so
the "insert" display will be drawn on top of the "lower" display.
This gives you a "picture-in-picutre" where the "insert" will appear
to be projected on top of the "lower" display.

``` yaml
slides:
  layout:
    background_color: blue
    widgets:
      - type: display
        width: 69
        height: 65
        x: 60
        y: 200
        anchor_x: left
        anchor_y: top
        source_display: insert
      - type: display
        width: 1040
        height: 280
        x: 20
        y: 1270
        anchor_x: left
        anchor_y: top
        source_display: upper
      - type: display
        width: 1040
        height: 580
        x: 20
        y: 940
        anchor_x: left
        anchor_y: top
        source_display: middle
      - type: display
        width: 1040
        height: 320
        x: 20
        y: 340
        anchor_x: left
        anchor_y: top
        source_display: lower
```
