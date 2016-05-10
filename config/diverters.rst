diverters:
==========

*Config file section*

.. include:: _machine_config_yes.rst
.. include:: _mode_config_no.rst

.. overview

The ``diverters:`` section of your config is where you...

.. todo::
   Add description.


Optional settings
-----------------

The following sections are optional in the ``diverters:`` section of your config. (If you don't include them, the default will be used).

activate_events:
~~~~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``ms``. Default: ``None``

.. todo::
   Add description.

activation_coil:
~~~~~~~~~~~~~~~~
Single value, type: string name of a ``coils:`` device. Default: ``None``

.. todo::
   Add description.

activation_switches:
~~~~~~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: string name of a ``switches:`` device. Default: ``None``

.. todo::
   Add description.

activation_time:
~~~~~~~~~~~~~~~~
Single value, type: ``time string`` (:doc:`Instructions </config/instructions/lists>` for entering time strings). Default: ``0``

.. todo::
   Add description.

deactivate_events:
~~~~~~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``ms``. Default: ``None``

.. todo::
   Add description.

deactivation_coil:
~~~~~~~~~~~~~~~~~~
Single value, type: string name of a ``coils:`` device. Default: ``None``

.. todo::
   Add description.

deactivation_switches:
~~~~~~~~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: string name of a ``switches:`` device. Default: ``None``

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

disable_switches:
~~~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: string name of a ``switches:`` device. Default: ``None``

.. todo::
   Add description.

enable_events:
~~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``ms``. Default: ``None``

.. todo::
   Add description.

feeder_devices:
~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: string name of a ``ball_devices:`` device. Default: ``playfield``

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

targets_when_active:
~~~~~~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: string name of a ``ball_devices:`` device. Default: ``playfield``

.. todo::
   Add description.

targets_when_inactive:
~~~~~~~~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: string name of a ``ball_devices:`` device. Default: ``playfield``

.. todo::
   Add description.

type:
~~~~~
Single value, type: one of the following options: hold, pulse. Default: ``hold``

.. todo::
   Add description.


