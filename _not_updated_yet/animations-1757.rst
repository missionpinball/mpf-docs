
You use the `animations:` section of your configuration file to
specify additional non-default settings for any animationsyou want to
use in your game. This sectioncan be used in your machine-wide config
files. This sectioncan be used in your mode-specific config files.
Note: You do *not* have to have an entry for every single animationyou
want to use, rather, you only need to add individual assets to your
config file that have settings which different from other assets in
that asset's folder. (See the ` `assetdefaults:``_ section for
details. Also be sure to read the section on `Managing Assets`_ for an
overview of how assets work.) Here’s a example:


::

    
    animations:
      rolling_ball:
        alpha_color: 15


Since Animationsare just a type of Asset in MPF, there are a few
config settings that are generic which apply to all types of assets,
so read the `reference documentation on Assets`_ for details about how
the name, `file:`, and `load:` settings work. Then on top of the
defaults, animationshave onespecific settings:



alpha_color:
~~~~~~~~~~~~

This is a color that will be rendered as transparent, allowing any
display elements at a lower layerto show through. Right now this is a
DMD shade value 0-15. We'll soon add support for per-pixel alpha where
you can build differing degrees of alpha blending into each pixel.

.. _Managing Assets: https://missionpinball.com/docs/managing-assets/
.. _assetdefaults:: https://missionpinball.com/docs/configuration-file-reference/assetdefaults/
.. _reference documentation on Assets: https://missionpinball.com/docs/configuration-file-reference/assets/


