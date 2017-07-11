Sound & Audio Tips & Tricks
===========================

This page contains a collection of miscellaneous tips and tricks when working with the sound &
audio features in MPF.

Review ``max_queue_time`` Settings for Long Sounds/Music
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``max_queue_time`` settings for sounds can lead to some unexpected behavior, especially for
longer sounds (like music).  This setting specifies the maximum time a sound can be queued before
it's played. On a track that supports only a single sound at a time (like a typical music track),
playing a sound with a priority that is less than or equal to the currently playing sound will
have to wait until the current sound is finished (it will be added to the queue).  That may be
acceptable to you, but you may also be surprised when you hear the sound a minute or two later.

It is suggested you review all your ``max_queue_time`` settings to make sure they make sense for
the sound and situation in which they will be played.  The default setting of ``None`` means the
sound will eventually be played, no matter how long the wait in the queue is.  A value of ``0``
specifies the sound will be immediately discarded if the track is already busy playing its
maximum number of sounds.  A value of ``2 secs`` specifies the sound will wait in the queue for
2 seconds to be played before being discarded. Sound effects for things like slingshots and pop
bumpers probably don't make much sense if they are played more than 250 milliseconds after they
are hit so setting ``max_queue_time`` to a value between ``0`` and ``250 ms`` is recommended.
On the other hand, an extra ball callout is probably fine to play a few seconds after the ball
is earned. Go through your sounds and consider how to set this setting for each one.

For more information, see the :doc:`sounds </config/sounds>` documentation.

Synchronizing Sound With an LED Show
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The key to synchronizing an LED show with a music track is to determine at what times in the sound
file you want events (such as LED color changes) to occur. There are many ways to do this, but here
are a few suggestions:

+ Use your favorite sound or editing software to open your music track and place markers in all the
  locations where you want LED changes to occur. This may take some trial and error and listening
  to portions of your music over and over again until you get it right.  Once your markers are in
  place, export them to a text file (if your software supports it), or write down the times of each
  marker. Use the times as step times in your show and assign the LED settings you want in each
  step. This is a bit of a tedious process, but should give you nice synchronization when the show
  is played at the same time as the music track (you can even put the sound play action in the
  first step of your show). I work on a PC and use Sony Sound Forge for sound editing, but there
  are many good editors available on every platform that support inserting markers.  Here is a
  screenshot of the process in the editor I use:

  .. image:: images/sound_editor_markers.png

  This feature is also available in `Audacity <http://www.audacityteam.org>`_ (free open-source
  cross-platform sound editing software) and many video editing packages.

+ As an alternative, you can determine the tempo of your song in beats per minute (BPM) and from
  that number calculate the time for each beat.  Once you have the time for each beat, you can
  use it to calculate various show step times (assuming you want LED changes to occur on the beat).
  There are some tools out there that will calculate the BPM of your song for you, but are not
  always very accurate depending upon the content of your song.

For more information on creating shows for your LED, see the :doc:`Shows </shows/index>`
documentation

Pausing Background Music While a Video is Playing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


With the addition of the new :doc:`track_player </config/track_player>` config player in 0.32, it
is now possible to control audio tracks using MPF events. One common use of this new functionality
is to pause your music track while you play a video and resume the music when the video is
finished playing.

The basic concept is to add an event to the video that is triggered when the video is played and
one when the video is stopped.  Those events are then added to the ``track_player`` section of
your config file:

::

    track_player:
        my_video_is_playing:
            music:
                action: pause
                fade: 1 sec
        my_video_has_stopped:
            music:
                action: play
                fade: 1 sec

That's all there is to it.  Now whenever the ``my_video_is_playing`` MPF event is posted, the
music track will be paused.  It will be resumed when the ``my_video_has_stopped`` MPF event
is posted.

