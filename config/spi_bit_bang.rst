spi_bit_bang:
=============

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``spi_bit_bang:`` section of your config is where you configure the
:doc:`/hardware/spi_bit_bang/index` platform.

.. config


Required settings
-----------------

The following sections are required in the ``spi_bit_bang:`` section of your config:

clock_pin:
~~~~~~~~~~
Single value, type: string name of a :doc:`digital_outputs <digital_outputs>` device. Defaults to empty.

This output is used to clock the SPI chip.

cs_pin:
~~~~~~~
Single value, type: string name of a :doc:`digital_outputs <digital_outputs>` device. Defaults to empty.

This output is used to chip select the SPI chip.
It usually also triggers the parallel read of the chip.

miso_pin:
~~~~~~~~~
Single value, type: string name of a :doc:`switches <switches>` device. Defaults to empty.

This input is read serially to determine the state of your inputs.


Optional settings
-----------------

The following sections are optional in the ``spi_bit_bang:`` section of your config. (If you don't include them, the default will be used).

bit_time:
~~~~~~~~~
Single value, type: ``time string (secs)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Default: ``50ms``

How long should the platform wait until reading the ``miso_pin``.
Depending on your platform it might need a while to settle.
Especially if your platform is connected via USB.
If your inputs are local (i.e. on a RPi) this might be very short compared.

clock_time:
~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Default: ``1ms``

How long should the clock pulse be?
1ms is the lower limit for most platforms and more than long enough for any
chip so this should be good.

debug:
~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

Set to true to get more debug output.

inputs:
~~~~~~~
Single value, type: ``integer``. Default: ``8``

How many inputs should the platform read?
Reading less inputs will result in faster updates.


Related How To guides
---------------------

* :doc:`/hardware/spi_bit_bang/index`
* :doc:`/mechs/troughs/spike_trough`
