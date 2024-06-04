---
title: MPFConditional
---

# MPFConditional

`MPFConditional` is a Godot node class provided by the MPF-GMC extension that conditionally shows or hides itself when added to the screen.

!!! note

    The `MPFConditional` node does not subscribe to variable changes, and only calculates the condition when first rendering and when updated by an `action: update` call from the slide or widget player

## Node Configuration


### condition_value:

Single value, type: `String`. Default: `None`

This is the value that the current value of `variable_name` will be compared to. If the comparison is true, this node will be shown. Otherwise, it will be hidden.

### condition_type:

Single value, type: `op`. Default: `Equals`

This is the comparison that will be made between the `variable_name` value and the `condition_value`.


### max_players:

Single value, type: `integer`. Default: `0`

If greater than zero, the condition will be evaluated only when the total number of players in the game is less than or equal to this value. Otherwise, it will be false and this node will be hidden.

### min_players:

Single value, type: `integer`. Default: `0`

If greater than zero, the condition will be evaluated only when the total number of players in the game is greater than or equal to this value. Otherwise, it will be false and this node will be hidden.

### variable_name:

Single value, type: `String`. Default: `None`

This is the name of the variable that the `condition_value` will be compared to. If the comparison is true, this node will be shown. Otherwise, it will be hidden.

### variable_type:

Single value, type: `String`. Default: `"Current Player"`

This is the source of the variable that will be looked up and compared to.