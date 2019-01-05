Grouping Shots for lane change, rotation, etc.
==============================================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/shots`                                                         |
+------------------------------------------------------------------------------+
| :doc:`/config/shot_profiles`                                                 |
+------------------------------------------------------------------------------+
| :doc:`/config/shot_groups`                                                   |
+------------------------------------------------------------------------------+

.. overview

Example config for lane changing lights.

.. code-block:: mpf-config

    #! switches:
    #!    lane_l:
    #!       number:
    #!    lane_a:
    #!       number:
    #!    lane_n:
    #!       number:
    #!    lane_e:
    #!       number:
    #!    upper_standup:
    #!       number:
    ##! mode: inlanes
    shots:
        shot_l_outlane:
            switch: lane_l
            show_tokens:
                light: lane_l
        shot_l_inlane:
            switch: lane_a
            show_tokens:
                light: lane_a
        shot_r_inlane:
            switch: lane_n
            show_tokens:
                light: lane_n
        shot_r_outlane:
            switch: lane_e
            show_tokens:
                light: lane_e

    shot_groups:
       outlanes:
           shots: shot_l_outlane, shot_l_inlane, shot_r_inlane, shot_r_outlane
           rotate_left_events: s_flipper_left_active
           rotate_right_events: s_flipper_right_active
           reset_events: outlanes_profile_hit_lit_complete
           enable_events: ball_started
           disable_events: ball_ending


Monitorable Properties
----------------------

For :doc:`dynamic values </config/instructions/dynamic_values>` and
:doc:`conditional events </events/overview/conditional>`,
the prefix for multiballs is ``device.shots.<name>``.

*common_state*
   The name of the common state of all shots in the group.
   Will be ``None`` if there is no common state.
   State names depend on the profile of your shots (by default ``lit`` and
   ``unlit``).


Shot Group Overview:
--------------------
Shot Group:
~~~~~~~~~~~
We're creating a shot group called "outlanes", which contains 4 shots that we defined in our Shots: section of a mode.

Rotate events:
~~~~~~~~~~~~~~
These will cycle the lights thru your shots, based on which flipper button is pressed in this case.

Reset_Events:
~~~~~~~~~~~~~
Describes an event that will cause this shot group to reset back to its original state.

Enable/Disable Events:
~~~~~~~~~~~~~~~~~~~~~~
Describe events that will cause this shot group to be enabled/disabled, in this case we are using Ball_Started and Ball_Ending.


Related Events
--------------

.. include:: /events/include_shot_groups.rst
