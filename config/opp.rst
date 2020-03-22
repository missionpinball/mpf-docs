opp:
====

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``opp:`` section of your config is where you configure your OPP platform.
See :doc:`/hardware/opp/index` for details.

This is an example:

.. code-block:: mpf-config

    hardware:
      platform: opp
      driverboards: gen2
    opp:
      ports: COM7

.. config


Required settings
-----------------

The following sections are required in the ``opp:`` section of your config:

ports:
~~~~~~
List of one (or more) events.

Serial ports to use.


Optional settings
-----------------

The following sections are optional in the ``opp:`` section of your config. (If you don't include them, the default will be used).

baud:
~~~~~
Single value, type: ``integer``. Default: ``115200``

Baud rate to use on the serial port.

debug:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

Set this to true if you want to see more debug output.

chains:
~~~~~~~
You can define multiple independent chains of OPP boards.
Give them an ID and prefix all your switches and coils with the chain ID.

This is an example:

.. code-block:: mpf-config

   opp:
     ports: /dev/ttyOPP0, /dev/ttyOPP1
     chains:
       0: /dev/ttyOPP0
       1: /dev/ttyOPP1

If you switch was number ``1-3`` before it will be ``0-1-3`` or ``1-1-3`` afterwards.

poll_hz:
~~~~~~~~
Single value, type: ``integer``. Default: ``100``

How many times per section the OPP hardware is polled for switch changes. Default is 100.

