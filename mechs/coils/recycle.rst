Recycle / "Cool Down" Time
==========================

Recycle time is the time a coil will rest after it has been pulsed.
This is either calculated as ratio on the pulse time (for instance, two
times the pulse time) or as absolute time.
In both cases this time is used to prevent thermal overheating of coils
similar to hold_power.

If your machine constantly triggers a coil with 50ms pulse time for some reason
then it would practically stay on permanently without recycle time.
Howver, with a recycle factor of 2 (or 100ms cool down time) it would be
enabled for at most 33% of the time.
