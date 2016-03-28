
You use the `sounds:` section of your configuration file to specify
additional non-default settings for any soundsyou want to use in your
game. (This section can be in your machine configuration files for
machine-wide assets and/or a mode-specific config file for mode-
specific assets.) This sectioncan be used in your machine-wide config
files. This sectioncan be used in your mode-specific config files.
Note: You do *not* have to have an entry for every single soundyou
want to use, rather, you only need to add individual assets to your
config file that have settings which different from other assets in
that asset's folder. (See the ` `asset_defaults:``_ section for
details. Also be sure to read the section on `Managing Assets`_ for an
overview of how assets work.) Here’s a example:


::

    
    sounds:
        jackpot:
            volume: 2
            track: voice
        ball_launch:
            volume: 1.1


Since Soundsare just a type of Asset in MPF, there are a few config
settings that are generic which apply to all types of assets, so read
the `reference documentation on Assets`_ for details about how the
name, `file:`, and `load:` settings work. Then on top of the defaults,
soundshave several sound-specific settings: (These are all default
settings for each sound. Many can be overridden when the sound is
actually played.)



track:
~~~~~~

This is the name of the track this sound will play on. (You configure
tracks and track names in the ` `sound_system:``_ section of your
machine config files.) You can specify the name of a standard track or
the name of your streaming track.



volume:
~~~~~~~

The volume offset of this sound, expressed at a number between 0 and
2. This value is factored into the track and overall MPF volumes. It's
used to "balance" your sounds if you have one particular sound that's
too loud or too quiet. A value of `1` (the default) means this sound
plays at normal volume. `0.5` means it plays at 50%, `1.5` means it
plays at 150%. The max value here is 2. Anything higher than 2 will be
reset to `2`.



max_queue_time:
~~~~~~~~~~~~~~~

An `MPF time string`_ which specifies the maximum time this sound can
be queued before it's played. If the time between when this sound is
requested and when MPF can actually play it is longer than this queue
time, then the request is discarded and the sound doesn't play. This
only comes into playifthis sound is requested but the track it's
playing on is at its `max_simultaneous` limit. Then if this sound
doesn't have a high enough priority to kill any of the existing
sounds, it will be queued to play later. Some sounds (like voice
callouts) might be ok to queue, but other sounds (like sound effects
for when you hit a pop bumper or slingshot) might only make sense if
they're played right away, so in those cases you might want to use a
short (or no) queue time. The default setting is "None" which means
this sound will have no queue limit and will always play eventually.



max_simultaneous_playing:
~~~~~~~~~~~~~~~~~~~~~~~~~

Not yet implemented.



fade_in:
~~~~~~~~

Not yet implemented.



fade_out:
~~~~~~~~~

Not yet implemented.



loops:
~~~~~~

Not yet implemented.



start_time:
~~~~~~~~~~~

Not yet implemented.



end_time:
~~~~~~~~~

Not yet implemented.

.. _reference documentation on Assets: https://missionpinball.com/docs/configuration-file-reference/assets/
.. _Managing Assets: https://missionpinball.com/docs/managing-assets/
.. _asset_defaults:: https://missionpinball.com/docs/configuration-file-reference/assetdefaults/
.. _sound_system:: https://missionpinball.com/docs/configuration-file-reference/soundsystem/
.. _MPF time string: https://missionpinball.com/docs/configuration-file-reference/entering-time-duration-values/


