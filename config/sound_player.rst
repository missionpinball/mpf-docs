sound_player:
=============

*Config file section*

.. include:: _machine_config_yes.rst
.. include:: _mode_config_yes.rst

.. note:: This section can also be used in a show file in the ``sounds:`` section of a step.

.. overview

The ``sound_player:`` section of your config is where you...

.. todo::
   Add description.


Optional settings
-----------------

The following sections are optional in the ``sound_player:`` section of your config. (If you don't include them, the default will be used).

action:
~~~~~~~
Single value, type: one of the following options: play, stop. Default: ``play``

.. todo::
   Add description.

loops:
~~~~~~
Single value, type: ``integer``. Default: ``None``

.. todo::
   Add description.

max_queue_time:
~~~~~~~~~~~~~~~
Single value, type: ``time string`` (:doc:`Instructions </config/instructions/lists>` for entering time strings). Default: ``None``

.. todo::
   Add description.

priority:
~~~~~~~~~
Single value, type: ``integer``. Default: ``None``

.. todo::
   Add description.

volume:
~~~~~~~
Single value, type: ``gain setting`` (-inf, db, or float between 0.0 and 1.0. Default: ``None``

.. todo::
   Add description.


.. note:: The ``sound_player:`` section of your config may contain additional settings not mentioned here. Read the introductory text for details of what those might be.


