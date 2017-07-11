MPF Version History
===================
Here's the history of the various release versions and changes of the Mission
Pinball Framework. (Patch releases and bug fixes are not included in this list.)

0.50
----

Currently in Dev, plan in time for Chicago Pinball Expo October 2017

.. rubric:: MPF

New Features

* TBD

.. rubric:: MPF-MC

New Features

* TBD

0.33
----

April 10, 2017

.. rubric:: MPF

New Features

* "Ball hold" device (Temporarily hold a ball while something else is happening)
* "Multiball lock" device (Track ball locks towards multiball, including virtual
  locks, across balls and players)
* Multiball "add a ball" feature
* Added support for Stern SPIKE platform
* :doc:`Revamped logging </config/logging>`
* Additional achievements control events
* BCP ports & interfaces are now configurable
* Drop target "keep up" feature (PWMs reset coil to "lock" target up)
* "Async" events (Events that wait for all handlers to finish before continuing)
* Additional multiball events
* More functions for people building games to use to write tests
* Built-in modes with code can have their code overloaded
* Added score reels to the smart virtual platform
* Allow machine variables to be set via BCP
* Allow setting default high scores
* Add "early save" events to ball saves
* Add all monitorable device properties to conditional events
* Use placeholders in mode timer start & end values
* More options for bonus (hurry ups, skip slides with 0 value, placeholders for score calculations, etc.)
* Improved ball search
* OPP - support for firmware 2.0 and dual wound coils
* MC scriptlets for video modes and code on the MC side
* Support for conditional events
* Template variables which are evaluated during runtime and can use
  placeholders (timers, logic_blocks, tilt, scoring, bonus_mode, and more)
* Early ball save
* Advanced bonus_mode
* TimedSwitch device - built-in event for flipper cradling and releasing
* Asynchronous logging - This is especially important on windows because
  logging previously slowed down the game. However, also important in production
  when under high I/O load or with slow discs.
* Timers work outside of the game now
* New "mpf diagnosis" command
* Scoring to machine variables
* Scoring for other players
* Weights in random_event_player
* Unlimited delay in ball_save to allow video modes or mode selection
* Added Machine vars for all kinds of versions
* Drop Target keep up support
* Multiball add a ball support
* New multiball_lock device which handles virtual saves for multiplayer game
* Allow BCP to bind on all IPs


Bug fixes & code improvements

* A lot of miscellaneous bug fixes
* Exiting service mode always put the machine back on free play
* Fixed a ball lock crash
* File loader will not try to load temp files
* Manual plunger in smart virtual platform now works properly
* Refactored ball devices to allow for different types of ball counters & be more robust for
  unexpected ball situations and different types of eject failures
* Made achievements and achievement groups smarter and more robust (also backported to 0.32)
* Improved log messages for BCP encoding errors
* "Hz" setting is gone (since MPF is now tickless)
* Active eject process trackers are canceled on shutdown
* Randomizer now works with a single element
* Fixed a bunch of small things that caused crashes
* Changed default on-screen DMD pixel settings
* Removed OSC plug-in since it hasn't worked in over a year and no one uses it
* Better errors on invalid configs
* Catching a lot more config problems
* Improved ball search. Drop Target reset no longer resets ball search
* Better start/stop procedures for modes. no more event races
* Improved extra ball
* Better yaml parsing for unescaped strings
* Performance improvements through better fast paths and offloading of logging
  from the synchronous path
* BCP version 1.1 with synchronisation during reset
* Improved handling of ball devices with entrance_switch
* Force UTF-8 for configs on windows
* Better errors when loading assets


.. rubric:: MPF-MC

New Features

* Added a camera widget (live video)
* Allow placeholders and settings
* Added keyboard debugging
* Added warnings if window size & display size aspect ratios are not the same
* MPF-MC now checks to make sure the MPF version it's talking to is compatible
* Change the default display size to 800x600 if a displays: section is not in the config
* Re-vamped Mac installation procedure. It's now a "real" install and does not use
  MPF.app anymore.
* Added a "volume" machine variable
* Added Interactive Media Controller (iMC)
* Added "anchor_y: baseline" option for text widgets
* Added gamma setting for physical DMDs
* Added new relative animation target values


Bug fixes & code improvements

* Improved sound asset loading speed (uses SDL_Mixer for loading to memory rather than GStreamer)
* Sound assets can be loaded while videos are playing
* Sound assets can be located in sub-folders as many levels deep as desired (not just a single
  level)
* Fixed points widget
* Improvements to automated testing on Travis
* widget_player positioning fixed
* Better error messages for malformed slide configs
* Prevent crash in text widget when empty and back is selected
* Changes to support BCP 1.1


0.32
----

Dec 1, 2016

.. rubric:: MPF

* Improved :doc:`achievements </game_logic/achievements/index>` and added
  :doc:`achievement groups </game_logic/achievements/achievement_groups>`.
* Added relay events and relay queues
* Improved :doc:`smart virtual platform </hardware/virtual/smart_virtual>`
* Improved support for :doc:`System 11 </mechs/troughs/two_coil_multiple_switches>`
  and :doc:`Gottlieb System 3 style </mechs/troughs/two_coil_one_switch>`
  troughs (including using the ball drain as a ball storage location to get one
  additional ball capacity with no hardware changes).
* Verify that duplicate sections don't exist in config files
* Check that event handlers are properly formatted before they're registered
* Added conditional events (handlers that only fire if certain conditions are
  met)
* You can :doc:`set starting values for player variables </config/player_vars>`
* Fixed the :doc:`physical mono DMD </displays/display/mono_dmd>` and
  :doc:`physical RGB (color) DMD </displays/display/rgb_dmd>`
* Added :doc:`multiball lost event </events/multiball_name_lost_ball>`
* Allow devices to have inline config specs
* Added shots with events
* Better OPP platform parsing
* Fixed & improved the high score mode
* Improved service mode
* Added options for "random" events (force next, force all, save per-player, etc.)
* Added events to the BCP monitor (meaning they can be viewed in the MPF Monitor app)
* Added ``-f`` command line option to force all assets to load on boot for testing purposes
* Added :doc:`scoring </config/scoring>` options (add, replace, block)
* Use color "on" for LED default colors
* Allow multiple config player entries to fire from the same event
* Ensure that events created by the MC are sent to MPF
* Added machine vars for P-ROC and FAST hardware revisions
* Added :doc:`combo switches </game_logic/combo_switches/index>` (for "flipper cancel", two-button skill shots, etc.)
* Lots of little bug fixes...

.. rubric:: MPF-MC

* Fixed the widget z-order layering bug (this has been backported to 0.31).
  Widget orders are now higher value z: settings are on top of lower value ones.
* Negative z: values are no longer used to target parent slide frames. Instead,
  ``target: (name)`` is used.
* Cleaned up debug logging so BCP frames are not included in it by default
* Events that are natively posted in the MC are now sent to MPF
* Fixed a bug to ensure that the slide_active event is only posted once per frame
* Fixed a bug that prevented slide frames from being animated
* Fixed a bug where videos were not stopping
* Allow the same slide to be used on multiple displays
* Switch to GStreamer instead of SDL_Mixer for loading and streaming sounds. (SDL2 still used for all sound output.)
* Sound file streaming is now supported from any track (streamed from disk instead of preloaded into memory)
* New "track_player" config controls sounds at the track-level (fade, volume, play, pause, stop, etc.)
* Custom loading & unloading events at the individual sound level.
* Lots of little bug fixes...

0.31
----

Sept 19, 2016

.. rubric:: MPF

* MPF is now "tickless", meaning everything runs faster, but with less overhead
* Improved flow control for FAST hardware serial communication
* Improved BCP communications
* Improved serial communications for all devices which use serial
* Additional options for ball saves
* Removed many threads which makes everything simpler and faster under the hood
* Improved "virtual" and "smart virtual" platforms
* Prevent broken data files from crashing MPF
* Added a basic service mode (this is just a start, much more to come)
* Detect balls that jump between playfields
* Prevent duplicate rules being written to P-ROC and P3-ROC controllers
* Allow mode config files to be broken into multiple files
* Allow multiple multiball modes to run at once and add options for how it tracks them
* Allow ball locks to wait for a ball to drain before releasing their locked balls
* Added the ability to use matrix lamps/LEDs at individual channels for RGB LEDs
* Re-added high score mode (Which was in 0.21 and removed in 0.30)
* OPP platform improvements
* Improved error messages for config file errors
* Improved the way the "mpf both" command works on all platforms
* Added ability to step backwards in shows
* Refactored and improved show player
* Added ball search for servos
* Added default colors to RGB LEDs
* Added support for nested shows
* Added the "LED Group" device (am easily-configured strip of LEDs which can be strobed, pulsed, etc.)
* Added kickback mechanisms
* Added magnets
* Added blocking show queues
* Many bug fixes...

.. rubric:: MPF-MC

* Audio library improvements (sound fading, markers, start position, instance limiting,
  ducking improvements)
* Allow widget events based on when slides are shown, hidden, etc.
* Improved error if you try to target a widget to an invalid slide
* Added default DMD fonts
* Many bug fixes...

0.30
----

July 15, 2016

* Python 3 required
* Mac OS X support
* The Media Controller is now a separate package from MPF
* The MPF-MC has been completely rewritten from scratch (based on Kivy, SDL2,
  OpenGL, and Gstreamer)
* GPU is used for graphics
* Brand-new audio interface specifically written for pinball audio, which
  includes advanced feature like ducking, attack, attenuation, etc.
* Proper Python package installers, and inclusion in PyPI so install can be done
  via *pip*.
* System-wide *mpf* launcher utility with pluggable commands
* New MPF clock module replaces the old timing and timers
* All shows are driven by MPF
* Show content is "played" by the standard config_players
* Playlists become shows
* "Tocks" are gone, shows now operate on real-world time
* Light scripts are gone, replaced by placeholder "tokens" in shows
* Named colors
* Hardware accelerated LED fades
* Asset Pools
* Ball Search
* Accelerometer-based tilts
* Servo support
* Text string support
* Player achievements

0.21
----

Dec 1, 2015

* SmartMatrix "real" RGB LED Color DMD support.
* System 11 support.
* High Score mode.
* Credits mode.
* Tilt mode.
* Smart virtual platform. (This is the new default platform.)
* New display elements: Character Picker and Entered Characters.
* Devices can be created and changed per mode.
* Machine variables.
* Untracked player variables.
* Central config processor, data manager, file manager, and file
  interfaces. This paves the way for config files in formats other than
  YAML.
* Added support for combo manual/auto plungers.
* Events for ball collection process.
* Driver-enabled devices.
* External light shows, controllable via BCP. (Thanks Quinn Capen!)
* Created a starter game machine config template you can use for your
  own machines.
* Started adding unit tests. (We're at the very beginning of this, but
  we have full coverage of the ball device, the event manager, and the
  tutorial configuration files.)
* Rewritten driver/coil device interface.
* Rewritten ball device and ball controller code. (Thanks Jan
  Kantert!)
* Rewritten score controller.
* Rewritten display & slides modules.
* Many improvements and features added to ball saves.
* Python 2.7 is now required. (Previous releases would also run on
  Python 2.6)
* Logic blocks can now persist between balls
* Fixed & enhanced the asset loading process.
* Many improvements and features added to modes and the mode
  controller
* Multiple config files can be chained together at the command line
* Improved text display element.
* Improved event manager and event dispatch queue
* Moved all utility functions to their own class.

0.20
----

Sept 14, 2015

* The *targets* and *shots* modules have been combined into a single
  module called *shots*.
* The new shots module adds several new features, including:

  * Shots can be members of more than one shot group, and added and
    removed dynamically.
  * Sequence shots can track more than one simultaneous sequences. (e.g.
    two balls going into an orbit at essentially the same time will now
    count as two shots made.)
  * Shots are mode-aware and will automatically enable or disable
    themselves based on modes starting and stopping.

* Modes now work outside of a game.

  * “Machine modes” have been removed. Attract and game machine modes
    are now regular modes.
  * This makes it easier to have always-running modes (volume control,
    coin door open, coin & credit tracking).
  * This makes it possible to configure custom branching of mode-flow
    logic. (i.e. long-press the start button to load a different game
    mode, etc.)

* Significant performance improvements for both starting MPF and
  starting a game:

  * Reading the initial states of switches on a P-ROC is significantly
    faster.
  * The auditor now waits a few seconds before writing its audit file,
    and it does it as a separate thread. Previously this was slowing down
    the game start and player rotation events.
  * The way modules that need to track “all” the switches (like the
    auditor and OSC) was changed and now it doesn’t bog things down.

* A device manager now manages all devices. (This will enable future
  GUI apps to easily be able to browse the device tree.)
* Devices can be “hot added” and removed while MPF is running. This
  includes automatic support to add and remove devices per mode.
* All device configuration is specified and validated via a central
  configuration service. This has several advantages:

  * The config files are now validated as they’re loaded. For example,
    if there a device has a settings entry for “switches”, MPF will now
    validate that the strings you enter in the are actual switch names. It
    will give you a smart error if not.
  * This paves the way for supporting config files in formats other than
    YAML. (JSON, XML, INI, etc.)
  * This led to the removal of about 500 lines of code since all the
    config processing was done manually in each module before.
  * The config processing is more efficient and less-error prone since
    it’s not written from scratch for each module.
  * There’s now a master list (in `mpfconfig.yaml`) of all config
    settings for all device types.
  * The config processor and validator can run as a service to support
    the back-end business logic behind future GUI tools which could be
    used to build machines.
  * If you’re configuration has an unrecognized setting, the config
    validator will load the config file migrator to tell you what the
    updated name is for the section it doesn’t recognized.

* Shot rotation has been improved:

  * You can now specify the states of shots you’d like to include or
    exclude. (i.e. only rotate between incomplete shots.)
  * You can specify custom rotation patterns (i.e. a “sweep” back-and-
    forth instead of a simple left or right rotation)

* A ball lock device was added to make it easy to specify ball locks.
* A multiball device was added.
* A simple ball save device was added.
* Created a “random_event_player” that lets you trigger random events
  based on another event being posted.
* Centralized debugging
* Drop targets and drop target banks have been simplified and
  separated from shots.
* The states of switches tagged with ‘player’ will be passed to the
  game start mode, allowing branching based on which combinations of
  switches were held in when the start button was pressed. (The amount
  of time the start button was held in for is also sent.)
* Official support for multiple playfields via config files
* Added x, y, and z positions to lights and leds
* Exposed wait queue events to mode configs, allowing code-less
  creation of modes that can hook into game flow (bonus, etc.)

0.19
----

August 6, 2015

* Completely rewritten target and drop target device module,
  including:

  * Per-player state tracking for targets
  * Target “profiles” that control how targets behave, completely
    integrated with the mode system

* Light show “sync_ms” which allows new light shows to sync up with
  existing running shows.
* Timed switch events can be set up via the config files.
* Added “recycle_time” to switches. (Switches can be configured to not
  report multiple events until a cool-down time has passed.)
* Created an events_player module
* Player variables in slides automatically update themselves when they
  change. (No more need to find an event to tie the slide to in order
  for it to update!)
* Device control events exposed via the config files
* Automatic control of GI
* Activation and deactivation events can be automatically created for
  every switch.
* Allow multiple playfield objects to be created at once (for head-to-
  head pinball)
* Added support for FAST Pinball’s new WPC controller
* Added a Linuxshell script to launch mc.py and mpf.py
* Created the config file migration tool
* Added per-timer debug loggers
* Standardization of many non-standard config file naming conventions
* Color logging to LEDs
* Added P3-ROC switch test tool
* Added reset to mode timer action list
* Added restart feature to mode timers
* Flipper Device: Add debug logging to rules
* FAST:Added minimum firmware version checking for IO boards
* Added “restart” method to logic blocks
* Text display element min_digits
* Allow system modules to be replaced and subclassed
* Added configurable event names for switch tag events
* Added callback kwargs to switch handlers
* Added light and LED reset on machine mode start
* Added default machine and mode delay managers

0.18
----

June 2, 2015

* FadeCandy and Open Pixel Control (OPC) support. This means you can
  use a FadeCandy or other OPC devices to control the LEDs in your
  machine.
* Rewritten FAST platform interface. It’s now “driverless,” meaning
  you no longer need to download and compile drivers to make it work.
* Added support to allow multiple hardware platforms to be used at
  once. (e.g. LEDs can be from a FadeCandy while coils are from a
  P-ROC.) You can even use multiple different platform interfaces for
  the same types of devices at once (e.g. some LEDs are FadeCandy and
  others are FAST).
* Added support for GI and flashers to light shows
* Added activation and deactivation events to switches
* Added support for sounds in media shows
* Added per-sound volume control
* Added support for P-ROC / P3-ROC non-debounced switches
* Exceptions and bugs that causeMPF to crash are now captured in the
  log file. (This will be great for troubleshooting since you can just
  send your log. No more needing to capture a screenshot of the crash.)
* If a child thread crashes, MPF will also crash. (Previously child
  threads were crashing but people didn’t know it, so things were
  breaking but it was hard to tell why.)
* MPF can now be used without switches or coils defined. (Makes
  getting started even easier.)
* “Preload” assets loading process is tracked as MPF boots, allowing
  display to show a countdown of the asset loading process
* Added *restart_on_complete* to mode timers
* Smarter handling of player-controlled eject requests while existing
  eject requests are in progress
* *eject_all()* returns *True* if it was able to eject any balls
* Playfield “add ball” requests are queued if there’s a current player
  eject request in progress
* Created a smarter asset loading process
* The attract mode start is held until all the “preload” assets are
  loaded
* Updated how the game controller tracks balls in play

0.17
----

May 4, 2015

* Broke MPF into two pieces: The MPF core engine and the MPF media
  player
* Added support for the Backbox Control Protocol (BCP)
* Added device-specific debugging for LEDs.
* Added version control to config files.
* Added volume control.
* Switches that you want to start active when using virtual hardware
  are now added to the `virtual platform start active switches:` section
  instead of being a property of the `keyboard:` entry.
* Converted several former plugins to system modules, including shots,
  scoring, bcp, and logic blocks.
* General performance improvements. (Running MPF on my machine used to
  take about 50% CPU. Now it’s down to 15%.)

0.16
----

April 9, 2015

* Added slide "expire" time settings to the Slide Player.
* Added *Demo Man* as the sample game code.
* Added start_time configuration parameter for music in the
  StreamTrack
* Added the SocketEvents plugin
* Created the LightScripts and LightPlayer functionality.
* Change light script "time" to "tocks"
* Created a centralized config processing module

0.15
----

March 9, 2015

* Added support for game modes.
* Converted several existing modules to be mode-specific, including:

  * LogicBlocks
  * SoundPlayer
  * SlidePlayer
  * ShowPlayer
  * Scoring
  * Shots

* Created an Asset Manager and converted the images, animations,
  sound, and show modules to use it instead of each handling their own
  assets.
* Created an asset loader which creates a background thread to load
  each type of asset.
* Added an AssetDefaults section to the asset loader to specify per-
  folder asset settings
* Created a universal player variable system
* Added movie support (for playing MPEG videos on the LCD and DMD).
  They're available as a standard display element type which means they
  can be positioned, layered as backgrounds, etc.
* Created a generic ModeTimers class that can be used for timed modes
  and goals. (With variable count rates, support for counting up and
  down, multiple actions which can start, stop, pause, and add time,
  etc.)
* Changed logic blocks so they maintain all their states and progress
  on a per-user basis.
* Added a "double zero" text filter. (Used to show zero-value scores
  as "00" instead of "0".)
* Updated the display code so that it doesn't show a slide until all
  that slides assets have been loaded.
* Renamed the "sphinx" folder to "docs".
* Broke the three phases of machine initialization into 5 phases.
* Created the mode timer
* Renamed the "HitCounter" logic block to "Counter" and updated it to
  be more flexible so it can track general player-specific counts (both
  up and down), for example, total shots made, combos, progress towards
  goals, etc.
* Changed window section of config so it uses the slide builder.
* Added the ability to control lights and LEDs by tag name in shows.
* Modified the switch controller so events from undefined switches
  simply log a warning rather than raises an exception and halting MPF.

0.14
----

February 9, 2015

* Completely rewritten ball controller.
* Completely rewritten ball device code.
* Major updates to the diverter device code.
* Creation of a new playfield module that's responsible for managing
  the playfield and any balls loose on it.
* Completely rewrote the "player eject" logic. (This is what happens
  when the game needs to wait for the player to push a button to eject a
  ball from a device.)
* The ball search code was moved from the game controller to the
  playfield device module.
* Different types of events were broken out into their own methods.
  For example, to post a boolean event, instead of calling
  `event.post(type='boolean')`, you now use `event.post_boolean()`.
  There are similar new methods for other event types, like
  `post_relay()` and `post_queue()`.
* Added a debug option for ball devices which enables extra debug
  logging for problem devices.
* Tilt status was removed from the machine controller. (It was
  inappropriate there. Tilt is a game-specific thing, not a machine-
  specific thing.)
* Virtual Platform: default NC switch states fixed

0.13
----

January 16, 2015

* Major update to the sound system, including:

  * Support for multiple sound tracks ("voice", "sfx", "music", etc.),
    each with their own channels, settings, volume, etc.
  * Using background threads to automatically load sound files from disk
    in the background without slowing down the main game loop.
  * Support for streaming sounds from disk versus preloading the entire
    sounds in memory.
  * Support for sound priorities and queues, so sounds can pre-empt
    other sounds if they have a higher priority.
  * System-wide volume control with settable steps.

* Support for the v1.0 update of FAST Pinball's libfastpinball
  library. (Basically we updated the FAST platform interface to support
  their latest firmware and drivers)
* Support for flashers. (Previously flashers were just driven like any
  other driver. Now they are their own device with their own flasher-
  specific settings.)
* Game Controller: Changed the player rotate routine to be driven from
  the game_started event so the player object isn't actually set up
  until the game has finished being set up.
* Pygame: Moved the Pygame event loop to the machine controller and
  out of the window manager. This lets us use Pygame events even if we
  don't have an on screen window. (This is needed for the sound system.)
* Display: Moved the SlideBuilder instantiation earlier in the boot
  process so it's available to other modules who want to use it when
  they're starting up. This will let us get the "loading" screen up
  earlier in the boot process.
* Switch Controller: Added a method to dump the initial active states
  of switches to the log. This is needed for our automated log playback
  utility so it can set the initial switches properly.
* Ball Devices: fixed a typo on the cancel ball request event

0.12
----

December 31, 2014

* Added full display and DMD support, with support for physical DMDs,
  on screen virtual DMDs, color DMDs, and high res LCD displays.
* Added transitions which flip between display slides with cool
  effects.
* Added decorators which are used to "decorate" display elements (make
  them blink, etc.)
* Added display support to shows so that shows can now combine display
  and lighting effects
* Added a Slide Builder which can assemble slides from text, image,
  animation, and shapes from shows and the config files.
* Added a SlidePlayer config setting which can show slides based on
  MPF events
* Modified the Virtual DMD display element so that it can render on
  screen DMDs that look more like real pixelated DMDs
* Added a font manager that lets you define font names and specify
  default settings (sizes, antialias, color, etc.)
* Added TrueType font support
* Added support for stand image types to be displayed on the DMD
* Added .dmd file type support for images and animations
* Addedthe OSC Sender tool
* Added the Font Tester tool
* Added the multi-language module which can replace text strings with
  alternate versions for multi-language environments and other (e.g.
  "family-friendly") text replacements
* Improved the diverter devices so they have knowledge of what ball
  devices and diverters are upstream and downstream, allowing them to
  automatically activate and deactivate based on where balls need to go.
* Improved the ball device class so ball devices are smarter about how
  they interact with target devices. (e.g. a ball device will
  automatically eject a ball if its target device wants a ball.)
* Added support for the P3-ROC
* Added many more events
* Modified displays so they can each have independent refresh rates

0.11
----

December 1, 2014

* Created a Display Controller module which is responsible for
  handling all interactions with all types of displays, including DMD,
  LCD, alphanumeric, 7-segment, etc.
* Created a DMD display module which controls both physical DMDs as
  well as on screen representations of physical DMDs
* Created a Window Manager, a centralized module which manages the on
  screen window, including full screen and resizable support
* P-ROC platform interface: Built the DMD control code
* FAST platform interface: Built the DMD control code
* Switched from Pyglet to Pygame
* Created a Sound Controller
* Created a Game Sounds plug-in that lets you control which sounds are
  played and looped based on MPF events
* Added PD-LED support
* Added support for P3-ROC SW-16 switch boards
* Switch Controller: Added verify_switches() method which verifies
  that switches are in the hardware state that MPF expects.
* Switch Controller: Adding logging so it can track when duplicate
  switch events were received
* LEDs: added on() and off() methods and "default color" support
* Ball Device: created _ball_added_to_feeder() and made it so the
  device watches for a ball entering and will request it if it needs it.
* Changed the command line options so you don't have to specify the
  .yaml extension for your configuration file
* Changed the command line options so you (optionally) don't have to
  specify the "machine_files" folder location
* Created default machine_files folder location settings in the config
  file
* Added support for absolute or relative paths in the command line
  options
* Added support for X/Y coordinates to LEDs and Lights for future
  light show mapping awesomeness.
* Created an early, early version of the Playfield Lights display
  interface which lets you "play" Pygame shows on your playfield lights
* Added system default font support
* Added a player number parameter to the player_add_success event
* Added a default MPF background image for the on screen window
* Added many more default settings to the system default
  mpfconfig.yaml file
* Virtual platform interface: Updated it so that it works when
  hardware DMDs are specified in the config files

0.10
----

October 25, 2014

* Added enable_events, disable_events, and reset_events to devices.
* Removed the First Flips plug-in. (Since the thing above replaces it)
* Added support for network switches and drivers for FAST Pinball
  controllers.
* Added support for multiple USB connections to FAST Pinball
  controllers to separate main controller traffic from RGB LED traffic.
* Changed default debounce on and off times to 20ms for FAST Pinball
  controllers.
* Individual targets hit in target groups will now post events
* Changed the default show priority to 1 so it will restore lights
  that weren’t set with a priority by default
* Driver: Added a power parameter to driver.pulse()
* Score Reel: Added resync events to individual reels
* Score Reel: Changed repeat_pulse_ms config setting to
  repeat_pulse_time.
* Score Reel: Changed hw_confirm_ms config setting to hw_confirm_time.
* Changed default pulse time for all coils to 10ms
* Coils: (Fast): Added separate debounce_on and debounce_off settings
* Info Lights: Forced game_over light to off when game starts
* LEDs: Added force parameter to the off() method

0.9
---

October 7, 2014

* Added a “Logic Blocks” plug-in which lets game programmers build
  flowchart-like game logic with the config files. No Python programming
  required!
* Created a “First Flips” plug-in which you can use to get your
  machine flipping as fast as possible. (This was written as part of our
  Step-by-Step Tutorial for getting started with MPF.)
* Added Tilt and Slam Tilt support. (This is built via our Logic
  Blocks, so they’re very advanced, supporting grouping multiple quick
  hits as a single hit, settling time (to make sure the plumb bob is not
  still swinging when the next ball is started, etc.).
* Added Extra Ball / Shoot Again support
* Created OSC interfaces for /audits
* MAJOR rewrite to the ball controller and ball device modules
* Created a non-instrumented optimized software loop which is as lean
  as possible if you’re running your game on a slow computer. (I’m
  looking at you Raspberry Pi!) Note: other single board computers are
  fine, like the BeagleBone Black or the ODOID, but man the Pi is slow.
* Added the ability to pull “data” from MPF via the OSC interface, so
  we can put player scores, ball in player, etc. on an iPhone, iPad, or
  Android device.
* Added an OSC audit interface so you can view audit data via your
  mobile device.
* Created an “Info Lights” plug-in which turns on or off lights
  automatically based on things that happen in the game. (Which player
  is up, current ball, tilt, game over, etc.) This is typically used in
  EM games, but of course the plug-in can be used wherever you need it.
* Finished the code for our Big Shot EM-to-SS conversion. This is
  included as a sample game in MPF, so you can see our config files and
* Logic Blocks which can be helpful when creating your own game.
* Fixed up drop targets to support the new lit/unlit scheme
* Added support for default states to targets and target groups (stand
  ups, rollovers, drop targets, etc.), including events that are posted
  when they are hit while lit or unlit, and the ability to light or
  unlight them via events
* Added Start Button press parameters which are automatically sent to
  the game when the start button is pressed. This is for things like how
  long the button was held and what other buttons where active at the
  time. (Start * Right Flipper, etc.)
* Added a “pre-load check) to plug-ins that allows them to test
  whether they’re able to run before they load and only load if
  everything checks out. (This means that a plug-in will no longer crash
  if a required Python module is missing.)
* Added ‘no_audit’ tag support. (If you add ‘no_audit’ as a tag to a
  switch, then the Auditor will not include that switch in the audit
  logs.)
* Created Action Events for shutting down the machine and added
  shutdown tag support (so you can cleanly shut down the machine simply
  by posting and event or pressing a button which is tagged with
  “shutdown”)
* Added performance data logging to the machine run loop (so it now
  tracks the percentage of time spent doing MPF tasks, hardware tasks,
  and idle).
* Added a reload() method to Shows which causes that show to reload
  itself from disk. This is nice for testing shows since you can reload
  them without having to restart the machine each time.
* Added support for null steps in shows (literally a step that
  performs no action). This makes it easier to get timing right for
  music shows.
* Added the ability to force a light or LED to move to a given state,
  regardless of its current priority or cache.
* Added a method to test whether a device is valid. This will be used
  for our config file validator
* Added option for restart on long start button press
* Added option to allow game start with loose balls
* Score reels maintain a valid status, allowing other modules to know
  whether the score reels are showing the right data or not.
* Score reels now post an event when they’re resyncing, allowing other
  modules to act on it. (For example the score reel controller uses this
  to turn off the lights for a score reel while it’s resyncing.)
* Added option to remove all handlers for an event regardless of what
  their registered \**kwargs are.
* Added mpf command line options for verbose to console and optimized
  loops. (Now we can support different logging levels to the console and
  log file, meaning you can configure it so you only see important
  things on the console but you can see everything in the log file.)
* Added light on/off action events
* Added action events and methods to award the extra ball
* Created ball device disable_auto_eject() and enable_auto_eject()
  methods. This is how we handle player-controlled ejects (like when a
  ball starts or they’re launching a ball out of a cannon).
* Changed scoring from “shots” to “events”
* Changed the hardware rules for clearing a rule so it disables any
  drivers that were currently active from that rule
* Updated are_balls_gathered() so that if you pass it a tag which
  doesn’t exist, it always returns True
* Added management of switch handlers to machine modes so they can be
  automatically removed
* Changed switch handlers so they process delays from new handlers
  that are added
* Removed “standup” target device type (it was redundant with
  “target”)
* Moved auditor, scoring, and shots out of system and into plugins

0.8
---

September 15, 2015

* Platform support for FAST Pinball hardware
* RGB LED support, including settings colors and fades
* Created target and target group device drivers for drop targets,
  standups, and rollovers (including events on complete, lit shot
  rotation, etc.)
* Created an OSC interface to view & control your pinball machine from
  OSC client software running on a phone or tablet
* Changed our “light controller” to a “show controller” and added
  support for things other than lights (like coils and events). So now a
  show can be a coordinated series of lights, RGB LEDs, coil firings,
  and events.
* Created an “event triggers” plugin which lets you configure series
  of switches that trigger events, including custom timings, decays, and
  resets. (We use this for our titlt functionality but it’s useful in
  other ways too.)
* Created the auditor module
* Created an intelligent diverter device driver (with hardware switch
  trigger integration)
* Created GI device drivers
* Created a system-wide MPF ‘defaults’ configuration file
* Created templates for new machines, new scriptlets, and new plugins
* Modified the on screen window to become a “real” LCD display plugin.
* Renamed “hacklets” to “scriptlets”
* Created a scriptlet parent class to make them even easier to use
* Broke the hardware module into “platforms” and “devices”
* Major rewrite of how the machine controller loads system modules and
  devices
* Shows now auto load
* Added the ability to attach handlers to lights so you can receive
  notifications of light status changes
* Reworked the EM score reel update process to simplify and streamline
  it

0.7
---

September 4, 2014

* Support for lights and light shows.
* An on-screen display of game metrics like score, player, and ball
  number.
* A “hacklet” extension architecture which lets you add python code to
  finish up the “last 10%” of your game that you can’t control via the
  machine configuration files.
* A formal plug-in architecture which allows easy creation and
  modification of plug-ins that will survive core MPF framework updates.
* Cleaned up the machine flow and made that controllable via the
  config files
* Changed the -x command line option so it doesn’t use fakepinproc,
  got rid of the p_roc methods that detected fakepinproc. (Now even with
  the P-ROC platform it will use our virtual platform interface when no
  physical hardware is present. This means you don’t need pyprocgame to
  use fakepinproc.
* Changed the command line options to break out machine root from
  config files
* Moved command line options to their own python dictionary
* Changed time.clock() back to time.time() since clock was not real
  world which affected the light shows
* Created new events to capture start and stop of machine flow modes
* Added light support to P-ROC platform interface
* Reorganized the machine files into machine-specific subfolders
* Created an int_to_pwm() static method in Timing

0.6
---

August 19, 2014

* Addition of a Shot Controller, allowing you to configure and group
  switches which become shots in the machine. (Read more about the
  concept of shots in our blog post from last week.)
* Addition of a Scoring Controller, allowing you to map score values
  to shots (and general scoring support for the machine).
* Addition of the Score Reel Controller, Score Reel devices, and Score
  Reel Group devices for mechanical score reels in EM-style machines.
  (Details here.)Switched entire framework timing over to real time
  system clock times (time.clock()) instead of ticks (for delays, tasks,
  switch waits, etc.)
* Changed ball controller that if it counts more balls than it thought
  it had, it will invoke ball_found()
* Changed the switch controller so it will ignore new switch events if
  they come in with the current status the switch already is
* The switch controller will ignore repeat switch events from the
  hardware if they are the same state that the switch was in before
* Added chime support for EM-style machines
* Changed game_start event to a queue
* Change game_start event name to game_starting (some of these entries
  might seem trivial, but I also use this list to track the changes I
  need to make to the documentation)
* Created a queue for adding new tasks so our set won’t change while
  iterating

0.5
---

August 5, 2014

* Created a single device parent class that’s used for all devices.
* Rewrote and cleaned up devices. Now coils, switches, and lights are
  all devices, as are the more complex ones.
* Added “events” to the keyboard interface. This means you can use the
  keyboard to post MPF events (along with parameters).
* Separated out ball live confirmation and valid playfield
* Built a bunch of valid playfield methods
* Changed ball_add_live_request from direct calls to events so they’d
  be slotted in properly
* Broke valid playfield out into its own module
* Made the ball device “entrance” switch work
* Built a quick “coil test” mode
* Added kwargs to event handlers (meaning you can register a handler
  with kwargs)
* Figured out how to handle the “first time” counts of ball devices
* Added checks to attract mode to make sure all balls are home, and to
  the ball controller to prevent game start if all balls are not home
* Changed ejects to events. (So if you want to request that a device
  ejects a ball, you post an event rather than calling the device)
* Changed the balldevice_name_eject_request to be the event you use to
  call it, rather than the notification of the eject attempt.
* Created a get_status() method for ball devices
* Created a gather_balls() method and wrote the code that will send
  all the balls home before a game can be started.
* Updated stage_ball() code so it didn’t ask for another ball if there
  was already an eject in progress
* Moved detection of how balls fall back in out of devices and into
  the events that watch for the entrance
* Create player and event based ejects. (This is a system to allow
  players or events to eject balls from ball devices. Useful for cannons
  like in STTNG.)
* Got stealth and auto eject out of the ball device code since they
  shouldn’t care about that.
* Rewrote a lot of the ball device stuff.
* Added a manual eject capability for devices without eject coils
* Moved around some things between the ball controller and ball
  devices so that everything lives where it ‘makes sense’
* Added method to check whether an event has any handlers registered
  for it.
* Ball devices now post events based on tags when balls enter them
* Ball devices can now eject their ball if no event is registered.
  This will prevent balls from getting “stuck” in unconfigured devices
  and will make prototyping on new machines faster.
* Changed event logging to show “friendly” names of handlers
* Converted flippers to use a config dictionary instead of variables
* Cleaned up the eject confirmation and valid playfield functionality
* Added a remove_switch_handler method to the switch controller

0.4
---

July 25, 2014

* MAJOR rewrite of how the hardware platform modules interact with the
  framework’s hardware module and how hardware is configured in general.
  It’s way simpler and cleaner now. :)
* Created a parent class for Devices
* Cleaned up the way hardware objects use their parent class
* Fixed the ball controller so it doesn’t get confused on the initial
  count after machine start up.
* Cleaned up switch processing and added a logical parameter so we
  only have to do all the conversion for NC or NO in one place
* Renamed the none interface to virtual. Rewrote it with the new
  platform interface way of working.
* Added support for holdPatter in coils
* Change add_live() to use tags instead of the plunger device
* Made it so many things, like ball search, autofires, etc. would not
  crash the machine if they weren’t there.

0.3
---

July 16, 2014

* Changed the way config files are loaded by making Config a normal
  section of any config file instead of using a special initial
  configuration file that did nothing but point to additional files.
  Details here.
* Created a virtualhardware platform for virtual / software only
  testing that does not require P-ROC or FAST drivers.

0.2
---

July 11, 2014

* Added docstring documentation
* Added /sphinx folder and got the sphinx html docs included
* Created the first version of the documentation

0.1
---

June 27, 2014

* Command line parameters to select real or fake (simulated)
  controller hardware.
* Command line parameters to select logging level
* Command line parameters to select the location of the initial config
  file
* Reads an initial config file which is a list of additional config
  files
* Processes those config files in order to build a config dictionary
* All platform-specific hardware code is isolated into its own module.
  Config files specify which platform is used. All game code is
  100%interchangeable between platforms.
* Game loop runs with configurable loop rate. System timer tick event
  is raised every tick.
* Periodic and one-time use timers can be setup
* Switches, Coils, Lamps, and LEDs are read in and configured from the
  config files
* Switch events are read from the hardware
* Driver commands can be sent to the hardware
* Autofire drivers are automatically configured from the config files.
  They can be enabled, disabled, and reconfigured as needed.
* Flippers are automatically configured based on config files. They
  can use EOS or not, and be based on two coils (main/hold) or one coil
  with pulse+pwm. Multiple coils can be connected to the same switch,
  and vice-versa.
* The computer keyboard can be used to simulate switch presses. Key
  map configuration information is stored in the config dictionary. It
  supports momentary, toggle (push on / push off), and inverted (key
  press = open) key modes. Also supports combo key mapping (Shift, Ctrl,
  etc.)
* A switch controller receives all notifications of debounced hardware
  switch events.
* Can specify timed switch modes that trigger certain methods. (i.e.
  do blah() when switch_1 is active for 500ms.)
* Event manager handles system events, including registering handlers,
  priorities, aborting events, and maintaining a queue.
