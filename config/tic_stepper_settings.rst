tic_stepper_settings:
=====================

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **NO**  |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

If you use the :doc:`Pololu Tic Stepper Controller </hardware/pololu_tic/index>`
you can use the following settings in ``platform_settings`` of your steppers.

.. config


Optional settings
-----------------

The following sections are optional in the ``tic_stepper_settings:`` section of your config. (If you don't include them, the default will be used).

current_limit:
~~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``192``

.. todo:: :doc:`/about/help_us_to_write_it`

max_acceleration:
~~~~~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``40000``

.. todo:: :doc:`/about/help_us_to_write_it`

max_deceleration:
~~~~~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``40000``

.. todo:: :doc:`/about/help_us_to_write_it`

max_speed:
~~~~~~~~~~
Single value, type: ``integer``. Default: ``2000000``

.. todo:: :doc:`/about/help_us_to_write_it`

poll_ms:
~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Default: ``100ms``

How often should MPF poll the state of your steppers?
This is used to check for completion of movements.
There should be no need to modify this.

starting_speed:
~~~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``0``

.. todo:: :doc:`/about/help_us_to_write_it`

step_mode:
~~~~~~~~~~
Single value, type: ``integer``. Default: ``1``

.. todo:: :doc:`/about/help_us_to_write_it`


Related How To guides
---------------------

* :doc:`/hardware/pololu_tic/index`
