
You use the `shows:` section of your configuration file to specify
additional non-default settings for any `show`_you want to use in your
game. (This section can be in your machine configuration files for
machine-wide assets and/or a mode-specific config file for mode-
specific assets.) Note: You do *not* have to have an entry for every
single showyou want to use, rather, you only need to add individual
assets to your config file that have settings which different from
other assets in that asset's folder. (See the ` `AssetDefaults:``_
section for details. Also be sure to read the section on `Managing
Assets`_ for an overview of how assets work.) Here’s a example:


::

    
    shows:
      extra_ball:
        load: preload


Since showsare just a type of Asset in MPF, there are a few config
settings that are generic which apply to all types of assets, so read
the `reference documentation on assets`_ for details about how the
name, `file:`, and `load:` settings work. There are no additional
settings for showsapart from the generic settings that apply to all
types of assets.

.. _Managing Assets: https://missionpinball.com/docs/managing-assets/
.. _show: https://missionpinball.com/docs/shows/
.. _AssetDefaults:: https://missionpinball.com/docs/configuration-file-reference/assetdefaults/
.. _reference documentation on assets: https://missionpinball.com/docs/configuration-file-reference/assets/


