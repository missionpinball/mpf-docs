---
title: GMC Configuration File
---

# GMC Configuration File

The *gmc.cfg* configuration file in your Godot project root contains options for customizing GMC behavior. It uses INI formatting and its supported features are documented here.

## \[filter\]

The filter section configures a shader for the GMC window, applying effects universally to all displays.

Full documentation can be found on the [Window Effects Filters guide](../guides/window-filters.md).

``` ini

    [filter]
    filter="virtual_dmd"
    columns=120
    rows=45
    hardness=5
    spacing=2
```

## \[gmc\]

The gmc section overrides the core GMC scripts for advanced customization of the GMC itself. Only for advanced users.

Full documentation can be found on the [Advanced Custom Code guide](../guides/advanced-custom-code.md).

``` ini

    [gmc]
    GMCServer="custom_code/my_custom_bcp.gd"
```

## \[keyboard\]

The keyboard section maps key inputs to switches and events for simulating MPF behavior during development.

Full documentation can be found on the [Keyboard Setup guide](../keyboard.md).

``` ini

    [keyboard]
    1=["switch", "s_switch_1"]
    enter=["switch", "s_start_button"]
    6=["switch", "s_drop_1", "active"]
    shift+6=["switch", "s_drop_1", "inactive"]
    x=["switch", "s_trough_6", "toggle"]
    m=["event", "start_mode_multiball"]
```

## \[settings\]

The settings section is where general customization options are defined.

``` ini

    [settings]
    content_root="content"
```

### `content_root`

Single value, type `String`. Default `None`

In addition to mode subfolders, GMC will look for slides, widgets, and sounds in those respective folders in the Godot project root (e.g. */sounds*, */slides*).

You may wish to consolidate your content in a common subfolder rather than the project root. You can define a content root folder here, which will be prepended to the individual content folders (e.g. */content/sounds*, */content/slides*).

## \[sound_system\]

The sound system section defines playback properties of the Audio Buses defined in your Godot project.

``` ini

    [sound_system]
    music={"type": "solo"}
    effects={"type": "simultaneous", "simultaneous_sounds": 3, "default": true}
    voice={"type": "sequential"}
```

### `default`

Single value, type `bool`. Default `false`

One audio bus is allowed to be set as default, and any sound playback trigger that does not include a value for `bus:` will play on this bus.

### `simultaneous_sounds`

Single value, type `int`. Default `None`

The maximum number of sounds that can be played concurrently in a `simultaneous`-type bus. If this limit is reached, subsequent sound calls will be dropped (i.e. they are *not* queued).

### `type`

Single value, type `String`. One of `"solo"`, `"sequential"`, `"simultaneous"`

The type of playback sequencing to use. Solo only allows one track at a time and will *replace* a current track with a new one. Sequential allows one track at a time and queues subsequent tracks to play sequentially as the previous one finishes. Simultaneous allows multiple tracks to be played concurrently.
