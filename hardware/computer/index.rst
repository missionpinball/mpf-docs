Choosing a PC for MPF
=====================

Generally speaking, MPF will run on any PC or embedded system which can run Python 3.
In most cases you also need a graphics card with working OpenGL to run the MPF Media Controller (MPF-MC).
Most operating systems work fine (we test on Linux, Windows, Mac OS X) but be careful with virtualized
environments because OpenGL might not work perfectly.
MPF benefits multiple CPU cores and during normal operations MPF and MC utilize two cores.
During startup, when playing sound or loading assets additional cores may be used.
Therefore, we recommend a CPU with at least two cores. MPF certainly benefits from four cores but
everything above that will not help during normal games.
However, during development, when using MPF Monitor and an IDE more cores will certainly help.
MPF needs at least 512MB RAM but we recommend 2-4GB depending on the amount of assets.
Again, during development you want to have more RAM (8GB+) for your IDE and other tools.
To load assets quickly a SSD helps. You definitely want that during development but you might use a cheaper
option for the final game.


Development setup
-----------------

* CPU with at least for cores
* 8GB RAM or more
* SSD

Final game
----------

We cannot emphasize this enough: Do not use such a setup for game development.

* CPU with two to four cores
* 2-4GB RAM (mostly for assets)
* SD-Card/Embedded flash/SSD
