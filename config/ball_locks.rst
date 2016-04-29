ball_locks:
===========

*Config file section*

.. include:: _machine_config_yes.rst
.. include:: _mode_config_yes.rst

.. overview

The ``ball_locks:`` section of your config is where you...

.. todo::
   Add description.


Required settings
-----------------

The following sections are required in the ``ball_locks:`` section of your config:

balls_to_lock:
~~~~~~~~~~~~~~
Single value, type: ``integer``. 

.. todo::
   Add description.

lock_devices:
~~~~~~~~~~~~~
List of one (or more) values, each is a type: string name of a ``ball_devices:`` device. 

.. todo::
   Add description.


Optional settings
-----------------

The following sections are optional in the ``ball_locks:`` section of your config. (If you don't include them, the default will be used).

debug:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

.. todo::
   Add description.

disable_events:
~~~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``ms``. Default: ``ball_ending``

.. todo::
   Add description.

enable_events:
~~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``ms``. Default: ``ball_started``

.. todo::
   Add description.

label:
~~~~~~
Single value, type: ``string``. Default: ``%``

.. todo::
   Add description.

release_one_events:
~~~~~~~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``ms``. Default: ``None``

.. todo::
   Add description.

request_new_balls_to_pf:
~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``True``

.. todo::
   Add description.

reset_events:
~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``ms``. Default: ``machine_reset_phase_3, ball_starting, ball_ending``

.. todo::
   Add description.

source_playfield:
~~~~~~~~~~~~~~~~~
Single value, type: string name of a ``ball_devices:`` device. Default: ``playfield``

.. todo::
   Add description.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

.. todo::
   Add description.


