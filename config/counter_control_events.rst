counter_control_events:
=======================

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **NO**  |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

Counter can contain ``control_events:`` which can add or substract to the count
of your counter.
Alternatively, you can set the counter to a certain value using an event.

.. config


Required settings
-----------------

The following sections are required in the ``counter_control_events:`` section of your config:

action:
~~~~~~~
Single value, type: one of the following options: add, subtract, jump.

``add`` will add ``value`` to the current count of your counter.
``subtract`` will subtract ``value`` from the current count of your counter.
``jump`` will set your counter to ``value``.

event:
~~~~~~
Single value, type: ``string``.

The event to trigger the ``action``.


Optional settings
-----------------

The following sections are optional in the ``counter_control_events:`` section of your config. (If you don't include them, the default will be used).

value:
~~~~~~
Single value, type: ``integer`` or ``template`` (:doc:`Instructions for entering templates </config/instructions/dynamic_values>`).

The value to use in ``action``.


Related How To guides
---------------------

* :doc:`counters`
