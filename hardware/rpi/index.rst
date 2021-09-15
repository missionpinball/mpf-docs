Raspberry PI (pigpio)
=====================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/hardware`                                                      |
+------------------------------------------------------------------------------+
| :doc:`/config/raspberry_pi`                                                  |
+------------------------------------------------------------------------------+
| :doc:`/config/switches`                                                      |
+------------------------------------------------------------------------------+
| :doc:`/config/coils`                                                         |
+------------------------------------------------------------------------------+
| :doc:`/config/servos`                                                        |
+------------------------------------------------------------------------------+


The rpi platform can be used to control inputs (switches), outputs (coils), I2C
and servos on the RPi remotely (or locally) using pigpio.

Video about the Raspberry PI and MPF:

.. youtube:: ihj5O0J-mD0

Installation
------------

You need to install the ``apigpio`` extension via pip to use it:

.. code-block:: console

   pip3 install apigpio_mpf

The `pigpiod <http://abyz.me.uk/rpi/pigpio/pigpiod.html>`_ service needs to be running
(in this example on localhost port 8888,  which is the default setting). To install
it and enable is (on debian based systems):

.. code-block:: console

  apt install pigpiod
  systemctl enable pigpiod.service
  systemctl start pigpiod.service

The `enable` step gets the service running at startup, thus it is optional.

Using pigpio via network
------------------------

If you want to use your RPi over ethernet you have to edit
``/lib/systemd/system/pigpiod.service`` and change
``ExecStart=/usr/bin/pigpiod -l`` to ``ExecStart=/usr/bin/pigpiod``.
This is not needed if you run MPF on the RPi itself.
Make sure your Raspberry PI is not accessible from the internet and
the network is segmented properly.

Config
------

This is an example config:

.. code-block:: mpf-config

   hardware:
     platform: rpi
   raspberry_pi:
     ip: localhost
     port: 8888
   switches:
     s_switch_8:
       number: 8
     s_switch_7:
       number: 7
   coils:
     output_2:
       number: 2
       default_pulse_ms: 1000
   servos:
     servo_26:
       number: 26

Configure the ip of your RaspberryPi in the ``raspberry_pi`` section.
You may use localhost if you are running MPF on the RPi.
Any pin on the RPi can be used as either input or output.
Additionally, you may use servos on any pin.

Available GPIOs
---------------

You check GPIO locations on your RPi at `pinout.xyz <https://pinout.xyz/>`_.
Please note that you have to use the Broadcom GPIO numbers instead of the
pin numbers.
Those slightly differ between different RPi models.
If you get permission errors in your MPF log this is usually because you
used a GPIO number which does not exist on your hardware.

Is this a real pinball controller?
----------------------------------

No. The RPi is not a pinball controller for various reasons:

 * Drivers are missing to drive coils
 * Inputs are unprotected and any error current will fry the CPU
 * Hardware rules are not supported by the ``pigpio`` daemon
 * A watchdog is missing

This platform is meant as a cheap interface for peripherals such as DMDs,
segment displays lights, servos, steppers and more.
You can also use it for inputs to some extend.

Can this be turned into a pinball controller?
---------------------------------------------

Sure it can. We just did not do that here. Have a look at
:doc:`/hardware/apc/index` which is kind of that already.

If you want to do it with pigpio you would have to do the following (and
probably more):

 * Build a PCB with FETs to drive outputs. Add proper protection.
 * Protect your inputs against high and negative voltages.
 * Implement hardware rules in ``pigpio`` (might be possible with callbacks)
 * Run a realtime linux for proper timing of your rules
 * Add a some watchdog (either in Linux or in hardware)

What if it did not work?
------------------------

Have a look at our :doc:`hardware troubleshooting guide </hardware/troubleshooting_hardware>`.
