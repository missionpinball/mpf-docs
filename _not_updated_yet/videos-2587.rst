
You use the `videos:` section of your configuration file to specify
additional non-default settings for any videoyou want to use in your
game. This sectioncan be used in your machine-wide config files. This
sectioncanbe used in mode-specific config files. Note:The precompiled
Mac binaries for Pygame do not include the movie module MPF needs to
play videos. Yet another reason we need to move away from Pygame.
Note: A videoin MPF is an MPEG-1 videothat can be displayed in an on
screen window. Typically this is either a background loop or a cut
scene. Videosare similar to Animations in MPF, though animations tend
to be for foreground elements and support alpha transparencies. Note:
You do *not* have to have an entry for every single videoyou want to
use, rather, you only need to add individual assets to your config
file that have settings which different from other assets in that
asset's folder. (See the ` `assetdefaults:``_ section for details.
Also be sure to read the section on `Managing Assets`_ for an overview
of how assets work.) Here’s a example:


::

    
    videos:
      background_fire:
        load: preload


Since videosare just a type of Asset in MPF, there are a few config
settings that are generic which apply to all types of assets, so read
the `reference documentation on Assets`_ for details about how the
name, `file:`, and `load:` settings work. There are no additional
settings for videosapart from the generic settings that apply to all
types of assets.

.. _Managing Assets: https://missionpinball.com/docs/managing-assets/
.. _assetdefaults:: https://missionpinball.com/docs/configuration-file-reference/assetdefaults/
.. _reference documentation on Assets: https://missionpinball.com/docs/configuration-file-reference/assets/


