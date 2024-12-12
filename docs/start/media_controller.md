---
title: The MPF Media Controller
---

# The MPF Media Controller


All modern pinball machines use graphics and sound. MPF's architecture
is build so that the core "game" engine is completely separate from
the "media" engine.

The "game" engine is the MPF software itself, and the "media" engine
is something called the MPF Media Controller (which we often abbreviate
as "MPF-MC").

When you run MPF, these two components are two separate processes that
talk to each other via something called the "Backbox Control
Protocol".

The details and inner workings of this are not really important, (and
frankly they're mostly hidden from you).

But as you start to learn about MPF, just keep in mind that the part of
MPF that runs your game and controls the hardware is separate from the
part that shows the graphics and plays the sounds.

Here's a diagram that shows what each piece does:

![image](/docs/mc/images/mpf_game_engine_mc.png)

More details about MPF's media controller architecture, as well as
guides which show you how to run them on separate computers, or even to
replace MPF's Media Controller with one based on Unity 3D or something
you write yourself, are available in the
[Displays, DMDs, & Graphics](../mc/index.md) section of the
documentation.
