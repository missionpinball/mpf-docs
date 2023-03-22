virtual_segment_display_connector:
==================================

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``virtual_segment_display_connector:`` section of your config is where you configure the
connector that establishes the link between segment displays and the virtual segment display
emulator widgets in the MPF-MC.

.. code-block:: mpf-config

    virtual_segment_display_connector:
      segment_displays: display1

.. config


Optional settings
-----------------

The following sections are optional in the ``virtual_segment_display_connector:`` section of your config. (If you don't include them, the default will be used).

bcp_connection:
~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``local_display``

The name of the BCP connection the MPF-MC is connected to. Normally this does not need to be modified as
the default value should be correct.

debug:
~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

.. todo:: :doc:`/about/help_us_to_write_it`

segment_displays:
~~~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: string name of a :doc:`segment_displays <segment_displays>` device. Defaults to empty.

A list of one or more segment display names which is used to specify which segment displays should be
activated in the connector to send the appropriate information to the MPF-MC.


Related How To guides
---------------------

.. todo:: :doc:`/about/help_us_to_write_it`
