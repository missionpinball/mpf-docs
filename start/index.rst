MPF overview (what it does and how it works)
============================================

The Mission Pinball Framework (which we call "MPF") is free and open source
software that you run on a computer (Windows, Mac, Linux, Raspberry Pi, etc.)
to control a real, physical pinball machine. (More info one what MPF is
`here <https://missionpinball.org>`_.)

You'll use MPF to configure and control everything in your machine, including:

* Physical pinball mechanisms (switches, LEDs, lights, motors, coils, servos, steppers,
  flippers, ball locks, diverters, etc.)
* The display (or displays): DMD, RGB LED, and/or LCD
* Audio & sounds
* Pinball logic (ball locks, multiball, modes, tilt, high scores, ball
  saves, ball search, extra balls, etc.)
* Coordinated "shows" of actions which flash lights, fade LEDs, play sounds and
  video, etc.
* Player management, including player progress, scoring, tracking towards
  goals, etc.
* Plus lots of other little things that you probably aren't even thinking about
  now.

We designed MPF to be hardware-independent. This means that it doesn't matter whether
you use a P-ROC, a FAST Pinball controller, Open Pinball Project hardware, etc. You
can easily change the hardware you use at any time.

.. note:: MPF is a work-in-progress!

   One important thing to remember is that MPF is a work-in-progress and not yet
   complete. It's being built by pinball-loving software developers in their
   spare time. There's a lot you can do with MPF today, but we also have a lot
   of work still to do. We're working hard though, typically adding 20-30 updates
   per week!


Read on to understand other important concepts about MPF:

.. toctree::
   :titlesonly:

   features
   hardware_interface
   config_files
   dsl_vs_programming
