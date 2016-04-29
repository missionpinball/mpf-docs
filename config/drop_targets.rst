drop_targets:
=============

*Config file section*

.. include:: _machine_config_yes.rst
.. include:: _mode_config_no.rst

.. overview

The ``drop_targets:`` section of your config is where you...

.. todo::
   Add description.


Required settings
-----------------

The following sections are required in the ``drop_targets:`` section of your config:

switch:
~~~~~~~
Single value, type: string name of a ``switches:`` device. 

.. todo::
   Add description.


Optional settings
-----------------

The following sections are optional in the ``drop_targets:`` section of your config. (If you don't include them, the default will be used).

ball_search_order:
~~~~~~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``100``

.. todo::
   Add description.

debug:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

.. todo::
   Add description.

knockdown_coil:
~~~~~~~~~~~~~~~
Single value, type: string name of a ``coils:`` device. Default: ``None``

.. todo::
   Add description.

knockdown_events:
~~~~~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``ms``. Default: ``None``

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

reset_events:
~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``ms``. Default: ``ball_starting, machine_reset_phase_3``

.. todo::
   Add description.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

.. todo::
   Add description.


