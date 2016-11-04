matrix_lights:
==============

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``matrix_lights:`` section of your config is where you...

.. todo::
   Add description.


Required settings
-----------------

The following sections are required in the ``matrix_lights:`` section of your config:

number:
~~~~~~~
Single value, type: ``string``.

.. todo::
   Add description.


Optional settings
-----------------

The following sections are optional in the ``matrix_lights:`` section of your config. (If you don't include them, the default will be used).

debug:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

.. todo::
   Add description.

fade_ms:
~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings) </config/instructions/time_strings>` . Default: ``None``

.. todo::
   Add description.

label:
~~~~~~
Single value, type: ``string``. Default: ``%``

.. todo::
   Add description.

off_events:
~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``ms``. Default: ``None``

.. todo::
   Add description.

on_events:
~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``ms``. Default: ``None``

.. todo::
   Add description.

platform:
~~~~~~~~~
Single value, type: ``string``. Default: ``None``

.. todo::
   Add description.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

.. todo::
   Add description.

x:
~~
Single value, type: ``integer``. Default: ``None``

.. todo::
   Add description.

y:
~~
Single value, type: ``integer``. Default: ``None``

.. todo::
   Add description.

z:
~~
Single value, type: ``integer``. Default: ``None``

.. todo::
   Add description.


