score_reels:
============

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``score_reels:`` section of your config is where you configure your score reels.
See :doc:`/mechs/score_reels/index` for more details.

.. config


Optional settings
-----------------

The following sections are optional in the ``score_reels:`` section of your config. (If you don't include them, the default will be used).

coil_inc:
~~~~~~~~~
Single value, type: string name of a :doc:`coils <coils>` device. Defaults to empty.

Coil to fire to increment this reel.

hw_confirm_time:
~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Default: ``20``

How long does the switch have to stay active until counted.

limit_hi:
~~~~~~~~~
Single value, type: ``integer``. Default: ``9``

The highest digit on your reel.

limit_lo:
~~~~~~~~~
Single value, type: ``integer``. Default: ``0``

The lowest digit on your reel.

repeat_pulse_time:
~~~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Default: ``200``

How long to wait after a pulse before pulsing the coil again.

switch_0:
~~~~~~~~~
Single value, type: string name of a :doc:`switches <switches>` device. Defaults to empty.

Switch which indicates that the reel is showing a 0.

switch_1:
~~~~~~~~~
Single value, type: string name of a :doc:`switches <switches>` device. Defaults to empty.

Switch which indicates that the reel is showing a 1.

switch_10:
~~~~~~~~~~
Single value, type: string name of a :doc:`switches <switches>` device. Defaults to empty.

Switch which indicates that the reel is showing a 10.

switch_11:
~~~~~~~~~~
Single value, type: string name of a :doc:`switches <switches>` device. Defaults to empty.

Switch which indicates that the reel is showing a 11.

switch_12:
~~~~~~~~~~
Single value, type: string name of a :doc:`switches <switches>` device. Defaults to empty.

Switch which indicates that the reel is showing a 12.

switch_2:
~~~~~~~~~
Single value, type: string name of a :doc:`switches <switches>` device. Defaults to empty.

Switch which indicates that the reel is showing a 2.

switch_3:
~~~~~~~~~
Single value, type: string name of a :doc:`switches <switches>` device. Defaults to empty.

Switch which indicates that the reel is showing a 3.

switch_4:
~~~~~~~~~
Single value, type: string name of a :doc:`switches <switches>` device. Defaults to empty.

Switch which indicates that the reel is showing a 4.

switch_5:
~~~~~~~~~
Single value, type: string name of a :doc:`switches <switches>` device. Defaults to empty.

Switch which indicates that the reel is showing a 5.

switch_6:
~~~~~~~~~
Single value, type: string name of a :doc:`switches <switches>` device. Defaults to empty.

Switch which indicates that the reel is showing a 6.

switch_7:
~~~~~~~~~
Single value, type: string name of a :doc:`switches <switches>` device. Defaults to empty.

Switch which indicates that the reel is showing a 7.

switch_8:
~~~~~~~~~
Single value, type: string name of a :doc:`switches <switches>` device. Defaults to empty.

Switch which indicates that the reel is showing a 8.

switch_9:
~~~~~~~~~
Single value, type: string name of a :doc:`switches <switches>` device. Defaults to empty.

Switch which indicates that the reel is showing a 9.

console_log:
~~~~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level for the console log for this device.

debug:
~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

Set to true to get more debug output in the log.

file_log:
~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level for the file log for this device.

label:
~~~~~~
Single value, type: ``string``. Default: ``%``

Name in service mode.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Defaults to empty.

Tags of this reel.


Related How To guides
---------------------

* :doc:`/mechs/score_reels/index`
