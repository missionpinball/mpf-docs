Tilt (mode)
===========

The MPF package includes built-in tilt mode that can be used to track
manage tilt warnings, tilts, and slam tilts.

The tilt mode runs at priority 10,000 and automatically starts when
MPF boots up. It never stops, even running while the attract mode is
running. (This is because you want it to watch for slam tilts that
reset the credits even when there's not a game in progress.)

The tilt mode can use traditional mechanical tilts (plumb bobs,
weighed switches, and rolling balls), or it can use accelerometers
to determine G-forces and angle of the machine which can trigger
tilts.

See the How To: Create a Tilt guide for details on how to use it in
your machine.
