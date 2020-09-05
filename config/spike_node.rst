spike_node:
===========

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **NO**  |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``node_config:`` section of your config is where you configure your node
boards in your ``spike:`` section.

.. config


Optional settings
-----------------

The following sections are optional in the ``spike_node:`` section of your config. (If you don't include them, the default will be used).

coil_priorities:
~~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: ``integer``.

A list of coils ordered by priority.
This list is send to the hardware to priorize coils when multiple hardware
rules active.
The exact logic is unknown.

num_inputs:
~~~~~~~~~~~
Single value, type: ``integer``.

Number of inputs on that node board.

num_leds:
~~~~~~~~~
Single value, type: ``integer``.

Number of LEDs on that node board.


Related How To guides
---------------------

* :doc:`/hardware/spike/index`
