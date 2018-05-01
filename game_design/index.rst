How to design a game in MPF
===========================

This section assumes that you already configured all your hardware devices
(especially all your :doc:`ball device </config/ball_devices>`).
If you did not configure your hardware please do that first.
You can go through the :doc:`tutorial </tutorial/index>` or have a look a the :doc:`mechs section </mechs/index>`.

This section is about laying out your modes and actually designing your game logic.
It is structured into the following subsections:


Mode Selection
--------------

Questions answered in this section:

* How does a player qualify for a mode?
* How to start the mode?
* Can multiple modes run at once?

Game Mode
---------

Questions answered in this section:

* How to track progress inside a mode?
* How does it end?
* Will it always succeed?
* Can it timeout?
* Can it restart if it failed?
* Where will it contine on restart?

Wizard Modes
------------

Questions answered in this section:

* How to track achievements towards one or multiple wizard modes?
* How to start a wizard mode?
* What to do after wizard mode?

.. toctree::
   :titlesonly:

   Mode Selection <mode_selection>
