---
title: API Reference - Player
---

# Player API Reference

Config Reference:

* [player_vars:](../../../config/player_vars.md)

``` python
class mpf.core.player.Player(machine, index)
```

Bases: `object`

Base class for a player in a game.

One instance of this class is automatically created for each player.

The game mode maintains a player attribute which always points to the current player and is available via self.machine.game.player.

It also contains a player_list attribute which is a list of the player instances (in order) which you can use to access the non-current player.

This Player class is responsible for tracking player variables which is a dictionary of key/value pairs maintained on a per-player basis. There are several ways they can be used:

First, player variables can be accessed as attributes of the player object directly. For example, to set a player variable foo for the current player, you could use:

``` python
self.machine.player.foo = 0
```

If that variable didn't exist, it will be automatically created.

You can get the value of player variables by accessing them directly. For example:

``` python
print(self.machine.player.foo)  # prints 0
```

If you attempt to access a player variable that doesn't exist, it will automatically be created with a value of 0.

Every time a player variable is created or changed, an MPF event is posted in the form player_ plus the variable name. For example, creating or changing the foo variable will cause an event called player_foo to be posted.

The player variable event will have four parameters posted along with it:

* `value` (the new value)
* `prev_value` (the old value before it was updated)
* `change` (the change in the value)
* `player_num` (the player number the variable belongs to)

For the change parameter, it will attempt to subtract the old value from the new value. If that works, it will return the result as the change. If it doesn't work (like if you're not storing numbers in this variable), then the change parameter will be True if the new value is different and False if the value didn't change.

For examples, the following three lines:

``` python
self.machine.player.score = 0
self.machine.player.score += 500
self.machine.player.score = 1200
```

will cause the following three events to be posted:

player_score with Args: value=0, change=0, prev_value=0 player_score with Args: value=500, change=500, prev_value=0 player_score with Args: value=1200, change=700, prev_value=500

## Methods & Attributes

The Player has the following methods & attributes available. Note that methods & attributes inherited from the base class are not included here.

`enable_events(enable=True, send_all_variables=True)`

Enable/disable player variable events.

Parameters:

* **enable** – Flag to enable/disable player variable events
* **send_all_variables** – Flag indicating whether or not to send an event with the current value of every player variable.

`is_player_var(var_name)`

Check if player var exists.

Parameters:

* **var_name** – String name of the player variable to test.

Returns: True if the variable exists and False if not.

`monitor_enabled = False`

Class attribute which specifies whether any monitors have been registered to track player variable changes.

`send_all_variable_events()`

Send a player variable event for the current value of all player variables.
