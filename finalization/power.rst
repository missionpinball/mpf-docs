Controlling your machine & computer power on / power off
========================================================

Unlike computers pinball machines are not expected to have a shutdown
procedure.
Users tend to just turn off the power which might cause problems with your
operating system and filesystems.

Two general approaches exist here:

Computer Start-up and Shutdown Controller
-----------------------------------------

Scott Danesi sells a board called
`Computer Start-up and Shutdown Controller (CSSC) <http://www.danesidesigns.com/products/cssc/>`_
which will trigger a shutdown of your PC when the main power supply of your
machine is turned of (part number: #600-0322-00).
However, you need to make sure that the PC still has power until shutdown is
complete.
You can either use a separate outlet (and make sure not to disconnect it early)
or add an Uninterruptible power supply (UPS) to your machine.

This solution is very useful during development and early prototypes.
Especially if you are using (older) Windows which very much dislikes unclean
shutdowns.
However, with modern operating systems and journalling filesystems (such as
ext4 or ReFS) this became less of an issue.

Make it work on Linux
~~~~~~~~~~~~~~~~~~~~~

If you use a Linux distribution with systemd set ``HandlePowerKey=ignore``
in ``/etc/systemd/logind.conf``.

To handle power button events install ``acpid``.
Add ``/etc/acpi/events/powerbtn`` with the following content (or change it if
if already exists):

.. code-block:: bash

   event=button[ /]power
   action=/sbin/poweroff

Restart ``acpid`` (or your computer) and you should be good to go.


Read-only Filsystems
--------------------

When you finished your machine you will usually run in on Linux on an embedded
PC.
Multiple solutions exist here such as OpenEmbedded/Yocto.
At that point you will usually have a build process which builds an image
which is then deployed to your target PC (via a SD card or flash process).
This image will be mounted read-only and cannot get damaged by a crash.

Furthermore, you often add one partition to store audits/highscores and
sometimes logs.
It is recommended to use a journaling filesystem for this partition and expect
it to break.
Usually, there is some kind of reset mechanism to wipe this partition in case
it gets corrupted (sometimes automatic in case it can no longer be mounted).

We are happy to discuss those topics in our forum (and extend this section as
a result of that).
