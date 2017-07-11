high_score:
===========

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **NO**  |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

.. overview

The ``high_score:`` section of your config is where you...

.. todo::
   Add description.

Required settings
-----------------

The following sections are required in the ``high_score:`` section of your config:

categories:
~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``list``.

.. todo::
   Add description.

Optional settings
-----------------

The following sections are optional in the ``high_score:`` section of your config. (If you don't include them, the default will be used).

award_slide_display_time:
~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings) </config/instructions/time_strings>` . Default: ``4s``

.. todo::
   Add description.

defaults:
~~~~~~~~~
