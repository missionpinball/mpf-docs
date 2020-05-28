How to use SPI Bit Bang in MPF
==============================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/spi_bit_bang`                                                  |
+------------------------------------------------------------------------------+
| :doc:`/config/digital_outputs`                                               |
+------------------------------------------------------------------------------+
| :doc:`/config/switches`                                                      |
+------------------------------------------------------------------------------+

Sometimes you want to read switches from PCBs which contain a shift register
or SPI chip (i.e. a 74HCT165).
This platforms uses two :doc:`/config/digital_outputs` and one
:doc:`/config/switches` on another platform to address the SPI chip.
Please note that this is relatively slow compared to platforms which interface
to SPI natively (such as :doc:`/hardware/spike/index`).
The main purpose of this platform is to access Stern Spike boards using other
control systems than Spike.
Primarily, this allows you to use the
:doc:`Spike Trough </mechs/troughs/spike_trough>` on any system.
However, if you are on Spike or any other platform which natively reads
switches via SPI use those means since they are much more efficient.

This is an example:

.. code-block:: mpf-config

   hardware:
     platform: your_platform, spi_bit_bang      # add your platform first here
   spi_bit_bang:
     miso_pin: s_miso
     cs_pin: o_cs
     clock_pin: o_clock
     bit_time: 50ms
     inputs: 8
   digital_outputs:
     o_cs:
       number: 1
       type: driver
     o_clock:
       number: 2
       type: driver
   switches:
     s_trough_0:
       number: 0
       platform: spi_bit_bang
     s_trough_1:
       number: 1
       platform: spi_bit_bang
     s_trough_2:
       number: 2
       platform: spi_bit_bang
     s_trough_3:
       number: 3
       platform: spi_bit_bang
     s_trough_4:
       number: 4
       platform: spi_bit_bang
     s_trough_5:
       number: 5
       platform: spi_bit_bang
     s_trough_6:
       number: 6
       platform: spi_bit_bang
     s_trough_7:
       number: 7
       platform: spi_bit_bang
     s_miso:
       number: 10

The refresh rate of your platform will be ``bit_time / (inputs + 2)``.
For instance 8 inputs with 50ms ``bit_time`` will result in 2Hz update rate
which is not terribly good.

``bit_time`` determines how long MPF will wait after clocking the chip for
``miso_pin`` to settle.
Depending on your platform it might this might need a while.
Especially if your platform is connected via USB because of USB latency and
jitter.
If your inputs are local (i.e. on a RPi) this might be very short compared
and you might be able to achieve 50Hz.
At the default 2Hz you will wait in average 250ms for a switch change
and 500ms in the worst case.
Have that in mind.

What if it did not work?
------------------------

Have a look at our :doc:`hardware troubleshooting guide </hardware/troubleshooting_hardware>`.
