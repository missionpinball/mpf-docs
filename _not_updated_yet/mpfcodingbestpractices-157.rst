
These will be fleshed out. For now this is just a list so we remember
what to write about.


+ For events, try to move on quickly. If anything is long-running then
  use a callback and come back later.
+ Don't mix direct calls and events.
+ Remember that there's an event queue and events are handled
  sequentially in the order they're posted, so events are *not*
  guaranteed to be handledwhen they're posted. If you need something to
  fire after an event, you need to either make it fire by an event or
  call it via a callback.
+ Don't make the valid playfield counttoo high, since it's disruptive
  for a ball to be plunged and to score without a valid playfield.




