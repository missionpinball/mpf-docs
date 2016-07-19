Mode controller
===============

The *mode controller* is responsible for starting, running, and stopping
modes in an MPF machine. It lives in the
``mpf/core/mode_controller.py`` module.

In traditional pinball
machines, you might think of a "mode" as a "game mode." (e.g. the
missions in *Star Trek*, the mansion modes in *Addams Family*, the
cities in *Road Show*, etc.) In MPF, the in-game modes are "modes"
too, but so is the attract mode (and even the game itself is a mode
called "game"). MPF uses modes for the bonus, the high score entry,
tilt monitoring, credit monitoring, and lots of other little things
you might not think of as actual "modes." (Don't worry. Running modes
don't really take up any memory or CPU if they're not doing anything,
so if you have 20 modes running at once, that's fine.) Individual
modes have access to switches, the display, timers, delays, logic
blocks, devices, light shows, and all sorts of other things, and the
mode controller keeps everything straight. The mode controller is also
responsible for watching for events that start modes and for making
sure that modes start and stop correctly.



