---
title: MPFVideoPlayer
---

# MPFVideoPlayer

`MPFVideoPlayer` is a Godot Node class provided by the MPF-GMC extension. It holds a video file for playback and provides convenient controls for end-of-video behavior.

## Node Configuration

An `MPFVideoPlayer` node can be placed anywhere in a slide or widget and offers the following custom properties.

### hide_behavior:

Single value, one of `"Restart"`, "`Pause`", `"Continue"`. Default: `"Restart"`

This behavior is triggered when the video player visibility changes (either directly or from an ancestor node's visibility).

#### `"Restart"`:

When the video is not visible, playback stops. When the video becomes visible again, playback restarts from the beginning.

#### `"Pause"`:

When the video is not visible, playback is paused. When the video becomes visible again, playback resumes from where it left off.

#### `"Continue"`:

The video will play regardless of whether it is visible or not.

### end_behavior:

Single value, one of `"Nothing"`, `"Remove Slide/Widget"`, `"Post Event"`. Default `"Nothing"`

This behavior is triggered when the video playback finishes and the video is not set to loop.

#### `"Nothing"`:

When the video finishes playing, no special behavior will occur.

#### `"Remove Slide/Widget"`:

When the video finishes playing, the slide or widget that holds this `MPFVideoPlayer` will be removed automatically.

#### `"Post Event"`:

When the video finishes playing, the event *video_finished* will be posted to MPF. This is in addition to any event configured in the `events_when_finished` option.

### events_when_stopped:

Multiple values, type: `String`. Default `None`.

When the video finishes playing, custom events can be posted to MPF. Enter the name of the event here, or multiple events separated by commas. The event(s) will be posted in addition to the `end_behavior` action.

## VideoStreamPlayer Node Configuration

Because `MPFVideoPlayer` extends from the base Godot `VideoStreamPlayer` node, the standard video parameters can be used and the most pertinent ones are detailed below.

### audio_track:

Single value, type `integer`. Default `0`

If the video stream has multiple audio tracks, you can specify which one to be played with this video.

### stream:

Single value, type `VideoStream`. Default `None`.

This is the video file that will be played by the video player. Use the *Quick Load* option to find a video in your project folder.

### volume_db:

Single value, type `integer`. Default `None`.

The volume this video should play at. `0db` is the standard volume level, and `-80db` is silent. Note that this value is mixed into the audio bus the video is playing on.

### autoplay:

Single value, type `boolean`. Default `false`.

If checked, this video will begin playing immediately when it is added to the scene tree and visible.

If `hide_behavior` is "continue", it will play immediately even if not visible.

### expand:

Single value, type `boolean`. Default `false`.

If checked, this video will scale to fill the size of the `MPFVideoPlayer` node. You can manually position and size the video player node to your liking, or let it inherit from its parent container.

If unchecked, the video will play at its native resolution. You will not be able to adjust the size of the video player node.


### loop:

Single value, type `boolean`. Default `false`.

If checked, this video will loop playback.

### bus:

Single value, type `AudioBus`. Default `Master`.

The audio bus that this video's audio will play on. This affects the video's playback level as its volume is mixed into the selected bus, and ducking effects applied to the bus will apply to the video as well.

## Methods

`MPFVideoPlayer` does not have any public methods exposed, but custom methods can be added to scene scripts that extend `MPFVideoPlayer`.