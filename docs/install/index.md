---
title: Downloading & Installing MPF
---

!!! note "New MPF Coming Soon!"

    The next major release of MPF will be 0.80 and is coming soon! This exciting advancement offers a brand-new media controller based on the powerful Godot game engine. If you are just getting started with MPF, consider giving 0.80 a try!

# Installing MPF 0.80 or 0.57

The current stable version of MPF is `0.80.0`. The long term legacy support version is `0.57.5`. MPF 0.80.0 requires the Godot MPF-GMC plugin to be version `1.0.0`.

--8<-- "latest_versions.md"

## Supported Operating Systems

MPF works with following platforms:

* Windows 10 / Windows 11 (64-bit only)
* macOS 10.14+, up through macOS 14 Sonoma (Intel & Apple Silicon)
* Linux (64-bit, lots of distros including Debian and Ubuntu)
* Raspberry Pi

## Python Version Matching

MPF 0.80 works with Python 3.10 - 3.14.

MPF 0.57 works with Python 3.8 - 3.12. Python 3.13 and 3.14 may work with 0.57, but MPF-MC is not updated to work with those Python versions yet.

## Migrating MPF 0.57 to MPF 0.80

If you have an existing MPF 0.57 project and would like to use MPF 0.80 and the GMC, there are just a few config changes needed. See the [MPF 0.80 Migration Guide](./0.80.md) for instructions.

## Video Tutorial

The following video shows on Windows how to install Python, Godot Engine, VS Code, and Sourcetree/Git, use Github to create a repo, and how to manage your Python Virtual Environment (venv) and install MPF.

<div class="video-wrapper">
<iframe width="560" height="315" src="https://www.youtube.com/embed/rQqKG2Ie6KM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Standard Installation: Pip Install (MPF 0.80)

Regardless of your platform or Python version, a [virtual environment](virtual-environments.md) is
strongly recommended when working with MPF unless you are using a precompiled binary.

!!! danger "Do not skip the Virtual Environment"

    Virtual environments are important for keeping your computer clean and preventing different packages from
    conflicting. Without virtual environments, you may encounter dependency conflicts and stale packages that
    will prevent MPF from running. Troubleshooting and manually cleaning up packages is a pain—do your future
    self a favor and setup an MPF virtual environment now!

After creating your Python 3.10-3.14 virtual environment and activating it, install MPF 0.80 with the latest dev build.

``` shell
pip install mpf --pre
```

Now when inside your virtual environment, you can run MPF simply by typing `mpf` while in your machine folder. To update MPF, type `pip install --upgrade mpf`.

***Advantages of Standard Installation:***

  * Fast startup times (compared to precompiled binaries)
  * Easy upgrading of MPF, including pre-release versions
  * Smallest size on disk

***Disadvantages of Standard Installation:***

  * Requires a local Python 3.10+ installation
  * Requires setting up a virtual environment
  * Mistakes can pollute Pip environments and cause dependency conflicts
  * No option to customize MPF or use bleeding-edge features

!!! note "Many Python Interpreters Supported"

    Without the MC's Kivy dependencies, MPF 0.80 now supports alternative Python interpreters like PyPy. You can use a different interpreter if you'd like.

## Expert Installation: Local Repository (MPF 0.80)

For complete control, you can clone the MPF repository to your computer and run it directly from the source code.

After creating your Python 3.10+ [virtual environment](virtual-environments.md), go to the folder where you wish to clone the MPF repository and type:

``` shell
git clone https://github.com/missionpinball/mpf
cd mpf
git checkout 0.80.x
pip install -e .
```

Now when inside your virtual environment, you can run MPF simply by typing `mpf` while in your machine folder. Typing `pip list` will reveal that the MPF module is being run directly from the repo folder on your computer. To update MPF, navigate inside the MPF repo folder and type `git fetch` and `git pull`.


***Advantages of Expert Installation:***

  * Faster startup times
  * Access to any version of MPF, including feature branches and forks
  * Edit the MPF source code and see the effects immediately

***Disadvantages of Expert Installation:***

  * Requires a local Python 3.10+ installation
  * Requires setting up a virtual environment
  * Requires knowledge of Git mechanics
  * Updates require a manual fetch and pull of the repository

## Installing MPF 0.57 (Legacy MC)

If you are installing MPF 0.57 to continue work on an existing MC-based project, here are links to the legacy installation guides for each platform:

* [Mac](mac.md)
* [Windows](windows.md)
* [Linux](linux/index.md)


## Next step: The Tutorial!

We have a tutorial which walks you through the first few steps of getting
your project started at [MPF Tutorial](../tutorials/legacy_mc/index.md).
