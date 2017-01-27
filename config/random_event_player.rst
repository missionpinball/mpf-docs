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

event_list:
~~~~~~~~~~~

.. deprecated:: 0.32

(Renamed to "events:")

events:
~~~~~~~

.. versionadded:: 0.32

List of one (or more) values, each is a type: ``string``.

.. todo::
   Add description.

force_different:
~~~~~~~~~~~~~~~~

.. versionadded:: 0.32

single|bool|true

TODO

force_all:
~~~~~~~~~~

.. versionadded:: 0.32

single|bool|true

TODO

disable_random:
~~~~~~~~~~~~~~~

.. versionadded:: 0.32

single|bool|false

TODO

scope:
~~~~~~

.. versionadded:: 0.32

single|enum(player,machine)|player

TODO
