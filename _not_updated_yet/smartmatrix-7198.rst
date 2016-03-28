
The `smartmatrix:` section of your machine-wide config contains the
settings for a SmartMatrix RGB LED DMD controller. (See our `How To
guide on these`_ for details of how to set one up.) This sectioncan be
used in your machine-wide config files. This section *cannot* be used
in mode-specific config files.


::

    
    smartmatrix:
        port: com12
        use_separate_thread: yes




port:
~~~~~

This is the name of the serial port that your Teensy uses. If you
don't know it, just look at your serial ports, then plug in your
Teensy and see which port appears. On a Mac or Linux, this will have a
Unix-style port name. There is no default setting.



use_separate_thread:
~~~~~~~~~~~~~~~~~~~~

This controls whether the code that communicates with the Teensy will
run as part of your machine MPF loop or whether it will run in a
separate thread. Options are yes/no or true/false. The correct setting
will depend on the specifics of your hardware and what size display
you’re running. For example, on one test system (MPF running in a
Windows VM on a MacBook), it didn’t matter what this was set to—the
experience was the same either way. Another user running a larger size
128×64 display, had to set `use_separate_thread: no` to get good
performance. So basically try it with both settings and see which one
works better. Default is *true*.

.. _How To guide on these: https://missionpinball.com/docs/howto/smartmatrix-rgb-dmd/


