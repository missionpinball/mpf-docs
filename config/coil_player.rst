coil_player:
============

*Config file section*

.. include:: _machine_config_yes.rst
.. include:: _mode_config_yes.rst

.. note:: This section can also be used in a show file in the ``coils:`` section of a step.

.. overview

The ``coil_player:`` section of your config is where you...

.. todo::
   Add description.


Optional settings
-----------------

The following sections are optional in the ``coil_player:`` section of your config. (If you don't include them, the default will be used).

action:
~~~~~~~
Single value, type: ``string`` (case-insensitive). Default: ``pulse``

.. todo::
   Add description.

ms:
~~~
Single value, type: ``time string`` (:doc:`Instructions </config/instructions/lists>` for entering time strings). Default: ``None``

.. todo::
   Add description.

power:
~~~~~~
Single value, type: ``number`` (will be converted to floating point). Default: ``1.0``

.. todo::
   Add description.


.. note:: The ``coil_player:`` section of your config may contain additional settings not mentioned here. Read the introductory text for details of what those might be.

