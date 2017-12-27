Grouping Shots for lane change, rotation, etc.
==============================================
.. overview
example config for lane changing lights

::

 shot_groups:
    outlanes:
        shots: shot_l_outlane, shot_l_inlane, shot_r_inlane, shot_r_outlane
        rotate_left_events: s_flipper_left_active
        rotate_right_events: s_flipper_right_active
        reset_events: outlanes_profile_hit_lit_complete
        enable_events: ball_started
        disable_events: ball_ending
        
Shot Group Overview:
------------
Shot Group: 
~~~~~~
We're creating a shot group called "outlanes", which contains 4 shots that we defined in our Shots: section of a mode.

Rotate events: 
~~~~~~
These will cycle the lights thru your shots, based on which flipper button is pressed in this case.

Reset_Events: 
~~~~~~
describes an event that will cause this shot group to reset back to its original state.

Enable/Disable Events:
~~~~~~
describe events that will cause this shot group to be enabled/disabled, in this case we are using Ball_Started and Ball_Ending. 
