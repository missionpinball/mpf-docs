modes:
======

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``modes:`` section of your config is where you configure which modes can be
loaded in your machine.

This is an example:

.. code-block:: yaml

  modes:
    - my_mode1
    - my_mode2

See :doc:`/game_logic/modes/index` and :doc:`/game_design/index` for details about modes.

.. config


Related How To guides
---------------------

* :doc:`/game_design/index`
* :doc:`/tutorial/14_add_a_mode`
* :doc:`/game_logic/modes/index`
