Video widget
============

The video widget is used to display a video on a :doc:`slide </displays/slides/index>`.
This can either be full-screen videos or smaller videos that appear on a portion of the
display.

Note that in MPF, videos are regular widgets, so they can go on top of other widgets, or
other widgets can go on top of them, they can be moved and animated, etc.

Settings
--------

.. code-block:: yaml

   type: video
   video:
   height:
   width:
   volume:
   auto_play:
   end_behavior:
   control_events:

.. note:: Video widgets also have "common" widget settings for position, opacity,
   animations, color, style, etc. Those are not listed here, but are instead covered in
   :doc:`common widget settings </displays/widgets/common_settings>` page.

Also remember that all widget settings can be controlled via
:doc:`widget styles </displays/widgets/styles>`, rather than
you having to set every setting on every widget.

type: video
~~~~~~~~~~~

Tells MPF that this is an image widget

video:
~~~~~~

The name of the video asset this widget will show. Details on video
assets are :doc:`here </assets/videos>`.

height:
~~~~~~~

Allows you to specify the size (along with ``width:`` of the video on the screen). Set to
``0`` (or leave this setting out) to play the video at whatever size the asset is configured
for (or, if a size is not specified there, at the native video size).

Note that the ``height:`` and ``width:`` settings cannot stretch or skew the video. So if
you enter values that result in an aspect ratio for the video widget that does not match
the video itself, then the video will be sized as large as it can within the bounds of
the size of the widget.

width:
~~~~~~

Lets you specify the width of the video. Set to ``0`` (or leave the setting out) to use
the setting from the video asset and/or the native video width.

See the ``height:`` setting above for details.

volume:
~~~~~~~

Volume for this video on a scale from ``0`` to ``1``. Default is ``1.0``. Note that you
can the volume during playback via the ``control_events:`` below.

.. note::

   Currently the video volume and playback is not integrated with the rest of MPF's sound
   system in terms of tracks, ducking, etc. This is on our roadmap.

auto_play:
~~~~~~~~~~

Boolean (True/False or Yes/No) which controls whether this video should start playing
automatically. Default is ``True``.

end_behavior:
~~~~~~~~~~~~~

Sets what happens when the video ends. Options include:

``loop``
   The video loops and starts playing again

``pause``
   The video stops and stays at the end (so it continues showing the final frame)

``stop``
   The video stops and the position is reset back to the beginning. This is the default.

control_events:
~~~~~~~~~~~~~~~

Control the playback of this video with MPF events. Options include:

``play``
   Starts playing the video from its current position.

``pause``
   Pauses the video at its current position.

``stop``
   Stops the video and resets the position back to the beginning.

``seek``
   Moves the video to a certain position based on a percentage. ``0`` is the beginning
   of the video, ``1`` is the end, ``0.5`` is 50% through, etc. (This is similar to
   ``position:``, except it's based on percent instead of position.

   This setting does not change the play/stop state.

``position``
   Moves the video to a certain position based on the time, (in seconds). In other words
   ``value: 4.2`` here would move the video to the 4.2 second mark. (This is similar to
   ``seek:`` except it's based on seconds instead of percent.)

``volume``
   Sets the volume of the video on a scale from ``0`` to ``1``.

   This setting does not change the play/stop state.

To use control events, add a ``control_events:`` section to the video widget, then create
a list (with dashes) of ``event:``, ``action:`` and (optionally) ``value:`` settings. Then
when the event is posted, the action will be applied to the video.

Consider the example below:

.. code-block:: mpf-config

   slides:
     my_slide:
       - type: video
         video: my_video
         control_events:
           - event: play_my_vid
             action: play
           - event: wizard_caught
             action: stop
           - event: some_event
             action: pause
           - event: what_event
             action: seek
             value: .5
           - event: move_it
             action: position
             value: 4.2
           - event: mute_me
             action: volume
             value: 0

In the example above, when the event *play_my_vid* is posted, the video will start playing.
When the event *wizard_caught* is posted, the video will stop. *some_event* will pause the video,
*what_event* will reset the video to the 50% position, *move_it* will set the video to the
4.2 second position, and *mute_me* will set the volume to zero.

Note that you can have as many different entries as you want here, even using different
events for the same actions, etc.
