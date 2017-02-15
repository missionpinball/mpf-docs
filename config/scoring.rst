scoring:
========

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **NO**  |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

.. versionchanged:: 0.31 (Now valid only in mode configs, not machine configs)

.. overview

The ``scoring:`` section of your config is where you...

.. todo::
   Add description.

score:
~~~~~~

.. versionadded:: 0.32

single|template_int|

TODO

Note that you can use a :doc:`placeholder value </config/instructions/placeholders>`
for this setting.

block:
~~~~~~

.. versionadded:: 0.32

single|bool|False

TODO

action:
~~~~~~~

.. versionadded:: 0.32

single|enum(add,set)|add

TODO
