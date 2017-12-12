score_reel_groups:
==================

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``score_reel_groups:`` section of your config is where you...

.. todo::
   :doc:`/about/help_us_to_write_it`

Required settings
-----------------

The following sections are required in the ``score_reel_groups:`` section of your config:

reels:
~~~~~~
List of one (or more) values, each is a type: string name of a ``score_reels:`` device.

.. todo::
   :doc:`/about/help_us_to_write_it`

Optional settings
-----------------

The following sections are optional in the ``score_reel_groups:`` section of your config. (If you don't include them, the default will be used).

chimes:
~~~~~~~
List of one (or more) values, each is a type: string name of a ``coils:`` device. Default: ``None``

.. todo::
   :doc:`/about/help_us_to_write_it`

config:
~~~~~~~
Single value, type: ``string``. Default: ``lazy``

.. todo::
   :doc:`/about/help_us_to_write_it`

confirm:
~~~~~~~~
Single value, type: ``string``. Default: ``lazy``

.. todo::
   :doc:`/about/help_us_to_write_it`

debug:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

.. todo::
   :doc:`/about/help_us_to_write_it`

hw_confirm_time:
~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings) </config/instructions/time_strings>` . Default: ``300``

.. todo::
   :doc:`/about/help_us_to_write_it`

label:
~~~~~~
Single value, type: ``string``. Default: ``%``

.. todo::
   :doc:`/about/help_us_to_write_it`

lights_tag:
~~~~~~~~~~~
Single value, type: ``string``. Default: ``None``

.. todo::
   :doc:`/about/help_us_to_write_it`

max_simultaneous_coils:
~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``2``

.. todo::
   :doc:`/about/help_us_to_write_it`

repeat_pulse_time:
~~~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings) </config/instructions/time_strings>` . Default: ``200``

.. todo::
   :doc:`/about/help_us_to_write_it`

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

.. todo::
   :doc:`/about/help_us_to_write_it`

