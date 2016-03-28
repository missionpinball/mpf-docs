

+ Sends DMD and Color DMD data to MPF
+ Sends external light show data to MPF
+ Handles multi-language translations
+ Slide builder based on MPF events / BCP triggers
+ All display stuff (slides, elements, transitions, decorations,
  fonts, etc.)
+ Updates text as player vars & machine vars change
+ Sound
+ Tracks which modes are running to start/stop

    + slide_player
    + sounds
    + load / unload assets

+ Tracks which player is active and how many players there are so it
  can update text
+ Captures keyboard keys and sends them to MPF
+ Asset management
+ Tracks game & ball start/stop (does it need to do this?)


Things the MPF MC reads from config files:


+ slide_player
+ sound_player
+ media_controller
+ timing
+ modes
+ displaydefaults
+ fonts
+ textstrings
+ assetdefaults


Classes MC shares with MPF


+ Config
+ CaseInsensitiveDict
+ EventManager
+ Timing
+ Task
+ DelayManager
+ Player
+ AssetManager
+ Util
+ FileManager


Threads


+ main
+ BCP receive
+ BCP send




