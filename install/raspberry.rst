Installing MPF on a Raspberry Pi running in a framebuffer
=========================================================

One first word:
Don't try to install mpf on a Raspberry Pi B+ or Raspberry zero, it just won't work or will be very slow.
Get yourself at least a Raspberry Pi 2 or 3, they have a quadcore processor running with more than 900MHz.

One nice thing we will have afterwards is a lowcost PC which will run fast enough for mpf-mc with audio, video, antialiazing and touchscreen support.

Let's start:

- get the latest Kivypie version (a minimal version without X-Server but preinstalled kivy) here:
  http://kivypie.mitako.eu/kivy-download.html
  Many Kudos to Albert Casals and their group, since normally its a pain to install kivy on a raspberry (compiling lasts forever).

- depending on your development os use Win32 Diskimager, dd, Imagewriter... to write your image to the sd-card (use at least an 8 GB Card). You can find Instructions here:
  https://www.raspberrypi.org/documentation/installation/installing-images/

- insert the sd-card into your pi and boot it up (first boot does take some time since it sets some os specific parameters)

- login with user:sysop password:posys

- now type this:

::

    sudo raspi-config

and choose 1. Expand Filesystem to use the whole SD-Card Space, we will need it.
You can change your username and localization settings too.

After that we will give the GPU a bit more of RAM:

Go to Advanced Options/A3 Memory split
and change the value to 256.

Now reboot, login and type:

::

    sudo apt-get update

to update the debian repositories links.

The standard /tmp "folder" is too small on pipaos, just type:

::

    sudo umount /tmp

to get rid of it. (It will be created automatically if needed and will have the whole space afterwards)

Now run the :doc:`MPF Linux Debian installer </install/linux>`. It will install MPF, MPF-MC and all dependencies for you.

This will take some time as it may compile some drivers mpf-mc needs like the audio driver.
Sometimes it looks like it hangs, but it does not. It will take up to half an hour, at least on a Raspberry 1 (which you should not use). Compiling is really slow on the Raspi.

Now copy your machine folder from your develop station or create a new one under your home directory (/home/sysop/your_machine)

If you need a file-manager start mc (No, not the mpf mediacontroller, its the midnight commander ;-))

If you need to copy your folders from an usb-stick you have to manually mount it (we dont have X, so everything has to be done by hand).

::

    sudo mount /dev/sda1 /mnt

This works in 90% otherwise your stick is not sda1, just look inside the /dev folder to find out which device you have to mount or type

::

    lsblk

to list your block devices.

Now you find the contents of your stick in /mnt.

To tell mpf-mc and the underlying kivy to use the framebuffer via SDL2 you have to put this in your machine/config/config.yaml:

::

  window:
    width: 1280
    height: 800
    title: Your ultimate pinball
    resizable: false
    fullscreen: auto
    borderless: false
    exit_on_escape: true

  kivy_config:
    graphics:
	  fbo: force-hardware

More or less important last steps:
----------------------------------

Serial communication:
---------------------
Linux always had and has the possibility to log in via a serial connection.
Since all of the pinball hardware I'm aware off uses serial communication with mpf leaving this feature running is not good at all, since you will get noise from your kernel.
The device is called /dev/ttyAMA0 and you need to stop it from starting:

Type:

::

  sudo systemctl disable serial-getty@ttyAMA0.service

Now you have to disable the console itself:

::

  sudo mc

to start Midnight Commander as root (normally you should not do this, but this time you have to.)

Now go to /boot and press F4 over cmdline.txt.

Remove these entries:

console=ttyAMA0,115200 kgdboc=ttyAMA0, 115200

and save the file.

You have the possibility to connect RS 232 devices directly to the raspi but take care, the voltage levels are 3.3V on the raspi gpio.
Further instructions here:
http://elinux.org/RPi_Serial_Connection

Sound output:
-------------

Navigate to /boot/config.txt if you want to use audio out of the Raspberry built in ""soundcard"":
edit this file as root and insert this line:

::

  dtparam=audio=on

Inside this file you can change some settings that initialize on boot, its like a bios which the raspberry does not have.

Video Playback:
---------------
If you need video capability in your mpf-mc you need to install one player that kivy will use to play your videos:

::

  sudo apt-get install omxplayer

You can try videoplayback with

::

  omxplayer your_video.mp4

To test the video playback capability under kivy into the framebuffer just run this command:

::

  python3 -m kivy.uix.videoplayer /usr/local/lib/python3.4/dist-packages/mpfmc/tests/machine_files/video/videos/mpf_video_small_test.mp4

Troubleshooting:
----------------

No sound:
---------
If you have trouble getting sound out of your speakers or monitor have a look here:

https://www.raspberrypi.org/documentation/configuration/audio-config.md

Do a reboot:
------------

::

  sudo reboot

OPP Hardware not found:
-----------------------
If you are using OPP Hardware you have to blacklist the Cypress Thermometer:
in /etc/modprobe.d/blacklist.conf add:

::

  blacklist cytherm

If blacklist.conf does not exist, just create a new empty file as root.
The USB Enumerator thinks a Thermometer is plugged in but it is definitely not ;-)

Remote log in:
--------------
To log in from your development machine into your raspberry you can do it easily via ssh.
For windows I recommend putty:
http://www.putty.org/

See whats going on on your pinball:
-----------------------------------

::

  sudo dispman_vncserver

This starts a vncserver on your raspi and you can log in remotely from a RealVNCViewer
https://www.realvnc.com/download/viewer/

Kivypie IP address, port 5900. It is not 100% reliable but fairly usable. Thanks to Peter Hanzel.

Start mpf and mpf-mc
--------------------

To test your installation type

::

  mpf

in your machine_folder.

Press (STRG+ALT F2) to change to the second terminal tty2.

Login and start mpf-mc inside your machine folder with

::

  mpf mc

Enjoy!
