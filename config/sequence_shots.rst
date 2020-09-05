sequence_shots:
===============

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

.. overview

The ``sequence_shots:`` section of your config is where you configure switch or
event sequences which should trigger an event.

A *sequence_shots* is a device with multiple
switches to hit, in order, for the sequence_shots to be registered as
being hit/completed. You can optionally specify a time limit for these switches (i.e.
the sequence must be completed within the time limit) with the ``sequence_timeout:``
setting.

When the first switch in a sequence is activated, the sequence_shot
will start watching for the next one. When that one is activated, it
looks for the next, and so on. Once the last switch is activated, the
shot is considered "hit" and the device posts ``your_sequence_shot_hit`` (if
your shot is called ``your_sequence_shot``).

.. code-block:: mpf-config

   #! switches:
   #!   top_right_opto:
   #!     number:
   #!   left_rollover:
   #!     number:
   #!   top_center_rollover:
   #!     number:
   sequence_shots:
     left_orbit:
       switch_sequence: left_rollover, top_right_opto
       sequence_timeout: 3s
     weak_right_orbit:
       switch_sequence: top_right_opto, top_center_rollover
       sequence_timeout: 3s

Notice in the example above that there are
two different shots with the same switches, but the order of the
switches is inverted between the two. This is because the *left orbit*
and *right orbit* shots in this machine use the same two switches, but
the order the switches are activated in dictates which shot was just
made.

Shots in MPF are able to track multiple simultaneous sequences
in situations which is nice when multiple balls are on the playfield.
If the first switch in a sequence is hit twice before the sequence
completes, MPF will start tracking two sequences. Then when the next
switch is it, it will only advance one sequence. If the next switch is
hit again, it will advance the other sequence. But if the next switch
is never hit a second time, then the second shot will not complete.

Here is an example with events:

.. code-block:: mpf-config

   sequence_shots:
     my_event_based_sequence_shot:
       event_sequence:
         - event1
         - event2
         - event3
       cancel_events: cancel
       delay_event_list:
         delay1: 1s
       sequence_timeout: 3s

And one with switches:

.. code-block:: mpf-config

   #! switches:
   #!   seq2_1:
   #!     number:
   #!   seq2_2:
   #!     number:
   #!   seq2_3:
   #!     number:
   #!   seq2_cancel:
   #!     number:
   #!   seq2_delay:
   #!     number:
   sequence_shots:
     my_switch_based_sequence_shot:
       switch_sequence:
         - seq2_1
         - seq2_2
         - seq2_3
       cancel_switches: seq2_cancel
       delay_switch_list:
         seq2_delay: 1s
       sequence_timeout: 3s

.. config


Optional settings
-----------------

The following sections are optional in the ``sequence_shots:`` section of your config. (If you don't include them, the default will be used).

cancel_events:
~~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

Those events will cancel the current sequence. Same as ``cancel_switches`` but with events.

cancel_switches:
~~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: string name of a :doc:`switches <switches>` device. Defaults to empty.

A switch (or list of switches) that will cause any in-progress switch
sequence tracking to be canceled. (Think of it like a cancel "abort"
switch.) If you enter more than one switch here, any of them being hit
will cause the sequence tracking to reset. If MPF is currently
tracking multiple in-process sequences, a cancel_switch hit will
cancel all of them.

delay_event_list:
~~~~~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

Events which will temporarily prevent new sequences from starting. Same as ``delay_switch_list`` but with events.

delay_switch_list:
~~~~~~~~~~~~~~~~~~
One or more sub-entries. Each in the format of string name of a :doc:`switches <switches>` device : ``time string (ms)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`)

Switches which will temporarily prevent new sequences from starting.
This lets you specify a switch along with a time value that will
prevent this shot from tracking from being hit. In other words, the
shot only counts if the delay_switch was *not* hit within the time
specified.

event_sequence:
~~~~~~~~~~~~~~~
List of one (or more) events. The device will add handlers for those events. Defaults to empty.

A sequence of events which will complete the sequence.

playfield:
~~~~~~~~~~
Single value, type: string name of a :doc:`playfields <playfields>` device. Default: ``playfield``

The playfield this sequence is on.

sequence_timeout:
~~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Default: ``0``

Timeout starting when the sequence starts (e.g. after the first switch was hit).
This is the time limit the switches in the ``switch_sequence:`` section have to
be activated in, from
start to finish, in order for the sequence to be hit/completed. You can enter
values with "s" or "ms" after the number, like `200ms` or `3s`. If you
just enter a number then the system assumes you mean seconds. If you
do not enter a time, or you enter a value of 0, then there is no
timeout (i.e. the player could literally take multiple minutes between
switch activations and the shot would count.)

switch_sequence:
~~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: string name of a :doc:`switches <switches>` device. Defaults to empty.

A sequence of switches which will complete the sequence.

console_log:
~~~~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level for the console log for this device.

debug:
~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

Set this to true to see additional debug output. This might impact the performance of MPF.

file_log:
~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level for the file log for this device.

label:
~~~~~~
Single value, type: ``string``. Default: ``%``

Name of this device in service mode.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Defaults to empty.

Not used.


Related How To guides
---------------------

* :doc:`/game_logic/shots/sequence_shots`
* :doc:`/mechs/loops/index`
