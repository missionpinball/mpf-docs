smartmatrix:
============

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``smartmatrix:`` section of your config is where you configure RGB DMD devices.

This is an example:

.. code-block:: mpf-config

   #config_version=5
   hardware:
     rgb_dmd: smartmatrix
   smartmatrix:
     my_smartmatrix:
       port: com4
       baud: 4000000
   displays:
     dmd:
       width: 128
       height: 32
   rgb_dmds:
     my_smartmatrix:
       hardware_brightness: .5

Required settings
-----------------

The following sections are required in the ``smartmatrix:`` section of your config:

port:
~~~~~
Single value, type: ``string``.

Name of the serial port of your smartmatrix device. This will be `comX` on Windows.
On Linux and Mac it depends on the usb-serial chip (usually /dev/ttyUSBX on
linux or /dev/tty.usbmodemYYY on Mac).

baud:
~~~~~

Baud rate of your serial port. Depends on the smartmatrix firmware.


Optional settings
-----------------

The following sections are optional in the ``smartmatrix:`` section of your config. (If you don't include them, the default will be used).

old_cookie:
~~~~~~~~~~~

Set to true to use the old cookie. Will use the new cookie by default.
