---
title: Media Controllers
---

# The MPF Media Controllers

The core MPF game engine does not handle graphics or audio. Instead, that is
handled by a completely separate program called a "media controller."

Two official media controllers exist - MPF-GMC, the Godot plugin, works with MPF 0.80+, and is the modern media controller. Legacy MPF-MC is a Python Kivy project used in versions up through 0.58.

However, you don't have to either of these. Many people have created their own media controllers in other languages (Unity 3D, C#, Lua versions all exist), or you can write your own.

The MPF game engine and media
controller talk to each other via something called "BCP" which is a
protocol we created for this purpose which stands for "Backbox Control
Protocol". (More details on BCP are available at the [MPF developer
site](http://developer.missionpinball.org).)

Here's a diagram that shows what each piece does:

![image](images/mpf_game_engine_mc.png)

Why are the MPF game engine and media controller two separate processes?
Two reasons:

First, having two processes means that each one can run on a separate
core in a multi-core host computer. This makes efficient use of hardware
since the trend is to have multiple cores. If the game engine and media
controller were combined, then your quad-core Raspberry Pi 3 would have
all the MPF stuff running on one core while the other three cores were
wasted doing nothing.

Second, having two processes means you can replace MPF's default media
controller with something else if you want different features. For
example, there is a group of people building an open source
[Unity 3D-based media controller](unity_bcp_server.md) which can be used for very advanced 3D display graphics.
