dual_wound_coils:
=================

*Config file section*

.. include:: _machine_config_yes.rst
.. include:: _mode_config_no.rst

.. overview

The ``dual_wound_coils:`` section of your config is where you...

.. todo::
   Add description.


Required settings
-----------------

The following sections are required in the ``dual_wound_coils:`` section of your config:

hold_coil:
~~~~~~~~~~
Single value, type: string name of a ``coils:`` device. 

.. todo::
   Add description.

main_coil:
~~~~~~~~~~
Single value, type: string name of a ``coils:`` device. 

.. todo::
   Add description.


Optional settings
-----------------

The following sections are optional in the ``dual_wound_coils:`` section of your config. (If you don't include them, the default will be used).

debug:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

.. todo::
   Add description.

eos_switch:
~~~~~~~~~~~
Single value, type: string name of a ``switches:`` device. Default: ``None``

.. todo::
   Add description.

label:
~~~~~~
Single value, type: ``string``. Default: ``%``

.. todo::
   Add description.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

.. todo::
   Add description.


