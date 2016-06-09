Sound & Audio Tips & Tricks
===========================

This page contains a collection of miscellaneous tips and tricks when working with the sound &
audio features in MPF.


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

  .. image:: sound_editor_markers.png

  This feature is also available in `Audacity <http://www.audacityteam.org>`_ (free open-source
  cross-platform sound editing software) and many video editing packages.

+ As an alternative, you can determine the tempo of your song in beats per minute (BPM) and from
  that number calculate the time for each beat.  Once you have the time for each beat, you can
  use it to calculate various show step times (assuming you want LED changes to occur on the beat).
  There are some tools out there that will calculate the BPM of your song for you, but are not
  always very accurate depending upon the content of your song.

For more information on creating shows for your LED, see the :doc:`Shows </shows/index>`
documentation

