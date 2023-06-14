---
title: Installing MPF on a Raspberry Pi 3
---

# Installing MPF on a Raspberry Pi 3



MPF can be installed on a Raspberry Pi 4, and possibly a 3.

MPF itself runs fine, but you might run into limitations with the
Media Controller since videos and sounds can potentially take more
resources than the Pi has. (You can address this by tuning the codecs
and configuration of your Pi, or, you can just buy a more powerful
NUC or single-board computer for $100-200 and then never have to worry about performance again.)

* Get the latest Raspberry Pi Imager from here:
    <https://www.raspberrypi.org/software/>
* Install Raspbian Lite onto your SD card.
* Boot your PI and connect keyboard + monitor
* Login with user:pi password:raspberry
* now type this:

``` shell
sudo raspi-config
```

and choose 7. Advanced Options -> A1. Expand Filesystem to use the
whole SD-Card Space, we will need it. You can change your username and
localization settings too.

After that we will give the GPU a bit more of RAM:

Go to 7. Advanced Options -> A3 Memory split and change the value to
256.

Now reboot, login and type:

``` shell
sudo apt update
sudo apt upgrade
sudo apt install git

git clone https://github.com/missionpinball/mpf-debian-installer.git
cd mpf-debian-install
sudo ./install
```

To checkout and run the
[MPF Linux Debian installer](index.md). It will install MPF, MPF-MC and all dependencies for you.

This will take some time as it may compile some drivers mpf-mc needs
like the audio driver. Sometimes it looks like it hangs, but it does
not. It will take up to half an hour, at least on a Raspberry 1 (which
you should not use). Compiling is really slow on the Raspi.

Now copy your machine folder from your develop station or create a new
one under your home directory (/home/pi/your_machine)

If you need a file-manager start mc (No, not the mpf mediacontroller,
its the midnight commander ;-))

If you need to copy your folders from an usb-stick you have to manually
mount it (we dont have X, so everything has to be done by hand).

``` shell
sudo mount /dev/sda1 /mnt
```

This works in 90% otherwise your stick is not sda1, just look inside the
/dev folder to find out which device you have to mount or type

``` shell
lsblk
```

to list your block devices.

Now you find the contents of your stick in /mnt.

To tell mpf-mc and the underlying kivy to use the framebuffer via SDL2
you have to put this in your machine/config/config.yaml:

``` mpf-mc-config
window:
  width: 1280
  height: 800
kivy_config:
  graphics:
    fbo: force-hardware
##! test
#! advance_time_and_run .1
```

## More or less important last steps:

## Serial communication:

Linux always had and has the possibility to log in via a serial
connection. If you run a hardware platform which uses the serial pin on
the Raspberry you should disable the Linux login shell on that port. The
device is called /dev/ttyAMA0 and you need to stop it from starting:

Type:

``` shell
sudo systemctl disable serial-getty@ttyAMA0.service
```

Now you have to disable the console itself:

``` shell
sudo mc
```

to start Midnight Commander as root (normally you should not do this,
but this time you have to.)

Now go to /boot and press F4 over cmdline.txt.

Remove these entries:

    console=ttyAMA0,115200 kgdboc=ttyAMA0, 115200

and save the file.

You have the possibility to connect RS 232 devices directly to the raspi
but take care, the voltage levels are 3.3V on the raspi gpio. Further
instructions here: <http://elinux.org/RPi_Serial_Connection>

## Sound output:

Navigate to /boot/config.txt if you want to use audio out of the
Raspberry built in ""soundcard"": edit this file as root and insert
this line:

    dtparam=audio=on

Inside this file you can change some settings that initialize on boot,
its like a bios which the raspberry does not have.

## Video Playback:

If you need video capability in your mpf-mc you need to install one
player that kivy will use to play your videos:

``` shell
sudo apt-get install omxplayer
```

You can try videoplayback with

``` shell
omxplayer your_video.mp4
```

To test the video playback capability under kivy into the framebuffer
just run this command:

``` shell
python3 -m kivy.uix.videoplayer /usr/local/lib/python3.4/dist-packages/mpfmc/tests/machine_files/video/videos/mpf_video_small_test.mp4
```

## Troubleshooting:

More documentation about kivypie can be found here:
<http://kivypie.mitako.eu/kivy-faq.html>

## No sound:

If you have trouble getting sound out of your speakers or monitor have a
look here:

<https://www.raspberrypi.org/documentation/configuration/audio-config.md>

If sound plays via omxplayer but not in MPF, set use_sdl_mixer_loader:
False in your MPF configuration file.

## Do a reboot:

``` shell
sudo reboot
```

## Remote log in:

To log in from your development machine into your raspberry you can do
it easily via ssh. For windows I recommend putty:
<http://www.putty.org/>

## See whats going on on your pinball:

``` shell
sudo dispman_vncserver
```

This starts a vncserver on your raspi and you can log in remotely from a
RealVNCViewer <https://www.realvnc.com/download/viewer/>

Kivypie IP address, port 5900. It is not 100% reliable but fairly
usable. Thanks to Peter Hanzel.

## Start mpf and mpf-mc

To test your installation type

``` shell
mpf
```

in your machine_folder.

Press (STRG+ALT F2) to change to the second terminal tty2.

Login and start mpf-mc inside your machine folder with

``` shell
mpf mc
```

Enjoy!

## What if it did not work?

In the following we list some common problems and solutions. If you got
another problem please ask in our [MPF User
Forum](https://groups.google.com/forum/#!forum/mpf-users).

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
