---
title: MPF-GMC Singleton
---

# MPF-GMC Singleton

The MPF-GMC Singleton is the Autoload node that exposes GMC functionality to Godot. For most users this functionality is leveraged through the use of the MPF nodes, but advanced users may want to access the singleton directly for fine-tuned control and custom code.

This document outlines the public methods and attributes of the MPF-GMC singleton that can be accessed through custom code in your scenes.

The MPF-GMC singleton is accessed through the global name `MPF` and is an aggregator of a number of submodules:

  *  `MPF.game`: Data related to the current game in progress
  *  `MPF.log`: Logging functionality
  *  `MPF.media`: Data related to the displays, slides, and widgets of the MC
  *  `MPF.server`: Methods for sending and receiving data to/from MPF via the BCP connection
  *  `MPF.util`: Utility functions and convenience methods

## MPF Game

Data about the current game is accessibly via `MPF.game` and includes readable properties and signals to manage data during gameplay.

### Signals

#### `credits`

Emitted when the credits value changes (i.e. money is inserted or a game is started).

#### `game_started`

Emitted when a game is started.

#### `player_added(total_players: int)`

Emitted when a new player is added to the game.

#### `player_update(variable_name: String, value: any)`

Emitted when a player variable changes.

#### `volume(bus: String, value: float, change: float)`

Emitted when the volume of an audio bus changes.

### Properties

#### `active_modes`

Array of values, type `String`

A list of all modes currently active in MPF.

#### `audits`

Dictionary, type `String: any`

A lookup table of all audit values tracked by MPF.

#### `machine_vars`

Dictionary, type `String: any`

All machine variables tracked by MPF.

#### `player`

Dictionary, type `String: any`

The current active player in the current game. If no game is active, will return an empty dictionary.

#### `players`

Array of values, type `Dictionary`

A list of all players in the current game.

#### `settings`

Dictionary, type `String: any`

All settings values tracked by MPF.

## MPF Media

The `MPF.media` manages the media contents of the project, including slides, widgets, and sounds. It is responsible for: traversing the project directory on startup to catalog all media assets; instantiating the SoundPlayer node; and handling the config player events from MPF (*slides_play*, *widgets_play*, and *sounds_play*).

### Methods

#### `get_slide_instance(slide_name: String, preload_only: bool) -> MPFSlide`

Instantiates and returns the instance of `MPFSlide` with the given name, or preloads it.


#### `get_sound_instance(sound_name: String, preload_only: bool) -> MPFSound`

Instantiates and returns the instance of `MPFSound` with the given name, or preloads it.


#### `get_widget_instance(widget_name: String, preload_only: bool) -> MPFWidget`

Instantiates and returns the instance of `MPFWidget` with the given name, or preloads it.


## MPF Server

The `MPF.server` manages the BCP connection to MPF and is responsible for sending and receiving data between the GMC and MPF processes.

### Signals

#### `bonus(payload: Dictionary)`

Emitted during the Bonus mode. See [bonus mode settings](bonus.md) for details.

#### `clear(mode_name)`

Emitted when a mode ends.

#### `carousel_item_highlighted(payload)`

Emitted during a carousel event.

#### `options(payload)`

Emitted when the *options* event is received from MPF. This is a generic subscribable event that can be used for any purpose, which can be simpler to use because it doesn't require creating custom event handlers and callbacks. Just post an event named "*options*"  from MPF and connect to this signal.

#### `player_var(value, prev_value, change, player_num)`

Emitted when a player variable changes. Can be subscribed to for manually triggering updates and scene behaviors based on player variables.

#### `service(payload)`

Emitted during Service mode.

### Methods

#### `add_event_handler(event: String, handler: Callable)`

Binds an event handler to a callable and subscribes to that event via BCP. When the event is triggered, the callable will be called with a single `payload` argument that is a dictionary of the event args.

#### `remove_event_handler(event: String, handler: Callable)`

Removes an event handler for the event `event` and the callback `handler`.

#### `send_event(event_name: String)`

Sends an event to MPF using the BCP connection. Used for simple event names.

#### `send_event_with_args(event_name: String, args: Dictionary)`

Sends an event to MPF using the BCP connection, and appends key/value pairs from a dictionary.

Note that `name` is reserved for the event name in the BCP protocol, so a `name` key in the args dictionary will be ignored.

#### `set_machine_var(name: String, value: any)`

Writes a machine variable `name` with value `value`.

## MPF Util

### Methods

#### `comma_sep(number: int) -> String`

Splits an integer into a string with thousands-separated commas.

#### `find_parent_slide(node: Node) -> Node`

Traverses the scene tree starting at the current node and returns the first parent node that is an `MPFSlide` type.

#### `pluralize(template: String, value: int, suffix: String = "s") -> String`

Returns a string with a conditional pluralization suffix `suffix` of `template` based on the value `value`.

The template will append the suffix using string substitution if the `value` is not equal to one, otherwise the suffix will not be appended.

Examples:

``` go
pluralize("Shot%s Remaining", 1)
# > "Shot Remaining"

pluralize("Shot%s Remaining", 3)
# > "Shots Remaining"
```
