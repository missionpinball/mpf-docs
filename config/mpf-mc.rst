mpf-mc:
=======

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

The ``mpf-mc:`` section of your config is where you configure options for the
MC itself.

Required Settings
-----------------

All of these settings are required in the ``mpf-mc:`` section. However, MPF-MC
includes a default config file called ``mcconfig.yaml`` which includes all
these settings with their defaults. So you only need to add/enter these if you
want to change something from the default.

bcp_port:
~~~~~~~~~
Single integer value, default is ``5050``.

This is the TCP port that the MC listens on for incoming BCP connections. If
you change this from the

bcp_interface:
~~~~~~~~~~~~~~
String, default is ``localhost``.

todo

fps:
~~~~

todo

allow_invalid_config_sections:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

todo
