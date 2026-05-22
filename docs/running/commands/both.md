---
title: mpf both (command-line utility)
---

# mpf both (command-line utility)


Starts both the MPF game engine and the MPF Media Controller from a
single command window with a single command. This is effectively the
same as running both `mpf game` and the Godot game (or Legacy MC project) separately,
but more convenient.

When you run `mpf both`, the console log outputs from both MPF and
the media controller will be mingled together in the console window. However the log
files in your machine's `/logs` folder will still be separate.

Note that the normal `mpf game` command line options are still available, for example:

``` shell
mpf both -a -x

mpf both -vVt
```

## Godot Media Controller

When using MPF 0.80+, both accepts two optional parameters, which help the tool find your Godot game project as well as the Godot executable itself.

Overall your command line call might look like this, in a Windows MINGW64 shell:

``` shell
mpf both -tX -g gmc-project/ -G ~/godot_installs/godot.exe
```

`both` should NOT be used with a Godot project that is configured to [auto-start MPF](../../gmc/guides/launching-the-mpf-game-with-godot.md),
as this will result in the Godot project attempting to start a second MPF game instance.


### `-g path/to/godot/project/`

By default, `both` will look for a `project.godot` file in the current working directory (likely your MPF game project folder).
This is how most MPF+GMC installs are configured, so you will not need to use this option.
However, if you decided to instead nest your Godot project in a subfolder, use `-g <path>` to specify the folder path in which `project.godot` can be found.

### `-G path/to/godot_executable`

By default, `both` will look for a Godot executable on the path.
In Windows, this can be achieved by renaming the `Godot_<version>.exe` file to `Godot.exe`, and putting a copy in the directory you call `mpf both` in.
Or, instead of adding Godot to your game folder directly, you can instead add the executable's folder path to your PATH environment variable.

Alternatively, you can use the `-G` option to specify the Godot executable file location directly.


## Legacy Media Controller

`mpf both` with mpf-mc allows passing command line options through to the mpf-mc process.

See the [mc](../../game/index.md) and
[mpf mc (command-line utility)](mc.md) command references for a full list of
command line options.

To quit MPF and MPF-MC, either click in the graphical pop up window (so
it has focus) and hit `Esc`, or click in the console window and press
`CTRL+C`.

!!! note

    If you use the `-l` (lowercase L) option to specify a log file along
    with `mpf both`, you need to use `-l` to specify the MPF log and `-L` to
    specify the MC log.
