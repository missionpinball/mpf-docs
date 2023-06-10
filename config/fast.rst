fast:
=====

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``fast:`` section of your machine-wide config is where you
configure hardware options that are specific to the FAST Pinball
Controller. Note that we have a how to guide which includes
:doc:`all the FAST-specific settings </hardware/fast/index>` throughout your entire config file,
so be sure to read that if you have FAST hardware.

.. code-block:: mpf-config

    fast:
      ports: com3, com4, com5

.. config


Optional settings
-----------------

The following sections are optional in the ``fast:`` section of your config. (If you don't include them, the default will be used).

aud:
~~~~
Single value, type: :doc:`fast_aud <fast_aud>`. Defaults to empty.

.. todo:: :doc:`/about/help_us_to_write_it`

console_log:
~~~~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``none``

Log level for the console log for this platform.

debug:
~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

See the :doc:`documentation on the debug setting </config/instructions/debug>`
for details.

dmd:
~~~~
Single value, type: :doc:`fast_dmd <fast_dmd>`. Defaults to empty.

.. todo:: :doc:`/about/help_us_to_write_it`

emu:
~~~~
Single value, type: :doc:`fast_emu <fast_emu>`. Defaults to empty.

.. todo:: :doc:`/about/help_us_to_write_it`

exp:
~~~~
Single value, type: :doc:`fast_exp <fast_exp>`. Defaults to empty.

.. todo:: :doc:`/about/help_us_to_write_it`

file_log:
~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level for the file log for this platform.

net:
~~~~
Single value, type: :doc:`fast_net <fast_net>`. Defaults to empty.

.. todo:: :doc:`/about/help_us_to_write_it`

rgb:
~~~~
Single value, type: :doc:`fast_rgb <fast_rgb>`. Defaults to empty.

.. todo:: :doc:`/about/help_us_to_write_it`

seg:
~~~~
Single value, type: :doc:`fast_seg <fast_seg>`. Defaults to empty.

.. todo:: :doc:`/about/help_us_to_write_it`


Related How To guides
---------------------

* :doc:`/hardware/fast/index`
