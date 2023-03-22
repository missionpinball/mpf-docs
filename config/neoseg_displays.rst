neoseg_displays:
================

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``neoseg_displays:`` section of your config is where you...

.. todo:: :doc:`/about/help_us_to_write_it`

.. config


Required settings
-----------------

The following sections are required in the ``neoseg_displays:`` section of your config:

light_template:
~~~~~~~~~~~~~~~
Single value, type: :doc:`lights <lights>`. Defaults to empty.

.. todo:: :doc:`/about/help_us_to_write_it`


Optional settings
-----------------

The following sections are optional in the ``neoseg_displays:`` section of your config. (If you don't include them, the default will be used).

number_start:
~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``0``

.. todo:: :doc:`/about/help_us_to_write_it`

number_template:
~~~~~~~~~~~~~~~~
Single value, type: ``string``. Defaults to empty.

.. todo:: :doc:`/about/help_us_to_write_it`

previous:
~~~~~~~~~
Single value, type: string name of a :doc:`lights <lights>` device. Defaults to empty.

.. todo:: :doc:`/about/help_us_to_write_it`

size:
~~~~~
Single value, type: one of the following options: 2digit, 8digit. Default: ``8digit``

.. todo:: :doc:`/about/help_us_to_write_it`

start_channel:
~~~~~~~~~~~~~~
Single value, type: ``string``. Defaults to empty.

.. todo:: :doc:`/about/help_us_to_write_it`

start_x:
~~~~~~~~
Single value, type: ``number`` (will be converted to floating point). Defaults to empty.

.. todo:: :doc:`/about/help_us_to_write_it`

start_y:
~~~~~~~~
Single value, type: ``number`` (will be converted to floating point). Defaults to empty.

.. todo:: :doc:`/about/help_us_to_write_it`

console_log:
~~~~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level for the console log for this device.

debug:
~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

Set this to true to see additional debug output. This might impact the performance of MPF.

file_log:
~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level for the file log for this device.

label:
~~~~~~
Single value, type: ``string``. Default: ``%``

Name of this device in service mode.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Defaults to empty.

.. todo:: :doc:`/about/help_us_to_write_it`


Related How To guides
---------------------

.. todo:: :doc:`/about/help_us_to_write_it`
