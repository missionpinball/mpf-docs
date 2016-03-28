
The `asset_defaults:` section of your machine config file lets you
configure the default settings for different types of assets based on
what folder those assets are in. Any settings you specify here are
just the defaults, though, and you can still override the defaults for
an individual asset by adding an entry for it to your machine or mode
config file. This sectioncan be used in your machine-wide config
files. This section *cannot* be used in mode-specific config files. An
`asset_defaults:` section of your config file is required for each
type of asset you use, so therefore there is an `asset_defaults:`
section in the system-wide `mpfconfig.yaml` file.Let's take a look at
it to under how the `asset_defaults:` section works:


::

    
    asset_defaults:
        images:
            default:
                load: preload
            screen:
                target: screen
            dmd:
                target: dmd
        animations:
            default:
                load: preload
                target: dmd
            screen:
                load: preload
                target: screen
        sounds:
            default:
                track: sfx
                load: preload
            voice:
                track: voice
                load: preload
            sfx:
                track: sfx
                load: preload
            music:
                track: music
                load: preload
        shows:
            default:
                load: preload
        movies:
            default:
                load: preload


First, notice that `asset_defaults:` has subsections for each
different type of asset that MPF uses: Images, Animations, Sounds,
Shows, and Movies. Then under each specific asset type, there are a
few more subsections. For example, the `Images:` section above
contains the subsections `default:`, `screen:`, and `dmd:`. The
`default:` section represents global default settings for this type of
asset. But any additionalsubsections (for example screen: and dmd: in
the Images: section) hold settings that will apply to a *subfolder
with the name of the section*. The following diagram should make this
clear: ` `_ A few notes on this:


+ Any images in the "screen" folder will have the default settings of
  `target: screen` and `load: preload`, since the default settings would
  be applied first, then the folder-specific settings.
+ Any images in the "attract" folder use the default settings since
  there is no folder-specific entry in the `asset_defaults:` section for
  `attract`.
+ Any images in the root folder (p_roc.dmd, purple_circle.dmd, etc.)
  will also receive the `default:` settings since they are not in one of
  the folders with a name in the config file.


So... what types of settings can you specify in the `asset_defaults:`
section? Any setting that the asset itself supports. (Just look up
`Images`_, `Animations`_, `Sounds`_, Shows, or Videosin the config
file reference to see a list of settings you can apply to an asset.)

.. _Animations: https://missionpinball.com/docs/configuration-file-reference/animations/
.. _Sounds: https://missionpinball.com/docs/configuration-file-reference/sounds/
.. _Images: https://missionpinball.com/docs/configuration-file-reference/images/


