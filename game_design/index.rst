How to design a game in MPF using Modes
=======================================

This section assumes that you already configured all your hardware devices
(especially all your :doc:`ball device </config/ball_devices>`).
If you did not configure your hardware please do that first.
You can go through the :doc:`tutorial </tutorial/index>` or have a look a the :doc:`mechs section </mechs/index>`.

This section is about laying out your modes and actually designing your game logic.
It is structured into the following subsections:


Mode Selection and Game Startup
-------------------------------

Questions answered in this section:

* How to select modes/players during start?
* How to implement a (timed) skill shot?
* How does a player qualify for a mode?
* How to start the mode?
* Can multiple modes run at once?

.. toctree::
   :titlesonly:

   Mode Selection <mode_selection>

Game Mode
---------

Questions answered in this section:

* How to track progress inside a mode?
* How does it end?
* Will it always succeed?
* Can it timeout?
* Can it restart if it failed?
* Where will it contine on restart?

* How to implement roll over lanes in a mode?
* How to implement a mystery award mode?
* How to implement a standup target bank mode?

.. toctree::
   :titlesonly:

   Game Mode <game_modes/index>

Wizard Modes
------------

Questions answered in this section:

* How to track achievements towards one or multiple wizard modes?
* How to start a wizard mode?
* What to do after wizard mode?

.. toctree::
   :titlesonly:

   Wizard Modes <wizard_modes>

Ball End Modes
--------------

Questions answered in this section:

* How to start a mode after the ball for a player drained?
* How to implement a bonus mode?

.. toctree::
   :titlesonly:

   Ball End Modes <ball_end_modes>

Game End Modes
--------------

Questions answered in this section:

* How to start a mode after the last player drain his ball?
* How to implement a highscore mode?
* How to implement a match mode?

.. toctree::
   :titlesonly:

   Game End Modes <game_end_modes>

Other modes
-----------

Questions answered in this section:

* Which modes run outside of a game?
* How to control attract?
* How do credits work?
* How does tilt work?
* What is the service mode?

.. toctree::
   :titlesonly:

   Other Modes <other_modes>

Layering Modes Example
----------------------

Examples given in this section:

* How to define mode categories and helper modes
* How to move in and out of game and wizard modes
* How to track and persist progress outside of modes

.. toctree::
   :titlesonly:

   Layering Modes Example <mode_layering>


