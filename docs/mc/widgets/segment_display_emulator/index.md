---
title: Segment Display Emulator widget
---

# Segment Display Emulator widget


The segment display emulator widget is used to emulate hardware segment
displays on a [slide](../../slides/index.md).

Here's an example:

``` yaml
#config_version=5
slide_player:
  mc_ready:
    display_slide:
      - type: segment_display_emulator
        name: display1
        character_count: 7
        character_slant_angle: 0
        character_spacing: 20
        segment_width: 0.11
        segment_interval: 0.04
        segment_off_color: 4b4c4a30
        segment_on_color: fe961bff
        side_bevel_enabled: true
        dot_enabled: true
        comma_enabled: true
        text: "HELLO"
        width: 600
        height: 150
        y: 100
```

The example above results in the following:

![image](../../images/widget_segment_display_emulator.png)

## Settings

``` yaml
type: segment_display_emulator
name:
text:
flash_mode:
flash_frequency:
flash_mask:
display_type:
character_count:
character_spacing:
character_slant_angle:
padding:
background_color:
segment_off_color:
segment_on_color:
segment_width:
segment_interval:
bevel_width:
side_bevel_enabled:
dot_enabled:
comma_enabled:
character_map:
width:
height:
rotation:
scale:
```

!!! note

    Segment Display Emulator widgets also have "common" widget settings
    for position, opacity, animations, color, style, etc. Those are not
    listed here, but are instead covered in
    [common widget settings](../common_settings.md) page.

Also remember that all widget settings can be controlled via
[widget styles](../styles.md), rather than you having to set every setting on every
widget.

The following segment display emulator widget settings may be
[animated](../animation.md):
`x:`, `y:`, `width:`, `height:`, `segment_on_color:`, `opacity:`,
`rotation:`, and `scale:`.

### type: segment_display_emulator

Tells MPF that this is a segment display emulator widget.

### name:

The segment display name. This value is used to uniquely identify the
segment display emulator widget when updating it using the
[Segment Display player](../../../config_players/segment_display_player.md)
in MPF. The value here must match the name assigned in the
[segment_displays:](../../../config/segment_displays.md) device section
of your config. This value is only required if you wish to control the
segment display emulator widget with the
[Segment Display player](../../../config_players/segment_display_player.md).

### width:

The width of the segment display emulator widget (in pixels). This value
is required.

### height:

The height of the segment display emulator widget (in pixels). This
value is required.

### text:

The text characters to display in the widget. This value is required. If
you don't want an initial text value, use "".

### flash_mode:

The current display flash mode. Options include:

`off`

:   The segment display does not flash (flashing is off). This is the
    default.

`all`

:   All characters in the display will flash.

`match`

:   Only the last two characters in the display will flash.

`mask`

:   The `flash_mask` parameter determines which characters in the
    display will flash.

### flash_frequency:

The number of times per second the display should flash. The default is
`1.0`.

### flash_mask:

Contains the flash mask string to use when flashing in mask mode. Each
character of the flash mask string represents a character in the
display. Character positions with an `F` character will be flashed while
any other character will not flash. The default is `None` (no characters
will flash). As an example, `FFFFFFFF________` will flash the first 8
character positions of a 16 character display which the last 8
characters will not flash. Note the `_` character could be replaced with
any other character (other than `F`). You can use whatever character you
wish for the non-flashing character positions.

### display_type:

The type of display (7 segment, 14 segment). Options include:

`7seg`

:   The segment display emulates a 7-segment display.

`14seg`

:   The segment display emulates a 14-segment display. This is the
    default value.

### character_count:

The number of character positions in the widget. The size of each
character is determined by the widget size and the width is divided by
the character count to get the character width.

### character_spacing:

The space between each character/element (in pixels). The default value
is `10`.

### character_slant_angle:

The angle at which the characters are slanted (degrees from vertical).
The default value is `0`.

### padding:

The padding (empty space) around the display (in pixels). The default
value is `20`.

### background_color:

The background color of the display widget, in rgba format. The default
value is `000000ff` (black).

### segment_off_color:

The color of a segment that is off, in rgba format. The default value is
`4b4c4aff` (gray).

### segment_on_color:

The color of a segment that is on (active) for each character in the
display in rgba format. If a single color is supplied, all characters in
the display will be set to that color. This parameter can be animated
and also controlled using the
[Segment Display player](../../../config_players/segment_display_player.md).See [Specifying Colors in Config Files](../../../config/instructions/colors.md) for more information on specifying colors in config files.

### segment_width:

Width of each segment (as a decimal percentage of character width). The
default value is `0.16` (16%).

### segment_interval:

Spacing between segments (as a decimal percentage of character width).
The default value is `0.05` (5%).

### bevel_width:

Size of segment bevels (as a decimal percentage of character width). The
default value is `0.06` (6%).

### side_bevel_enabled:

Determines if the sides of each character should be beveled (`true` or
`false`). The default value is `true`.

### dot_enabled:

Determines if an integrated dot/period should be displayed in each
character (`true` or `false`). The default value is `false`. When this
is enabled, dot/period characters in the current `text` parameter value
will be combined with the character immediately prior to the dot/period
character and the dot segment will be on for that character (the dot
will not use it's own character position in the display).

### comma_enabled:

Determines if an integrated comma should be displayed in each character
(`true` or `false`). The default value is `false`. When this is enabled,
comma characters in the current `text` parameter value will be combined
with the character immediately prior to the comma character and the
comma segment will be on for that character (the comma will not use
it's own character position in the display).

### character_map:

The `character_map` parameter allows custom character segment mappings
(which segments are on/off for each text character sent to the display).
This advanced feature is useful for creating your own special characters
or simply overriding the default mappings for any individual character.
For more information on segment display character mappings, see [David
Madison's Segmented LED Display - ASCII Library page](https://github.com/dmadison/LED-Segment-ASCII).
This parameter is a dictionary with integer keys and values (key is the ascii
character ordinal number, value is the segment bit mapping as an integer).

* [How to setup and use the virtual segment display emulator](how_to.md)
