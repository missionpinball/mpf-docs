show_config:
============

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **NO**  |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``show_config:`` section of your config is where you configure a show to play within a device.

See :doc:`show_player <show_player>` for more details about the settings.


Required settings
-----------------

The following sections are required in the ``show_config:`` section of your config:

show:
~~~~~
Single value, type: ``string``.

The show to play.


Optional settings
-----------------

The following sections are optional in the ``show_config:`` section of your config. (If you don't include them, the default will be used).

loops:
~~~~~~
Single value, type: ``integer``. Default: ``-1``

How often should the show loop? ``-1`` means forever.

manual_advance:
~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False).

Whatever, the show should advance manually only.

priority:
~~~~~~~~~
Single value, type: ``integer``. Default: ``0``

Priority for this show.
This is usually added to the mode priority if the device is defined within a
mode.

show_tokens:
~~~~~~~~~~~~
One or more sub-entries, each in the format of ``string`` : ``string``
Dict of show tokens to pass to the show.

speed:
~~~~~~
Single value, type: ``number`` (will be converted to floating point). Default: ``1``

Speed multiplier for this show.

start_step:
~~~~~~~~~~~
Single value, type: ``integer``. Default: ``1``

First step to play.

sync_ms:
~~~~~~~~
Single value, type: ``integer``.

See the :doc:`/shows/sync_ms` documentation for details.


