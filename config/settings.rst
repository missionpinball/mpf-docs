settings:
=========

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``settings:`` section of your config is where you configure settings which
are configurable in :doc:`service mode </game_logic/service_mode/index>`.

This is an example:

.. code-block:: mpf-config

   settings:
     replay_score:
       label: Replay Score
       values:
         500000: "500000 (default)"
         1000000: "1000000"
         1500000: "1500000"
       default: 500000
       key_type: int
       sort: 100

.. config


Required settings
-----------------

The following sections are required in the ``settings:`` section of your config:

default:
~~~~~~~~
Single value, type: ``string``. Defaults to empty.

Default value to use if not changed or on reset. Must be included in ``values``.

label:
~~~~~~
Single value, type: ``string``. Defaults to empty.

Label to use in service mode for this setting.

sort:
~~~~~
Single value, type: ``integer``. Defaults to empty.

Sort in service mode.

values:
~~~~~~~
One or more sub-entries. Each in the format of ``string`` : ``string``

Values for this setting in the format ``value: label``.
``value`` will be assigned to the ``machine_var`` and ``label`` will be shown
in service mode.


Optional settings
-----------------

The following sections are optional in the ``settings:`` section of your config. (If you don't include them, the default will be used).

key_type:
~~~~~~~~~
Single value, type: one of the following options: str, float, int. Default: ``str``

Type of the key. If you want to do math with the variable you need either
``float`` or ``int``.

machine_var:
~~~~~~~~~~~~
Single value, type: ``string``. Defaults to empty.

Name of the machine variable to use. If this is not set it will use the name
of this setting as machine variable.


Related How To guides
---------------------

* :doc:`/machine_management/service_mode/index`
* :doc:`/game_logic/service_mode/index`
