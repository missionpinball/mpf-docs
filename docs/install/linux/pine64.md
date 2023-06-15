---
title: Installing MPF on a Pine64 with Ubuntu
---

# Installing MPF on a Pine64 with Ubuntu


!!! note

    This procedure for installing MPF on a Pine64 does not fully work. (MPF
    runs fine, Kivy installs fine, but MPF-MC does not run.) If you want to
    use MPF on a Pine64, maybe you can help figure out why this doesn't
    work and share your findings with us?)

## Hardware Notes

* Spring for the fastest MicroSD card you can (Samsung Evo cards are
    reportedly the fastest), at least 16GB.
* The Pine64's video seems to only support 1080p and 4K resolutions,
    so make sure your display can do one or both of those at a proper
    16:9 aspect ratio or else everything will be scaled and squished and
    it looks awful.
* If you find that your pine64 does not boot it maybe due to using a
    HDMI->DVI cable, try HDMI to HDMI first.

## System Notes

There are a bunch of things that arrive broken with the current Ubuntu
installer for Pine64 (as of this writing in November 2016). Some of them
will prevent MPF from installing, and a few are just annoying.

## Instructions

After installing the OS following the instructions on the [Pine64
Wiki](http://wiki.pine64.org/index.php/Main_Page)), expanding the volume
to the full size of the SD card, and getting connected to the Internet,
follow these steps. Don't try to update the installed system before
following this.

## Locale

Locale arrives broken and this wreaks all kinds of havoc, so here's how
to fix it.

Assuming you want US English, substitute your preferred language if not:

``` console
$ sudo locale-gen "en_US.UTF-8"
Generating locales...
  en_US.UTF-8... done
Generation complete.

$ sudo dpkg-reconfigure locales
Generating locales...
  en_US.UTF-8... up-to-date
Generation complete.
```

That command will open a text-based dialog, we recommend that you don't
choose "ALL" and only select the one or a few languages you want
(generating them all takes a long time). Then reboot, then do the above
reconfigure step AGAIN, then reboot, then run:

``` console
$ locale
```

And make sure it looks good. Mine says:

``` console
LANG=en_US.UTF-8
LANGUAGE=en
LC_CTYPE="en_US.UTF-8"
LC_NUMERIC=en_US.UTF-8
LC_TIME=en_US.UTF-8
LC_COLLATE="en_US.UTF-8"
LC_MONETARY=en_US.UTF-8
LC_MESSAGES="en_US.UTF-8"
LC_PAPER=en_US.UTF-8
LC_NAME=en_US.UTF-8
LC_ADDRESS=en_US.UTF-8
LC_TELEPHONE=en_US.UTF-8
LC_MEASUREMENT=en_US.UTF-8
LC_IDENTIFICATION=en_US.UTF-8
LC_ALL=
```

It took a few tries for this to stick for me, so do it again, including
reboot, if your results here are wrong.

## Fix the Software Boutique

This arrives broken, too. Oddly, running the Mate Welcome as root and
clicking a button partly fixes it.

``` console
$ sudo ubuntu-mate-welcome
```

When it comes up, click on the "Subscribe to updates" button, then
quit it.

Now go to System -> Administration -> Software Boutique. Click on the
wrench, then do each repair option (after clicking one, wait for it to
say it has finished).

Now go to System -> Administration -> Software Updater and get
everything up to date. You will need to reboot again after that.

## Install Missing pip3

``` console
$ apt-get install python3-pip
```

The path where `pip` puts executables is not in the system default path,
so edit `~/.bashrc` to add the following path:

``` console
$ sudo nano ~/.bashrc
```

At the bottom of the file add the following:

``` console
export PATH=~/.local/bin:$PATH
```

Hit "control + x" to save and "y" then "return" to save the file
as the same name.

Now start a fresh terminal so that this new PATH is included in your
current environment. Then:

## Install MPF

Download the MPF Debian Installer from
<https://github.com/missionpinball/mpf-debian-installer/archive/0.55.x.zip>

To unzip the file navigate in your terminal to the location of the
downloaded files.

Unzip the file:

``` console
$ unzip dev.zip .
```

If this does not run you may need to install unzip:

``` console
$ sudo apt-get install unzip
```

After unzip, run ./dev/install from the folder you unzipped the files
to. Consult the README for more information.

## Running MPF

See the [How to start MPF and run your game](../../running/index.md) page for details
and command-line options.

What if it did not work? ------------------------

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
