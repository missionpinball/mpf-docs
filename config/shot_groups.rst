shot_groups:
============

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

.. overview

The ``shot_groups:`` section of your config is where you...

.. todo::
   Add description.

Optional settings
-----------------

The following sections are optional in the ``shot_groups:`` section of your config. (If you don't include them, the default will be used).

advance_events:
~~~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``ms``. Default: ``None``

.. todo::
   Add description.

debug:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

.. todo::
   Add description.

disable_events:
~~~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``ms``. Default: ``None``

.. todo::
   Add description.

disable_rotation_events:
~~~~~~~~~~~~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``ms``. Default: ``None``

.. todo::
   Add description.

enable_events:
~~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``ms``. Default: ``None``

.. todo::
   Add description.

enable_rotation_events:
~~~~~~~~~~~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``ms``. Default: ``None``

.. todo::
   Add description.

label:
~~~~~~
Single value, type: ``string``. Default: ``%``

.. todo::
   Add description.

profile:
~~~~~~~~
Single value, type: ``string``. Default: ``None``

.. todo::
   Add description.

remove_active_profile_events:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``ms``. Default: ``None``

.. todo::
   Add description.

reset_events:
~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``ms``. Default: ``None``

.. todo::
   Add description.

rotate_events:
~~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``ms``. Default: ``None``

.. todo::
   Add description.

rotate_left_events:
~~~~~~~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``ms``. Default: ``None``

.. todo::
   Add description.

rotate_right_events:
~~~~~~~~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``ms``. Default: ``None``

.. todo::
   Add description.

shots:
~~~~~~
List of one (or more) values, each is a type: string name of a ``shots:`` device. Default: ``None``

.. todo::
   Add description.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

.. todo::
   Add description.

