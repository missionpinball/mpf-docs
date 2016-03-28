Show format
===========
Shows are defined via nested key/value pairs in YAML files. You can define shows in the ``shows:`` section of a regular
machine or mode config file, or you can define them in their own standalone files. It makes no difference from a
functional standpoint--it's purely up to you and a matter of preference. (We tend to create small simple shows in
existing config files and make bigger shows their own standalone files.)


::

   - time: 0
     leds:
       led1: red
   - time: +1
     leds:
       led1: off
   - time: + 1

Separating steps
----------------
Every step is separated with a dash.

Setting step time
-----------------
The time for each step represents the time when that step *starts*. The first step will always be ``time: 0``

If you just enter a number for the *time*, that number represents seconds. However, you can enter the time in
standard MPF time format, which could be ms, secs, etc. The following are all valid *time* entries:

* ``time: 1`` (1 second)
* ``time: 1.0`` (1 second)
* ``time: 1s`` (1 second)
* ``time: 1000ms`` (1 second)

When shows are played, it's possible to specify a *speed* setting which is a multiplier for how fast the
show is played. The default is ``1.0`` which would use the time values entered here, but keep in mind that it's
possible to play a show back at any speed. You can even change the speed of a running show.

.. note:: The precision of shows is limited to clock speed that MPF runs at. By default, MPF runs at 60fps, which
   means that each "tick" of MPF is about 16ms. So in that case, you can't get resolution of shows more precise than
   that.

Absolute time
~~~~~~~~~~~~~
The time value for each step indicates when this step will play referenced from the start of the show. This is
useful if you're syncrhonizing show steps with sound of video.

Relative time
~~~~~~~~~~~~~
Sometimes it's more convenient to specify the timing of a step in a show relative to the step before it. To do
that, enter the *time* value with a + in front of it, like this:

::

   time: +1

Note that you can mix-and-match incremental and absolute times in the same show, and you can also combine the plus
sign for relative times with seconds or millisecond values. For example:

::

  - time: 0  # plays right away, at 0 seconds
    ...
  - time: +1  # plays 1 sec after the previous, 1 sec after show start
    ...
  - time: +1  # plays 1 sec after the previous, 2 secs after show start
    ...
  - time: 4  # plays 4 seconds after show start, 2 secs after the previous
    ...
  - time: +1  # plays 1 sec after the previous, 5 secs after show start
    ...

Setting the duration of the last step
-------------------------------------
Since the time values of shows control the timing of when a step starts, you need to add a final step with no actions to
the end of your show which controls the duration of the final step.

If you don't do this, then your final step will appear to be skipped since the show will repeat or end end as soon as
the last step is played.
