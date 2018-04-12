kickbacks:
==========

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+


The ``kickbacks:`` section of your machine config is used to define
:doc:`kickback mechanisms </mechs/kickbacks/index>` which are a type of
:doc:`autofire coil </mechs/autofire_coils/index>`
that kicks the ball back into play, typically located in an outlane.

Example:

.. literalinclude:: /mpf_examples/kickback/config/config.yaml
   :caption: `/config/config.yaml </_static/kickback/config/config.yaml>`_
   :language: yaml

Since kickbacks are a type of autofire coil, they have the same settings as
:doc:`/config/autofire_coils`. See that documentation for a list of all the
settings and options.
