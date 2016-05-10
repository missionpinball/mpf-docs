shot_profiles:
==============

*Config file section*

.. include:: _machine_config_yes.rst
.. include:: _mode_config_yes.rst

.. overview

The ``shot_profiles:`` section of your config is where you...

.. todo::
   Add description.


Optional settings
-----------------

The following sections are optional in the ``shot_profiles:`` section of your config. (If you don't include them, the default will be used).

advance_on_hit:
~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``True``

.. todo::
   Add description.

block:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``true``

.. todo::
   Add description.

hold:
~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``None``

.. todo::
   Add description.

loop:
~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

.. todo::
   Add description.

player_variable:
~~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``None``

.. todo::
   Add description.

rotation_pattern:
~~~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``R``

.. todo::
   Add description.

show:
~~~~~
Single value, type: ``string``. Default: ``None``

.. todo::
   Add description.

show_when_disabled:
~~~~~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

.. todo::
   Add description.

state_names_to_not_rotate:
~~~~~~~~~~~~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

.. todo::
   Add description.

state_names_to_rotate:
~~~~~~~~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

.. todo::
   Add description.


states:
-------

The ``states:`` section contains the following nested sub-settings

Required settings
~~~~~~~~~~~~~~~~~

The following sections are required in the ``states:`` section of your config:

name:
^^^^^
Single value, type: ``string``. 

.. todo::
   Add description.


Optional settings
~~~~~~~~~~~~~~~~~

The following sections are optional in the ``states:`` section of your config. (If you don't include them, the default will be used).

action:
^^^^^^^
Single value, type: one of the following options: play, stop, pause, resume, advance, update. Default: ``play``

.. todo::
   Add description.

hold:
^^^^^
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``True``

.. todo::
   Add description.

key:
^^^^
Single value, type: ``string``. Default: ``None``

.. todo::
   Add description.

loops:
^^^^^^
Single value, type: ``integer``. Default: ``-1``

.. todo::
   Add description.

manual_advance:
^^^^^^^^^^^^^^^
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

.. todo::
   Add description.

priority:
^^^^^^^^^
Single value, type: ``integer``. Default: ``0``

.. todo::
   Add description.

reset:
^^^^^^
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``True``

.. todo::
   Add description.

show:
^^^^^
Single value, type: ``string``. Default: ``None``

.. todo::
   Add description.

show_tokens:
^^^^^^^^^^^^
One or more sub-entries, each in the format of type: ``str``:``str``. Default: ``None``

.. todo::
   Add description.

speed:
^^^^^^
Single value, type: ``number`` (will be converted to floating point). Default: ``1``

.. todo::
   Add description.

start_step:
^^^^^^^^^^^
Single value, type: ``integer``. Default: ``1``

.. todo::
   Add description.

sync_ms:
^^^^^^^^
Single value, type: ``integer``. Default: ``0``

.. todo::
   Add description.


.. note:: The ``states:`` section of your config may contain additional settings not mentioned here. Read the introductory text for details of what those might be.



