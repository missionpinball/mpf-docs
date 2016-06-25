MPF overview (what it does and how it works)
============================================

The Mission Pinball Framework (which we call "MPF") is free and open source
software that you run on a computer (Windows, Mac, Linux, Raspberry Pi, etc.)
to control a real, physical pinball machine. (More info one what MPF is
`here <https://missionpinball.com/mpf/>`_.)

You'll use MPF to configure and control everything in your machine, including:

* Physical hardware (switches, LEDs, lights, motors, coils, servos, steppers,
  etc.)
* The display (or displays): DMD, RGB LED, and/or LCD
* Audio & sounds
* Pinball devices, like ball troughs, flippers, pop bumpers, diverters, etc.
* Pinball logic, like ball locks, multiball, modes, tilt, high scores, ball
  saves, ball search, extra balls, etc.
* Coordinated "shows" of actions which flash lights, fade LEDs, play sounds and
  video, etc.
* Player management, including player progress, scoring, tracking towards
  goals, etc.
* Plus lots of other little things that you probably aren't even thinking about
  now.

We designed MPF to be hardware-independent. (A list of all the hardware
MPF currently supports is :doc:`here</hardware/index>`, and we're always adding
more.) This means that it doesn't matter whether you use a P-ROC, a FAST Pinball
controller, Open Pinball Project hardware, etc. You can also use all sorts of
little USB devices to do different things (FadeCandy for LEDs, servo
controllers, etc.)

MPF is a work-in-progress!
--------------------------
MPF is far from complete. We're not even to our 1.0 release yet so the code is
very "beta" at this point. That said, we have a lot done and you can absolutely
build a game with it today. (Several people have already built complete
machines!)

We don't have specific time frames in mind for a 1.0 release. We've been
releasing new stable-ish versions every few months with dev versions almost
daily.) That said, we have a "to do" list with probably 2-3 years worth of
ideas, and we're sure that list will continue to grow. (Don't worry, we'll
release a 1.0 before that!)
