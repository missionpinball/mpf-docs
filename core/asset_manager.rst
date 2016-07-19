Asset Manager
=============

The *asset manager* is an MPF core component that's responsible loading and unloading assets. An instance
of the asset manager is created in both the MPF game engine and media controller.

The asset manager is responsible for scheduling assets to be loaded (by the asset loader thread), for unloading assets,
and for scanning the disk to build a list of assets to load and unload. The asset manager also posts events which
track the asset loading progress which you can use to create loading progress screens.