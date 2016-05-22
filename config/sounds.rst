sounds:
=======

*Config file section*

.. include:: _machine_config_yes.rst
.. include:: _mode_config_yes.rst

.. overview

The ``sounds:`` section of your config is where you...

.. todo::
   Add description.


Optional settings
-----------------

The following sections are optional in the ``sounds:`` section of your config. (If you don't include them, the default will be used).

events_when_played:
~~~~~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

.. todo::
   Add description.

events_when_stopped:
~~~~~~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

.. todo::
   Add description.

file:
~~~~~
Single value, type: ``string``. Default: ``None``

.. todo::
   Add description.

loops:
~~~~~~
Single value, type: ``integer``. Default: ``0``

.. todo::
   Add description.

max_queue_time:
~~~~~~~~~~~~~~~
Single value, type: ``time string (secs)`` (:doc:`Instructions for entering time strings) </config/instructions/time_strings>` . Default: ``None``

.. todo::
   Add description.

priority:
~~~~~~~~~
Single value, type: ``integer``. Default: ``0``

.. todo::
   Add description.

track:
~~~~~~
Single value, type: ``string``. Default: ``None``

.. todo::
   Add description.

volume:
~~~~~~~
Single value, type: ``gain setting`` (-inf, db, or float between 0.0 and 1.0. Default: ``0.5``

.. todo::
   Add description.


ducking:
--------

The ``ducking:`` section contains the following nested sub-settings

Required settings
~~~~~~~~~~~~~~~~~

The following sections are required in the ``ducking:`` section of your config:

target:
^^^^^^^
Single value, type: ``string``. 

.. todo::
   Add description.


Optional settings
~~~~~~~~~~~~~~~~~

The following sections are optional in the ``ducking:`` section of your config. (If you don't include them, the default will be used).

attack:
^^^^^^^
Single value, type: ``string``. Default: ``10ms``

.. todo::
   Add description.

attenuation:
^^^^^^^^^^^^
Single value, type: ``gain setting`` (-inf, db, or float between 0.0 and 1.0. Default: ``1.0``

.. todo::
   Add description.

delay:
^^^^^^
Single value, type: ``string``. Default: ``0``

.. todo::
   Add description.

release:
^^^^^^^^
Single value, type: ``string``. Default: ``10ms``

.. todo::
   Add description.

release_point:
^^^^^^^^^^^^^^
Single value, type: ``string``. Default: ``0``

.. todo::
   Add description.



