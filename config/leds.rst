leds:
=====

*Config file section*

.. include:: _machine_config_yes.rst
.. include:: _mode_config_no.rst

.. overview

The ``leds:`` section of your config is where you...

.. todo::
   Add description.


Required settings
-----------------

The following sections are required in the ``leds:`` section of your config:

number:
~~~~~~~
Single value, type: ``string``. 

.. todo::
   Add description.


Optional settings
-----------------

The following sections are optional in the ``leds:`` section of your config. (If you don't include them, the default will be used).

color_correction_profile:
~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``None``

.. todo::
   Add description.

debug:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

.. todo::
   Add description.

default_color:
~~~~~~~~~~~~~~
Single value, type: ``color`` (*color name*, *hex*, or list of values *0*-*255*). Default: ``ffffff``

.. todo::
   Add description.

fade_ms:
~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings) </config/instructions/time_strings>` . Default: ``None``

.. todo::
   Add description.

label:
~~~~~~
Single value, type: ``string``. Default: ``%``

.. todo::
   Add description.

off_events:
~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``ms``. Default: ``None``

.. todo::
   Add description.

on_events:
~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``ms``. Default: ``None``

.. todo::
   Add description.

platform:
~~~~~~~~~
Single value, type: ``string``. Default: ``None``

.. todo::
   Add description.

polarity:
~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

.. todo::
   Add description.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

.. todo::
   Add description.

type:
~~~~~
Single value, type: ``string`` (case-insensitive). Default: ``rgb``

.. todo::
   Add description.

x:
~~
Single value, type: ``integer``. Default: ``None``

.. todo::
   Add description.

y:
~~
Single value, type: ``integer``. Default: ``None``

.. todo::
   Add description.

z:
~~
Single value, type: ``integer``. Default: ``None``

.. todo::
   Add description.


