---
title: MPF Quickstart
---

# Quickstart guide to MPF 0.80 and GMC

This is for people who know what they're doing. If you're lost, check out our full
[installation guides](../install/index.md).


## Quick links and git remotes

Updated: January 2026

* [Python 3.13](https://www.python.org/downloads/release/python-31311/)
* [MPF 0.80](https://github.com/missionpinball/mpf/tree/0.80.x) `0.80.0.dev11` - `git@github.com:missionpinball/mpf.git` branch `0.80.x`
* [MPF-GMC](https://github.com/missionpinball/mpf-gmc) `0.1.6` - `git@github.com:missionpinball/mpf-gmc.git` branch `main`
* [Godot Editor 4.5](https://godotengine.org/download)
* [MPF Monitor](https://github.com/missionpinball/mpf-monitor) `0.57.2` - `git@github.com:missionpinball/mpf-gmc.git` branch `dev`


## Quickstart for GMC

For full guide see: [GMC Installation](../gmc/installation.md)

1. Download the Godot Editor from [https://godotengine.org](https://godotengine.org)

1. Download the latest GMC release from [https://github.com/missionpinball/mpf-gmc/releases/](https://github.com/missionpinball/mpf-gmc/releases/) (under *Assets > Source code*).

1. Open the Godot Editor and create a new Project in a new folder of your choosing. This will be the project folder for your MPF machine code as well, so if you already have an MPF project choose that folder instead.

1. Extract the GMC download and copy the *addons* folder into your project folder.

1. In the Godot Editor, go to *Project Settings > Plugins* and check the Enable box for **Godot MC**. (Godot will show lots of errors during this step and the next, ignore them).

1. In the Godot Editor *Project Settings > Globals* click the folder icon to add a new Autoload and choose the file *addons/mpf-gmc/mpd_gmc.gd*. Set the Node name to `MPF` (all caps) and press Add.

1. Save your Godot project and then in the editor menu select *Project > Reload Current Project*.

## Quickstart for MPF

1. MPF 0.80 requires Python 3.10 - 3.13. Validate that you have a supported version of Python with `python3 --version`.

1. Create a virtual environment for mpf. In your home folder (or virtual environments folder) type `python3 -m venv mpf`

1. Activate your virtual environment: `source mpf/bin/activate` (on Mac/Linux) or `mpfenv/Scripts/Activate.ps1` (Windows PowerShell)

1. Install MPF 0.80: `pip install --pre mpf`

1. In your terminal, navigate to the project folder you created and initialize an MPF config file.

    ``` shell
(mpf) my_project_folder $> mkdir config
(mpf) my_project_folder $> echo "#config_version=6" > config/config.yaml
    ```

## Running the Game

1. To run the GMC project, press the play button in the top-right of the Godot Editor. When prompted to select a main scene, select *addons/mpf-gmc/slides/window.tscn*. You should see a window appear with the MPF logo and text reading "Waiting for MPF..."

1. To run the MPF game with virtual platform and console logging, type `mpf -xt`.


    For full run options see: [MPF command-line utility](../running/mpf.md) and [mpf game (command-line utility)](../running/commands/game.md)

    To configure the GMC project to automatically run the `mpf game` for you, see: [Launching the MPF game with Godot](../gmc/guides/launching-the-mpf-game-with-godot.md)


1. The Godot window should now say "Connected to MPF". Congratulations, you're running a pinball game!


You can now proceed to [set up your GMC slides](../gmc/setup.md) and [start creating modes](../game_logic/modes/custom_modes.md).
