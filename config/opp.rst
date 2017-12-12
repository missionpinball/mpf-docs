opp:
====

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``opp:`` section of your config is where you...

.. todo::
   :doc:`/about/help_us_to_write_it`

Required settings
-----------------

The following sections are required in the ``opp:`` section of your config:

ports:
~~~~~~
List of one (or more) values, each is a type: ``string``.

.. todo::
   :doc:`/about/help_us_to_write_it`

Optional settings
-----------------

The following sections are optional in the ``opp:`` section of your config. (If you don't include them, the default will be used).

baud:
~~~~~
Single value, type: ``integer``. Default: ``115200``

.. todo::
   :doc:`/about/help_us_to_write_it`

debug:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

.. todo::
   :doc:`/about/help_us_to_write_it`

chains:
~~~~~~~

:doc:`/about/help_us_to_write_it`

poll_hz:
~~~~~~~~

How many times per section the OPP hardware is polled for switch changes. Default is 100.
