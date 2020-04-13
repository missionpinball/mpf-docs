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
List of one (or more) values, each is a type: ``string``. Defaults to empty.

Serial ports to use.


Optional settings
-----------------

The following sections are optional in the ``opp:`` section of your config. (If you don't include them, the default will be used).

baud:
~~~~~
Single value, type: ``integer``. Default: ``115200``

Baud rate to use on the serial port.

chains:
~~~~~~~
One or more sub-entries. Each in the format of ``string`` : ``string``

This is an example:

.. code-block:: mpf-config

   opp:
     ports: /dev/ttyOPP0, /dev/ttyOPP1
     chains:
       0: /dev/ttyOPP0
       1: /dev/ttyOPP1

If you switch was number ``1-3`` before it will be ``0-1-3`` or ``1-1-3`` afterwards.

console_log:
~~~~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``none``

Log level for the console log for this platform.

debug:
~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

Set this to true if you want to see more debug output.

driverboards:
~~~~~~~~~~~~~
Single value, type: one of the following options: gen2. Default: ``gen2``

Similar to ``driverboards`` in the :doc:`/config/hardware` section.
Use this setting if you use multiple playforms (i.e. FAST and OPP) in one
machine.

file_log:
~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level for the file log for this platform.

incand_update_hz:
~~~~~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``25``

The update rate for incandecant bulbs.
Do not set this too high or you might saturate the OPP bus.

poll_hz:
~~~~~~~~
Single value, type: ``integer``. Default: ``100``

How many times per section the OPP hardware is polled for switch changes. Default is 100.


Related How To guides
---------------------

* :doc:`/hardware/opp/index`
