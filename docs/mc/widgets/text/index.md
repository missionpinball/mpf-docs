---
title: Text Widget
---

!!! warning "MPF-MC is being deprecated"

    This instruction page is for the legacy MPF-MC for MPF versions 0.57 and prior. For users of MPF 0.80 and later, please refer to the [Godot Media Controller (GMC) Documentation](../../../gmc/index.md)

# Text Widget


The text widget is used to show text on a
[slide](../../slides/index.md).

![image](../../images/text_widget1.jpg)

In addition to being able to specify static text, text widgets also
include powerful functionality:

* You can configure dynamic text that is automatically updated (in
    real time) based on the value of a player variable or a machine
    variable.
* You can configure a placeholder "text string" that uses a lookup
    value to get its actual text. This is useful for things like
    multi-language support, or to be able to have different text strings
    based on a configuration file (family-friendly versus R-rated text,
    etc.)
* You can configure fonts and font styles to be automatically applied
    to text, and you can override them on a widget-by-widget basis.

You can also use
[bitmap fonts](../bitmap_fonts.md) to customize fonts for your machine.

## Settings

Here are a list of the settings you can use for text widgets:

``` yaml
type: text
text:
font_size:
font_name:
bold:
italic:
casing:
number_grouping:
min_digits:
halign:
valign:
outline_color:  # added in MPF 0.56.1
outline_width:  # added in MPF 0.56.1
```

!!! note

    Text widgets also have "common" widget settings for position, opacity,
    animations, color, style, etc. Those are not listed here, but are
    instead covered in
    [common widget settings](../common_settings.md) page.

Also remember that all widget settings can be controlled via
[widget styles](../styles.md), rather than you having to set every setting on every
widget.

The following text widget settings may be
[animated](../animation.md):
`x:`, `y:`, `font_size:`, `color:`, `opacity:`, `rotation:`, and
`scale:`.

### type: text

Tells MPF that this is a text widget. This setting is required when
using text widgets.

### text:

This value is required. If you don't want text, use ""

Your text can contain placeholders as described in
[dynamic text](text_dynamic.md).

Newline characters ([n](#)) are supported in text values to
create multiple lines with line breaks, however you must surround the
text with quotes or the backslash will be treated as a printing
character and will appear in the output. For example:

``` yaml
text: "Multiple\nlines"
```

will create multiple text lines with a line break, while the following
will not:

``` yaml
text: Multiple\nlines
```

### font_name:

The name of the font you want to use. This is the name only, without the
file extension. For example:

Correct:

``` yaml
font_name: arial
```

Wrong:

``` yaml
font_name: arial.ttf
```

There's a lot that goes into fonts, so we have a whole section on
[fonts](../fonts.md) which
you should read.

Usually fonts are controlled via
[widget styles](../styles.md). Also, if you're using a DMD or color DMD (or other
pixel-style display), we have some
[built in DMD fonts](../dmd_fonts.md) that you can use which are pre-configured for DMDs.

### bitmap_font:

A true/false value indicating whether the [font_name:](#)
setting contains the name of a
[bitmap_font](../../../config/bitmap_fonts.md)
asset. When set to [True](#), [font_name:](#) must
refer to an existing bitmap_font asset name and [font_size:](#)
will be ignored. When set to [False](#),
[font_name:](#) should refer to a font name.

### font_size:

The size of the font (in points). Default is 15.

See the
[full documentation on fonts](../fonts.md) for details.

### bold:

Boolean (True/False or Yes/No) which controls whether this font is bold.
Note that this setting attempts to over-draw the font a few times to
make it look bold, so the results are often not that great. You're
better off finding an actual bold version of your font and using that
font instead.

The default setting is `False`.

### italic:

Boolean (True/False or Yes/No) which controls whether this font is
italicized. Note that this setting simply skews the font when it's
drawn, so the results are often not that great. You're better off
finding an actual italicized version of your font and using it instead.

The default setting is `False`.

### casing:

A string value that changes the casing of the text on the widget.
Available values are:

* "lower": all characters will be lower case
* "upper": ALL CHARACTERS WILL BE UPPER CASE
* "title": All First Characters Are Capitalized
* "capitalize": Only the first character is capitalized

The default setting is `None` and the characters are displayed as-is.

### number_grouping:

Boolean (True/False or Yes/No) which controls whether you want the
separator between digits. In other words, it converts `1234567` into
`1,234,567`.)

Note that this setting will search through the text string for digits
and then insert the commas. In other words, if your text is "YOU SCORED
12345 POINTS", then it will convert it into "YOU SCORED 12,345
POINTS" even though the text is a mix-and-match of letters and numbers.

The default setting is `False`. (Note that prior to MPF 0.30, the
default setting was `True`.)

!!! note

    Currently this setting only inserts a comma. We need to add a setting to
    allow other characters (like a period which is common in Europe). If
    this is you, post a message to the forum and we'll bump up the priority
    on our to-do list.

### min_digits:

Configures the minimum number of digits for the text to be displayed.
This setting adds zeros to the left for digits that are shorter than the
setting.

This is typically used in score displays, since pinball machines usually
show a score as `00` instead of `0` when the player starts the game and
has no points.

So for most machines, you'd add `min_digits: 2` to your text widgets
which show the player's score.

The default setting is `0`.

### halign:

Specifies the horizontal alignment of the text within the bounding box.
Note that this setting *is not used* to align a widget on the screen.
(See the [How to position widgets on slides](../positioning.md)
documentation for details on that.)

This setting is almost never used in MPF because the bounding box of a
text widget is automatically created and sized based on the actual text
and font chosen.

The default setting is `center`.

### valign:

Specifies the vertical alignment of the text within the bounding box.
Note that this setting *is not used* to align a widget on the screen.
(See the [How to position widgets on slides](../positioning.md)
documentation for details on that.)

This setting is almost never used in MPF because the bounding box of a
text widget is automatically created and sized based on the actual text
and font chosen.

The default setting is `middle`.

### outline_color:

Added in MPF 0.56.1.

The color of the text outline. Default is black, but also the default outline width is 0, so you won't see it unless you set the outline width to something greater than 0.

### outline_width:

Added in MPF 0.56.1.

The width of the text outline. Default is 0, which means no outline. You can also use dynamic placeholders here.

### anchor_y: baseline

Text widgets have an additional `baseline` option in addition to the
other baseline options detailed in the
[common widget settings](../common_settings.md) documentation.

## Examples

The example config files section of the documentation contains
[examples of text widgets](../../../examples/index.md).

[text_dynamic](text_dynamic.md)
[text_strings](text_strings.md)
