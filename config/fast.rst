fast:
=====

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

The ``fast:`` section of your machine-wide config is where you
configure hardware options that are specific to the FAST Pinball
Controller. Note that we have a how to guide which includes
:doc:`all the FAST-specific settings </hardware/fast/index>` throughout your entire config file,
so be sure to read that if you have FAST hardware.

.. code-block:: yaml

    fast:
        ports: com3, com4, com5
        config_number_format: hex
        baud: 921600
        watchdog: 1s
        default_debounce_close: 10ms
        default_debounce_open: 30ms

Required settings
-----------------

The following sections are required in the ``fast:`` section of your config:

default_normal_debounce_close:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings) </config/instructions/time_strings>` .

Specifies the default value for the debounce time for switches that are
configured with ``debounce: normal`` when they close.

Even though this is listed as a required setting, this entry is in the
``mpfconfig.yaml`` file, (with a value of ``10ms``), so you don't have to
enter it here unless you want to override that.

Also, keep in mind that this setting is only a default. You can override
it for any switch in that switch's config.

default_normal_debounce_open:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings) </config/instructions/time_strings>` .

Specifies the default value for the debounce time for switches that are
configured with ``debounce: normal`` when they open.

Even though this is listed as a required setting, this entry is in the
``mpfconfig.yaml`` file, (with a value of ``10ms``), so you don't have to
enter it here unless you want to override that.

Also, keep in mind that this setting is only a default. You can override
it for any switch in that switch's config.

default_quick_debounce_close:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings) </config/instructions/time_strings>` .

Specifies the default value for the debounce time for switches that are
configured with ``debounce: quick`` when they close.

Even though this is listed as a required setting, this entry is in the
``mpfconfig.yaml`` file, (with a value of ``2ms``), so you don't have to
enter it here unless you want to override that.

Also, keep in mind that this setting is only a default. You can override
it for any switch in that switch's config.

default_quick_debounce_open:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings) </config/instructions/time_strings>` .

Specifies the default value for the debounce time for switches that are
configured with ``debounce: quick`` when they open.

Even though this is listed as a required setting, this entry is in the
``mpfconfig.yaml`` file, (with a value of ``2ms``), so you don't have to
enter it here unless you want to override that.

Also, keep in mind that this setting is only a default. You can override
it for any switch in that switch's config.

ports:
~~~~~~
List of one (or more) values, each is a type: ``string``.

A comma-separated list of the serial port names your FAST controller uses.

Optional settings
-----------------

The following sections are optional in the ``fast:`` section of your config. (If you don't include them, the default will be used).

baud:
~~~~~
Single value, type: ``integer``. Default: ``921600``

The baud rate for the FAST COM ports.

config_number_format:
~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``hex``

This setting controls whether you to specify the addresses of your
lights, LEDs, coils, and switches by their integer values or as hex
values. Note if you configure
your `driverboards:` as `wpc` (in the `hardware:` section),
then you also have the option of using the original WPC numbers from
your operators manual.

debug:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

See the :doc:`documentation on the debug setting </config/instructions/debug>`
for details.

hardware_led_fade_time:
~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings) </config/instructions/time_strings>` . Default: ``0``

Controls how quickly LEDs will fade to their new color when they receive a
color instruction from MPF.

The default is 0, which means if you set an LED to be red, it will turn
red instantly. But if you set ``hardware_led_fade_time: 20``, that means that
when an LED receives an instruction to turn RED, it will smoothly fade from
whatever color it is now to red over a period of 20ms.

You can play with different settings to pick something you like. Some people
prefer the instant 0ms snappiness that's possible with LEDs. Others like to
set this value to something like ``100ms`` which gives LEDs the more gentle
fade style reminiscent of incandescent bulbs.

watchdog:
~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings) </config/instructions/time_strings>` . Default: ``1000``

The FAST controllers include a "watchdog" timer. A watchdog is a timer
that is continuously counting down towards zero, and if it ever hits
zero, the controller shuts off all the power to the drivers. The idea
is that every time MPF runs a game loop (so, 30 times a second or
whatever), MPF tells the FAST controller to reset the watchdog timer.
So this timer is constantly getting reset and never hits zero.

But if MPF crashes or loses communication with the FAST controller, then
this watchdog timer won't be reset. When it hits zero, the FAST controller
will kill the power to the drivers. This should prevent an MPF crash from
burning up driver or somehow damaging your hardware in another way.

You can
set the watchdog timer to whatever you want. (This is essentially the
max time a driver could be stuck "on" if MPF crashes.) The default is
1 second which is probably fine for almost everyone, and you don't
have to include this section in your config if you want to use the
default.

net_buffer:
~~~~~~~~~~~

single|int|10

:doc:`/about/help_us_to_write_it`

rgb_buffer:
~~~~~~~~~~~

single|int|3

:doc:`/about/help_us_to_write_it`

dmd_buffer:
~~~~~~~~~~~

single|int|3

:doc:`/about/help_us_to_write_it`
