asset_loading_complete
======================

*MPF Event*

Posted when the asset manager has loaded all the assets in
its queue.

Note that this event does *NOT* necessarily mean that all asset
loading is complete. Rather is just means that the asset manager
has loaded everything in its queue.

For example, when the MPF-MC boots, it will load the assets it is
configured to load on start. However, if the MPF MC is started but
MPF is not, then the MPF MC will load its assets and then post this
*asset_loading_complete* event when it's done. Then when MPF is
started and connects, MPF will need to load its own assets, which
means the MPF MC will post more *loading_assets* and then
a final *asset_loading_complete* event a second time for the
MPF-based assets.

*This event does not have any keyword arguments*
