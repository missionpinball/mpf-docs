shots:
======

*Config file section*

.. include:: _machine_config_yes.rst
.. include:: _mode_config_yes.rst

.. overview

The ``shots:`` section of your config is where you...

.. todo::
   Add description.


Optional settings
-----------------

The following sections are optional in the ``shots:`` section of your config. (If you don't include them, the default will be used).

advance_events:
~~~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``ms``. Default: ``None``

.. todo::
   Add description.

cancel_switch:
~~~~~~~~~~~~~~
List of one (or more) values, each is a type: string name of a ``switches:`` device. Default: ``None``

.. todo::
   Add description.

debug:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

.. todo::
   Add description.

delay_switch:
~~~~~~~~~~~~~
Parent setting for one (or more) sub-settings. Each sub-setting is a type: string name of a ``switches):m:`` device. Default: ``None``

.. todo::
   Add description.

disable_events:
~~~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``ms``. Default: ``None``

.. todo::
   Add description.

enable_events:
~~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``ms``. Default: ``None``

.. todo::
   Add description.

hit_events:
~~~~~~~~~~~
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

switch:
~~~~~~~
List of one (or more) values, each is a type: string name of a ``switches:`` device. Default: ``None``

.. todo::
   Add description.

switch_sequence:
~~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: string name of a ``switches:`` device. Default: ``None``

.. todo::
   Add description.

switches:
~~~~~~~~~
List of one (or more) values, each is a type: string name of a ``switches:`` device. Default: ``None``

.. todo::
   Add description.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

.. todo::
   Add description.

time:
~~~~~
Single value, type: ``time string`` (:doc:`Instructions </config/instructions/lists>` for entering time strings). Default: ``0``

.. todo::
   Add description.


.. note:: The ``shots:`` section of your config may contain additional settings not mentioned here. Read the introductory text for details of what those might be.

