---
title: How MPF works
---

# How MPF works

The Mission Pinball Framework ("MPF") is free and open
source software that you run on a computer (Windows, Mac, Linux,
Raspberry Pi, etc.) to control a real, physical pinball machine. (More
info one what MPF is [here](http://missionpinball.org).)

Most people develop their game on their laptop, and then when they're
done, transfer it to a smaller computer permanently installed in their
pinball machine.

The computer running MPF is connected to a
[modern pinball control system](../hardware/index.md) via USB. (MPF supports several different control systems,
including FAST Pinball, P-ROC, Open Pinball Project open source
hardware, and Stern SPIKE hardware.)

You put that control system in your pinball machine, which can be a
custom (homebrew) machine or an existing machine you want to reprogram.

This diagram shows how it all fits together:

![image](images/computer-controller-machine.jpg)

The MPF software is used to configure and control everything in your
machine, including:

* Pinball mechanisms (switches, LEDs, lights, motors, coils, servos,
    steppers, flippers, ball locks, diverters, etc.)
* Pinball logic (ball locks, multiball, modes, tilt, high scores, ball
    saves, ball search, extra balls, etc.)
* The display (or displays): DMD, RGB LED, and/or LCD
* Audio & sounds
* Coordinated "shows" of actions which flash lights, fade LEDs, play
    sounds and video, etc.
* Player management, including player progress, scoring, tracking
    towards goals, etc.
* Plus lots of other little things that you probably aren't even
    thinking about yet :)

!!! note "MPF is not a simulator"

    MPF is not a pinball simulator. It's not a pinball game. It's a
    framework that lets you build the game software for a physical pinball machine.

Read on to understand other important concepts about MPF:
