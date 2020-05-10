How to modify a Stern SPIKE SD card & install the MPF SPIKE bridge
==================================================================

1. Backup the existing SD card
------------------------------

When you download firmware updates from Stern's websites to a USB stick,
the updates only contain the specific parts of the code that have changed
since the original version.

In other words, if you break or somehow screw up the SD card with the
SPIKE game code on it, you will not be able to fix it by
re-downloading the latest firmware. (You'll have to call Stern and get
a new SD card with the software already on it.)

So be very careful here.

Our recommendation is to create an image of the original SD card, and then
put the original in a safe place and then copy the image to a new SD card.
That way you're always working with a copy and the original SD card is
never touched.

Note that we do not yet know which cards are best or will be fully
compatible, so our recommendation is to get a card that's around the
same size as the current one. Let us know what you find in terms of
what works and what doesn't!

Known SD Cards that work:
SanDisk Ultra Plus 16GB purchased from Best Buy

One tool you can use to backup an image of your SD Card is HDD Raw Copy. This tool will back up a copy to your local
drive and you can restore it to the new SD card. For a tutorial on backing up your Stern SD card using HDD Copy check
out the following video.

https://www.youtube.com/watch?v=KlKw8raWixI&t=35s

.. note:: Save a copy of your SD card image in case you need to restore your SD card. If, at one point, your SD memory
          card becames corrupted, restoring from the backed up image fixes the issue.

2. Mount the SD card
--------------------

You need to mount the Linux root partition (which is probably #3).

On Windows you need an additional tools to mount ext3. We got a
report that "Paragon ExtFS for Windows" works fine for this.

On Mac OS X, the tool "FUSE-ext2" is an option. You will most likely need to use sudo, and depending on your configuration
the appropriate disk device may vary. In the following example, the Linux root is on partition 3 of the SD card, which is disk2:

::

   sudo fuse-ext2 /dev/disk2s3 /Volumes/SD -o force


3. Edit /etc/inittab
--------------------

Last line needs to be changed to enable login without a password:

::

   S0:2345:respawn:/sbin/getty 115200 ttyS0 -n -l /bin/sh

Furthermore, you might want to add this line to allow USB login
(e.g. if your board does not have DBGU populated).

::

   USB0:2345:respawn:/sbin/getty 115200 ttyUSB0 -n -l /bin/sh

If your USB to serial adapter has a "RTS" and "CTS" pin or if you are using
a null-modem cabel you can enable hardware flow control.
In that case use the following line (notice that we added ``-h``):

::

   USB0:2345:respawn:/sbin/getty 115200 ttyUSB0 -h -n -l /bin/sh

4. Edit /etc/rc2.d/S95game
--------------------------

Add the following two lines as the new second and third lines in this file:

::

   /usr/local/bin/avrisp /usr/local/spike/netbridge.hex /usr/local/spike/netbridge.fuses
   exit 1

This causes this script to exit instead of running the original
Stern game code. (You can remove this line again if you want
to run the original game again.)

5. Install the spike bridge
---------------------------

Add mpf-spike-bridge to /bin/bridge and mark it as executable.

On Linux this can be done with `chmod +x bridge` from within the folder.

Get the bridge from https://github.com/missionpinball/mpf-spike

Note that we have a precompiled binary in there (as well as the Rust source code).


.. note:: It might be hard to mark the bridge binary as executable on Windows
   (but should be possible). If you cannot do this proceed to the next step
   and afterwards do the following:

   1. Download PuTTY from www.putty.org.  PuTTY is a free telnet app that allows you to remotely connect to the Linux
      OS running on the SPIKE system. PuTTY was also useful for verifying the connection from your Windows machine to
      the Linux OS running on SPIKE.
   2. In PuTTY, select the "Serial" buttont, change to correct COM (COM1, COM3, COM4, etc) port and set speed to
      115200 baud. If you are unsure of which COM port Windows used when you plugged in your cable, open the Device
      Manager in the Control Panel. Click open the PORTS drop down to find which COM port is in use.
   3. Power up spike
   4. Press enter and you should get a command promt (if not, your serial
      connection is probably not working).
   5. Type the following:

   ::

      mount -o remount,rw /
      chmod +x /bin/bridge
      mount -o remount,ro /

.. note:: On OS X with fuse-ext2, overwriting files can fail without a message. When updating mpf-spike-bridge,
   you may want to remove the old bridge file before copying the new one.

   ::
      rm <sd_mount>/bin/bridge
      cp <your_path>/mpf-spike-bridge/bridge <sd_mount>/bin/bridge
      chmod 755 <sd_mount>/bin/bridge


6. Unmount the SD card. Put it back in your spike system
--------------------------------------------------------

Unmount the card. Really! Do that! Spike will not boot from a corrupted
filesystem. SD cards may need a while to write everything. Give them those
extra 10s. This is particularly important on Windows. If the red LED in
the middle of the Stern CPU board is not blinking your SD card may be corrupt.

.. note:: The SD card can become corrupted when removing the card without ejecting it properly. You can fix this by
          restoring your backup from above.

Now when you power up the pinball machine, instead of running the
original game code, it will run the spike bridge which will listen
for commands from the CN2 connector and will send out information
about the state of the machine via that connector.

What if it did not work?
------------------------

Have a look at our :doc:`SPIKE troubleshooting guide <troubleshooting>`.
