Text Input Widget
=================

The text input widget is a special widget which lets the player use the flipper
buttons to cycle through letters and numbers and to select them. This is used
in the high score name entry and the service mode.

Currently the text input widget flashes a cursor over the selected letter, and
the player hitting the flipper buttons changes the letter in place. In the future,
we'll add an option to show all the letters on the screen in a long list as well.

Settings
--------

Here are the list of settings you can use for text_input widgets:

.. code-block:: yaml

   type: text_input
   key:
   char_list:
   max_chars:
   initial_char:
   keep_selected_char:
   dynamic_x:
   dynamic_x_pad:
   shift_left_event:
   shift_right_event:
   select_event:
   abort_event:
   force_complete_event:
   font_size:
   font_name:
   bold:
   italic:
   halign:
   valign:

.. note:: Text widgets also have "common" widget settings for position, opacity,
   animations, color, style, etc. Those are not listed here, but are instead covered in
   :doc:`common widget settings </displays/widgets/common_settings>` page.

Also remember that all widget settings can be controlled via
:doc:`widget styles </displays/widgets/styles>`, rather than
you having to set every setting on every widget.

type: text_input
~~~~~~~~~~~~~~~~

Tells MPF that this is a text_input widget. This setting is required when using text_input
widgets.

key:
~~~~

single

char_list:
~~~~~~~~~~

String value, default is ``ABCDEFGHIJKLMNOPQRSTUVWXYZ\_- \``.

A list of all the characters that are available to be chosen by the player
as they're entering their name or initials. The order they are here is the order
they show up as the uses scrolls left or right. If you want to add, remove, or
change any of the defaults, just add a new ``char_list:`` setting to this text_input
widget and completely replace the default list with your own list.

Note that "back" and "end" characters will automatically be added to the end of
this list.

max_chars:
~~~~~~~~~~

Integer value, default is ``3``.

How many characters can be entered into this text input field.

initial_char:
~~~~~~~~~~~~~

Single character value. Default is ``A``.

The character from your ``char_list:`` that you want to be the initial character
selected before the player starts entering their name.

keep_selected_char:
~~~~~~~~~~~~~~~~~~~

Boolean (True/False or Yes/No), default is ``True``.

When a player hits the start button to select a character and then the cursor moves
to the next position, should the selected character stay with the character they
just selected, or should it go back to the ``initial_char:``?

dynamic_x:
~~~~~~~~~~

Boolean (True/False or Yes/No), default is ``True``.

If True, then the x position of this text widget will be updated as characters are selected and entered. If False,
then the widget's x position will not change, and additional characters will be added to the right edge.

In other words, if you plan to center this widget, set this to True. If you plan on left justifying it, set it to False.

dynamic_x_pad:
~~~~~~~~~~~~~~

Integer value. Default is ``0``.

If you're using the ``dynamic_x:`` setting above, this is the number of additional pixels that will be added to the
total width of the widget to calculate the dynamic x position.

block_events:
~~~~~~~~~~~~~

A list of events that, when posted, will prevent the text input from shifting or selecting input values. Useful for
when a flipper cancel is used to select and the subsequent flipper inactive events shouldn't change the input.

Used in conjucting with ``release_events`` setting below.

release_events:
~~~~~~~~~~~~~~~

A list of events that, when posted, will unblock the text input from shifting or selecting input values.

Used in conjuction with ``block_events`` setting above.

shift_left_event:
~~~~~~~~~~~~~~~~~

The event that, when posted, will shift the selected character from the *char_list* to the left. Default is
``sw_left_flipper``.

shift_right_event:
~~~~~~~~~~~~~~~~~~

The event that, when posted, will shift the selected character from the *char_list* to the right. Default is
``sw_right_flipper``.

select_event:
~~~~~~~~~~~~~

The event that, when posted, will select (or "enter") the currently highlighted character and move the cursor to the
next position. Default is ``sw_start`` (which is the event that's posted when a switch tagged with *start* is hit).

abort_event:
~~~~~~~~~~~~

The event that, when posted, will abort (or cancel) the character entry process. Default is ``sw_esc`` (which is the
event that's posted when a switch tagged with *esc* is hit).

force_complete_event:
~~~~~~~~~~~~~~~~~~~~~

The event that, when posted, will mark the text entry process as complete, even if the player hasn't entered all their
characters yet. Default is ``None``.

font_size:
~~~~~~~~~~

Same as the ``font_size:`` setting for the :doc:`/displays/widgets/text/index`. See that
documentation for usage.

font_name:
~~~~~~~~~~

Same as the ``font_name:`` setting for the :doc:`/displays/widgets/text/index`. See that
documentation for usage.

bold:
~~~~~

Same as the ``bold:`` setting for the :doc:`/displays/widgets/text/index`. See that
documentation for usage.

italic:
~~~~~~~

Same as the ``italic:`` setting for the :doc:`/displays/widgets/text/index`. See that
documentation for usage.

halign:
~~~~~~~

Same as the ``halign:`` setting for the :doc:`/displays/widgets/text/index`. See that
documentation for usage.

valign:
~~~~~~~

Same as the ``valign:`` setting for the :doc:`/displays/widgets/text/index`. See that
documentation for usage.

anchor_y: baseline
~~~~~~~~~~~~~~~~~~

Text input widgets have an additional ``baseline`` option in addition to the other baseline
options detailed in the :doc:`common widget settings </displays/widgets/common_settings>`
documentation.
