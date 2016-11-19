timers:
=======

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **NO**  |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

.. overview

The ``timers:`` section of your config is where you...

.. todo::
   Add description.

Optional settings
-----------------

The following sections are optional in the ``timers:`` section of your config. (If you don't include them, the default will be used).

bcp:
~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

Controls whether the various timer events (count, start, stop, complete, etc.) are sent to the MPF-MC via BCP.

TODO Is this needed? If a slide_player, etc. uses one of these events, then they'll automatically be sent to the MC?

control_events:
~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: sub-configuration containing control_events settings. Default: ``None``

.. todo::
   Add description.

debug:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

.. todo::
   Add description.

direction:
~~~~~~~~~~
Single value, type: ``string``. Default: ``up``

.. todo::
   Add description.

end_value:
~~~~~~~~~~
Single value, type: ``integer``. Default: ``None``

.. todo::
   Add description.

max_value:
~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings) </config/instructions/time_strings>` . Default: ``None``

.. todo::
   Add description.

restart_on_complete:
~~~~~~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

.. todo::
   Add description.

start_running:
~~~~~~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

.. todo::
   Add description.

start_value:
~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``0``

.. todo::
   Add description.

tick_interval:
~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings) </config/instructions/time_strings>` . Default: ``1s``

.. todo::
   Add description.

