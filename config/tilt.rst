tilt:
=====

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

.. overview

The ``tilt:`` section of your config is where you...

.. todo::
   Add description.

Optional settings
-----------------

The following sections are optional in the ``tilt:`` section of your config. (If you don't include them, the default will be used).

multiple_hit_window:
~~~~~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings) </config/instructions/time_strings>` . Default: ``300ms``

.. todo::
   Add description.

reset_warnings_events:
~~~~~~~~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``ball_ending``

.. todo::
   Add description.

settle_time:
~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings) </config/instructions/time_strings>` . Default: ``5s``

.. todo::
   Add description.

slam_tilt_switch_tag:
~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``slam_tilt``

.. todo::
   Add description.

tilt_events:
~~~~~~~~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

.. todo::
   Add description.

tilt_slam_tilt_events:
~~~~~~~~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

.. todo::
   Add description.

tilt_switch_tag:
~~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``tilt``

.. todo::
   Add description.

tilt_warning_events:
~~~~~~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

.. todo::
   Add description.

tilt_warning_switch_tag:
~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``tilt_warning``

.. todo::
   Add description.

tilt_warnings_player_var:
~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``tilt_warnings``

.. todo::
   Add description.

warnings_to_tilt:
~~~~~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``3``

.. todo::
   Add description.

