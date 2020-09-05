rpi_dmd:
========

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``rpi_dmd:`` section of your config is where you configure a :doc:`RPi DMD </hardware/rpi_dmd/index>`.
All settings are directly passed to the
`rpi-rgb-led-matrix library <https://github.com/hzeller/rpi-rgb-led-matrix>`_.
Read their documentation (or the source) if in doubt.

.. config


Optional settings
-----------------

The following sections are optional in the ``rpi_dmd:`` section of your config. (If you don't include them, the default will be used).

brightness:
~~~~~~~~~~~
Single value, type: ``integer``. Default: ``100``

Brightness value to use between 0 and 100\%.

chain_length:
~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``1``

Number of panels in your chain. Longer chains mean less frames per second.

cols:
~~~~~
Single value, type: ``integer``. Default: ``32``

How many columns of LEDs does your matrix have?

daemon:
~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

Leave this at ``False`` of thing will go wrong.

disable_hardware_pulsing:
~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

Disable hardware pulsing. Only useful for debugging.

drop_privileges:
~~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``true``

Drop root rights after opening the hardware.
It is highly recommended to leave it this way.

gpio_slowdown:
~~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``1``

Slow down the GPIOs a bit. Otherwise the RPi might be too fast for your LEDs.

hardware_mapping:
~~~~~~~~~~~~~~~~~
Single value, type: one of the following options: regular, adafruit-hat, adafruit-hat-pwm. Default: ``regular``

Select which hardware you are using.
Consult manual if in doubt.

inverse_colors:
~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

Inverse colors. You know it if you see it.

led_rgb_sequence:
~~~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``RGB``

The color order of your LEDs. You know it if you see that colors are mixed up.

multiplexing:
~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``0``

Select your multiplexing settings. Consult manual.

parallel:
~~~~~~~~~
Single value, type: ``integer``. Default: ``1``

How many chains to run in parallel?

pixel_mapper_config:
~~~~~~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``""``

Select your pixel mapper. Consult manual.

pwm_bits:
~~~~~~~~~
Single value, type: ``integer``. Default: ``11``

How many bits to use for PWM?

pwm_lsb_nanoseconds:
~~~~~~~~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``130``

On-time for your LEDs. Lower means more fps but potential less quality.

row_address_type:
~~~~~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``0``

Row address type. Consult manual.

rows:
~~~~~
Single value, type: ``integer``. Default: ``32``

How many rows of LEDs does your matrix have?

scan_mode:
~~~~~~~~~~
Single value, type: ``integer``. Default: ``0``

Scan mode. 0 = progressive; 1 = interlaced. Consult manual.

show_refresh_rate:
~~~~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

Print refresh rate on terminal.


Related How To guides
---------------------

* :doc:`/hardware/rpi_dmd/index`
