Troubleshooting Spike
=====================

If you got problems with your hardware platform we first recommend to read our
:doc:`troubleshooting guide </troubleshooting/index>`.
Here are some hardware platform specific steps:

Enable Debugging
----------------

If you got problems with your platform try to enable ``debug`` first.
As described in the
:doc:`general debugging section </troubleshooting/general_debugging>`
of our :doc:`troubleshooting guide </troubleshooting/index>`
this is done by
adding ``debug: true`` to your ``spike`` config section:

.. code-block:: mpf-config

   spike:
     debug: true

This will add a lot more debugging and might slow down MPF a bit.
We recommend to disable/remove it after finishing debugging.

Debugging the MPF-Spike Bridge
------------------------------

To debug the bridge you can enable more logging to a USB drive.
First open a shell to your serial port (the one connected to your Spike).
Stick some USB drive to a USB port on Spike and mount it to ``/mnt/``.

If you USB drive contains a partition use:

.. code-block:: console

   mount /dev/sda1 /mnt

Alternatively use:

.. code-block:: console

   mount /dev/sda /mnt

If you did not get an error your operation succeeded.
You can have a look at the content of your stick using:

.. code-block:: console

   ls /mnt

Afterwards, add the following options to your spike config:

.. code-block:: mpf-config

   spike:
     debug: true
     bridge_debug: true
     bridge_debug_log: /mnt/spike.log

Now close your shell and start MPF.
MPF will instruct the bridge to create a log file on your USB drive with more
debug information about the nodebus and other things.
This will be helpful to find issues with incorrect commands or responses.

To safely unmount your drive stop MPF, open the console again and type:

.. code-block:: console

   unmount /mnt
   sync

You can now safely remove the USB drive and download the file on your PC.

Capturing the Bus Traffic of Your Game Using Interceptty
--------------------------------------------------------

To understand what the game does it is sometimes helpful to capture what it
sends and receives on netbus.
Unfortunately, we don't know how to enable debugging or verbose mode in the
game binary.
(Please let us know if you find out.)

Instead, we redirect the serial in Linux and capture the bus this way.
Unfortunately, this is not perfect and at least on Spike 1 causes timing
issues.
Nevertheless, this shows us how things work and also sometimes teaches us
how error recovery works in Spike.

Get our `interceptty binary <https://github.com/missionpinball/interceptty/raw/master/bin/interceptty-arm>`_
and put it on your USB drive.
Mount the USB drive as above and run the following command:

Spike 1
^^^^^^^

.. code-block:: console

   cd /mnt && chmod +x interceptty-arm
   mv /dev/ttyS4 /dev/ttyS4_real; interceptty-arm -s 'ispeed 460800 ospeed 460800' -l /dev/ttyS4_real /dev/ttyS4 > /mnt/serial_dump &

Spike 2
^^^^^^^

.. code-block:: console

   cd /mnt && chmod +x interceptty-arm
   mv /dev/ttymxc1 /dev/ttymxc1_real; interceptty-arm -s 'ispeed 460800 ospeed 460800' -l /dev/ttymxc1_real /dev/ttymxc1 > /mnt/serial_dump &

This command should return instantly and run in the background.
Now start the game binary in the foreground:

.. code-block:: console

   /games/game

Some versions of some games give you a nice service CLI here.
Play the game and make sure you activate all relevant features.
Flippers might not work some times.
Just try again as this unfortunately sometimes messes up timings.

When you are done after a while stop the game using ``ctrl+c``.
Then type ``fg`` to get interceptty in the foreground and stop it
using ``ctrl+c``.

Restore the serial:

Spike 1
^^^^^^^

.. code-block:: console

   mv /dev/ttyS4_real /dev/ttyS4

Spike 2
^^^^^^^

.. code-block:: console

   mv /dev/ttymxc1_real /dev/ttymxc1

Now unmount the USB drive as above and you are done.
Please share the capture on the MPF user forum.



.. include:: ../include_troubleshooting_coils.rst
.. include:: ../include_troubleshooting_lights.rst
.. include:: ../include_troubleshooting.rst
