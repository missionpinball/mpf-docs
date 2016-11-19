physical_rgb_dmds:
==================

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. versionchanged:: 0.31

.. overview

The ``physical_rgb_dmd:`` section of your config is where you...

.. todo::
   Add description.

Optional settings
-----------------

The following sections are optional in the ``physical_rgb_dmd:`` section of your config. (If you don't include them, the default will be used).

brightness:
~~~~~~~~~~~
Single value, type: ``number`` (will be converted to floating point). Default: ``1.0``

.. todo::
   Add description.

fps:
~~~~
Single value, type: ``integer``. Default: ``30``

.. todo::
   Add description.

only_send_changes:
~~~~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

.. todo::
   Add description.

source_display:
~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``dmd``

.. todo::
   Add description.

platform:
~~~~~~~~~

.. versionadded:: 0.31

Single value, type: ``string``. Default: ``None``

Name of the platform this DMD is connected to. The default value of ``None`` means the
default hardware platform will be used. You only need to change this if you have
multiple different hardware platforms in use and this coil is not connected
to the default platform.

See the :doc:`/hardware/platform` guide for details.

