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

The ``widget_player:`` section of your config is where you configure widgets to be added to,
removed from, or updated on slides based on based on events being posted.

Note that the widget player is a :doc:`config_player </config_players/index>`, so everything
mentioned below is valid in the ``widget_player:`` section of a config file *and* in the ``widgets:``
section of a :doc:`show step </shows/content>`.

Full instructions on how to use the slide_player are included in the
:doc:`/displays/widgets/index` section of the documentation. The stuff here
in the config reference is for reference later.
You can test slides and widgets interactively using
:doc:`Interactive MC (iMC) </tools/imc/index>`.

Generically-speaking, there are two formats you can use for widget_player
entries: "express" and "full" configs. Express configs will look like this:

.. code-block:: mpf-config

   widget_player:
      event1: widget1
      event2: widget2
      event3: widget3

Full configs will look like this:

.. code-block:: yaml

   widget_player:
      event1:
         widget1:
            <settings>
      event2:
         widget2:
            <settings>
      event3:
         widget3:
            <settings>

In both cases, these configurations are saying, "When *event1* is posted,
add widget *widget1*. When *event2* is posted, add *widget2*. Etc."

This "express" config is down-and-dirty, with no options, to just add widgets to
the current slide on the default display.
The full config lets you specify additional options (based on the settings
detailed below).

For example, the following config will add *widget_1* when *some_event* is posted, but it
will also override the default settings and add widget to the slide called *slide_2*, even
if that's not the current slide that's showing.

.. code-block:: mpf-config

   widget_player:
      some_event:
         widget_1:
            slide: slide_2

Settings
--------

The following sections can be added under the the a particular widget's settings ``widget_player:`` section of your config.
(If you don't include any of them, the default will be used).

So again, the format in a config file would be:

.. code-block:: yaml

   #config_version=5

   widget_player:
      some_event:
         name_of_your_widget:
            <list of settings below go here>
      some_other_event:
         name_of_a_different_widget:
            <list of settings below go here>

And the format in a show file would be:

.. code-block:: yaml

   #show_version=5

   - duration: 1s
     widgets:
         name_of_your_widget:
            <list of settings below go here>
         name_of_a_different_widget:
            <list of settings below go here>

Here are the settings you can use:

action:
~~~~~~~
Single value, type: one of the following options: *add*, *remove*, *update*. Default: ``add``

Specifies what action will take place when this event is posted.

``add``
   The widget or widget group is added to the slide or display target.

``remove``
   The widget or widget group is removed from the slide or display target.

``update``
   One or more of the widget or widget group's properties is updated.

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

widget_settings:
~~~~~~~~~~~~~~~~

Used to override and/or update
