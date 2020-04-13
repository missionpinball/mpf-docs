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
     flow_control: true
     debug: false
     nodes: 0, 1, 8, 9, 10, 11

.. config


Required settings
-----------------

The following sections are required in the ``spike:`` section of your config:

baud:
~~~~~
Single value, type: ``integer``. Defaults to empty.

This needs to match the value from Step 3 in the MPF SPIKE bridge
instructions.

nodes:
~~~~~~
List of one (or more) values, each is a type: ``integer``. Defaults to empty.

Configure the nodes from your manual. Note that there should
always be a node 0 and 1.

port:
~~~~~
Single value, type: ``string``. Defaults to empty.

on the RPi.


Optional settings
-----------------

The following sections are optional in the ``spike:`` section of your config. (If you don't include them, the default will be used).

bridge_debug:
~~~~~~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

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
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

Set to true for troubleshooting to print more details in the log.

default_debounce_close:
~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Default: ``4``

Default debounce close time.

default_debounce_open:
~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Default: ``4``

Default debounce open time.

file_log:
~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level to file.

flow_control:
~~~~~~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

Set to ``True`` to enable serial RTS/CTS flow control between MPF and the Spike bridge. May
help improve responsiveness and reduce latency when streaming display data to the DMD.
Default is ``False``.

max_led_batch_size:
~~~~~~~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``6``

Maximum number of leds to batch.
This seems to differ between machines.
``3`` seems to be safe everywhere.

node_config:
~~~~~~~~~~~~
One or more sub-entries. Each in the format of ``integer`` : :doc:`spike_node <spike_node>`

A list of your nodes with their config each.
This is entirely optional but may improve performance.

oc_time:
~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Default: ``100``

Some time related to over current.
We believe this is the time over which spike averages the value.

periodically_query_nodes:
~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

Whether to periodically query nodes.
The spike game does this but we do not use the values so it is probably
save to disable this.
Related to over current detection.

poll_hz:
~~~~~~~~
Single value, type: ``integer``. Default: ``1000``

Numeric value of how many times per second MPF will poll the SPIKE
system to check for switch changes. Default is ``1000``.

response_time:
~~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``837``

A parameter send to the spike bus driver.
We believe this is some kind of bus timeout.
No need to change it.

runtime_baud:
~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``921600``

Baud rate to use during runtime.

spike_version:
~~~~~~~~~~~~~~
Single value, type: one of the following options: 1, 2. Default: ``1``

The spike version you are using.

use_send_key:
~~~~~~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

Send some magic commands like Spike does.
Not needed as far as we know.

verify_checksums_on_readback:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``true``

Whether to verify checksums on readback from commands.
This should be always on unless you are debugging something.

wait_times:
~~~~~~~~~~~
One or more sub-entries. Each in the format of ``integer`` : ``integer``

A list of commands and their corresponding wait times on the bus.
Ususally, you do not have to change this.


Related How To guides
---------------------

* :doc:`/hardware/spike/index`
