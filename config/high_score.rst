high_score:
===========

*Config file section*

* Valid in machine config files: **YES**
* Valid in mode config files: **YES**

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

select_tag:
~~~~~~~~~~~
Single value, type: ``string``. Default: ``start``

.. todo::
   Add description.

shift_left_tag:
~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``left_flipper``

.. todo::
   Add description.

shift_right_tag:
~~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``right_flipper``

.. todo::
   Add description.


