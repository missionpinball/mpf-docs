widget_player:
==============

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`shows </shows/index>`                                       | **YES** |
+----------------------------------------------------------------------------+---------+

.. note:: This section can also be used in a show file in the ``widgets:`` section of a step.

.. overview

The ``widget_player:`` section of your config is where you...

.. todo::
   Add description.

Optional settings
-----------------

The following sections are optional in the ``widget_player:`` section of your config. (If you don't include them, the default will be used).

action:
~~~~~~~
Single value, type: one of the following options: *add*, *remove*, *update*. Default: ``add``

Specifies what action will take place when this event is posted.

``add``
   The widget or widget group is added to the slide or display target.

``remove``
   The widget or widget group is removed from the slide or display target.

``update``
   One or more of the widget or widget group's priorities is updated.

key:
~~~~
Single value, type: ``string``. Default: ``None``

Used to uniquely identify a widget. With "add" actions, this sets the key name,
and with "remove" or "update" actions, the key is used to identify which widget
should be removed or updated.

Note that more than one widget (across displays and across slides) can have the
same key, and if you remove a widget based on a key, it will remove all the
widgets with that key. (In fact this is how MPF works internally to remove all
widgets that were created by a mode when that mode ends.)

See the :doc:`/displays/widgets/keys` guide for details.

slide:
~~~~~~
Single value, type: ``string``. Default: ``None``

The name of the slide you want to add this widget to. If this is not specified,
then the widget will be added to whichever slide is currently active on the
default display.

target:
~~~~~~~
Single value, type: ``string``. Default: ``None``

The name of the display or slide frame this widget will be added to. When this
setting is used, the widget is not added to a slide, rather, it's added "on top"
of the slide (to the parent display or slide frame). See the
:doc:`/displays/widgets/layers` guide for details.

Note that the ``target:`` and ``slide:`` setting are fundamentally not
compatible with each other. If you used both, the ``target:`` setting will be
used and the ``slide:`` value will be ignored.

