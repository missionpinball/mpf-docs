spike:
======


*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

The ``spike:`` section of your machine-wide config is where you
configure hardware options that are specific to the SPIKE interface
when you're using MPF with a Stern SPIKE machine.
Note that we have a how to guide which includes
:doc:`all the SPIKE-specific settings </hardware/spike/index>` throughout your entire
config file, so be sure to read that if you have a SPIKE machine.

.. code-block:: yaml

   hardware:
      platform: spike

   spike:
      port: /dev/ttyUSB0
      baud: 115200
      debug: False
      nodes: 0, 1, 8, 9, 10, 116

Required Settings
-----------------

The following sections are required in the ``spike:`` section of your config:

port:
~~~~~

Use the port of your USB-serial adapter or of the internal serial
on the RPi.

baud:
~~~~~

This needs to match the value from Step 3 in the MPF SPIKE bridge
instructions.

nodes:
~~~~~~

Configure the nodes from your manual. Note that there should
always be a node 0 and 1.

Optional Settings
-----------------
The following sections are optional in the ``spike:`` section of your config.
(If you don't include them, the default will be used).

debug:
~~~~~~

Set to true for troubleshooting to print more details in the log.
Default is ``False``.

flow_control:
~~~~~~~~~~~~~

Set to ``True`` to enable serial RTS/CTS flow control between MPF and the Spike bridge. May
help improve responsiveness and reduce latency when streaming display data to the DMD.
Default is ``False``.

poll_hz:
~~~~~~~~

Numeric value of how many times per second MPF will poll the SPIKE
system to check for switch changes. Default is ``1000``.

connection:
~~~~~~~~~~~

Default is ``shell``. Currently there are no other options.
