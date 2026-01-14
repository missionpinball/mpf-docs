---
title: GMC Configuration File
---

# GMC Configuration File

The *gmc.cfg* configuration file in your Godot project root contains options for customizing GMC behavior. It uses INI formatting and its supported features are documented here.

!!! note

    Currently the Godot engine will remove comments from this file when it chooses to rewrite it.
    
### Local Overrides

Any configuration options in *gmc.cfg* can be overridden with a local file *gmc.local.cfg* in the Godot User Data folder. This allows you to commit the primary configuration to version control while still having platform-specific configurations (e.g. MPF executable path and logging levels) on each machine.

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

The GMC section contains settings related to the GMC itself, including logging.

### `content_root`

Single value, type `String`. Default `None`

In addition to mode subfolders, GMC will look for slides, widgets, and sounds in those respective folders in the Godot project root (e.g. */sounds*, */slides*).

You may wish to consolidate your content in a common subfolder rather than the project root. You can define a content root folder here, which will be prepended to the individual content folders (e.g. */content/sounds*, */content/slides*).

### `exit_on_esc`

If true, the GMC process will exit if the Escape key is pressed during runtime.

### Logging

Logging can be specified in the `\[gmc\]` section with the following components:

  * `logging_global` for all components not otherwise specified
  * `logging_game` for the MPF.game script, holding all game-related data
  * `logging_server` for the BCP Server, with all comms between GMC and MPF
  * `logging_process` for the MPF.process manager, running the MPF subprocess
  * `logging_media` for the media controller (slides, widgets, and sound)
  * `logging_sound_player` for the sound player specifically

``` ini
[gmc]
logging_global=20
logging_sound_player=10
```

Each core component's log level can be adjusted here, and any unspecified components will use the global log level. The log levels are stored as integers with the following values:

  * USE_GLOBAL_LEVEL: 0
  * VERBOSE: 1
  * DEBUG: 10
  * INFO: 20
  * LOG: 25
  * WARNING: 30
  * ERROR: 40

By default, debug/editor builds will run at INFO while production builds run at LOG.

### Script Overrides (Advanced)

The gmc section can override the core GMC scripts for advanced customization of the GMC itself. Only for advanced users.

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

## \[mpf\]

If you have configured [Godot to launch the MPF game](../guides/launching-the-mpf-game-with-godot.md) for you, this section contains the values you set in that menu.
These options are assembled together into the following shell command and run when you play the Godot project:

``` shell
<executable_path> <executable_args> <machine_path> <mpf_args>
```

The Godot editor misbehaves if you edit the `gmc.cfg` values while also editing in this UI form, so take care to save changes and reload the editor if you notice odd behaviors. If the top line "Launch MPF with GMC" is enabled, the values here will be used to spawn an MPF game instance when you press the **Play** button to play your GMC project. 


### Options:

#### `spawn_mpf`

Single value, type `bool`. Default `false`.

If true, GMC will spawn a subprocess to run MPF when the main project is run. The rest of these values will only be used if this is true.

#### `executable_path`

Single value, type `String`. Default `None`.

The path to the executable entry point for the MPF process. It can be a Python interpreter, a symlink to a virtual environment mpf executable, or a precompiled MPF binary.

#### `executable_args`

Single value, type `String`. Default `None`

Additional arguments to pass to the executable. For example, if the executable is a Python interpreter then the executable args may be `-m mpf` to load the MPF module.

Note that MPF-specific command line args should *not* go here, even if the executable is an MPF binary.

#### `machine_path`

Single value, type `String`. Defaults to the GMC project folder.

The path of the MPF machine folder, i.e. the root folder containing the */config* and */modes* folders for your project. If not specified, the GMC project folder will be used.

#### `mpf_args`

Single value, type `String`. Default `None`

Additional arguments to pass to MPF after the machine path. Common values may include `-x` for virtual mode, `-vV` for verbose logging, or `-P` for production mode. Note that values defined specifically for virtual or verbose (see below) will supersede. See [mpf game](../../running/commands/game.md) for full reference.

#### `virtual`

Single value, type `bool`. Default `false`.

If true, the MPF process will spawn in virtual mode (i.e. `-x` will be appended to the `mpf_args`).

#### `verbose`

Single value, type `bool`. Default `false`.

If true, the MPF process will have verbose logging (i.e. `-vV` will be appended to the `mpf_args`).


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

### `duck_default`

Single value, type `bool`. Default `false`

One audio bus is allowed to be set as the default ducking target. Any sound playback trigger using ducking settings that has not specified a value for `bus:` in the ducking settings will duck the audio on this bus.

### `simultaneous_sounds`

Single value, type `int`. Default `None`

The maximum number of sounds that can be played concurrently in a `simultaneous`-type bus. If this limit is reached, subsequent sound calls will be dropped (i.e. they are *not* queued).

### `type`

Single value, type `String`. One of `"solo"`, `"sequential"`, `"simultaneous"`

The type of playback sequencing to use. Solo only allows one track at a time and will *replace* a current track with a new one. Sequential allows one track at a time and queues subsequent tracks to play sequentially as the previous one finishes. Simultaneous allows multiple tracks to be played concurrently.
