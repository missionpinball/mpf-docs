servo_controllers:
==================

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``servo_controllers:`` section of your config is where you...

.. todo::
   :doc:`/about/help_us_to_write_it`

Optional settings
-----------------

The following sections are optional in the ``servo_controllers:`` section of your config. (If you don't include them, the default will be used).

address:
~~~~~~~~
Single value, type: ``integer``. Default: ``64``

.. todo::
   :doc:`/about/help_us_to_write_it`

debug:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

.. todo::
   :doc:`/about/help_us_to_write_it`

label:
~~~~~~
Single value, type: ``string``. Default: ``%``

.. todo::
   :doc:`/about/help_us_to_write_it`

platform:
~~~~~~~~~
Single value, type: ``string``. Default: ``None``

Name of the platform this servo controller is connected to. The default value of ``None`` means the
default hardware platform will be used. You only need to change this if you have
multiple different hardware platforms in use and this coil is not connected
to the default platform.

See the :doc:`/hardware/platform` guide for details.

servo_max:
~~~~~~~~~~
Single value, type: ``integer``. Default: ``600``

.. todo::
   :doc:`/about/help_us_to_write_it`

servo_min:
~~~~~~~~~~
Single value, type: ``integer``. Default: ``150``

.. todo::
   :doc:`/about/help_us_to_write_it`

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

.. todo::
   :doc:`/about/help_us_to_write_it`

