
Even though you're reading a section called "Assets" in the
configuration file reference, `assets:` is actually not a valid entry.
Instead this documentation explains the generic common settings
acrossindividual types of assets, including:


+ animations
+ images
+ movies
+ shows
+ sounds


Basically all of those things are assets, and so they all have certain
settings in common, so we're explaining the common settings here so we
don't have to waste space by copying-and-pasting this stuff into five
different places. This sectioncan be used in your machine-wide config
files. This sectioncan be used in your mode-specific config files.
Even though these settings apply to any one of the five asset types,
we'll use an image as an example:


::

    
    images:
        insert_coin:
            load: preload
        hello_face:
            file: hello_face_300.jpg
            load: None


First, even though we've mentioned this before, remember that *you do
not have to create an entry in your config file for every asset you
want to use*!



<name>:
~~~~~~~

Each sub-entry in your asset section is the name that MPF will use to
refer to that asset. (In other words it's how you specify that asset
in other areas of your config files.) The asset manager works by first
scanning the file system to build up a list of asset files it finds.
Then it looks at the config to see if there are any additional
settings specified for each asset. So in the images example above, if
the asset manager found a file called `insert_coin.jpg` on disk, then
it will also see the `insert_coin` entry in the config file and know
that those two match. (The "match" is just based on the part of the
file name without the extension, so the settings entry for
`insert_coin:` would match `insert_coin.jpg` and `insert_coin.png`. In
other words, don't name two files with the same name if you want to
keep them straight.)



file:
~~~~~

Sometimes you might want to name a file one thing on disk but refer to
it as another thing in your game and config files. In this case, you
can create an `file:` setting in an asset entry. (Note the file:
`hello_face_300.jpg` setting in the example above, and note that it
includes the file extension.) In this example, you would refer to that
image asset as `hello_face` even though the file is `hello_face_300`.
You might be wondering why this exists? Why not just change the file
name to be whatever you want and/or who cares what the name is? The
reason this function exists is because it allows for the separation of
the actual file on disk from the way it's called in the game. For
example, you could use this to create two sets of assets—one for a
traditional DMD and one for a color DMD—and then you could refer to
the asset by its generic name throughout your configs. (In other
words, you could swap out assets for different physical machine types
without having to update your display code.) That said, we expect that
99% of people won't use this `file:` setting, which is fine.



load:
~~~~~

Specifies when this asset should be loaded. (See the documentation on
`Managing Assets`_ for an explanation of what loading is.) Options for
load: are:


+ `preload` (The asset isloaded when MPF boots and stays in memory as
  long as MPF is running.)
+ `mode_start` (The asset is loaded when the mode starts and is
  unloaded when the mode ends. This option is only valid for asset files
  that are in mode folders, not machine-wide assets.)
+ Anything else (or nothing at all) means that the asset it loaded "on
  demand" when it's first called for. (At this point, assets loaded on
  demand stay in memory forever, but at some point we'll change that so
  they get unloaded on demand too.)


Note that you can configure `load:` options in the `
`assetdefaults:``_ section of your machine config files. It's nice to
be able to override those on an asset-by-asset basis. For example, you
might configure your assets for a mode to all load when the mode
starts, but you could also create a few entries in your config files
with `load: preload` for the assets that are needed for the intro show
of the mode. That way that show can play while the other assets are
loading in the background. (Of course you could also create a
subfolder for the assets that you want to preload and specific an
`assetdefaults:` entry for that folder rather than specifying entries
in your config for specific assets. The choice is up to you.)

.. _Managing Assets: https://missionpinball.com/docs/managing-assets/
.. _assetdefaults:: https://missionpinball.com/docs/configuration-file-reference/assetdefaults/


