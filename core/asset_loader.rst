Asset loader
============

The *asset loader* is a separate thread that runs that physically loads
asset files from disk (images, sounds, show files, etc.). The asset loader thread is running
at all times, even though most of the time it's idle. Assets can be configured to load and/or unload
based on certain events (e.g. on MPF boot, on game start, on mode start, etc.).

* In the MPF game engine, the asset loader is responsible for loading shows.
* In the MPF media controller, the asset loader is responsible for loading images, videos, and sounds.