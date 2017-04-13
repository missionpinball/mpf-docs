Assets
======

Assets are files that your machine uses that are loaded from disk, such as
show YAML files, images, and sound files. MPF has lots of flexibility for
how assets are loaded and unloaded. (For example, if you're running MPF on a
machine that doesn't have a lot of memory, you may not be able to load all the
assets at startup and may instead have to dynamically load and unload assets
throughout the game.)

MPF also has the ability to automatically "discover" various types of assets
in your machine folder, meaning you don't have to manually type every single
asset file name into your config files. You can even set asset properties
based on what folder and/or subfolder they're in. (For example, audio files
in ``/sounds/fx`` are automatically played on the sound effects track, while
sound files in ``/sounds/voice`` are played on the voice track.

As of MPF 0.33, assets can be in nested subfolders too. For example:

.. code-block::

   \sounds
   \sounds\fx
   \sounds\fx\pops
   \sounds\fx\slings
   \sounds\voice\red
   \sounds\voice\ted
   \sounds\voice\bob

MPF also supports "asset pools" for sound and image assets which allow you
to group multiple asset files into a single asset name that you use in MPF.
This lets you add "variation" to assets during game play. For example, if you
have a laser sound when a pop bumper is hit, you could actually have four
different laser sound files that are each slightly different which you pool
into the "laser" asset which is associate with the pop bumper, and then each
time the pop bumper is hit you get one of the four sounds played at random
instead of the same sound over and over.

.. toctree::
   :maxdepth: 1

   asset_pools
   images
   shows
   sounds
   videos
