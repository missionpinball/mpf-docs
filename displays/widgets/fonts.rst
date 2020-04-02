Working with Fonts
==================

You can specify which font you want to use as a property of any of the widgets that contain text.
You can use system-wide fonts that are installed on the computer running MPF as well as fonts that
are in your machine's ``/fonts`` folder.

You specify fonts by name only (not including the extension), and MPF will first look in your
machine's fonts folder, and if it doesn't find the font there, it will look in the MPF-MC's
built-in fonts folder, and finally in your machine's system fonts location.

.. note::

   The MPC MC contains a few pixel-based for use on DMDs. See :doc:`dmd_fonts` for details.

For consistency of appearance across computers, we highly recommend that you put the
fonts you want to use in your machine's fonts folder.

Specifying which font a particular widget uses is done via that widget's ``font_name:``
setting, so see either the :doc:`text/index` or :doc:`text_input/index` reference for
details.

Keep in mind that all widget properties, including fonts, can be configured as part of a
widget style and easily applied to new widgets with a single line.

.. toctree::
   :hidden:

   dmd_fonts


How to Set Fonts and Sizes Globally?
------------------------------------

You usually want to use three to five different font + size combinations in
your machine.
However, you often want to adjust them later on without touching all your
slides and widgets.
For that reason it makes sense to define a :doc:`widget_style <styles>` for all
your fonts and sizes:

.. code-block:: mpf-mc-config

   widget_styles:
     text_small:
       font_size: 15
       color: red
     text_default:
       font_size: 21
       color: blue

You can then use ``style: text_default`` in your text widgets.
See :doc:`widget_style <styles>` for details.
