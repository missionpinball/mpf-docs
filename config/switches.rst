switches:
=========

*Config file section*

.. include:: _machine_config_yes.rst
.. include:: _mode_config_no.rst

.. overview

The ``switches:`` section of your config is where you...

.. todo::
   Add description.


Required settings
-----------------

The following sections are required in the ``switches:`` section of your config:

number:
~~~~~~~
Single value, type: ``string``. 

.. todo::
   Add description.


Optional settings
-----------------

The following sections are optional in the ``switches:`` section of your config. (If you don't include them, the default will be used).

debounce:
~~~~~~~~~
Single value, type: one of the following options: auto, quick, normal. Default: ``auto``

.. todo::
   Add description.

debug:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

.. todo::
   Add description.

events_when_activated:
~~~~~~~~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

.. todo::
   Add description.

events_when_deactivated:
~~~~~~~~~~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

.. todo::
   Add description.

ignore_window_ms:
~~~~~~~~~~~~~~~~~
Single value, type: ``time string`` (:doc:`Instructions </config/instructions/lists>` for entering time strings). Default: ``0``

.. todo::
   Add description.

label:
~~~~~~
Single value, type: ``string``. Default: ``%``

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

type:
~~~~~
Single value, type: one of the following options: NC, NO. Default: ``NO``

.. todo::
   Add description.


