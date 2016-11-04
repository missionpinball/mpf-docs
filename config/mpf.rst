mpf:
====

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``mpf:`` section of your config is where you...

.. todo::
   Add description.


Optional settings
-----------------

The following sections are optional in the ``mpf:`` section of your config. (If you don't include them, the default will be used).

allow_invalid_config_sections:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``false``

.. todo::
   Add description.

auto_create_switch_events:
~~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``True``

.. todo::
   Add description.

default_flash_ms:
~~~~~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``50``

.. todo::
   Add description.

default_pulse_ms:
~~~~~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``10``

.. todo::
   Add description.

hz:
~~~
Single value, type: ``number`` (will be converted to floating point). Default: ``30.0``

.. todo::
   Add description.

save_machine_vars_to_disk:
~~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``true``

.. todo::
   Add description.

switch_event_active:
~~~~~~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``%_active``

.. todo::
   Add description.

switch_event_inactive:
~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``%_inactive``

.. todo::
   Add description.

switch_tag_event:
~~~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``sw_%``

.. todo::
   Add description.


