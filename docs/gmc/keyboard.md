---
title: GMC Keyboard
---

# GMC Keyboard

You can configure keys on your keyboard to trigger switches and events in order to simulate gameplay and test aspects of your game.

Keyboard configuration is done in the */gmc.cfg* file at the root of your project. You may already have this file if you followed the setup instructions for defining your audio bus configuration. If so, the `[keyboard]` section of this file will go before or after the `[sound_system]` section.

## Create a Keyboard Config Section

In your */gmc.cfg* file create a new section by adding a new line and typing `[keyboard]` into it.

Below that line, you can add as many key mappings as you'd like, for events and switches.

### Add a Switch Keymap

Switch keymaps are an array of the key map type ("switch"), the name of the switch, and (optionally) an action to perform on that switch.

Keymaps can be any individual key (`1`, `w`) the name of a standard key (`enter`, `tab`), or a key with modifier (`shift+2`, `ctrl+enter`).

#### Default Behavior

If no action is specified, pressing the mapped key will activate the switch and releasing the key will deactivate it.

A basic example is having the "1" key press the switch `s_switch_1` and the "Enter" key press the switch `s_start_button`.

``` ini
[keyboard]
1=["switch", "s_switch_1"]
enter=["switch", "s_start_button"]
```

#### Explicit Actions

GMC keymaps support three explicit actions: `active`, `inactive`, and `toggle`.

When an action is set, pressing the mapped key will trigger that action. Releasing the key has no effect.

``` ini
[keyboard]
6=["switch", "s_drop_1", "active"]
shift+6=["switch", "s_drop_1", "inactive"]
x=["switch", "s_trough_6", "toggle"]
```

### Add an Event Keymap

Event keymaps are an array of key map type ("event") and the name of an event to pass to MPF. This can be to simulate events triggered by GMC, or simply for testing modes easily.

``` ini
[keyboard]
m=["event", "start_mode_multiball"]
d=["event", "drop_bank_left_complete"]
```
