random_event_player:
====================

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`shows </shows/index>`                                       | **YES** |
+----------------------------------------------------------------------------+---------+

.. note:: This section can also be used in a show file in the ``randoms:`` section of a step.

.. overview

The ``random_event_player:`` section of your config is where you...

.. todo::
   :doc:`/about/help_us_to_write_it`

Required settings
-----------------

The following sections are required in the ``random_event_player:`` section of your config:

events:
~~~~~~~


List of one (or more) values, each is a type: ``string``.

.. todo::
   :doc:`/about/help_us_to_write_it`

force_different:
~~~~~~~~~~~~~~~~

single|bool|true

:doc:`/about/help_us_to_write_it`

force_all:
~~~~~~~~~~

single|bool|true

:doc:`/about/help_us_to_write_it`

disable_random:
~~~~~~~~~~~~~~~

single|bool|false

:doc:`/about/help_us_to_write_it`

scope:
~~~~~~


single|enum(player,machine)|player

:doc:`/about/help_us_to_write_it`
