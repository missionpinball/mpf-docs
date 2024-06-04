---
title: MPFChildPool
---

# MPFChildPool

`MPFChildPool` is a Godot Node class provided by the MPF-GMC extension. It selects one of its children to be displayed when its added to the scene tree, and optionally calls a method on that child.

Child node selection can be done randomly or sequentially, and tracked globally or per-player.

To use a Child Pool, add the node to your scene and place child nodes inside it.

!!! note "Children require show/hide methods"

    The display of the child nodes is managed by calling `show()` or `hide()` on the respective children. Every Godot `Node2D`, `Node3D`, and `Control` node has these methods built-in, but if you are using a custom class you must ensure that it has `func show()` and `func hide()` defined.

## Node Configuration

### playback_method:

Single value, type `PlaybackMethod`. Default: `Random`

This is how the child will be selected from the available children. Note that if the `MPFChildPool` only has one child, it will always be selected.

#### `Random`

One of the children is chosen at random. The same child may be chosen multiple times in a row.

#### `Random No Repeat`

One of the children is chosen at random. The same child will _not_ be chosen twice in a row.

#### `Random Force All`

One of the children is chosen at random. All children will be selected before any one is repeated, and the same child will not be chosen twice in a row.

#### `Sequential`

The first child will be chosen first, then the second, et cetera. After all children have been chosen, it will loop back to the first.

### track_per_player:

Single value, type `bool`. Default `false`.

If checked, the children will be tracked on a per-player basis. The same child may be chosen twice in a row if two players get it randomly. Can be useful for `Sequential` pools where the children are ordered to correspond to game progression.

### reset_on_game_end:

Single value, type `bool`. Default `false`.

If checked, the pool will reset its state at the end of the game and any sequences and previously-chosen random choices will be reset.

### child_method:

Single value, type `String`. Default `None`

The name of a method on the child node to call when it becomes active. Can be used to initialize nodes or begin video playback (e.g. `"play"` if the child is a `VideoStreamPlayer`).

Will only be called for the selected child when it enters the scene tree.

### call_child_method_in_editor:

Single value, type `bool`. Default `false`

If checked, the selected child node's `child_method` will be called when the scene is loaded into the editor. Can be helpful when the child has a dynamic layout, but can be annoying when the child plays a video.