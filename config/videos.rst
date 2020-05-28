videos:
=======

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

.. overview

The ``videos:`` section of your config is where you configure non-default
parameter values for any video assets you want to use in your game. Note: You
do *not* have to have an entry for every
single video you want to use, rather, you only need to add individual assets to
your config file
that have settings which different from other assets in that asset's folder.
(This section is part of the MPF media controller and only available if you're
using MPF-MC for your media controller.)

More information on working with assets is in the :doc:`/assets/index` section
of the documentation.


Each sub-entry in your ``videos:`` section is the name that MPF will use to
refer to that asset. (In other words it's how you specify that asset
in other areas of your config files.) The asset manager works by first
scanning the file system to build up a list of asset files it finds.
Then it looks at the config to see if there are any additional
settings specified for each asset.

For example:

.. code-block:: mpf-config

   videos:
     intro_video:
       width: 100
       height: 70
       file: mpf_video_small.mpg

So in the example above, if
the asset manager found a file called ``mpf_video_small.mpg`` on disk, then
it will also see the ``intro_video`` entry in the config file and know
that those two match. (The "match" is just based on the part of the
file name without the extension, so the settings entry for
``intro_video:`` would match ``mpf_video_small.mpg`` and ``mpf_video_small.m4v``.
In other words, don't name two files with the same name if you want to
keep them straight.)

.. config


Optional settings
-----------------

The following sections are optional in the ``videos:`` section of your config. (If you don't include them, the default will be used).

events_when_played:
~~~~~~~~~~~~~~~~~~~
List of one (or more) events. Those will be posted by the device. Defaults to empty.

A list of one or more names of events that MPF will post when this video is played. Enter the list
in the MPF config list format. These events are posted exactly as they’re entered.

events_when_stopped:
~~~~~~~~~~~~~~~~~~~~
List of one (or more) events. Those will be posted by the device. Defaults to empty.

A list of one or more names of events that MPF will post when this video stops playing. Enter the list
in the MPF config list format. These events are posted exactly as they’re entered.  These events can
be useful to trigger some action when a video has finished playing (like remove a slide).

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

height:
~~~~~~~
Single value, type: ``number`` (can be integer or floating point). Defaults to empty.

The height of this video, in pixels.

load:
~~~~~
Single value, type: ``string``. Default: ``preload``

Videos are always streamed from disk (rather than preloaded into memory), so
this setting has no effect with video assets.

priority:
~~~~~~~~~
Single value, type: ``integer``. Default: ``0``

Loading priority of this asset.

width:
~~~~~~
Single value, type: ``number`` (can be integer or floating point). Defaults to empty.

The width of this video, in pixels.


Related How To guides
---------------------

.. todo:: :doc:`/about/help_us_to_write_it`
