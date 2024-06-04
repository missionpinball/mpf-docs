---
title: MPFWindow
---

# MPFWindow

`MPFWindow` is a Godot Node class provided by the MPF-GMC extension. The entry scene of the GMC project must derive from the `MPFWindow` class.

## Node Configuration

The root instance of `MPFWindow` is expected to have at least one child node of type `MPFDisplay`, where slides and widgets will be targeted. If multiple displays are provided and none are explicitly set to `is_default`, then the first child will be default.

## Parameters

The `MPFWindow` class does not take any parameters. The overall window dimensions should be configured in the *Project > Project Settings > Display > Window > Size* menu.

## Methods

`MPFWindow` does not have any public methods.


## Multiple Displays

For multiple displays, you'll want to create your own scene with an `MPFWindow` node as the root element, and set the window size to the maximum bounding box of all displays.

Then create an `MPFDisplay` child for each display you want, and give them the appropriate size and position for where they will appear relative to each other.

To get the displays to appear on the correct monitors, you'll want to lock the top-left corner of the Window scene to the top-left corner of the first (primary) monitor. Use the menu *Project > Project Settings > Display > Window > Size* and change the *Initial Position Type* to `Absolute`.

You may also need to adjust the window position and fullscreen modes, depending on your operating system.

~~~ note "Multiple Displays Need Your Help"

    Theoretically everything exists in Godot and GMC to run multiple displays across multiple monitors, but we need folks with multi-display projects to help test and debug. Please share your experience!