
You use the `images:` section of your configuration file to specify
additional non-default settings for any images you want to use in your
game. This sectioncan be used in your machine-wide config files. This
sectioncan be used in your mode-specific config files. Note: You do
*not* have to have an entry for every single image you want to use,
rather, you only need to add individual assets to your config file
that have settings which different from other assets in that asset's
folder. (See the ` `assetdefaults:``_ section for details. Also be
sure to read the section on `Managing Assets`_ for an overview of how
assets work.) Here’s a example:


::

    
    images:
        jackpot:
            alpha_color: 0
            target: dmd
        happy_face:
            alpha_color: 15


Since Images are just a type of Asset in MPF, there are a few config
settings that are generic which apply to all types of assets, so read
the `reference documentation on Assets`_ for details about how the
name, `file:`, and `load:` settings work. Then on top of the defaults,
images have two specific settings:



target:
~~~~~~~

Specifies whether the "target" display for this image will be a DMD or
on screen window. This setting tells MPF whether it needs to convert a
full-color image (JPG, PNG, etc.) down to the 16-shade palette for use
on a DMD. Use the value "dmd" here (so, `target: dmd`) when you want
to load a traditional image file (JPG, PNG, BMP, etc.) for use on a
DMD. If you want to load a traditional image and use it on the screen,
you don't need to specify a `target`. You only need to use this
setting when you have traditional image file formats you want to
display on a DMD. If you load a `.dmd` file, MPF assumes it's going to
the DMD.



alpha_color:
~~~~~~~~~~~~

This is a color that will be rendered as transparent, allowing any
display elements at a lower layerto show through. For DMD files, or
for image files that you're targeting for the DMD, this is a shade
value from 0-15.If this is a 24-bit image then you can specify the
color that will be transparent. Alpha and blending functionality will
be expanded in the future with support for RGBA and proper alpha
channels.

.. _Managing Assets: https://missionpinball.com/docs/managing-assets/
.. _assetdefaults:: https://missionpinball.com/docs/configuration-file-reference/assetdefaults/
.. _reference documentation on Assets: https://missionpinball.com/docs/configuration-file-reference/assets/


