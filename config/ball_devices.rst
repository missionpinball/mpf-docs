ball_devices:
=============

*Config file section*

.. include:: _machine_config_yes.rst
.. include:: _mode_config_no.rst

.. overview

The ``ball_devices:`` section of your config is where you...

.. todo::
   Add description.


Optional settings
-----------------

The following sections are optional in the ``ball_devices:`` section of your config. (If you don't include them, the default will be used).

auto_fire_on_unexpected_ball:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``True``

.. todo::
   Add description.

ball_capacity:
~~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``None``

.. todo::
   Add description.

ball_missing_target:
~~~~~~~~~~~~~~~~~~~~
Single value, type: string name of a ``playfields:`` device. Default: ``playfield``

.. todo::
   Add description.

ball_missing_timeouts:
~~~~~~~~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: ``time string`` (:doc:`Instructions </config/instructions/lists>` for entering time strings). Default: ``None``

.. todo::
   Add description.

ball_search_order:
~~~~~~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``100``

.. todo::
   Add description.

ball_switches:
~~~~~~~~~~~~~~
List of one (or more) values, each is a type: string name of a ``switches:`` device. Default: ``None``

.. todo::
   Add description.

captures_from:
~~~~~~~~~~~~~~
Single value, type: string name of a ``playfields:`` device. Default: ``playfield``

.. todo::
   Add description.

confirm_eject_event:
~~~~~~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``None``

.. todo::
   Add description.

confirm_eject_switch:
~~~~~~~~~~~~~~~~~~~~~
Single value, type: string name of a ``switches:`` device. Default: ``None``

.. todo::
   Add description.

confirm_eject_type:
~~~~~~~~~~~~~~~~~~~
Single value, type: one of the following options: target, switch, event, fake. Default: ``target``

.. todo::
   Add description.

debug:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

.. todo::
   Add description.

eject_all_events:
~~~~~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``ms``. Default: ``None``

.. todo::
   Add description.

eject_coil:
~~~~~~~~~~~
Single value, type: string name of a ``coils:`` device. Default: ``None``

.. todo::
   Add description.

eject_coil_jam_pulse:
~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``time string`` (:doc:`Instructions </config/instructions/lists>` for entering time strings). Default: ``None``

.. todo::
   Add description.

eject_coil_retry_pulse:
~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``time string`` (:doc:`Instructions </config/instructions/lists>` for entering time strings). Default: ``None``

.. todo::
   Add description.

eject_events:
~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``ms``. Default: ``None``

.. todo::
   Add description.

eject_targets:
~~~~~~~~~~~~~~
List of one (or more) values, each is a type: string name of a ``ball_devices:`` device. Default: ``playfield``

.. todo::
   Add description.

eject_timeouts:
~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: ``time string`` (:doc:`Instructions </config/instructions/lists>` for entering time strings). Default: ``None``

.. todo::
   Add description.

entrance_count_delay:
~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``time string`` (:doc:`Instructions </config/instructions/lists>` for entering time strings). Default: ``500ms``

.. todo::
   Add description.

entrance_events:
~~~~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``ms``. Default: ``None``

.. todo::
   Add description.

entrance_switch:
~~~~~~~~~~~~~~~~
Single value, type: string name of a ``switches:`` device. Default: ``None``

.. todo::
   Add description.

entrance_switch_full_timeout:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``time string`` (:doc:`Instructions </config/instructions/lists>` for entering time strings). Default: ``0``

.. todo::
   Add description.

exit_count_delay:
~~~~~~~~~~~~~~~~~
Single value, type: ``time string`` (:doc:`Instructions </config/instructions/lists>` for entering time strings). Default: ``500ms``

.. todo::
   Add description.

hold_coil:
~~~~~~~~~~
Single value, type: string name of a ``coils:`` device. Default: ``None``

.. todo::
   Add description.

hold_coil_release_time:
~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``time string`` (:doc:`Instructions </config/instructions/lists>` for entering time strings). Default: ``1s``

.. todo::
   Add description.

hold_events:
~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``ms``. Default: ``None``

.. todo::
   Add description.

hold_switches:
~~~~~~~~~~~~~~
List of one (or more) values, each is a type: string name of a ``switches:`` device. Default: ``None``

.. todo::
   Add description.

jam_switch:
~~~~~~~~~~~
Single value, type: string name of a ``switches:`` device. Default: ``None``

.. todo::
   Add description.

label:
~~~~~~
Single value, type: ``string``. Default: ``%``

.. todo::
   Add description.

max_eject_attempts:
~~~~~~~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``0``

.. todo::
   Add description.

mechanical_eject:
~~~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

.. todo::
   Add description.

player_controlled_eject_event:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``None``

.. todo::
   Add description.

request_ball_events:
~~~~~~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

.. todo::
   Add description.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

.. todo::
   Add description.

target_on_unexpected_ball:
~~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: string name of a ``ball_devices:`` device. Default: ``None``

.. todo::
   Add description.


