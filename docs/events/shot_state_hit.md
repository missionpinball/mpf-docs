---
title: (shot_name)_(state)_hit
---

# (shot_name)_(state)_hit


--8<-- "event.md"

The shot called (shot_name) was just hit while in the profile (state).

Note that there are four events posted when a shot is hit, each with
variants of the shot name, profile, and current state, allowing you to
key in on the specific granularity you need.

Also remember that shots can have more than one active profile at a time
(typically each associated with a mode), so a single hit to this shot
might result in this event being posted multiple times with different
(profile) and (state) values.

## Keyword arguments

(See the [Conditional Events](overview/conditional.md)
guide for details for how to create entries in your config file that
only respond to certain combinations of the arguments below.)

`profile`

:   The name of the profile that was active when hit.

`state`

:   The name of the state the profile was in when it was hit

Event is posted by [shots:](../config/shots.md)
