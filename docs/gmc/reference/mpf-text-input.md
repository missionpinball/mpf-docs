---
title: MPFTextInput
---

# MPFTextInput

`MPFTextInput` is a Godot Node class provided by the MPF-GMC extension. It renders an on-screen keyboard and accepts button inputs to highlight, select, and submit user-input text.

## Node Configuration

An `MPFTextInput` node can be placed anywhere in a slide or widget and is configured with the following properties.

### allow_space:

Single value, type `bool`. Default `True`

If enabled, a special "SPACE" key will be added to the end of the on-screen keyboard for users to input a space.

### allowed_characters:

Single value, type `String`. Default `"ABCDEFGHIJKLMNOPQRSTUVWXYZ"`

This is the list of characters that will appear in the on-screen keyboard. There is no delimiter—each character present in the string will be rendered as an input key.

### display_node:

Single value, type `Node`.

A `Label` or `RichTextLabel` node to render the current text string.

If `RichTextLabel` is used and `preview_character` is enabled, the preview character will have a highlight animation to indicate it's preview state.

### grid_width:

Single value, type `int`. Default `0`

The width (in pixels) of the grid that the keyboard will lay out in. If zero, the characters will have their natural width. If a character is wider than the defined grid width, it will be extended to the nearest multiple to maintain proper appearance.

!!! note "Updates may not sync"

    Due to nuances in the Godot Editor, changing the `grid_width` and character font sizes may not always reflect accurately. It's recommended to close and reload the scene after saving one before adjusting the other.

### input_name:

Single value, type `String`. Default `"high_score"`

This is the name of the text input, which is used to identify input presses from MPF and submit the text back to MPF.

### max_length:

Single value, type `int`. Default `10`

The maximum number of characters that can be input. When this limit is reached, the highlight will automatically move to END and additional character selections will be ignored.

### preview_character:

Single value, type `bool`. Default `True`

If selected, the currently highlighted character will be rendered at the end of the text string to preview what the string will look like after the character is added.

If not selected, characters will only appear in the display node after they are selected.

### Text Formatting:


#### character_appearance:

Single value, type `LabelSettings`.

A `LabelSettings` resource that will be applied to the characters of the on-screen keyboard. A saved file can be provided with *Quick Load*, or a resource created directly within the node by clicking *New LabelSettings*.

#### highlight_color:

Single value, type `Color`.

A color that will be applied to the highlight pulse animation to indicate the current highlight character on the keyboard.

#### special_appearance:

Single value, type `LabelSettings`.

A `LabelSettings` resource that will be applied to the special characters (SPACE, DEL, END) of the on-screen keyboard. A saved file can be provided with *Quick Load*, or a resource created directly within the node by clicking *New LabelSettings*.

If no settings are provided, the `character_appearance` will be applied to the special characters.

## Events and MPF Integration

To control the on-screen keyboard from the pinball machine, an `event_player` must be setup that sends the event *"text_input"* with an appropriate `action` value (one of "left", "right", or "select").

``` yaml
event_player:
  s_flipper_left_active:
    text_input:
      action: left
  s_flipper_right_active:
    text_input:
      action: right
  s_start_button_active:
    text_input:
      action: select
```

When the END key on the on-screen keyboard is selected, GMC will post an event *text_input_\<input_name\>_complete* where input_name is the `input_name` value of the MPFTextInput node.

This event will include an argument `text` with the text string entered by the user.