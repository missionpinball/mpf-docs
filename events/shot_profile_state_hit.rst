(shot)_(profile)_(state)_hit
============================

*MPF Event*

The shot called (shot) was just hit with the profile (profile)
active in the state (state).

Note that there are four events posted when a shot is hit, each
with variants of the shot name, profile, and current state,
allowing you to key in on the specific granularity you need.

Also remember that shots can have more than one active profile at a
time (typically each associated with a mode), so a single hit to this
shot might result in this event being posted multiple times with
different (profile) and (state) values.


Keyword arguments
-----------------

profile
~~~~~~~
The name of the profile that was active when hit.

state
~~~~~
The name of the state the profile was in when it was hit

