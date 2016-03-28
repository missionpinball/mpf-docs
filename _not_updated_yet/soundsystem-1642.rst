
The `sound_system:`section of the machine config file controls the
general settings for the machine's sound system. This sectioncan be
used in your machine-wide config files. This sectioncan be used in
your mode-specific config files. Here's an example:


::

    
    sound_system:
        buffer: 512
        frequency: 44100
        channels: 1
        initial_volume: 1
        volume_steps: 20
        tracks:
            voice:
                volume: 1
                priority: 2
                simultaneous_sounds: 1
                preload: no
            sfx:
                volume: 1
                priority: 1
                preload: no
                simultaneous_sounds: 3
        stream:
            name: music
            priority: 0
            
    




buffer:
~~~~~~~

This is the size of your sound buffer. It must be a power of 2.If you
leave this setting out (or set it to `auto`), then MPF will
automatically pick a buffer size. The exact value you use will take
some trial-and-error. A bigger buffer means that there's less chance
of skipping and dropout, but it also means that sounds can take longer
to play since the buffer has to fill first. We use the value of 512 on
the BeagleBone Black and it seems fine. Sounds are still instant as
far as we can tell, and we don't have problems with skipping. Some
people have run with a buffer of 4096 or 8192 or 16384, others at 512
or 256. So just play with it and see what works for you.



bits:
~~~~~

This is the number of bits (8-bit for 16-bit) for your sound. You need
to enter the number as negative for signed values. Probably you should
never use this, which is why it's not included in the example config
file above. Just leave it out.



frequency:
~~~~~~~~~~

How many sound samples per second you want. 44100 is so-called "CD
quality" audio, though with the sound systems in most pinball
machines, if you cut it in half (to 22050) it still sounds the same.
If you're running on a resource-constrained host computer, you should
make sure all your sound files are encoded at the same rate so MPF
doesn't waste time re-encoding them on the fly. Smaller values mean
smaller sound files, less memory consumption, and less CPU processing.
So if you're on a resource constrained host computer, think about
22050 instead of 44100. (But be sure to resample all your sound files
to match.)



channels:
~~~~~~~~~

The number of channels the sound system will support. 1 for mono, 2
for stereo. You're probably thinking, "aww man, I need stereo sound!"
But almost no pinball machines do this since the speakers in the
backbox are 2 feet apart and they're 4 feet away from the player's
ears. (Maybe if you're going to use headphones or put tweeters in the
front of the machine?) Again, if you have a resource-constrained
system, then go for mono and make sure all your sound files are mono.
If not, meh, go ahead and use stereo.



initial_volume:
~~~~~~~~~~~~~~~

The initial MPF overall volume, represented as a number between 0 and
1. 1 is max volume, 0 is off, .9 is 90%, etc. Note that this only
controls the volume of the MPF app, not the host OS'es system volume.
So you still need to make sure that the host OS is not on mute and
that the volume is turned up.



volume_steps:
~~~~~~~~~~~~~

This is the number of steps of volume you want when you present the
volume controls to the operator or player. For example, a value of
`20` means that the volume of a machine at full will show to the
player as "20", and then as they turn it down it will step through,
19, 18, etc. Note that this setting does not affect the internal
volume. (That's still always a value between 0 and 1.) The
`volume_steps:` setting only affects how it's displayed to the player.



tracks:
~~~~~~~

Every sound that's played in MPF is played on a track. Each track can
have it's own settings, and you can set volume on a per-track basis.
The example above shows two tracks, called *voice* and *sfx*. The idea
(in case it isn't obvious) is that you play all your voice callouts on
the voice track and the sound effects on the sfx track. To create a
track, add a sub entry to the `tracks:` section which will be the name
of that track. (So again, `voice:` and `sfx:` in the example. Then
create one or more of the following settings for each track:



volume:
```````

This is the volume offset for this track, as a value between 0 and 1.
A value of 1 (the default) means that this track plays at full volume.
Note that each track's volume will be combined with the overall system
volume. So if your MPF overall volume is set to .8 (80%) and you have
a track set to .5 (50%),sounds on that track will play at 40% overall
volume (50% of 80%).



priority:
`````````

The relative priority of this track. This feature is not really
implemented yet, but it will be used in the future to control tracks
automatically getting quieter (called "ducking" in the audio world)
when higher priority tracks are playing. (For example, you might want
the sound effects track to lower its volume when voice callouts are
playing.)



simultaneous_sounds:
````````````````````

This sets the maximum number of simultaneous sounds that can be played
on this track. The example config file above shows the *voice* track
with a max of 1 simultaneous sound playing, since if you have two
voice callouts playing at the same time, it will sound like gibberish.
A sound effects track, on the other hand, can probably have a few
sounds playing at once. Note that MPF gives you detailed control over
what happens if a new sound wants to play when the max simultaneous
sounds are already playing on that track. Should the new sound break
in and stop an existing sound? Should it wait until the existing sound
is done? How long should it wait? You can control all this.



preload:
````````

Controls whether the sound files for this track should be preloaded
into memory when MPF starts up. Preloading sounds means they're
available to play instantly, but it also means that those sounds will
always be consuming memory. Whether you preload sounds depends on how
many sounds you have and how much memory your computer has. This
preload setting only sets the default for the track. You can choose to
override it on a sound-by-sound basis. (So if you set preload to
"False" (or "no") here, you can still choose to preload a few key
sounds when you set up your sounds. Note that if a sound is not
preloaded, it can still play—it's just that MPF has to load it from
the disk first. Again, whether that's bad or not depends on your
computer. If you have an SSD you can probably get away without
preloading any sounds and they'll all play fine.



stream:
~~~~~~~

This setting lets you configure a "stream" track which is a special
kind of track which streams sound files from disk as they're being
played instead of loading the complete sounds into memory. The catch
is that you can only stream a single sound file at a time. (This is a
limitation of SDL which is what MPF's sound system is based on.) In
practice, the stream track works great for background music since
those files are long (and would therefore take up a lot of memory),
and you only ever have one background sound playing at a time.
Specific settings for the stream track include:



name:
`````

The name of the streaming track which you'll use later when you want
to control which track each sound plays on.



priority:
`````````

The relative priority of this track. Again, this setting doesn't
really do anything right now.



