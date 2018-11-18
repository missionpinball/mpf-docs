steppers:
=========

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``steppers:`` section of your config is where you...

.. todo:: :doc:`/about/help_us_to_write_it`


Required settings
-----------------

The following sections are required in the ``steppers:`` section of your config:

number:
~~~~~~~
Single value, type: ``string``.

.. todo:: :doc:`/about/help_us_to_write_it`


Optional settings
-----------------

The following sections are optional in the ``steppers:`` section of your config. (If you don't include them, the default will be used).

acceleration_limit:
~~~~~~~~~~~~~~~~~~~
Single value, type: ``number`` (will be converted to floating point). Default: ``1.0``

.. todo:: :doc:`/about/help_us_to_write_it`

ball_search_max:
~~~~~~~~~~~~~~~~
Single value, type: ``number`` (will be converted to floating point). Default: ``1.0``

.. todo:: :doc:`/about/help_us_to_write_it`

ball_search_min:
~~~~~~~~~~~~~~~~
Single value, type: ``number`` (will be converted to floating point). Default: ``0.0``

.. todo:: :doc:`/about/help_us_to_write_it`

ball_search_wait:
~~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`) . Default: ``5s``

.. todo:: :doc:`/about/help_us_to_write_it`

fullstep_per_userunit:
~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``number`` (will be converted to floating point). Default: ``1.0``

.. todo:: :doc:`/about/help_us_to_write_it`

hold_current:
~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``0``

.. todo:: :doc:`/about/help_us_to_write_it`

homing_direction:
~~~~~~~~~~~~~~~~~
Single value, type: one of the following options: clockwise, counterclockwise. Default: ``clockwise``

.. todo:: :doc:`/about/help_us_to_write_it`

homing_speed:
~~~~~~~~~~~~~
Single value, type: ``number`` (will be converted to floating point). Default: ``1.0``

.. todo:: :doc:`/about/help_us_to_write_it`

include_in_ball_search:
~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``True``

.. todo:: :doc:`/about/help_us_to_write_it`

microstep_per_fullstep:
~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``16``

.. todo:: :doc:`/about/help_us_to_write_it`

mode:
~~~~~
Single value, type: one of the following options: position, velocity. Default: ``position``

.. todo:: :doc:`/about/help_us_to_write_it`

move_current:
~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``20``

.. todo:: :doc:`/about/help_us_to_write_it`

named_positions:
~~~~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``float``:``str``.

.. todo:: :doc:`/about/help_us_to_write_it`

platform:
~~~~~~~~~
Single value, type: ``string``.

.. todo:: :doc:`/about/help_us_to_write_it`

pos_max:
~~~~~~~~
Single value, type: ``number`` (will be converted to floating point). Default: ``1.0``

.. todo:: :doc:`/about/help_us_to_write_it`

pos_min:
~~~~~~~~
Single value, type: ``number`` (will be converted to floating point). Default: ``0.0``

.. todo:: :doc:`/about/help_us_to_write_it`

reset_events:
~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Default: machine_reset_phase_3, ball_starting, ball_will_end, service_mode_entered

.. todo:: :doc:`/about/help_us_to_write_it`

reset_position:
~~~~~~~~~~~~~~~
Single value, type: ``number`` (will be converted to floating point). Default: ``0.0``

.. todo:: :doc:`/about/help_us_to_write_it`

velocity_limit:
~~~~~~~~~~~~~~~
Single value, type: ``number`` (will be converted to floating point). Default: ``1.0``

.. todo:: :doc:`/about/help_us_to_write_it`

console_log:
~~~~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level for the console log for this device.

debug:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

Set this to true to see additional debug output. This might impact the performance of MPF.

file_log:
~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level for the file log for this device.

label:
~~~~~~
Single value, type: ``string``. Default: ``%``

Name of this device in service mode.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``.

.. todo:: :doc:`/about/help_us_to_write_it`


