bitmap_fonts:
=============

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

.. overview

The ``bitmap_fonts:`` section of your config is where you configure non-default parameter values
for any bitmap font assets you want to use in your game. Note: You do *not* have to have an entry
for every single bitmap font you want to use, rather, you only need to add individual assets to
your config file that have settings which differ from the default values. (This section is part
of the MPF media controller and only available if you're using MPF-MC for your media controller.)

A bitmap font is one that stores each glyph (character) as an array of pixels (that is, a bitmap).
It is less commonly known as a raster font. Bitmap fonts are simply collections of raster images
of glyphs. For each variant of the font, there is a complete set of glyph images, with each set
containing an image for each character. For example, if a font has three sizes, and any combination
of bold and italic, then there must be 12 complete sets of images.

MPF-MC currently supports Portable Network Graphics (.png), Graphic Interchange Format (.gif),
and bitmap (.bmp) image files for bitmap fonts.  In order for MPF to use the bitmap font, a font
descriptor must be present. This contains the information necessary to locate each glyph
(character) in the bitmap image and other associated information. The font descriptor information
may be loaded from a file or provided in the asset settings (
`font descriptor file format <http://www.angelcode.com/products/bmfont/doc/file_format.html>`_).
MPF supports both .xml, .fnt, and .txt files for font descriptor files (binary files are not
currently supported).

There is a great online tool for generating bitmap fonts (and the associated font descriptor file)
from True Type Fonts: `http://kvazars.com/littera/ <http://kvazars.com/littera/>`_

Here's an example:

.. code-block:: mpf-config

  bitmap_fonts:
    F1fuv:
      file: F1fuv.png
      descriptor: [' !"#$%&,()*+`-./', '0123456789:;<=>?', '@ABCDEFGHIJKLMNO', 'PQRSTUVWXYZ[\]^_', '''abcdefghijklmno', 'pqrstuvwxyz{|}~ ']
    example_font:
      file: example_font.png
      descriptor: example_font_descriptor.xml

.. config


Optional settings
-----------------

The following sections are optional in the ``bitmap_fonts:`` section of your config. (If you don't include them, the default will be used).

descriptor:
~~~~~~~~~~~
Unknown type. See description below.

Here is an example of a descriptor list for a bitmap image that contains three rows of 15 characters and the
specific characters mapped to each position in each row:

.. code-block:: yaml

  descriptor: [ 'abcdefghijklmno', 'pqrstuvwxyz 012', '3456789,.:=<>-+' ]

Remember the descriptor list only works for monospaced characters (characters that are all the same width and
height).

file:
~~~~~
Single value, type: ``string``. Defaults to empty.

The file to load when using this bitmap font.

load:
~~~~~
Single value, type: ``string``. Defaults to empty.

When should the asset loader load this file?
One out of ``mode_start``, ``on_demand`` or ``preload``.


Related How To guides
---------------------

* :doc:`/assets/bitmap_fonts`
