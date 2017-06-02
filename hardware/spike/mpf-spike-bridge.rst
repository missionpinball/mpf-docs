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

2. Mount the SD card
--------------------

You need to mount the Linux root partition (which is probably #3).

On Windows you need an additional tools to mount ext3. We got a
report that "Paragon ExtFS for Windows" works fine for this.

3. Edit /etc/inittab
--------------------

Last line needs to be changed to enable login without a password:

::

   S0:2345:respawn:/sbin/getty 115200 ttyS0 -n -l /bin/sh
   
Furthermore, you might want to add this line to allow USB login
(e.g. if your board does not have DBGU populated).

::

   USB0:2345:respawn:/sbin/getty 115200 ttyUSB0 -n -l /bin/sh

4. Edit /etc/rc2.d/S95game
--------------------------

Add the following line as the new second line in this file:

::

   exit 1

This causes this script to exit instead of running the original
Stern game code. (You can remove this line again if you want
to run the original game again.)

5. Install the spike bridge
---------------------------

Add mpf-spike-bridge to /bin/bridge and mark it as executable.

On Linux this can be done with `chmod +x bridge` from within the folder.

Get the bridge from https://gituhub.com/missionpinball/mpf-spike-bridge

Note that we have a precompiled binary in there (as well as the C source code).


.. note:: It might be hard to mark the bridge binary as executable on Windows
   (but should be possible). If you cannot do this proceed to the next step
   and afterwards do the following:
   
   1. Download putty (might be useful for other purposes as well)
   2. Connect to the new COM port via putty and set speed to 115200 baud.
   3. Power up spike
   4. Press enter and you should get a command promt (if not your serial
      connection is probably not working).
   5. Type the following:
   
   ::

      mount -o remount,rw /
      chmod +x /bin/bridge
      mount -o remount,ro /


6. Unmount the SD card. Put it back in your spike system
--------------------------------------------------------

Unmount the card. Really! Do that! Spike will not boot from a corrupted
filesystem. SD cards may need a while to write everything. Give them those
extra 10s. This is particularly important on windows.

Now when you power up the pinball machine, instead of running the
original game code, it will run the spike bridge which will listen
for commands from the CN2 connector and will send out information
about the state of the machine via that connector.
