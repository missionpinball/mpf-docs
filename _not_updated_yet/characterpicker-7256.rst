
The *character picker* `display element`_ is used to render a list of
characters to the display that the player can use to pick from when
entering their name or initials. It's typically used in the high score
entry mode, though you could use it in any slide if you want to do
other things (custom message in the operator menu, allow players to
set their name for a player profile, etc.) You can specify what
characters are included in the list, the spacing and positioning of
the characters, the font they used, colors for the selected and
unselected characters, and images to be used for "special" characters
like the backspace and end characters. The character picker's size and
position on the screen is controlled just like any other display
element, so you can refer to the`positioning & placement settings`_
settings there. ` `_ Character picker-specific settings include:



font:
~~~~~

The name of the font that will be used to render the characters. This
is `configured like any other font`_ in MPF.



name:
~~~~~

The name setting for the character picker display element is no
different than the name of any display element. However, the name is
more important for the character picker because this is the name you
use to link a related ` *entered chars*`_ display element to display
the characters that have been entered so far.



selected_char_color:
~~~~~~~~~~~~~~~~~~~~

The color of the character that is selected (highlighted) in the list.
For mono-color displays, this is an integer value corresponding to the
brightness. For color displays, this is a six-character hex color
code. Typically this would be dark.



selected_char_bg:
~~~~~~~~~~~~~~~~~

The background color of the character that is selected (highlighted)
in the list. For mono-color displays, this is an integer value
corresponding to the brightness. For color displays, this is a six-
character hex color code. Typically this would be a light color to
create a bright box around the selected character (which itself would
be dark).



char_x_offset:
~~~~~~~~~~~~~~

This is a positive or negative value that lets you fine-tune the x
position (horizontal) of the character in the box. Most font render
the individual characters to go right up to the edge of their bounding
box, so this value lets you shift the character horizontally so it's
not smashed up against the edge.



char_y_offset:
~~~~~~~~~~~~~~

This is the same as the *char_x_offset*, but it affects the y
(vertical) positioning.



char_width:
~~~~~~~~~~~

This is the width, in pixels, that each character will take up in the
list. This is needed because most fonts are variable-width, meaning a
character "i" takes up much less horizontal space than a "w". When an
entire list is rendered to the display, it looks weird if all the
characters have different spacing, so this setting lets you specific
how many pixels wide each character will be regardless of how wide the
actual font character is rendered.



char_list:
~~~~~~~~~~

This is a list of all the characters (in order) that will be in this
character picker. Basically it's where you specific a list of letters
the player can pick from. For example: `"ABCDEFGHIJKLMNOPQRSTUVWXYZ_-
"`. (If you put it in quotes, you can also include a space as a valid
character in the list.)



back_char:
~~~~~~~~~~

This is the name of the MPF image asset that will be used to render
the "back" arrow which, when chosen, causes the entered characters to
delete the last one and go back a space. This image is what the back
character looks like when it's not selected.



end_char:
~~~~~~~~~

This is the name of the MPF image asset that will be used to render
the "end" character which is what the player selects when they're done
entering their name.



back_char_selected:
~~~~~~~~~~~~~~~~~~~

This is like the *back_char*, except it's the image that's used when
the *back_char* is selected.



end_char_selected:
~~~~~~~~~~~~~~~~~~

This is like the *end_char*, except it's the image that's used when
the *end_char* is selected.



image_padding:
~~~~~~~~~~~~~~

This is how many pixels of spacing you want on the left and right
sides of the back and end character images.



shift_left_tag:
~~~~~~~~~~~~~~~

The tag of the switch in the machine that causes the character picker
to shift the selected character one position to the left.



shift_right_tag:
~~~~~~~~~~~~~~~~

The tag of the switch in the machine that causes the character picker
to shift the selected character one position to the right.



select_tag:
~~~~~~~~~~~

The tag of the switch in the machine that causes the character picker
to select the currently-selected (highlighted) character.



max_chars:
~~~~~~~~~~

The maximum number of characters the player can select. If you just
want initials, this would be 3. If you want to allow full names, this
could be longer, like 10.



timeout:
~~~~~~~~

This is the timeout (in MPF time string format) that specifies how
long the character picker will sit there waiting for the player to
enter their name before it times out.



return_param:
~~~~~~~~~~~~~

The character picker works by collecting the characters the player has
entered and sending them back to MPF as an input. This setting is
where you specify what that return parameter will be called.

.. _display element: https://missionpinball.com/docs/mpf-core-architecture/displays-dmd/display-elements/
.. _entered chars: https://missionpinball.com/docs/mpf-core-architecture/displays-dmd/display-elements/entered-chars/
.. _configured like any other font: https://missionpinball.com/docs/howto/how-to-adding-truetype-fonts/
.. _ placement settings: https://missionpinball.com/docs/mpf-core-architecture/displays-dmd/display-elements/positioning/


