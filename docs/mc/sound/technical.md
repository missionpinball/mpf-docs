---
title: MPF Sound & Audio Technical Overview
---

!!! warning "MPF-MC is being deprecated"

    This instruction page is for the legacy MPF-MC for MPF versions 0.57 and prior. For users of MPF 0.80 and later, please refer to the [Godot Media Controller (GMC) Documentation](../../gmc/index.md)

# MPF Sound & Audio Technical Overview


The MPF MC Audio Interface is a custom audio Python extension library
with features designed to support common pinball sound requirements. It
is written on top of the SDL2, SDL_Mixer, and GStreamer libraries that
are installed with Kivy which is required to run the MPF MC software (no
additional installs necessary for the audio library).

![image](images/technical_overview.png)

The SDL2 library (<https://www.libsdl.org/>) is responsible for all
low-level communications with the system audio hardware. The user
selects the basic audio interface settings: sample rate, output
channels, and buffer size (defaults are provided). These settings are
used to initialize the SDL2 library which then negotiates with the
system audio hardware to create a connection that is as close to the
desired settings as possible. The SDL2 library is responsible for
creating the main audio thread and calling the main audio callback
function at a fast enough rate to provide audio buffers to the hardware
without any gaps in playback. It also provides the thread
synchronization and protection utilized in the audio library through its
mutex-related functions. The audio library also uses the SDL2 audio
format conversion functions to convert between various low-level audio
formats to communicate with the system sound hardware.

SDL_Mixer (<https://www.libsdl.org/projects/SDL_mixer/>) is an add-on
library for SDL2 that provides basic audio mixing, sound loading and
playback, and sound streaming capabilities. The MPF MC audio interface
does not use the mixing features of SDL_Mixer. Instead, it only utilizes
the sound file loading functions of the library.

GStreamer (<https://gstreamer.freedesktop.org/>) is an open source,
cross-platform pipeline-based multimedia framework that links together a
wide variety of media-handling components (including simple audio
playback, audio and video playback, recording, streaming and editing) to
complete complex workflows. The MPF MC audio interface uses GStreamer
for all its sound file loading functions and real-time audio streaming.
All audio is fed into SDL2 for final output.

The audio interface is divided into
[tracks](tracks.md), which are
analogous to channels on an audio mixer. There are multiple types of
audio tracks, each with its own specialized feature set. The output of
each track is mixed together and fed to the SDL_Mixer track via the
custom music player function. The audio mixing engine uses 16-bit
integer calculations and brickwall limiting to ensure there are no
numeric overflows (and their resulting distortion). All of the sound
generation and mixing functions are C functions (written in Cython) that
run in the SDL2 audio thread.

It is important to understand the threading models of both SDL2 and
Python to avoid common threading problems. Python supports multiple
threads, however it uses a mechanism called the "global interpreter
lock" (GIL) to ensure that only one thread runs in the Python
interpreter at once. This simplifies many low-level details. SDL2
creates its own audio thread in which to receive and process audio data
and send it to the audio hardware. As this audio thread is not a Python
thread, it does not interact with the GIL and therefore is unable to
access any Python objects within its context. This means that only C
types and data structures may be utilized in the SDL2 audio callback
function; no Python objects can be used. Because the MPF MC is a Python
application, a Python extension library is the only choice in which to
use the GStreamer, SDL_Mixer and SDL2 libraries. Since the extension
library utilizes both Python and C objects, the GIL needs to be managed
in the audio library along with thread protection to avoid race
conditions and deadlocks. These design constraints led to the choice of
using Cython (<http://cython.org/>) as the language to implement the MPF
MC audio library. Cython is a superset of the Python language that
additionally supports calling C functions and using C types, an ideal
choice for wrapping external C libraries and using them in a Python
application.

Sounds are MPF assets and are created by the MPF asset loader. The
actual sound loading code is contained in the audio library and is
performed by SDL_Mixer and GStreamer. A Python container object wraps
the C object returned by the loading process. This wrapper allows the
sound data to be managed by a Python object. The audio library extracts
the C object when necessary and passes it to the audio thread where it
can be used to generate audio.

The [sound_player:](../../config_players/sound_player.md) enables MPF events to trigger sound actions, such as play,
stop, and stop looping. It is a config_player and runs as a plug-in in
MPF and also creates event handlers in MPF MC. The audio library also
generates MPF events for various sound events (sound played, stopped,
looping, etc.) and sends them to MPF via BCP.
