logic_blocks:
=============

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

.. overview

The ``logic_blocks:`` section of your config is where you configure your logic blocks.

There are three sub-sections that go under the ``logic_blocks:`` section which each
correspond to a different type of logic block:

* accruals:
* counters:
* sequences:

Then under each of these sections, you add the specific logic blocks. Logic blocks in
mode config files are only active while that mode is active, and logic blocks in your
machine config can be active any time.

Full documentation for logic blocks is in the
:doc:`logic block documentation </game_logic/logic_blocks/index>` in the
:doc:`/game_logic/index` section of the documentation. Look there for
the description of all the settings and what they do, as well as
examples of logic blocks in use.
