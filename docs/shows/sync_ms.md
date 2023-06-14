---
title: Synchronizing multiple shows
---

# Synchronizing multiple shows


One thing you might notice in professional pinball machines is that all
the lights flash in sync with each other. But in MPF, if you have lots
of separate shows, then you'll notice they all sort of start randomly
when they start, and it looks bad because they're not all perfectly
aligned with each other.

MPF solves this by incorporating a "sync_ms" setting when playing
shows. When you add this setting to a show and then play it, MPF will
not start the show until the next exact multiple of that number from
zero.

For example, if you have `sync_ms: 500`, then MPF will start a show at
the exact second or half second. (e.g. the seconds value of the current
time will either be .0 or .5).

If you have `sync_ms: 250`, then shows will be delayed and start at the
nearest quarter second, either .0, .250, .5, or .750 past the second.

You only need to use the sync_ms setting for the specific shows you want
to keep in sync. Typically this would be used for light or LED shows, as
new shows starting should align nicely to existing shows that are
already running.

The value of sync_ms you should use should be one complete "cycle" of
the show. For example, if you flash your lights or LEDs at a rate of
250ms on / 250ms off, then you should use `sync_ms: 500` to ensure every
show starts at the nearest 500ms point, thus ensuring that all lights
will be "on" or "off" at the same time. (If you set `sync_ms: 250`
in this case, then your shows will be in sync but they might be offset
from each other.)

If your show is 200ms on / 200ms off, set sync_ms to 400. If your show
is 400ms on / 250ms off, set sync_ms to 650. Etc.

If you're wondering whether sync_ms is bad because it delays a show
start, and you don't want a show to be delayed, don't worry about it.
The main use for sync_ms is when you have lights or LEDs that are
flashing repeatedly, and in those cases, there's so much other stuff
happening when they start flashing that no one is going to notice a
delay of a fraction of a second when the show starts. (This is how is
has to work anyway since you want the lights to be in sync.)
