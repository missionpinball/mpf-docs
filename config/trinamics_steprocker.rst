trinamics_steprocker:
=====================

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``trinamics_steprocker:`` section of your config is where you configure
the :doc:`trinamics steprocker platform </hardware/trinamics/index>`.

.. config


Required settings
-----------------

The following sections are required in the ``trinamics_steprocker:`` section of your config:

port:
~~~~~
Single value, type: ``string``. Defaults to empty.

Serial port to use to connect to the steprocker.


Related How To guides
---------------------

* :doc:`/hardware/trinamics/index`
