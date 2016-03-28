
The `fonts:` section of your machine configuration files is where you
map out the names and settings for the fonts your machine uses,
including mapping source fonts and setting antialiasing, size, and
cropping options. This sectioncan be used in your machine-wide config
files. This section *cannot* be used in mode-specific config files.
Note that in addition to this reference,we havea `Step-by-Step
tutorial guide which explains how to set up fonts`_ in MPF. We also
have a `Font Tester tool`_ which comes in handy as you're figuring out
the settings you'll enter into your configuration file here. Example
usage:


::

    
    fonts:
        default:
            file: Quadrit.ttf
            size: 10
            crop_top: 2
            crop_bottom: 5
        space title huge:
            file: DEADJIM.TTF
            size: 29
            antialias: yes
            crop_top: 3
            crop_bottom: 3
        space title:
            file: DEADJIM.TTF
            size: 21
            antialias: yes
            crop_top: 2
            crop_bottom: 3
        medium:
            file: pixelmix.ttf
            size: 8
            crop_top: 1
            crop_bottom: 1
        small:
            file: smallest_pixel-7.ttf
            size: 9
            crop_top: 2
            crop_bottom: 3
        tall title:
           file: big_noodle_titling.ttf
           size: 20


You enter multiple groups of settings, each with its own name. Then
whenever you want to use one of those fonts in your game, you can
simply call it by name. For example, in the configuration file above,
if you ask for something to be rendered to the display with thefont
called "space title", it will use the DEADJIM.TTF font, point size 29,
antialiased, and crop three rows of pixels off the top and 3 rows of
off the bottom. Let's look through each of these settings:



<MPF font name>:
~~~~~~~~~~~~~~~~

The top-level entries in your `fonts:`section are for the font names
that you want to use to refer to the fonts in your game. In the above
example, we have `default`, `space title hug`e, `space title`,
`medium`, etc. You can name these whatever you want. Note that each of
them is only meant to be used for one size since, though you can use
the same font files over and over to create `title_big`,
`title_medium`, `title_small`, etc. If you create an entry for called
`default:`(like we have in the first entry above), then MPF will use
those settings whenever text is rendered without a font being
specified.



size:
~~~~~

The size this font will be rendered at.



file:
~~~~~

The name of the font file that will be used when the game programmer
calls for a font in this size. MPF will first look in the fonts folder
location in the machine's folder, and then it will look in the MPF
system fonts folder.



antialias:
~~~~~~~~~~

Whether this font should be antialiased.



crop_top:
~~~~~~~~~

The number of blank rows that will be removed from above the font
after its rendered.



crop_bottom:
~~~~~~~~~~~~

The number of black rows that will be removed from the bottom of the
font surface after it's rendered.



Alpha blending
~~~~~~~~~~~~~~

In the next few weeks we'll add settings for alpha blends, including
controlling whether the background is opaque or transparent, and, when
antialiasing is used, whether per-pixel alpha blends are used.

.. _Step-by-Step tutorial guide which explains how to set up fonts: https://missionpinball.com/docs/tutorial/how-to-adding-truetype-fonts/
.. _Font Tester tool: https://missionpinball.com/docs/tools/font-tester/


