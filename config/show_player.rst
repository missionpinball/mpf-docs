show_player:
============

*Config file section*

.. include:: _machine_config_yes.rst
.. include:: _mode_config_yes.rst

.. note:: This section can also be used in a show file in the ``shows:`` section of a step.

.. overview

The ``show_player:`` section of your config is where you...

.. todo::
   Add description.


Optional settings
-----------------

The following sections are optional in the ``show_player:`` section of your config. (If you don't include them, the default will be used).

action:
~~~~~~~
Single value, type: one of the following options: play, stop, pause, resume, advance, update. Default: ``play``

.. todo::
   Add description.

hold:
~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``None``

.. todo::
   Add description.

key:
~~~~
Single value, type: ``string``. Default: ``None``

.. todo::
   Add description.

loops:
~~~~~~
Single value, type: ``integer``. Default: ``-1``

.. todo::
   Add description.

manual_advance:
~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

.. todo::
   Add description.

priority:
~~~~~~~~~
Single value, type: ``integer``. Default: ``0``

.. todo::
   Add description.

reset:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``True``

.. todo::
   Add description.

speed:
~~~~~~
Single value, type: ``number`` (will be converted to floating point). Default: ``1``

.. todo::
   Add description.

start_step:
~~~~~~~~~~~
Single value, type: ``integer``. Default: ``1``

.. todo::
   Add description.

sync_ms:
~~~~~~~~
Single value, type: ``integer``. Default: ``0``

.. todo::
   Add description.


.. note:: The ``show_player:`` section of your config may contain additional settings not mentioned here. Read the introductory text for details of what those might be.

