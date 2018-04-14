machine_vars:
=============

*Config file section*


+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+


The ``machine_vars:`` section of your machine-wide config file lets you
specify the initial state of machine variables that are set when MPF starts up.

Example:

.. literalinclude:: /mpf_examples/player_vars/config/player_vars.yaml
   :language: yaml

Settings
--------

Each subsection in the ``machine_vars:`` section is the name of a machine
variable to set. Then there are three sub-settings under there:

initial_value: (required)
~~~~~~~~~~~~~~~~~~~~~~~~~

The initial value of this machine variable that you're setting. This
is set when MPF starts.

value_type:
~~~~~~~~~~~

Select one of the options from this list: ``int`` (integer), ``float``, or
``str`` (string). The default is "int", and there is no intelligence to
try to detect which type of value you have, so if you have a floating
point number or a string, you also need to set the value_type.

persist:
~~~~~~~~

True/False value which controls whether this machine variable will be persisted
to when MPF shuts down.
