drop_target_banks:
==================

*Config file section*

.. include:: _machine_config_yes.rst
.. include:: _mode_config_no.rst

.. overview

The ``drop_target_banks:`` section of your config is where you...

.. todo::
   Add description.


Required settings
-----------------

The following sections are required in the ``drop_target_banks:`` section of your config:

drop_targets:
~~~~~~~~~~~~~
List of one (or more) values, each is a type: string name of a ``drop_targets:`` device. 

.. todo::
   Add description.


Optional settings
-----------------

The following sections are optional in the ``drop_target_banks:`` section of your config. (If you don't include them, the default will be used).

debug:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

.. todo::
   Add description.

label:
~~~~~~
Single value, type: ``string``. Default: ``%``

.. todo::
   Add description.

reset_coil:
~~~~~~~~~~~
Single value, type: string name of a ``coils:`` device. Default: ``None``

.. todo::
   Add description.

reset_coils:
~~~~~~~~~~~~
List of one (or more) values, each is a type: string name of a ``coils:`` device. Default: ``None``

.. todo::
   Add description.

reset_events:
~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``ms``. Default: ``machine_reset_phase_3, ball_starting``

.. todo::
   Add description.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

.. todo::
   Add description.


