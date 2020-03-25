fast_switches:
==============

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **NO**  |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``fast_switches:`` section of your config is where you configure platform
specific details about switches when using
:doc:`fast hardware </hardware/fast/index>`.

.. code-block:: mpf-config

   switches:
     some_switch:
       number:
       platform_settings:
         debounce_close: 2ms
         debounce_open: 4ms

Please make sure to read :doc:`/mechs/switches/debounce` before changing those
times.

.. config


Optional settings
-----------------

The following sections are optional in the ``fast_switches:`` section of your config. (If you don't include them, the default will be used).

debounce_close:
~~~~~~~~~~~~~~~
Single value, type: ``string``.

Set the switch debounce time for closing the switch.

debounce_open:
~~~~~~~~~~~~~~
Single value, type: ``string``.

Set the switch debounce time for opening the switch.


Related How To guides
---------------------

* :doc:`/hardware/fast/index`
