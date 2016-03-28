
The playfield in MPF is actually a special type of `ball device`_.
This is needed since MPF wants to know where all the balls are at all
times, so it needs to know which balls are "in" the playfield device.
The playfield is also responsible for tracking balls that
"disappeared" from it without going into other devices—a process which
kicks off the ball search. The default playfield ball device (called
*playfield*) is created automatically based on settings in the
*mpfconfig.yaml* default configuration file. Most machines only have
one playfield, though if you have a mini-playfield or a head-to-head
machine then you can configure additional playfield devices.
Playfields are configured in the playfields: section of the
configuration file.

.. _ball device: https://missionpinball.com/docs/mpf-core-architecture/devices/logical-devices/ball-device/


