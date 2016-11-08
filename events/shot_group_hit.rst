(shot_group)_hit
================

*MPF Event*

A member shot in the shot group called (shot_group) was just hit.

Note that there are three events posted when a member shot is hit, each
with variants of the shot name, profile, and current state,
allowing you to key in on the specific granularity you need.

Also remember that shots can have more than one active profile at a
time (typically each associated with a mode), so a single hit to this
shot might result in this event being posted multiple times with
different (profile) values.

Keyword arguments
-----------------

profile
~~~~~~~
The name of the profile that was active when hit.

state
~~~~~
The name of the state the profile was in when it was hit

