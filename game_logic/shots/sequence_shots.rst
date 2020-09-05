Sequence Shots
==============

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/sequence_shots`                                                |
+------------------------------------------------------------------------------+

A sequence of switches which need to be hit in order with a timeout.

This is an example:

.. code-block:: mpf-config

   switches:
     s_ramp_entry:
       number: 1
     s_ramp_success:
       number: 2
   sequence_shots:
     ramp:
       switch_sequence: s_ramp_entry, s_ramp_success
       sequence_timeout: 3s
   ##! test
   #! mock_event ramp_hit
   #! hit_and_release_switch s_ramp_entry
   #! assert_event_not_called ramp_hit
   #! hit_and_release_switch s_ramp_success
   #! advance_time_and_run 1
   #! assert_event_called ramp_hit

When both switches are hit in sequence ``ramp_hit``
(:doc:`/events/sequence_shot_hit`) will be posted.
You can use that event to trigger further logic/shows/etc.

Using Sequence Shots in Shot Groups
-----------------------------------

Sequence shots got shots in their name but they cannot be used in
:doc:`shot_groups <shot_group>`.
If you want to use them in a shot groups create a
:doc:`shot </config/shots>` which is triggerd on the
:doc:`/events/sequence_shot_hit` event.

This is an example:

.. code-block:: mpf-config

   switches:
     s_ramp_entry:
       number: 1
     s_ramp_success:
       number: 2
   sequence_shots:
     ramp:
       switch_sequence: s_ramp_entry, s_ramp_success
       sequence_timeout: 3s
   ##! mode: test_mode
   # In your mode
   shots:
     shot_ramp:
       hit_events: ramp_hit
   shot_groups:
     your_group:
       shots: shot_ramp
   ##! test
   #! start_game
   #! start_mode test_mode
   #! mock_event ramp_hit
   #! mock_event shot_ramp_hit
   #! mock_event your_group_complete
   #! hit_and_release_switch s_ramp_entry
   #! assert_event_not_called ramp_hit
   #! hit_and_release_switch s_ramp_success
   #! advance_time_and_run 1
   #! assert_event_called ramp_hit
   #! assert_event_called shot_ramp_hit
   #! assert_event_called your_group_complete

Related How To guides
---------------------

* :doc:`/mechs/loops/index`

Related Events
--------------

.. include:: /events/include_sequence_shots.rst
