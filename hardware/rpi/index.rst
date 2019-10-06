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
and servos on the RPi remotely (or locally) using pigpio. You need to install
the ``apigpio`` extension via pip to use it:

.. code-block:: console

   pip3 install apigpio
   
The `pigpiod <http://abyz.me.uk/rpi/pigpio/pigpiod.html>`_ service needs to be running 
(in this example on localhost port 8888,  which is the default setting). To install 
it and enable is (on debian based systems) : 

.. code-block:: console

  apt install pigpiod
  systemctl enable pigpiod.service 
  systemctl start pigpiod.service 

The `enable` step gets the service running at startup, thus it is optionnal. 

This is an example config:

.. code-block:: mpf-config

   hardware:
       platform: rpi

   raspberry_pi:
       ip: localhost
       port: 8888

   switches:
       s_switch_1:
           number: 1
       s_switch_7:
           number: 7

   coils:
       output_23:
           number: 23
           default_pulse_ms: 23
       output_30:
           number: 30
           default_hold_power: 1.0
       output_2:
           number: 2
           default_hold_power: 0.2

   servos:
       servo_10:
           number: 10


Configure the ip of your RaspberryPi in the ``raspberry_pi`` section.
You may use localhost if you are running MPF on the RPi.
Any pin on the RPi can be used as either input or output.
Additionally, you may use servos on any pin.
