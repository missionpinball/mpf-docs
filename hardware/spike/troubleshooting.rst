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


.. include:: ../include_troubleshooting_coils.rst
.. include:: ../include_troubleshooting_lights.rst
.. include:: ../include_troubleshooting.rst
