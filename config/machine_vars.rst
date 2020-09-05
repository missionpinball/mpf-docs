machine_vars:
=============

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``machine_vars:`` section of your machine-wide config file lets you
specify the initial state of machine variables that are set when MPF starts up.

Example:

.. literalinclude:: /mpf_examples/player_vars/config/player_vars.yaml
   :language: yaml

.. config


Required settings
-----------------

The following sections are required in the ``machine_vars:`` section of your config:

initial_value:
~~~~~~~~~~~~~~
Single value, type: ``string``. Defaults to empty.

The initial value of this machine variable that you're setting. This
is set when MPF starts.


Optional settings
-----------------

The following sections are optional in the ``machine_vars:`` section of your config. (If you don't include them, the default will be used).

persist:
~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``true``

True/False value which controls whether this machine variable will be persisted
to when MPF shuts down.

value_type:
~~~~~~~~~~~
Single value, type: one of the following options: str, float, int. Default: ``int``

Select one of the options from this list: ``int`` (integer), ``float``, or
``str`` (string). The default is "int", and there is no intelligence to
try to detect which type of value you have, so if you have a floating
point number or a string, you also need to set the value_type.


Related How To guides
---------------------

* :doc:`/machine_vars/index`
