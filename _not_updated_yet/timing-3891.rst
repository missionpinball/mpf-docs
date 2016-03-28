
The `timing:` sectionspecifies how many "ticks" per second the MPF
game engine runs at. If you're using the MPF media controller, this
setting will also control it. This sectioncan be used in your machine-
wide config files. This section *cannot* be used in mode-specific
config files. This setting is set to `30` (i.e. 30Hz) in the
`mpconfig.yaml` file, so you only need to add it if you want your
machine to run at a speed other than 30Hz. Setting it is simple:


::

    
    timing:
      hz: 30


More details about the machine Hz are available in the `Timers &
Machine Tick Speed documentation`_ in the MPF Core Architecture
section.



hz:
~~~

This setting controls how many "loops" per second your game code runs
at. (Another way to phrase this is it's how many times per second MPF
"wakes up" to do things.) It also represents the fastest speed any
periodic updates can occur in your machine, so if you want to run your
display at 60fps then set your *hz* to 60. Note that when switches are
hit, they will "wake up" MPF immediately, so having a low hz setting
does not mean that MPF will not be responsive. See the document about
Machine HZ & Loop Rates for details. The default value is 30.



hw_thread_sleep_ms:
~~~~~~~~~~~~~~~~~~~

This is how many milliseconds MPF will sleep between polling the
hardware for switch changes. The default value is 1 which should be
fine for most cases. If you set this to 0 then MPF will poll the
hardware as fast as possible, but this is not advised since it means
MPF would consume 100% of your CPU which means it will run hotter and
your overall system will not be responsive.

.. _ Machine Tick Speed documentation: https://missionpinball.com/docs/mpf-core-architecture/machine-hz-loop-rates/


