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
   Add description.

Required settings
-----------------

The following sections are required in the ``random_event_player:`` section of your config:

events:
~~~~~~~


List of one (or more) values, each is a type: ``string``.

.. todo::
   Add description.

force_different:
~~~~~~~~~~~~~~~~


single|bool|true

TODO

force_all:
~~~~~~~~~~


single|bool|true

TODO

disable_random:
~~~~~~~~~~~~~~~


single|bool|false

TODO

scope:
~~~~~~


single|enum(player,machine)|player

TODO
