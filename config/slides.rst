slides:
=======

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

.. overview

The ``slides:`` section of your config is where you...

.. todo::
   Add description.

Optional settings
-----------------

The following sections are optional in the ``slides:`` section of your config. (If you don't include them, the default will be used).

background_color:
~~~~~~~~~~~~~~~~~
Single value, type: ``color`` (*color name*, *hex*, or list of values *0*-*255*). Default: ``000000ff``

.. todo::
   Add description.

debug:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

.. todo::
   Add description.

expire:
~~~~~~~
Single value, type: ``time string (secs)`` (:doc:`Instructions for entering time strings) </config/instructions/time_strings>` . Default: ``None``

.. todo::
   Add description.

opacity:
~~~~~~~~
Single value, type: ``number`` (will be converted to floating point). Default: ``1.0``

.. todo::
   Add description.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

.. todo::
   Add description.

.. note:: The ``slides:`` section of your config may contain additional settings not mentioned here. Read the introductory text for details of what those might be.

