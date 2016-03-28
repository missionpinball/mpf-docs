
The `volume:` section of your machine config file specifies several
things, including:


+ The names of the audio tracks in your machine.
+ The default volume settings for each track.
+ How many "steps" you want between 0 (off) and full volume.


This sectioncan be used in your machine-wide config files. This
section *cannot* be used in mode-specific config files. There's a
default volume: configuration in the machine-wide `mpfconfig.yaml`
default file. This should be fine for most cases, though you can
change it here if you want to do something different.


::

    
    volume:
        tracks:
            master: 20
            voice: 20
            sfx: 20
            music: 20
        steps: 20


Note that all audio is controller via the standalone media player. So
these MPF core engine volume settings only control what MPF sends to
the media controller via BCP. The media controller handles the actual
processing of the volume changes.



tracks:
~~~~~~~

This is a list of track names along with the default (initial power-
on) volume settings for each. By default, MPF uses four tracks:


+ `master:` the overall volume of the entire machine
+ `voice:` a track which playsall voice callouts
+ `sfx:` a track which plays sound effects
+ `music:` a track which plays the continuous background music




steps:
~~~~~~

This is simply how many steps you want between the volume at zero
(off, or mute) and full volume. Internally MPF uses 100 steps, but you
probably don't want to actually have 100 because itwould be really
annoying to have to hit the volume up or volume down key so many
times. 20 is probably fine for most cases.



