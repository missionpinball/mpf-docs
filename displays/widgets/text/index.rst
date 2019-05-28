Text Widget
===========

The text widget is used to show text on a :doc:`slide </displays/slides/index>`.

.. image:: /displays/images/text_widget1.jpg

In addition to being able to specify static text, text widgets also include
powerful functionality:

* You can configure dynamic text that is automatically updated (in real time)
  based on the value of a player variable or a machine variable.
* You can configure a placeholder "text string" that uses a lookup value to
  get its actual text. This is useful for things like multi-language support,
  or to be able to have different text strings based on a configuration file
  (family-friendly versus R-rated text, etc.)
* You can configure fonts and font styles to be automatically applied to text,
  and you can override them on a widget-by-widget basis.

Settings
--------

Here are a list of the settings you can use for text widgets:

.. code-block:: yaml

   type: text
   text:
   font_size:
   font_name:
   bold:
   italic:
   casing:
   number_grouping:
   min_digits:
   halign:
   valign:

.. note:: Text widgets also have "common" widget settings for position, opacity,
   animations, color, style, etc. Those are not listed here, but are instead covered in
   :doc:`common widget settings </displays/widgets/common_settings>` page.

Also remember that all widget settings can be controlled via
:doc:`widget styles </displays/widgets/styles>`, rather than
you having to set every setting on every widget.

The following text widget settings may be :doc:`animated </displays/widgets/animation>`: ``x:``, ``y:``, ``font_size:``,
``color:``, ``opacity:``, ``rotation:``, and ``scale:``.

type: text
~~~~~~~~~~

Tells MPF that this is a text widget. This setting is required when using text
widgets.

text:
~~~~~

This value is required. If you don't want text, use ""

Your text can contain placeholders as described in :doc:`dynamic text </displays/widgets/text/text_dynamic>`.

Newline characters (`\\n`) are supported in text values to create multiple lines with line breaks, however
you must surround the text with quotes or the backslash will be treated as a printing character and will
appear in the output.  For example:

.. code-block:: yaml

   text: "Multiple\nlines"

will create multiple text lines with a line break, while the following will not:

.. code-block:: yaml

   text: Multiple\nlines


font_name:
~~~~~~~~~~
The name of the font you want to use. This is the name only, without the file
extension. For example:

Correct:

.. code-block:: yaml

   font_name: arial

Wrong:

.. code-block:: yaml

   font_name: arial.ttf

There's a lot that goes into fonts, so we have a whole section on
:doc:`fonts </displays/widgets/fonts>` which you should read.

Usually fonts are controlled via
:doc:`widget styles </displays/widgets/styles>`. Also, if you're using
a DMD or color DMD (or other pixel-style display), we have some
:doc:`built in DMD fonts </displays/widgets/dmd_fonts>` that you
can use which are pre-configured for DMDs.

bitmap_font:
~~~~~~~~~~~~
A true/false value indicating whether the `font_name:` setting contains the name of a
:doc:`bitmap_font </config/bitmap_fonts>` asset.  When set to `True`, `font_name:` must
refer to an existing bitmap_font asset name and `font_size:` will be ignored. When set to
`False`, `font_name:` should refer to a font name.

font_size:
~~~~~~~~~~

The size of the font (in points). Default is 15.

See the :doc:`full documentation on fonts </displays/widgets/fonts>` for details.

bold:
~~~~~

Boolean (True/False or Yes/No) which controls whether this font is bold. Note
that this setting attempts to over-draw the font a few times to make it look
bold, so the results are often not that great. You're better off finding an
actual bold version of your font and using that font instead.

The default setting is ``False``.

italic:
~~~~~~~

Boolean (True/False or Yes/No) which controls whether this font is italicized.
Note that this setting simply skews the font when it's drawn, so the results are
often not that great. You're better off finding an actual italicized version
of your font and using it instead.

The default setting is ``False``.

casing:
~~~~~~~

A string value that changes the casing of the text on the widget. Available
values are:

* "lower": all characters will be lower case
* "upper": ALL CHARACTERS WILL BE UPPER CASE
* "title": All First Characters Are Capitalized
* "capitalize": Only the first character is capitalized

The default setting is ``None`` and the characters are displayed as-is.

number_grouping:
~~~~~~~~~~~~~~~~

Boolean (True/False or Yes/No) which controls whether you want the separator
between digits. In other words, it converts ``1234567`` into ``1,234,567``.)

Note that this setting will search through the text string for digits and then
insert the commas. In other words, if your text is "YOU SCORED 12345 POINTS",
then it will convert it into "YOU SCORED 12,345 POINTS" even though the text is
a mix-and-match of letters and numbers.

The default setting is ``False``. (Note that prior to MPF 0.30, the default
setting was ``True``.)

.. note::

   Currently this setting only inserts a comma. We need to add a setting to
   allow other characters (like a period which is common in Europe). If this is
   you, post a message to the forum and we'll bump up the priority on our to-do
   list.

min_digits:
~~~~~~~~~~~

Configures the minimum number of digits for the text to be displayed. This
setting adds zeros to the left for digits that are shorter than the setting.

This is typically used in score displays, since pinball machines usually show
a score as ``00`` instead of ``0`` when the player starts the game and has no
points.

So for most machines, you'd add ``min_digits: 2`` to your text widgets which
show the player's score.

The default setting is ``0``.

halign:
~~~~~~~

Specifies the horizontal alignment of the text within the bounding box. Note
that this setting *is not used* to align a widget on the screen. (See the
:doc:`/displays/widgets/positioning` documentation for details on that.)

This setting is almost never used in MPF because the bounding box of a text
widget is automatically created and sized based on the actual text and font
chosen.

The default setting is ``center``.

valign:
~~~~~~~

Specifies the vertical alignment of the text within the bounding box. Note that
this setting *is not used* to align a widget on the screen. (See the
:doc:`/displays/widgets/positioning` documentation for details on that.)

This setting is almost never used in MPF because the bounding box of a text
widget is automatically created and sized based on the actual text and font
chosen.

The default setting is ``middle``.

anchor_y: baseline
~~~~~~~~~~~~~~~~~~

Text widgets have an additional ``baseline`` option in addition to the other baseline
options detailed in the :doc:`common widget settings </displays/widgets/common_settings>`
documentation.

Examples
--------

The example config files section of the documentation contains
:doc:`examples of text widgets </examples/text/index>`.

.. toctree::
   :hidden:
   :titlesonly:

   text_dynamic
   text_strings
