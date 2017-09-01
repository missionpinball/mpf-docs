How to setup sound for your machine
===================================

This guide explains the basic steps to setup sound for your machine. Sound support is part of the
MPF media controller and only available if you're using MPF-MC for your media controller.  Please
ensure your system is properly setup to play sound (drivers are installed and configured) before
proceeding with this guide.

1. Configuring the `sound_system`
---------------------------------

The first step in the process of setting up sound for your machine is to setup the
``sound_system:`` section of your machine configuration file (see
:doc:`sound_system: </config/sound_system>` for more detailed information).  Generally you can
just use the default values for the settings in the section.  However, you do need to define the
tracks the sound system will use.  Tracks can be thought of as channels on an audio mixer with
their own volume and other settings.  The example below shows a typical pinball machine sound
setup with three tracks: *music*, *voice*, and *sfx*.  The ``simultaneous_sounds:`` setting controls
how may sounds may be played at the same time on each track.  It is recommended that you only
allow one music and one voice clip to be played at a time and that many sound effects (sfx) can
be played simultaneously so that is what we have configured in the example below.

Example:

::

    sound_system:
        master_volume: 0.75
        tracks:
           music:
              type: standard
              simultaneous_sounds: 1
              volume: 0.5
           voice:
              type: standard
              simultaneous_sounds: 1
              volume: 0.7
           sfx:
              type: standard
              simultaneous_sounds: 8
              volume: 0.4

2. Configuring your sound asset folders
---------------------------------------

The next step is to configure your sound asset folders.  First you will need to create a folder
named ``sounds`` directly under your machine folder.  The recommended way to organize your sound
files is to create sub-folders for each track in the ``sounds`` folder (``music``, ``sfx``, and
``voice``). If you are going to be using a lot of sounds you can create as many sub-folders
beneath each track folder as you like. It can help you stay organized and be able to locate your
sounds.

File system directory structure example:

::

    machine_folder
        sounds
            music
            sfx
            voice

Now that our sound asset folders have been created, it's time to let MPF know where to look for
sound files when it starts and what basic settings to apply to each sound it finds.  This is done
by adding a ``sounds:`` section to the ``assets:`` section in our machine configuration file. The
example below illustrates what this should look like in your machine configuration file.  The
``default:`` setting contains the default settings that should be applied to all sound assets.
In this example below, ``load:`` should be assigned a value of ``on_demand`` for all sound assets.
Next we enter a setting for each sub-folder located in our ``sounds`` directory and specify the
settings we want applied to each sound asset found in those sub-folders.  In our case we have
created sub-directories for each track and want the sounds contained in them to play on their
respective tracks (*music*, *sfx*, and *voice*) so we set the ``track:`` setting accordingly.

``assets:`` section in machine configuration file:

::

    assets:
        sounds:
            default:
                load: on_demand
            music:
                track: music
            sfx:
                track: sfx
            voice:
                track: voice

When your machine launches, the asset manager will now search for supported audio files in the
specified directories and assign the proper settings to each file it finds.  We're well on our
way to actually hearing some sound!

3. Put some sounds in your sound folders
----------------------------------------

You probably don't need much assistance with this obvious step, but let's go through the process
anyway just in case.  As of version 0.33, MPF supports 16-bit .wav (Wave), .ogg (Ogg Vorbis), and
.flac (FLAC) audio files (we hope to add other formats in future releases such as .mp3).  Locate
some supported audio files and place them in the appropriate track folders that you created in the
previous step (a good site to find free public domain sounds is
`www.freesound.org <http://www.freesound.org/>`_). Put all music files in the ``music`` folder,
voice callouts in the ``voice`` folder, and all other sound effects in the ``sfx`` folder.

4. Additional configuration for selected sounds
-----------------------------------------------

Now when you start your machine you will have some sounds available (assuming you placed some
supported sound files in your folder during the last step) and they will all have some very basic
default settings.  It is very likely that you won't be happy with the default settings for all of
your sounds so let's create some more tailored settings for a few of them.

Renaming some sounds
~~~~~~~~~~~~~~~~~~~~

Your sounds now all have names based on their file names (without the extensions), and by default
that is how they must be referenced in your config files.  Perhaps some of your file names are
either a bit cryptic or contain additional text that you'd like to shorten.  One option is to
simply rename any files you'd like in the operating system.  Another option is to setup some
configuration options in your config files to reference the sound file by a different name which
is what we will do next.

I downloaded a triangle sound from `www.freesound.org <http://www.freesound.org/>`_ that has an
undesirable filename: ``22783__franciscopadilla__80-mute-triangle.wav``.  I would rather just refer
to it in my config files as ``triangle`` and not ``22783__franciscopadilla__80-mute-triangle``
(which is what it will be by default).  In my ``sounds:`` section of my machine configuration file
(see :doc:`sounds: </config/sounds>` in the documentation for more details) I can put the following
text:

::

    sounds:
        triangle:
            file: 22783__franciscopadilla__80-mute-triangle.wav

That simple configuration change will allow the sound as to be referred to as ``triangle`` wherever
you refer to that sound in other configuration locations. *Note*: be sure to include the complete
file name, including the extension when using the ``file:`` setting.

Setting the volume of a sound
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A very common adjustment to make is to set the volume for each and every sound you load in your
machine.  This allows you to balance out sounds from various sources rather than trying to adjust
the levels in each sound file using audio editing software.  Building on the example above, let's
set the volume of the *triangle* sound in our config file:

::

    sounds:
        triangle:
            file: 22783__franciscopadilla__80-mute-triangle.wav
            volume: 0.85

``volume:`` controls the volume of the sound and works in conjunction with the track volume and the
master volume.  Volume can either be entered as a number between 0.0 and 1.0 or as a decibel level
(see :doc:`Instructions for entering gain values) </config/instructions/gain_values>` for more
information).  You will probably have to spend some time adjusting the volumes of many sounds in
your machine to get everything to sound just the way you want it.

*Note:* If you hear distortion in your sounds when they are played back in a mix, be sure to try
lowering the volume as you may be experiencing clipping.

Other sound settings
~~~~~~~~~~~~~~~~~~~~

There are many other settings you may wish to change for some sounds in your machine.

+ How do you cause your sound to loop 3 times every time it is played?  Add ``loops: 3`` to the
  config section for your sound. How do you loop a sound indefinitely? Add ``loops: -1``.
+ How do you adjust the which sounds can preempt other sounds and how long a sound may wait to be
  played before it is discarded?  Use the ``priority:`` and ``max_queue_time:`` settings.
+ How do you send events to MPF when a sound begins or finished playing?  Use the
  ``events_when_played:`` and ``events_when_stopped:`` settings.
+ What about ducking? Just what is it anyway?  Learn about :doc:`ducking </sound/ducking>` in the
  documentation.

The documentation for the :doc:`sounds: </config/sounds>` configuration section contains further
information about all these settings.

Example ``sounds:`` configuration demonstrating most common settings:

::

    sounds:
        triangle:
            file: 22783__franciscopadilla__80-mute-triangle.wav
            volume: 0.85
            max_queue_time: 0
        laser:
            volume: 0.5
            loops: 3
            max_queue_time: 0
        extra_ball:
            file: extra_ball_12753.wav
            events_when_started: extra_ball_callout_started
            events_when_stopped: extra_ball_callout_finished
            volume: 0.8
            priority: 50
            max_queue_time: None
            ducking:
                target: music
                delay: 0
                attack: 0.3 sec
                attenuation: 0.45
                release_point: 2.0 sec
                release: 1.0 sec
        slingshot_01:
            volume: 0.5
            max_queue_time: 0
        song_01:
            volume: 1.0
            priority: 100

5. Hooking up an MPF event to play a sound
------------------------------------------

Now that your sounds have been setup and are available in your machine, the next step is to
configure them to be played.  The sound player was designed to do just this (associate a sound
action, such as play or stop, with an MPF event).  The sound player can be configured in either
the machine configuration file, a mode configuration file, or even in a show step (or in all of
them).  To keep things simple here, let's configure the sound player in the machine configuration
file.

The scenario in this example is we want our song from the previous example (``song_01``) to play
infinitely when the *attract* mode starts and stop when the *attract* mode stops.  Create the
following entries in the ``sound_player:`` section of the machine config file:

::

    sound_player:
        mode_attract_started:
            song_01:
                action: play
                loops: -1
        mode_attract_stopped:
            song_01:
                action: stop

That's it.  The ``song_01`` sound will be played on the music track whenever *attract* mode is
started and will stop whenever *attract* mode is stopped.  The ``mode_attract_started``
section refers to a standard MPF event that is sent whenever a mode named *attract* is started
and ``mode_attract_stopped`` is a standard MPF event that is sent whenever a mode named *attract*
is stopped.  For more information, see the :doc:`sound_player: </config_players/sound_player>`
documentation.

Finished
--------

Congratulations!  You have completed your the basic sound system setup and should have some simple
audio playing in your machine.

References
----------

+ :doc:`Sound & Audio </sound/index>`
+ :doc:`Ducking </sound/ducking>`
+ :doc:`Tips & tricks </sound/tips_tricks>`
+ :doc:`sound_system: </config/sound_system>`
+ :doc:`sounds: </config/sounds>`
+ :doc:`sound_player: </config_players/sound_player>`
+ :doc:`Instructions for entering gain values </config/instructions/gain_values>`

