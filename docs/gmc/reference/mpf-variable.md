---
title: MPFVariable
---

# MPFVariable

`MPFVariable` is a Godot node class provided by the MPF-GMC extension. It is derived from the Godot `Label` node and offers all the features and functionality of a Label, plus some built-in methods for displaying MPF game data.

## Node Configuration

An `MPFVariable` node can be placed anywhere in a slide or widget and will automatically update itself based on its configured parameters.

### comma_separate:

Single value, type: `boolean`. Default: `false`

When checked, the (presumed numeric) value of the variable will be comma-separated into thousands before being rendered on screen.

### format_string:

Single value, type: `String`. Default `None`

This is a string that can be used to format multiple variables and include other text beyond just the variable value. This uses the `{}`-style string format method and is compatible with all Godot format method features.

When using `format_string`, the slide player config settings, tokens, and event args will be combined into a dictionary for use in the formatting.

For detailed usage of format methods, see [GDScript String Format Method](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_format_string.html#format-method-examples) in the Godot documentation.

!!! note "format_string vs template_string"

     The `variable_name` has no effect on `format_string`, and can only be used with `template_string`.

     In an MPFVariable, the `format_string` and `template_string` are exclusive and if both are provided, only `format_string` will be used.

### initialize_empty:

Single value, type: `bool`. Default `false`

If checked, this MPFVariable will initialize as empty when it is created for a slide or widget. This does not effect variables that are derived from player or machine variables, or event args from the event that triggers the slide/widget containing the MPFVariable.

### max_players:

Single value, type: `integer`. Default: `0`

If greater than zero, the MPFVariable will only appear when the total number of players in the game is less than or equal to this value.

This is useful for featuring larger or extra information on one-or-two-player games that becomes hidden to make room for more player scores.

### min_digits:

Single value, type: `integer`. Default: `0`

This is the minimum number of digits the (presumed numeric) value will display. If the value is less than the minimum number, it will be left-padded with zeroes to fill in the minimum number of digits.

### min_players:

Single value, type: `integer`. Default: `0`

If greater than zero, the MPFVariable will only appear when the total number of players in the game is greater than or equal to this value.

This is useful for player number indicators and other players' scores in multiplayer games that don't make sense to display on games with fewer players.

### template_string:

Single value, type: `String`. Default `None`

This is a string that can be used to format the variable and include other text beyond just the variable value. This uses the `%`-style format string and is compatible with all Godot format string features.

For detailed usage of format strings, see [GDScript Format Strings](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_format_string.html) in the Godot documentation.

!!! note "format_string vs template_string"

     In an MPFVariable, the `format_string` and `template_string` are exclusive and if both are provided, only `format_string` will be used.

### update_event:

Single value, type: `String`. Default `None`

This is the name of an event that will trigger this variable to update. Only applicable to variables of type *"Event Arg"*.

### variable_name:

Single value, type: `String`. Default: `None`

This is the name of the variable that will be displayed. It will be looked up based on the player number (for player variable type), machine settings (for machine variable type), or the triggering event's arguments (for event variable type).

Has no effect when a `format_string` is provided.

### variable_type:

Single value, type: `String`. Default: `"Current Player"`

This is the source of the variable that will be looked up and displayed. *"Current Player"* is the current player of the game, while *"Player 1"* through *"Player 4"* are those specific players. *"Machine"* will display a machine variable, and *"Event Arg"* will display a keyword argument passed by an event.

!!! note "Up to 4 Players"

    `MPFVariable` currently supports a maximum of four players for player-specific variables. If you need more than this, please let us know!
