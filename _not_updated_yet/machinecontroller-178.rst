
If MPF is a pinball operating system, then the machine controller is
its kernel. The machine controller lives in the
*mpf/system/machine.py* module and is responsible foralmost
everything, including:


+ Loading and processing all the core system modules, plugins, and
  devices.
+ Loading and processing the machine configuration files.
+ Loading and processing the machine-specific scriptlets.
+ Setting up the platform interfaces which communicate with the
  physical hardware.
+ Resetting the machine.
+ Running the main game loop.


If you're writing Python code, the machine controller is typically
accessed via `self.machine`. One quick side note: The pinball
community tends to use the terms "game" and "machine" interchangeably.
(We're certainly guilty of this too. We would say that "Road Show is
our favorite game", not "Road Show is our favorite machine.") That's
fine, and we're not on a mission to change peoples' terminology. But
in the context of the Mission Pinball Framework, a "game" and a
"machine" are not the same thing. In MPF, "machine" is a physical
machine, and "game" is an actual game that's in progress. So that's
why you build your "machine" code and your "machine" configuration.
The "game" for us is what happens when players are actively playing a
game. (So when an MPF-powered machine is in Attract mode, your machine
is running, but you don't have a game.)



