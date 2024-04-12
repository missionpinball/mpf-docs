---
title: GMC Sounds
---

# Sound Playback in GMC

All sounds in GMC are managed through Godot, but MPF can be used to trigger playback actions through the `sound_player` config settings.

All sound files (including resource files) must be placed in either a */sounds* folder in the project root, or in */modes/<mode_name>/sounds* folder in any mode. Subfolders within these folders are allowed as well.

## Sound Resources: Files, Native, and Custom Types

GMC supports playback of sounds from a variety of different resource types interchangably. This allows you to quickly and conveniently play back back sounds from file reference, while also allowing custom sound behavior and advanced sound features by referencing a Godot resource file.

### Direct File Playback

If you just want to play a sound, you can reference that sound by its file name (without extension) in the `sound_player`.

For example, if you have files in your project called *frenzy_background_music.ogg* and *small_explosion_one.wav* you could trigger those sounds with the following config:

``` yaml

    sound_player:
        mode_frenzy_started:
            frenzy_background_music:
                bus: music
                fade_in: 500ms
                fade_out: 1s
        drop_targets_complete: small_explosion_one

```

### MPFSound Resource

GMC includes a custom class called `MPFSound` that provides properties that can be saved to a resource file. When this resource is played, the playback properties are read from the file and don't need to be passed as part of the `sound_player` config.

This is a convenient way to keep the same settings for a sound file without having to specify it every time it's called in `sound_player`.

More details on can be found on the [MPFSound Reference Doc](reference/mpf-sound.md).

### Other Godot Resources

Any Godot class that derives from [`AudioStream`](https://docs.godotengine.org/en/stable/classes/class_audiostream.html) can also be used as a sound resource as long as its in one of the *sounds* folders.

[**AudioStreamRandomizer**](https://docs.godotengine.org/en/stable/classes/class_audiostreamrandomizer.html#class-audiostreamrandomizer) can be used to create a sound pool with randomized playback of any number of sounds, and/or randomized pitch and volume for quick variations on a base set of sounds to reduce repetition.

[**AudioStreamPolyphonic**](https://docs.godotengine.org/en/stable/classes/class_audiostreampolyphonic.html#class-audiostreampolyphonic) can be used to stack multiple playbacks of the same sound in a single stream rather than instantiating a separate sound playback instance for each one.

[**AudioStreamSynchronized**](https://docs.godotengine.org/en/latest/classes/class_audiostreamsynchronized.html#class-audiostreamsynchronized) *(coming in Godot 4.3)* can be used to layer and synchronize multiple sound files for seamless playback mixing.

[**AudioStreamPlaylist**](https://docs.godotengine.org/en/latest/classes/class_audiostreamplaylist.html#class-audiostreamplaylist) *(coming in Godot 4.3)* can be used to create playlists of sound files that can be played back, shuffled, cross-faded, and looped.