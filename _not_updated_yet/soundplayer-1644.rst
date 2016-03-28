
You can use the `sound_player:` section of your config file to
configure sounds to automatically play based on certain `MPF events`_.
This sectioncan be used in your machine-wide config files. This
sectioncan be used in your mode-specific config files. Here's an
example:


::

    
    sound_player:
        intro loop:
            sound: intro_loop
            start_events: ball_starting
            stop_events: ball_live_added
            duration:
            loops: -1
            priority:
            fade_in: 0
            fade_out: 0
            volume: 1
        this level entry can be whatever you want:
            sound: ball_launch_motorcycle
            start_events: balldevice_shooterLaneR_ball_eject_attempt
        slingshot:
            sound: crime 12
            start_events: shot_Slingshot
        anything you want:
            sound: main_loop
            start_events: player_eject_request
            loops: -1
            stop_events: ball_ending


To use the Sound Player, add a `sound_player:` section to your config
file. Then create sub-entries from each sound/event combination you
want. Note that the actual name of each sub-entry doesn't really
matter. What matters is the sound and events in the entry. So for each
sub entry, there are two required settings:



sound: (required)
~~~~~~~~~~~~~~~~~

The name of the sound object that will play. Note that this is *not* a
file name, rather, it's the name of the sound in MPF.



start_events: (required)
~~~~~~~~~~~~~~~~~~~~~~~~

Alist of one (or more) MPF events that will cause this sound to play.
You can separate them with commas, or enter one event on each line if
you start each line with a dash. More details on how to enter lists
into config files is `here`_.



stop_events:
~~~~~~~~~~~~

A list of events that will cause this sound to stop playing.



duration:
~~~~~~~~~

Not yet implemented.



loops:
~~~~~~

The number of times this sound will loop. (So `0` means it plays once,
`1` means it plays twice because it loops once, etc.) Enter a value of
`-1` to have it just loop forever until one of the `stop_events` is
posted. Default is 0 which means it just plays once and stops.



priority:
~~~~~~~~~

The relative priority this sound will be played at. For
`sound_player:` settings in mode config files, this priority will be
added to the mode's base priority. The priority is only used ifthe
track the sound isplaying on is currently playing its max number of
simultaneous sounds. If so, the new sound will replace one of the
existing sounds if the the new sound has a higher priority than the
lowest priority current sound. Otherwise the new sound will be added
to the queue and played when the next available slot is free. By the
way, if you find that you have too many sounds cutting off other
sounds, then you can increase the `max_simultaneous_sounds` value for
that track.



fade_in:
~~~~~~~~

Not yet implemented.



fade_out:
~~~~~~~~~

Not yet implemented.



volume:
~~~~~~~

A value of how loud this sound should play, between 0 and 2. The
volume you configure here is mixed in with the track and overall MPF
volume. A value of 1 (the default) plays the sound at the full normal
volume. 0 is mute. 0.1 would be 10%, 1.5 would be 150%, etc. Max value
is 2.

.. _MPF events: https://missionpinball.com/docs/events/
.. _here: https://missionpinball.com/docs/configuration-file-reference/adding-lists-and-lists-of-lists-to-config-files/


