logic_block:
============

*Config file section*

.. include:: _machine_config_yes.rst
.. include:: _mode_config_yes.rst

.. note:: This section can also be used in a show file in the ``logics:`` section of a step.

.. overview

The ``logic_block:`` section of your config is where you...

.. todo::
   Add description.


accrual:
--------

The ``accrual:`` section contains the following nested sub-settings

Required settings
~~~~~~~~~~~~~~~~~

The following sections are required in the ``accrual:`` section of your config:

events:
^^^^^^^
List of one (or more) values, each is a type: ``string``. 

.. todo::
   Add description.


common:
-------

The ``common:`` section contains the following nested sub-settings

Optional settings
~~~~~~~~~~~~~~~~~

The following sections are optional in the ``common:`` section of your config. (If you don't include them, the default will be used).

disable_events:
^^^^^^^^^^^^^^^
List of one (or more) values, each is a type: ``string``. Default: ``None``

.. todo::
   Add description.

disable_on_complete:
^^^^^^^^^^^^^^^^^^^^
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``True``

.. todo::
   Add description.

enable_events:
^^^^^^^^^^^^^^
List of one (or more) values, each is a type: ``string``. Default: ``None``

.. todo::
   Add description.

events_when_complete:
^^^^^^^^^^^^^^^^^^^^^
List of one (or more) values, each is a type: ``string``. Default: ``None``

.. todo::
   Add description.

persist_state:
^^^^^^^^^^^^^^
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

.. todo::
   Add description.

player_variable:
^^^^^^^^^^^^^^^^
Single value, type: ``string``. Default: ``None``

.. todo::
   Add description.

reset_events:
^^^^^^^^^^^^^
List of one (or more) values, each is a type: ``string``. Default: ``None``

.. todo::
   Add description.

reset_on_complete:
^^^^^^^^^^^^^^^^^^
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``True``

.. todo::
   Add description.

restart_events:
^^^^^^^^^^^^^^^
List of one (or more) values, each is a type: ``string``. Default: ``None``

.. todo::
   Add description.


counter:
--------

The ``counter:`` section contains the following nested sub-settings

Required settings
~~~~~~~~~~~~~~~~~

The following sections are required in the ``counter:`` section of your config:

count_complete_value:
^^^^^^^^^^^^^^^^^^^^^
Single value, type: ``integer``. 

.. todo::
   Add description.

count_events:
^^^^^^^^^^^^^
List of one (or more) values, each is a type: ``string``. 

.. todo::
   Add description.


Optional settings
~~~~~~~~~~~~~~~~~

The following sections are optional in the ``counter:`` section of your config. (If you don't include them, the default will be used).

count_interval:
^^^^^^^^^^^^^^^
Single value, type: ``integer``. Default: ``1``

.. todo::
   Add description.

direction:
^^^^^^^^^^
Single value, type: ``string``. Default: ``up``

.. todo::
   Add description.

event_when_hit:
^^^^^^^^^^^^^^^
Single value, type: ``string``. Default: ``None``

.. todo::
   Add description.

multiple_hit_window:
^^^^^^^^^^^^^^^^^^^^
Single value, type: ``time string`` (:doc:`Instructions </config/instructions/lists>` for entering time strings). Default: ``0``

.. todo::
   Add description.

starting_count:
^^^^^^^^^^^^^^^
Single value, type: ``integer``. Default: ``0``

.. todo::
   Add description.


sequence:
---------

The ``sequence:`` section contains the following nested sub-settings

Required settings
~~~~~~~~~~~~~~~~~

The following sections are required in the ``sequence:`` section of your config:

events:
^^^^^^^
List of one (or more) values, each is a type: ``string``. 

.. todo::
   Add description.



