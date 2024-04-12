---
title: MPFSoundAsset
---

# MPFSoundAsset

`MPFSound` is a Godot Node class provided by the MPF-GMC extension. It provides the same options as `sound_player` for configuring playback, with the convenience of coding those options once rather than on each `sound_player` call.

In the Godot Editor *FileSystem* panel, find an appropriate *sounds* folder and right click to *Create New > Resource > MPFSoundAsset*. Choose a name for the sound that you'll use to call it from `sound_player` and save the file.

!!! note "Sound name uniqueness"

    Each sound resource needs a unique name so GMC can find it when referenced by `sound_player`. It's okay to create an MPFSoundAsset and save it with the same name as the sound file. GMC maps all sound files first and then all resources, so a resource with the same name will override the sound file.


## Node Configuration

In the *Inspector* tab on the right side, you can configure the `MPFSoundAsset` with these options.

!!! note

    Options configured in the `MPFSoundAsset` will be the defaults for this sound, but can be overridden with values in `sound_player` for different behavior when needed.

### file:

Single value, type: `Resource`. Default: `None`

This is the sound file or sound resource that will be played for this sound's name. It can be a single sound file (WAV, OGG), or any `AudioStream`-based resource in the project (`AudioStreamRandomizer`, `AudioStreamPlaylist`, etc).

### bus:

Single value, type: `String`. Default: `None`

The name of the bus this sound will play on.

### fade_in:

Single value, type: `float`. Default: `0.0`

The number of seconds over which this sound will fade in when it is played.

### fade_out:

Single value, type: `float`. Default: `0.0`

The number of seconds over which this sound will fade out when it is stopped.

### start_at:

Single value, type `float`. Default: `0.0`

The timecode (in seconds) where playback of this sound should start when it is played.

## Methods

`MPFSoundAsset` does not have any public methods exposed.