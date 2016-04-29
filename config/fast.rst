fast:
=====

*Config file section*

.. include:: _machine_config_yes.rst
.. include:: _mode_config_no.rst

.. overview

The ``fast:`` section of your config is where you...

.. todo::
   Add description.


Required settings
-----------------

The following sections are required in the ``fast:`` section of your config:

default_normal_debounce_close:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``time string`` (:doc:`Instructions </config/instructions/lists>` for entering time strings). 

.. todo::
   Add description.

default_normal_debounce_open:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``time string`` (:doc:`Instructions </config/instructions/lists>` for entering time strings). 

.. todo::
   Add description.

default_quick_debounce_close:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``time string`` (:doc:`Instructions </config/instructions/lists>` for entering time strings). 

.. todo::
   Add description.

default_quick_debounce_open:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``time string`` (:doc:`Instructions </config/instructions/lists>` for entering time strings). 

.. todo::
   Add description.

ports:
~~~~~~
List of one (or more) values, each is a type: ``string``. 

.. todo::
   Add description.


Optional settings
-----------------

The following sections are optional in the ``fast:`` section of your config. (If you don't include them, the default will be used).

baud:
~~~~~
Single value, type: ``integer``. Default: ``921600``

.. todo::
   Add description.

config_number_format:
~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``hex``

.. todo::
   Add description.

debug:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

.. todo::
   Add description.

hardware_led_fade_time:
~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``time string`` (:doc:`Instructions </config/instructions/lists>` for entering time strings). Default: ``0``

.. todo::
   Add description.

watchdog:
~~~~~~~~~
Single value, type: ``time string`` (:doc:`Instructions </config/instructions/lists>` for entering time strings). Default: ``1000``

.. todo::
   Add description.


