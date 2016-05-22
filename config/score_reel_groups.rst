score_reel_groups:
==================

*Config file section*

.. include:: _machine_config_yes.rst
.. include:: _mode_config_no.rst

.. overview

The ``score_reel_groups:`` section of your config is where you...

.. todo::
   Add description.


Required settings
-----------------

The following sections are required in the ``score_reel_groups:`` section of your config:

reels:
~~~~~~
List of one (or more) values, each is a type: string name of a ``score_reels:`` device. 

.. todo::
   Add description.


Optional settings
-----------------

The following sections are optional in the ``score_reel_groups:`` section of your config. (If you don't include them, the default will be used).

chimes:
~~~~~~~
List of one (or more) values, each is a type: string name of a ``coils:`` device. Default: ``None``

.. todo::
   Add description.

config:
~~~~~~~
Single value, type: ``string``. Default: ``lazy``

.. todo::
   Add description.

confirm:
~~~~~~~~
Single value, type: ``string``. Default: ``lazy``

.. todo::
   Add description.

debug:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

.. todo::
   Add description.

hw_confirm_time:
~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings) </config/instructions/time_strings>` . Default: ``300``

.. todo::
   Add description.

label:
~~~~~~
Single value, type: ``string``. Default: ``%``

.. todo::
   Add description.

lights_tag:
~~~~~~~~~~~
Single value, type: ``string``. Default: ``None``

.. todo::
   Add description.

max_simultaneous_coils:
~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``2``

.. todo::
   Add description.

repeat_pulse_time:
~~~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings) </config/instructions/time_strings>` . Default: ``200``

.. todo::
   Add description.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

.. todo::
   Add description.


