MPF Feature List
================

Even though MPF is a work-in-progress that's not yet complete, the core dev team
has been working on it for about two years, with over 5,000 hours of combined
effort.

As we mentioned already, the MPFis a work in progress and not yet
complete. That said, here's a list of features that are actually
implemented so far. You can also read about the `features we're
working`_ on for the next release, as well as our `long-term list of
features`_ we want to get done before "v1". (And you can read our
`super-long-term list of features`_ that will probably take years to
do!)

Major Features & Concepts
-------------------------

+ The vast majority of "programming" your game can be done with text-based
  config files that make it easy to get powerful and complex pinball
  features running in your game. They're also easy for non-programmers to use.
+ Advanced programmers and customization can be done via the API. (The
  API is fully documented at `api.missionpinball.com <http://api.missionpinball.com>`_
+ Easily switch between hardware platforms, so if sometime down the road
  you want to switch hardware or the company whose hardware you're using
  goes out of business, all your effort is not lost as you can easily move
  everything to a new hardware platform with a simple config file change.

Full feature list (all real today)
----------------------------------

+ Support for `Multimorphic`_ *P-ROC* and *P3-ROC* pinball
  controllers(with either Williams WPC, Williams System 11, Data East,
  Stern Whitestar or S.A.M., or P-ROC driver boards), `FAST Pinball`_
  *WPC*, *Core*, and *Nano* controllers(with either FAST or WPC driver
  boards) and virtual (software only) games without hardware attached.
+ Support for Open Pixel Control LED controllers, including the
  `FadeCandy`_.
+ Hardware support for coils, switches, matrix-based lights, RGB &
  single-color LEDs, flashers, andGI strings.
+ Intelligent device support forflippers, auto-firing coils
  (slingshots, bumpers, etc.), ball devices (things that hold balls like
  the trough, VUKs, locks, poppers, etc.), diverters, and EM score
  reels. (We say "intelligent" support because it's more than just being
  able to fire a coil when a switch is hit. MPF understands what the
  device is, how it fits into a pinball game flow, what state it's in,
  etc.)
+ Intelligent management of shots and shot groups, including automatic
  per-player state management, automatic integration with lights, shots
  based on sequences of switches, and a shots profile manager that lets
  you apply different behavioral profiles to shots based on game modes.
+ Full DMD and LCD support (including traditional DMDs, color DMDs,
  color RGB DMD matrix displays, and modern HD displays), with multiple
  types of display elements, slides, transitions, decorators, and
  support for TrueType fonts. On-screen and physical DMDs are supported.
+ Machine and game controller modules which manage the overall
  machines and game flows. Right out of the box you can play complete
  games, cycle through balls and players, etc.
+ Intelligent ball and playfield tracking, including balls in play,
  balls on the playfield, and automatic control of ball devices and
  diverters to move balls to where they need to be.
+ A score controllerwhich lets you configure shots, switches, or other
  game events that add to the player's score and the player's progress
  in other areas (ramps, loops, aliens destroyed, etc.).
+ Game mode support. (Run one or more game modes at once, each with
  their own priorities, display slides, scoring, shots, sounds, display
  effects, lighting, and game logic, all which loads when the mode
  starts and unloads when the mode ends).
+ Built-in modes to run the attract mode, the game, and high score,
  credits, and tilt.
+ Ball save, ball lock, and multiball modules.
+ A light showcontroller which lets you build complex
  coordinated"shows" of lights, LEDs, coils, and GI. You can create
  playlists, layers, and play multiple shows at once.
+ Sound & audio support, including multiple tracks, dynamic loading &
  unloading of sounds, track-specific volume control, sound priorities,
  and a sound queue.
+ "Logic Block" modules which let you sequence flowchart-style game
  logic.
+ Timers which let you start, stop, pause, and extend all the timers
  you need (timed modes, shots, countdowns, count ups, hurry ups, etc.).
+ Full per-player variable and settings support. Save/restore anything
  on a per-player bases (shots, objectives, goals collected, targets
  hit, etc.)
+ A game auditor which records and saves game information, high
  scores, game events, total switch hits, etc. (This is highly
  configurable.)
+ A data manager which reads and writes data from disk, including
  audits, earnings, machine variables, high scores, etc.
+ A keyboard interface which lets you simulate switch actions with
  your computer keyboard. (Great for testing!)
+ A multi-language module which can replace text strings on the fly
  with alternate versions for other languages.
+ And OSC interface which lets you interface, control, and view status
  of your pinball machine via a tablet or phone.
+ An EM-style score reel controller (in case you want to `convert an EM game to solid state`_).
+ A plugin architecture which allows you to write your own plugins to
  extend baseline functionality.
+ A "scriptlet" interface lets you add Python code snippets to extend
  the functionality you can get with the configuration files.
+ A switch "player" which lets you play back timed sequences of
  switches for automated testing and simulation.
+ And the best part: The bulk of your gameconfiguration and logic can
  be built via text-based configuration files. If you don't want to be a
  "coder," you don't have to be. (Though the plugin, scriptlet, mode
  coding, and `API documentation`_ mean that if you want to use MPF for
  your groundwork and code your game in "real" Python, that's fine too.)

.. toctree::

   0.30
   /version_history/index

.. _FAST Pinball: http://www.fastpinball.com
.. _API documentation: /apidocs
.. _Multimorphic: http://www.pinballcontrollers.com
.. _super-long-term list of features: https://missionpinball.com/blog/2014/10/the-mission-pinball-framework-roadmap-vision-for-the-future-of-pinball/
.. _features we're working: https://missionpinball.com/docs/road-map/currently-in-dev/
.. _FadeCandy: http://www.adafruit.com/products/1689
.. _long-term list of features: https://missionpinball.com/docs/road-map/
.. _convert an EM game to solid state: /blog/category/big-shot-em-conversion/
