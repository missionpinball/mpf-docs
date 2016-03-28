
*Entered Chars* (short for "Entered Characters") is a `display
element`_ that works hand-in-hand with the *`character picker`_*
display element. It's where the characters the player is selecting
when entering text appear on the display. The entered char’s size and
position on the screen is controlled just like any other display
element, so you can refer to the`positioning & placement settings`_
settings there. ` `_ Entered chars-specific settings include:



character_picker:
~~~~~~~~~~~~~~~~~

The name of the character picker display element that the player uses
to generate the characters for this entered chars display element. It
can be whatever you want, just make sure you have the same value set
for the *name:* section of the *character_picker* element.



cursor_char:
~~~~~~~~~~~~

The character that will be used as the cursor character. The
underscore is the default.



cursor_offset_x:
~~~~~~~~~~~~~~~~

Let's you specify the x (horizontal) offset of the cursor character,
in pixels. This can be positive or negative and is used to fine-turn
the placement of the cursor character.



cursor_offset_y:
~~~~~~~~~~~~~~~~

Like cursor_offset_x, except for the y (vertical) offset.



cursor_decorator:
~~~~~~~~~~~~~~~~~

This is the `decorator`_ that will be applied to the cursor character.
It's a separate setting from the overall decorator that's applied to
the entered chars element so you can make the cursor blink without all
of the entered characters blinking.

.. _display element: https://missionpinball.com/docs/mpf-core-architecture/displays-dmd/display-elements/
.. _character picker: https://missionpinball.com/docs/mpf-core-architecture/displays-dmd/display-elements/character-picker/
.. _decorator: https://missionpinball.com/docs/mpf-core-architecture/displays-dmd/decorators/
.. _ placement settings: https://missionpinball.com/docs/mpf-core-architecture/displays-dmd/display-elements/positioning/


