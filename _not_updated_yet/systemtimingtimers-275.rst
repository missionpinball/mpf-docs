
MPF includes a timing module ( `mpf/system/timing.py`) which includes
the *Timing* class (used for the main system timer) as well as a
*Timer*class (used to set up periodic system timers).



Machine Tick Speed (Hz)
-----------------------

One of the configuration options that you specify when using the
Mission Pinball Framework is a constant called *HZ*which is how many
"ticks" the framework software runsper second. Basicallythe
machinedoes some action, then goes to sleep, then wakes up to do more
actions, then goes to sleep, etc. as many times per second as what you
set your HZ rate to be. The timing module controls that. (For a
detailed discussion on this topic, read the `Machine HZ & Loop Rates
document`_.)



Periodic Timers
---------------

In addition to the system timer that "ticks" along at the machine's Hz
rate, the Mission Pinball Framework also has periodic timers. A
periodic timer is simply a method that you register to call on a
regular basic (every x seconds or milliseconds). You can have as many
periodic timers as you want and they can all be different rates and be
started, stopped, created, or deleted at any time. For example,
countdown modes employ periodic timers that are called once per second
to do their countdown and to update a variable which holds the number
of seconds remaining in the mode. The DMD code uses a periodic timer
set to the frame rate to update the DMD, and the light controller uses
a periodic timer to update all the lights multiple times per second.

.. _ Loop Rates document: https://missionpinball.com/docs/mpf-core-architecture/machine-hz-loop-rates/


