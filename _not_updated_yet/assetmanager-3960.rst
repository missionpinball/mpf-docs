
The *Asset Manager* is responsible for loading and unloading game
assets from disk. It's in the *mpf/system/assets.py* module.


+ In the MPF game engine, the asset manager is used to manage hardware
  shows (lights, LEDs, and drivers).
+ In the MPF media controller, the asset manager is used to manage
  media shows (displays, images, videos, and sounds).


Asset loading is done in a separate thread (called the *Asset
Loader*), so assets can be loaded in the background without slowing
down your game. You can configure assets to be preloaded when MPF
starts, to be loaded when the mode that needs them loads, or to be
loaded on-demand. The exact decision for how each type of asset will
load depends on several factors, like how long the asset takes to
load, how fast your computer is, and how much memory your computer
has.



Tracking the asset manager loading progress with events
-------------------------------------------------------

When MPF first starts up, it loads all the assets configured for
preload from disk. This happens while MPF is starting, and the attract
mode of your machine won't actually begin until the all the assets are
loaded. Since this can take awhile on a complex machine, asset loading
status events have been created which you can use to show a loading
status on the display. As MPF loads its assets, it sends updated (via
`BCP`_) to the media controller which the media controller can use for
the progress update on the display. (Since the media controller has to
load its own assets, it will track the combined progress of both the
MPF and the media controller assets.) Whenever there’s a status update
change (on either side), the media controller will post an event
called *asset_loader* with parameters *total* (total assets that still
need to be loaded), *pc* (number of assets the pinball controller
still needs to load), *mc* (number of assets the media controller
still needs to load), and *percent* (an integer from 0 to 100
representing the percentage complete the loading process is. The
default config file for the media controller ( `mcconfig.yaml`) now
includes the following sections in its `slide_player`:


::

    
    asset_loader:
      type: text
      text: "LOADING: %percent%%"
      font: small
    asset_loading_complete:
    
    waiting_for_client_connection:
      - type: text
        text: WAITING FOR
        font: small
        v_pos: center
        y: -4
        slide: waiting
      - type: text
        text: CLIENT CONNECTION...
        font: small
        v_pos: center
        y: 4


This will create an asset loader screen like this: ` `_ You can
customize this by creating your own `slide_player:` entry for the
*asset_loader* event and doing whatever you want with the *total*,
*pc*, *mc*, and/or *percent* parameters. You might notice that the
complete percentage suddenly drops. 88%, 89%, 91%, 92%, 55%… What?!?
This is because the complete percent is the combined percentage of MPF
and the media controller. So when the media controller first starts,
it will start loading its own assets and that’s the percentage you’ll
see. Then when MPF connects, themedia controller will merge in the
count of its assets, and MPF might have more to load than the media
controller, so the overall percentage goes down. (In the future we can
fix this by having the media controller cache the number of assets MPF
needs to load so the media controller can give an accurate number from
the start.) Once the media controller loads its assets, if it doesn’t
have a connection to MPF, it will post a
*waiting_for_client_connection* event that you can also hook, like
this: ` `_ Also note that there’s an *asset_loading_complete* event
posted when the asset loading process finishes. In the sample config
above, there’s an empty `asset_loading_complete:` section which will
post a blank slide (to clear out the slide with the percentage so it
doesn’t stay at *LOADING: 100%* forever).

.. _BCP: https://missionpinball.com/docs/mpf-core-architecture/system-modules/bcp-system-module/


