lisy:
=====

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``lisy:`` section of your config is where your lisy platform.

.. todo:: :doc:`/about/help_us_to_write_it`


Optional settings
-----------------

The following sections are optional in the ``lisy:`` section of your config. (If you don't include them, the default will be used).

baud:
~~~~~
Single value, type: ``integer``. Default: ``None``

.. todo:: :doc:`/about/help_us_to_write_it`

connection:
~~~~~~~~~~~
Single value, type: one of the following options: network, serial. Default: ``network``

.. todo:: :doc:`/about/help_us_to_write_it`

console_log:
~~~~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``none``

.. todo:: :doc:`/about/help_us_to_write_it`

display_flash_frequency:
~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``number`` (will be converted to floating point). Default: ``1.0``

.. todo:: :doc:`/about/help_us_to_write_it`

file_log:
~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

.. todo:: :doc:`/about/help_us_to_write_it`

network_host:
~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``None``

.. todo:: :doc:`/about/help_us_to_write_it`

network_port:
~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``None``

.. todo:: :doc:`/about/help_us_to_write_it`

poll_hz:
~~~~~~~~
Single value, type: ``integer``. Default: ``1000``

.. todo:: :doc:`/about/help_us_to_write_it`

port:
~~~~~
Single value, type: ``string``. Default: ``None``

.. todo:: :doc:`/about/help_us_to_write_it`


