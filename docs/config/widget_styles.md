---
title: "widget_styles:"
---

# widget_styles:


--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

The `widget_styles:` section of your config is where you configure
styles for your widgets.

## Default styles for widget types

You can define defaults for certain
[widget types](../mc/widgets/index.md).
A widget will use the style `(name)_default` if no other style is
specified. For instance, a default style for all
[text widgets](../mc/widgets/text/index.md) would look like:

``` yaml
widget_styles:
  text_default:
    font_size: 21
    color: red
```

## Specifying widget styles

You can also specify re-usable styles and apply them to widgets. In the
following example, the text "HELLO" will render at font size 100:

``` yaml
widget_styles:
  big_style:
    font_size: 100
slides:
  slide1:
    - type: text
      text: HELLO
      style: big_style
```

You can supply multiple styles to a single widget, and they will be
applied in the order given.

``` yaml
widget_styles:
  warning_text:
    font_size: 12
    color: yellow
  bottom_left:
    anchor_x: left
    anchor_y: bottom
    x: 5
    y: 5
  hurryup:
    color: red
widgets:
  timer_runout:
    - type: text
      text: Hurry!
      style: warning_text, bottom_left, hurryup
```

In the above example, the text "Hurry!" will be anchored in the
lower-left of the display and rendered at size 12 and color red. Notice
that the color from the *hurryup* style overwrites the color from
*warning_text* style, because of the order the styles are listed in the
widget.

The config reference below is incomplete. You can use all settings of
your widget.

## Optional settings

The following sections are optional in the `widget_styles:` section of
your config. (If you don't include them, the default will be used).

### color:

Single value, type: `color` (*color name*, *hex*, or list of values
*0*-*255*). Default: `ffffffff`

The color of the widget.

## Related How To guides

* [Working with Fonts](../mc/widgets/fonts.md)
