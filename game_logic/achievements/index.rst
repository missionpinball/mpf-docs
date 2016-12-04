Achievements
============

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/achievements`                                                  |
+------------------------------------------------------------------------------+

.. versionchanged:: 0.32

MPF uses "achievements" to track major goals that a player must achieve
throughout the progression of a game. Achievements typically have an associated
light or LED on the playfield (though not always), and they're tracked
separately per player.

The biggest use for achievements is for modes, where you have a bunch of modes
in a machine which each have a light, and as you complete the modes, the light
turns on. (In many cases the lights/LEDs associated with achievements have
multiple states, for example, they're "off" when not complete, "flashing" when
active, "on" when complete, etc.)

Here are some examples from real machines that would map to "achievements" in
MPF:

* Attack from Mars:
    * The countries (France, Germany, Italy, England, USA)
    * The Capture inserts (Capture 1, Capture 2, Capture 3)
    * The Big -O- Beam inserts (1, 2, and 3)
    * The Atomic Blaster inserts (1, 2, and 3)
    * The Blue circles to Rule The Universe (Super Jackpot, Super Jets, Martian
      Attack Multiball, Total Annihilation, Conquer Mars, and 5-way Combo)
* Indiana Jones: The Pinball Adventure:
    * The Modes inserts (Streets of Cairo, Well of Souls, Monkey Brains, etc.)
* The Addams Family:
    * Mansion Modes (Raise the Dead, Hit Cousin It, Mamushka, etc.)
* Star Trek: The Next Generation:
    * Missions (Time Rift, Asteroid Threat, Rescue, Q's Challenge, etc.)
* Red & Ted's Road Show:
    * The cities on the Map (each city is an achievement)
    * The wheel (Lunch Time, Flying Rocks, Big Blast, Special, etc.)

You can have as many achievements as you want in your machine, and you can
re-use the same lights/LEDs for different achievements in different modes.
(For example, you might have red arrow inserts that turn on and off to highlight
shots in your base mode, but then you might have a timed mode where those
inserts are mapped to achievements and they're all lit, and they go out as
they're hit.)

You can also group individual achievements into "achievement groups". This is
useful for tracking when all the achievements in the group have been complete
(e.g. to light a wizard mode). You can also use achievement groups to "rotate"
lit achievements (e.g. every slingshot hit changes the achievement that's
flashing, but it only rotates through incomplete achievements.)

+------------------------------------------------------------------------------+
| Related How To Guides                                                        |
+==============================================================================+
| TODO                                                                         |
+------------------------------------------------------------------------------+

+------------------------------------------------------------------------------+
| Related Events                                                               |
+==============================================================================+
| :doc:`/events/achievement_name_state_state`                                  |
+------------------------------------------------------------------------------+
| Plus any custom events as defined in the achievement's configuration in your |
| config files.                                                                |
+------------------------------------------------------------------------------+

.. toctree::

   achievement_groups
