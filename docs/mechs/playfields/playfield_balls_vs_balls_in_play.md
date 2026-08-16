---
title: Playfield "balls" versus "balls in play"
---

# Playfield "balls" versus "balls in play"


One important concept for ball tracking to understand is that there's a
difference between the number of balls on a playfield and the "balls in
play".

Most of the time, the number of balls rolling around the playfield is
the same as the number of balls in play. However this is not always the
case.

For example, when the machine tilts, the player's ball is "dead" and
the number of balls in play is set to zero. But of course when that
happens, there are still balls loose on the playfield which MPF has to
track to make sure they all drain without getting stuck.

Also, if you have more than one playfield (like with an upper or lower
playfield), then the number of balls on the individual playfields will
be lower than the total number of balls in play.

Another time these two values are different is when the player shoots
the ball into a lock. At that moment the playfield has no balls (and the
lock has one), though there's technically still a ball in play.
