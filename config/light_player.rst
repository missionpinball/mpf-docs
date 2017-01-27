light_player:
=============

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`shows </shows/index>`                                       | **YES** |
+----------------------------------------------------------------------------+---------+

.. note:: This section can also be used in a show file in the ``lights:`` section of a step.

.. overview

The ``light_player:`` section of your config is where you...

.. todo::
   Add description.

Optional settings
-----------------

The following sections are optional in the ``light_player:`` section of your config. (If you don't include them, the default will be used).

brightness:
~~~~~~~~~~~
Single value, type: 2-byte hex value (``00`` to ``ff``). Default: ``ff``

.. todo::
   Add description.

fade:
~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings) </config/instructions/time_strings>` . Default: ``0``

.. todo::
   Add description.

