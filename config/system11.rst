system11:
=========

*Config file section*

.. include:: _machine_config_yes.rst
.. include:: _mode_config_no.rst

.. overview

The ``system11:`` section of your config is where you...

.. todo::
   Add description.


Required settings
-----------------

The following sections are required in the ``system11:`` section of your config:

ac_relay_driver:
~~~~~~~~~~~~~~~~
Single value, type: string name of a ``coils:`` device. 

.. todo::
   Add description.


Optional settings
-----------------

The following sections are optional in the ``system11:`` section of your config. (If you don't include them, the default will be used).

ac_relay_delay_ms:
~~~~~~~~~~~~~~~~~~
Single value, type: ``time string`` (:doc:`Instructions </config/instructions/lists>` for entering time strings). Default: ``75ms``

.. todo::
   Add description.


