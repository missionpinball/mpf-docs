---
title: MPF Quickstart
---

# Quickstart guide to MPF 0.80 and GMC

This is for people who know what they're doing. If you're lost, check out our full
[installation guides](../install/index.md).


## Quickstart for GMC

1. Download the Godot Editor from [https://godotengine.org](https://godotengine.org)

1. Download the latest GMC release from [https://github.com/missionpinball/mpf-gmc/releases/](https://github.com/missionpinball/mpf-gmc/releases/) (under Assets > Source code).

1. Open the Godot Editor and create a new Project in a new folder of your choosing.

1. Extract the GMC download and copy the *addons* folder into your project folder.

1. In the Godot Editor, go to *Project Settings > Plugins" and check the Enable box for **Godot MC**. (Godot will show lots of errors, ignore them).

1. In the Godot Editor *Project Settings > Autoload* select the folder to add a new Autoload and choose the file *addons/mpf-gmc/mpd_gmc.gd*. Set the Node name to `MPF` (all caps) and press Add.

1. Save your Godot project and then in the editor menu select *Project > Reload Current Project*.

## Quickstart for MPF

1. MPF requires Python 3.8 - 3.12. Validate that you have a supported version of Python with `python3 --version`.

1. Create a virtual environment for mpf. In your home folder (or virtual environments folder) type `python3 -m venv mpf`

1. Activate your virtual environment: `source mpf/bin/activate` (on Mac/Linux) or `mpfenv/Scripts/Activate.ps1` (Windows PowerShell)

1. Install MPF 0.80: `pip install --pre mpf`

1. In your terminal, navigate to the project folder you created and initialize an MPF config file.

``` console

    (mpf) my_project_folder $> mkdir config
    (mpf) my_project_folder $> echo "#config_version=6" > config/config.yaml
```

## Running the Game

1. Press the play button in the top-right of the Godot Editor. When prompted to select a main scene, select *addons/mpf-gmc/slides/window.tscn*. You should see a window appear with the MPF logo and text reading "Waiting for MPF..."

1. In your terminal, type `mpf -xt`

The Godot window should now say "Connected to MPF". Congratulations, you're running a pinball game!

You can now proceed to [set up your GMC slides](../gmc/setup.md) and start creating modes.
