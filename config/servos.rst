servos:
=======

*Config file section*

.. include:: _machine_config_yes.rst
.. include:: _mode_config_no.rst

.. overview

The ``servos:`` section of your config is where you...

.. todo::
   Add description.


Required settings
-----------------

The following sections are required in the ``servos:`` section of your config:

number:
~~~~~~~
Single value, type: ``integer``. 

.. todo::
   Add description.


Optional settings
-----------------

The following sections are optional in the ``servos:`` section of your config. (If you don't include them, the default will be used).

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

platform:
~~~~~~~~~
Single value, type: ``string``. Default: ``None``

.. todo::
   Add description.

positions:
~~~~~~~~~~
One or more sub-entries, each in the format of type: ``float``:``str``. Default: ``None``

.. todo::
   Add description.

reset_events:
~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``ms``. Default: ``ball_starting``

.. todo::
   Add description.

reset_position:
~~~~~~~~~~~~~~~
Single value, type: ``number`` (will be converted to floating point). Default: ``0.5``

.. todo::
   Add description.

servo_max:
~~~~~~~~~~
Single value, type: ``number`` (will be converted to floating point). Default: ``1.0``

.. todo::
   Add description.

servo_min:
~~~~~~~~~~
Single value, type: ``number`` (will be converted to floating point). Default: ``0.0``

.. todo::
   Add description.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

.. todo::
   Add description.


