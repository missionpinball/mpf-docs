Text Widget
===========

The text widget is used to show text on a slide. Pretty straightforward.

.. image:: /displays/images/text_widget1.jpg

In addition to being able to specify static text, text widgets also include
powerful functionality:

* You can configure dynamic text that is automatically updated (in real time)
  based on the value of a player variable or a machine variable.
* You can configure a placeholder "text string" that uses a lookup value to
  get its actual text. This is useful for things like multi-language support,
  or to be able to have different text strings based on a configuration file
  (family-friendly versus R-rated text, etc.)

Text widget settings
--------------------

::

        type: text
        text:
        font_size:
        font_name:
        bold:
        italic:
        number_grouping:
        min_digits:
        halign:
        valign:
        x:
        y:
        anchor_x:
        anchor_y:
        opacity:
        z:
        animations:
        reset_animations_events:
        color:
        style:
        adjust_top:
        adjust_bottom:
        adjust_left:
        adjust_right:
        expire:
        key:

type: text
~~~~~~~~~~

A text widget

text:
~~~~~

This value is required. If you don't want text, use ""

Link to dynamic text and text strings

font_name:
~~~~~~~~~~
The name of the font you want to use.

There's a lot that goes into fonts, so we have a whole section on
:doc:`fonts </displays/widgets/fonts>` which you should read.

Usually fonts are controlled via
:doc:`widget styles </displays/widgets/styles>`. Also, if you're using
a DMD or color DMD (or other pixel-style display), we have some
:doc:`built in DMD fonts </displays/widgets/dmd_fonts>` that you
can use which are pre-configured for DMDs.

font_size:
~~~~~~~~~~


        text: single|str|
        font_size: single|num|15
        font_name: ignore

bold:
~~~~~

The default setting is ``False``.

italic:
~~~~~~~

The default setting is ``False``.

number_grouping:
~~~~~~~~~~~~~~~~

The default setting is ``True``.

min_digits
~~~~~~~~~~

The default setting is ``1``.

halign
~~~~~~

The default setting is ``center``.

valign
~~~~~~

The default setting is ``middle``.


.. include:: common.rst



.. toctree::
   :hidden:
   :titlesonly:

   text_dynamic
   text_fonts
   text_dmd_fonts
   text_strings
