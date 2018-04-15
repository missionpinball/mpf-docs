Expiring (auto removing) widgets
================================

You can use the widget player to add widgets to slides which will be removed automatically after
a pre-determined about of time. This is done via a widget's "expire" setting. There are
several ways you can expire a widget:

Option 1: In the widget or slide definition
-------------------------------------------

.. code-block:: mpf-config

   widgets:
      my_widget:
         type: text
         text: HELLO
         expire: 2s

In the example above, whenever you add that widget to a slide (via the widget_player or
the widgets: section of a show), that widget will expire and disappear two seconds
later.

Option 2: In the widget player
------------------------------

Instead of tying an expire time to a widget when you define the widget, you can specify
the expiration when the widget is shown via the widget player.

Here's an example:

.. code-block:: mpf-config

   widgets:
      my_widget:
         type: text
         text: HELLO  # no expiration here

   widget_player:
      some_event:
         my_widget:
            widget_settings:
               expire: 2s

In the above example, the widget player dynamically adds the 2 second expiration time
when the widget is shown after *some_event* is posted.

Option 3: Remove a widget on some event
---------------------------------------

Instead of automatically removing a widget after a pre-determined amount of time, remember
you can use the widget player to remove a widget by name, which means you can use one event
to show the widget and another event to remove it. For example:

.. code-block:: mpf-config

   widgets:
      my_widget:
         type: text
         text: HELLO  # no expiration here

   widget_player:
      some_event: my_widget
      some_other_event:
         my_widget:
            action: remove

In the example above, the event *some_event* will cause my_widget to be added to the
current slide on the default display, and the event *some_other_event* will cause it
to be removed.

