---

title: Installing MPF on Linux
---

# Installing MPF on Linux

!!! warning "MPF 0.80 is Coming Soon"

    This installation guide is for MPF 0.57 and the legacy MC, which is being replaced in the upcoming MPF 0.80 with the Godot MC. If you are just getting started with MPF, we recommend you [install MPF 0.80](../index.md) instead.

## OS Preparation

In order to communicate with your pinball hardware over USB you need to add your user to the user group `dialout`. This is necessary regardless of the version of MPF (thus including the upcoming 0.80).


## May 2023 Update

We need to update this page (for instance, we no longer suggest pipx), but if you
want the "real" linux install instructions, read through the GitHub
Actions job scripts in the [build_wheels](https://github.com/missionpinball/mpf/blob/dev/.github/workflows/build_wheels.yml) file.
You'll see the exact steps we use to build MPF-MC (MPF is simple to
install, it's the MC part that's tricky). Various jobs in there use
both apt-get and yum to set everything up before building the MC.

As part of our automated build process, we build and test MPF and MPF-MC
against Ubuntu 20.04 & 22.04 and Debian Stretch & Buster. MPF 0.54
supports Python 3.5 to 3.7. MPF 0.55 supports Python 3.6 to 3.9. MPF
0.56 supports Python 3.7 to 3.9

## Installing MPF Using Our Debian Installer

Download the MPF Debian Installer version from
[here](https://github.com/missionpinball/mpf-debian-installer/archive/0.55.x.zip)

Unzip it, and from a terminal run `chmod +x install && sudo ./install`
from the folder you unzipped the files to. If you are using a P-Roc or
P3-Roc also run `chmod +x install-proc && ./install-proc` (skip for
other platforms). Consult the README for more information.

## Installing MPF Manually

Current version these instructions are for v0.57, which is the current
"main" branch of MPF.

MPF 0.57 requires Python 3.8, 3.9, 3.10, 3.11, or 3.12.
Various Linux distributions offer to install multiple versions of Python in parallel.
First check what version of Python you might have already running on your computer.

MPF 0.80 requires Python 3.10+, so you may wish to start with a Python that can be
used in either version, if you less hassle when upgrading in the future.

``` doscon
python3 --version
```

In some cases you might only get a Python version of 3.6, then run your
admin tool and install a higher version of python. If you don't want to remove the older version of Python
you can keep it in parallel, just make sure to run the installer
commands with the right version of python. If you have for example
installed Python 3.9 try to running

``` doscon
python3.9 --version
```

You will need pip further down the line to complete the installation.
Same as above for Python, check what version of pip you are running and
choose the command to match the version you would like to use. Try the
following commands to figure out what pip command works for you and has
the right version.

``` doscon
pip --version
pip3 --version
pip3.9 --version
```

For the rest of the chapter I will always write python3.9 and pip3.9 as
commands as reminder to use the right version, any of the above commands
might work for you (or fail).

NOTE: If you already have an earlier version of MPF installed, uninstall
that first by using this command:

``` doscon
sudo pip3.9 uninstall mpf-mc mpf
```

If you are unsure which version of MPF you have installed, you can run
this command to check what is installed:

``` doscon
mpf --version
```

First you need to update your Python environment, run the following commands

``` doscon
python3.9 -m pip install --upgrade pip
python3.9 -m pip install --upgrade setuptools
python3.9 -m pip install --upgrade pillow
```

Next you need to install mpf itself as well as some additional mpf packages. Run the following commands


``` doscon
pip3.9 install mpf[all]
pip3.9 install mpf-mc
pip3.9 install mpf-monitor
```

Now you should be ready to use mpf, for a first test run

``` doscon
mpf --version
```

You should see a version number printed, as time of writing it is 0.56.2. Maybe you see some higher
number. If you get a message that the command `mpf` is not being found or known you might have to add the location of the
command to your `PATH` variable. Most likely (it depends on the shell type you use) you need to add to your `.profile` or `.bashrc` file an entry like

``` doscon
export PATH="$PATH:/home/user/.local/bin"
```

Where you need to substitue the word user with your real user name. In doubt open a file browser and look for the location
where mpf is located.


Your installation should be located now in your users' `.local` directory. To be more precise the executables will be in `/home/user/.local/bin`. The python code
will be in `/home/user/.local/lib/python3.9/site-packages`.

## Download & run the "Demo Man" example game

Now that you have MPF installed, you probably want to see it in action.
The easiest way to do that is to download a bundle of MPF examples and
run our "Demo Man" example game. To do that, follow the instructions
in the [How to run "Demo Man", an MPF example game](../../examples/demo_man.md) guide.

There's another example project you can also check out if you want
called the "MC Demo" (for media controller demo) that lets you step
through a bunch of example display things (slides, widgets, sounds,
videos, etc). Instructions for running the MC Demo are
[here](../../examples/mc_demo.md).

## Running MPF

See the [How to start MPF and run your game](../../running/index.md) for details and
command-line options.

If you see a Failed to initialize MPF exception when trying to start MPF
with Multimorphic P-ROC/P3-ROC boards with Python 3.8.

Example Error:

``` console
Failed to initialize MPF
Traceback (most recent call last):
File “/usr/local/lib/python3.8/dist-packages/mpf/platforms/p_roc_common.py”, line 31, in <module>
  import pinproc
ModuleNotFoundError: No module named 'pinproc'
During handling of the above exception, another exception occurred:
Traceback (most recent call last):
File “/usr/local/lib/python3.8/dist-packages/mpf/platforms/p_roc_common.py”, line 41, in <module>
  raise ImportError
ImportError: No module named 'pinproc'
```

Try Changing `Edit install-proc:`

From:

``` console
cd pypinproc
sudo python3 setup.py install
```

To:

``` console
cd pypinproc
python3 setup.py install --user
```

## Keeping MPF up-to-date

To upgrade MPF just re-run the installer which will make sure that you
will also get updated dependencies:

``` console
sudo ./install
```

If you have MPF installed via the manual procedure above, you can keep
it up-to-date by running the final two pipx commands from above which
you used to install MPF and MPF-MC.

To install the latest dev release (not generally recommended) which
allows you to try bleeding-edge features run:

``` console
pip3 install mpf[all] mpf-mc --pre --upgrade
```

To downgrade (or install a specific release x.yy.z) run:

``` console
pip3 install mpf[all]==x.yy.z
pip3 install mpf-mc==x.yy.z
```

## Uninstalling MPF

To remove MPF either because it is no longer needed or to perform a
clean install run:

``` console
sudo pip3 uninstall mpf-mc mpf
```

## Specific Hardware Devices

We got some write-ups for specific hardware platforms. They follow the
general linux installation schema but also cover some details about that
hardware.

* [Raspberry Pi](raspberry.md)
* [Pine64](pine64.md)

## Specific Linux Distributions

Specifics about certain linux distributions.

* [Xubuntu Linux](xubuntu.md)

## What if it did not work?

In the following we list some common problems and solutions. If you got
another problem please ask in our [forum](../../community/index.md).

### YAML error on first start

You will see this error if there is already a different version of
ruamel.yaml installed on your system:

``` doscon
pkg_resources.VersionConflict: (ruamel.yaml 0.15.37 (c:\users\robert\appdata\local\programs\python\python36\lib\site-packages), Requirement.parse('ruamel.yaml<0.11,>=0.10')
```

This could have happened if you are upgrading to a newer version of MPF
or you have incompatible versions of MPF, MPF-MC and/or the MPF-Monitor
installed. The required ruamel.yaml version is different on newer MPF
versions. We used to install ruamel 0.11 and switched to 0.15 in MPF
0.53+. MPF cannot start with two yaml libraries. To fix this check your
versions `pip3 list` and check `mpf`, `mpf-mc` and `mpf-monitor`. Remove
the wrong version and install the right one. All versions need to match
(for instance all or all dev).

The following command will remove all three and install the latest
release:

``` doscon
pip3 uninstall mpf mpf-mc mpf-monitor
pip3 install mpf mpf-mc mpf-monitor
```

This error can also occur if you already have ruamel.yaml installed in
your python system packages for a non-MPF package. Often times, you will
have a newer version of ruamel.yaml than MPF requires. Unfortunately,
MPF cannot use a newer version of this package because that caused
issues in the past because newer versions dropped support (wheels for
windows) for older python versions. In the case that you need a
different version than the one MPF requires, it is advised to create a
python virtual environment and install the required packages there, and
use that virtual environment for running MPF.
