spike:
======

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``spike:`` section of your machine-wide config is where you
configure hardware options that are specific to the SPIKE interface
when you're using MPF with a Stern SPIKE machine.
Note that we have a how to guide which includes
:doc:`all the SPIKE-specific settings </hardware/spike/index>` throughout your entire
config file, so be sure to read that if you have a SPIKE machine.

.. code-block:: mpf-config

   hardware:
      platform: spike

   spike:
      port: /dev/ttyUSB0
      baud: 115200
      runtime_baud: 3000000
      flow_control: True
      debug: False
      nodes: 0, 1, 8, 9, 10, 11


Required settings
-----------------

The following sections are required in the ``spike:`` section of your config:

baud:
~~~~~
Single value, type: ``integer``.

This needs to match the value from Step 3 in the MPF SPIKE bridge
instructions.

nodes:
~~~~~~
List of one (or more) values, each is a type: ``integer``.

Configure the nodes from your manual. Note that there should
always be a node 0 and 1.

port:
~~~~~
Single value, type: ``string``.

on the RPi.


Optional settings
-----------------

The following sections are optional in the ``spike:`` section of your config. (If you don't include them, the default will be used).

bridge_debug:
~~~~~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

Set to True if you want to debug your MPF Spike bridge.

bridge_debug_log:
~~~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``/mnt/spike.log``

Path on your Spike system where the bridge logs to if ``bridge_debug`` is ``True``.
Needs to be writable and sufficiently large.
A USB stick mounted to ``/mnt/`` will work fine.

bridge_path:
~~~~~~~~~~~~
Single value, type: ``string``. Default: ``/bin/bridge``

Path of your bridge.

console_log:
~~~~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``none``

Log level to console.

debug:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

Set to true for troubleshooting to print more details in the log.

file_log:
~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level to file.

flow_control:
~~~~~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

Set to ``True`` to enable serial RTS/CTS flow control between MPF and the Spike bridge. May
help improve responsiveness and reduce latency when streaming display data to the DMD.
Default is ``False``.

poll_hz:
~~~~~~~~
Single value, type: ``integer``. Default: ``1000``

Numeric value of how many times per second MPF will poll the SPIKE
system to check for switch changes. Default is ``1000``.

runtime_baud:
~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``921600``

Baud rate to use during runtime.

use_send_key:
~~~~~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

Send some magic commands like Spike does.
Not needed as far as we know.

wait_times:
~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``int``:``int``.

A list of commands and their corresponding wait times on the bus.
Ususally, you do not have to change this.
