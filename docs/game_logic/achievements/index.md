---
title: Achievements
---

# Achievements


Related Config File Sections:

* [achievements:](../../config/achievements.md)

MPF uses "achievements" to track major goals that a player must
achieve throughout the progression of a game. Achievements typically
have an associated light or LED on the playfield (though not always),
and they're tracked separately per player.

The biggest use for achievements is for modes, where you have a bunch of
modes in a machine which each have a light, and as you complete the
modes, the light turns on. (In many cases the lights/LEDs associated
with achievements have multiple states, for example, they're "off"
when not complete, "flashing" when active, "on" when complete, etc.)

Here are some examples from real machines that would map to
"achievements" in MPF:

* Attack from Mars:

    * The countries (France, Germany, Italy, England, USA)
    * The Capture inserts (Capture 1, Capture 2, Capture 3)
    * The Big -O- Beam inserts (1, 2, and 3)
    * The Atomic Blaster inserts (1, 2, and 3)
    * The Blue circles to Rule The Universe (Super Jackpot, Super
      Jets, Martian Attack Multiball, Total Annihilation, Conquer
      Mars, and 5-way Combo)

* Indiana Jones

*state*

(  The string name of the state this achievement is in. Options will be
    one of the following)
