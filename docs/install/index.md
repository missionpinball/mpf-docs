---
title: Downloading & Installing MPF
---

# Installing MPF 0.80 or 0.57


The current stable version of MPF is `0.57.3`, and the upcoming release is `0.80.0` along with a long-term support release of `0.57.4`.

!!! note "New MPF Coming Soon!"

    The next major release of MPF will be 0.80 and is coming soon! This exciting advancement offers a brand-new media controller based on the powerful Godot game engine. If you are just getting started with MPF, consider giving 0.80 a try!

--8<-- "latest_versions.md"

## Supported Operating Systems

MPF works with following platforms:

* Windows 10 / Windows 11 (64-bit only)
* macOS 10.14+, up through macOS 14 Sonoma (Intel & Apple Silicon)
* Linux (64-bit, lots of distros including Debian and Ubuntu)
* Raspberry Pi

## Python Version Matching

MPF 0.57 works with Python 3.8 - 3.12.

MPF 0.80 works with Python 3.10-3.13, with upcoming support for 3.14.


<!-- TODO(Bosh) Disabled because dev1 is not a good choice given the myriad of changes on the way to dev11

 ## Simplest Installation: Precompiled Binary (MPF 0.80)

As of MPF 0.80 we are providing precompiled binaries for new users to get up and running as easily as possible. You can see all the latest binaries at the [MPF Precompiled Binaries](https://github.com/missionpinball/prepackaged-mpf-binaries/tree/main/latest) repository, but here are some links:

  *  [**Mac OSX, Apple Silicon**, MPF 0.80.0.dev1 Python 3.12.3](https://github.com/missionpinball/prepackaged-mpf-binaries/raw/main/latest/mpf-0.80.0.dev1_cpython-3.12.3_darwin_arm64)

  * [**Mac OSX, Intel x86**, MPF 0.80.0.dev1, Python 3.12.3](https://github.com/missionpinball/prepackaged-mpf-binaries/raw/main/latest/mpf-0.80.0.dev1_cpython-3.12.3_darwin_x86_64)

  * [**Linux, x86_64**, MPF 0.80.0.dev1, Python 3.9.12](https://github.com/missionpinball/prepackaged-mpf-binaries/raw/main/latest/mpf-0.80.0.dev1_cpython-3.9.2_linux_x86_64)

***Advantages of Simplest Installation:***

  * Fastest way to get MPF running on a computer
  * No installation or dependencies necessary
  * Always has compatible Python and package versions

***Disadvantages of Simplest Installation:***

  * Startup times are slower than a Standard Installation
  * Not (yet) available for all platforms
  * No option to customize MPF or use bleeding-edge features

!!! note ""

    Okay, it's not technically "pre-compiled". MPF is written in Python, which is an interpreted language, and therefore cannot be truly "compiled" into a binary. The provided binaries are special applications that bundle a copy of Python, the MPF framework modules, and all dependency packages into a single file.

    The point is, you can download a single file and run it and have a working copy of MPF! -->

## Standard Installation: Pip Install (MPF 0.80)

Regardless of your platform or Python version, a [virtual environment](virtual-environments.md) is
strongly recommended when working with MPF unless you are using a precompiled binary.

!!! danger "Do not skip the Virtual Environment"

    Virtual environments are important for keeping your computer clean and preventing different packages from
    conflicting. Without virtual environments, you may encounter dependency conflicts and stale packages that
    will prevent MPF from running. Troubleshooting and manually cleaning up packages is a pain—do your future
    self a favor and setup an MPF virtual environment now!

After creating your Python 3.10-3.13 virtual environment and activating it, install MPF 0.80.

``` shell
pip install mpf --pre
```

Now when inside your virtual environment, you can run MPF simply by typing `mpf` while in your machine folder. To update MPF, type `pip install --upgrade mpf`.

***Advantages of Standard Installation:***

  * Fast startup times (compared to precompiled binaries)
  * Easy upgrading of MPF, including pre-release versions
  * Smallest size on disk

***Disadvantages of Standard Installation:***

  * Requires a local Python 3.8+ installation
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

## Migrating MPF 0.57 to MPF 0.80

If you have an existing MPF 0.57 project and would like to use MPF 0.80 and the GMC, there are just a few config changes needed. See the [MPF 0.80 Migration Guide](0.80.md) for instructions.

## Next step: The Tutorial!

We have a tutorial which walks you through the first few steps of getting
your project started at [missionpinball.org/latest/tutorial](../tutorial/index.md)
