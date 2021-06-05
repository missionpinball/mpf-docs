pkone:
======

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``pkone:`` section of your machine-wide config is where you
configure hardware options that are specific to the Penny K Pinball PKONE
Controller. Note that we have a how to guide which includes
:doc:`all the PKONE-specific settings </hardware/pkone/index>` throughout your entire config file,
so be sure to read that if you have Penny K Pinball PKONE hardware.

.. code-block:: mpf-config

    pkone:
      port: com3

.. config


Required settings
-----------------

The following sections are required in the ``pkone:`` section of your config:

port:
~~~~~
Single value, type: ``string``. Defaults to empty.

The serial port name your PKONE controller uses.


Optional settings
-----------------

The following sections are optional in the ``pkone:`` section of your config. (If you don't include them, the default will be used).

baud:
~~~~~
Single value, type: ``integer``. Default: ``115200``

Baud rate to use on the serial port.

console_log:
~~~~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``none``

Log level for the console log for this platform.

debug:
~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

See the :doc:`documentation on the debug setting </config/instructions/debug>`
for details.

file_log:
~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level for the file log for this platform.

watchdog:
~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Default: ``1000``

The PKONE controller includes a "watchdog" timer. A watchdog is a timer
that is continuously counting down towards zero, and if it ever hits
zero, the controller shuts off all the power to the drivers and turns
off all the lights. The idea is that every time MPF runs a game loop
(so, 30 times a second or whatever), MPF tells the FAST controller to
reset the watchdog timer. So this timer is constantly getting reset and
never hits zero.

But if MPF crashes or loses communication with the PKONE hardware, then
this watchdog timer won't be reset. When it hits zero, the PKONE controller
will kill the power to the coils and servos and turn off all lights. This
should prevent an MPF crash from burning up a coil or somehow damaging your
hardware in another way.

You can set the watchdog timer to whatever you want (up to 10 seconds). This
is essentially the maximum time a coil could be stuck "on" if MPF crashes.
The default is 1 second which is probably fine for almost everyone, and you don't
have to include this section in your config if you want to use the default.

Related How To guides
---------------------

* :doc:`/hardware/pkone/index`
