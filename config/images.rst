images:
=======

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

.. overview

The ``images:`` section of your config is where you configure non-default
parameter values for any image assets you want to use in your game. Note: You
do *not* have to have an entry for every
single image you want to use, rather, you only need to add individual assets to
your config file
that have settings which different from other assets in that asset's folder.
(This section is part of the MPF media controller and only available if you're
using MPF-MC for your media controller.)

More information on working with assets is in the :doc:`/assets/index` section
of the documentation.

Each sub-entry in your ``image:`` section is the name that MPF will use to
refer to that asset. (In other words it's how you specify that asset
in other areas of your config files.) The asset manager works by first
scanning the file system to build up a list of asset files it finds.
Then it looks at the config to see if there are any additional
settings specified for each asset.

For example:

.. code-block:: mpf-config

    images:
      insert_coin:
        load: preload
      hello_face:
        file: hello_face_300.jpg
        load: None

So in the example above, if
the asset manager found a file called ``insert_coin.jpg`` on disk, then
it will also see the ``insert_coin`` entry in the config file and know
that those two match. (The "match" is just based on the part of the
file name without the extension, so the settings entry for
``insert_coin:`` would match ``insert_coin.jpg`` and ``insert_coin.png``. In
other words, don't name two files with the same name if you want to
keep them straight.)

.. config


Optional settings
-----------------

The following sections are optional in the ``images:`` section of your config. (If you don't include them, the default will be used).

file:
~~~~~
Single value, type: ``string``. Defaults to empty.

Sometimes you might want to name a file one thing on disk but refer to
it as another thing in your game and config files. In this case, you
can create an ``file:`` setting in an asset entry. (Note the file:
``hello_face_300.jpg`` setting in the example above, and note that it
includes the file extension.) In this example, you would refer to that
image asset as ``hello_face`` even though the file is ``hello_face_300``.

You might be wondering why this exists? Why not just change the file
name to be whatever you want and/or who cares what the name is? The
reason this function exists is because it allows for the separation of
the actual file on disk from the way it's called in the game.
For example, you could use this to create two sets of assets—one for a
traditional DMD and one for a color DMD—and then you could refer to
the asset by its generic name throughout your configs. (In other
words, you could swap out assets for different physical machine types
without having to update your display code.) That said, we expect that
99% of people won't use this ``file:`` setting, which is fine.

load:
~~~~~
Single value, type: ``string``. Defaults to empty.

Specifies when this asset should be loaded. (See the
:doc:`/assets/index` documentation for an explanation on loading.)

+ `preload` (The asset is loaded when MPF boots and stays in memory as
  long as MPF is running.)
+ `mode_start` (The asset is loaded when the mode starts and is
  unloaded when the mode ends. This option is only valid for asset files
  that are in mode folders, not machine-wide assets.)
+ Anything else (or nothing at all) means that the asset it loaded "on
  demand" when it's first called for. (At this point, assets loaded on
  demand stay in memory forever, but at some point we'll change that so
  they get unloaded on demand too.)

Note that you can configure ``load:`` options in the
:doc:`/config/assets` section of your config files. It's nice to
be able to override those on an asset-by-asset basis. For example, you
might configure your assets for a mode to all load when the mode
starts, but you could also create a few entries in your config files
with ``load: preload`` for the assets that are needed for the intro show
of the mode. That way that show can play while the other assets are
loading in the background. (Of course you could also create a
subfolder for the assets that you want to preload and specific an
``assets:`` entry for that folder rather than specifying entries
in your config for specific assets. The choice is up to you.)


Related How To guides
---------------------

* :doc:`/displays/widgets/image/index`
