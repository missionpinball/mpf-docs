
Audio and sound support is handled via the a plug-in called the Sound
Controller (in `/mpf/plugins/sound.py`). All audio files are played
back via Pygame—arequiredadd-on module for Python that MPF also uses
for its display system and the on screen window. The basic concept
with audio in MPF is that you collect all your audio files (.wav or
.ogg) and put them in the `/sounds`folder in your machine folder. Then
in your config file you create entries for each sound which map a
friendly name to the actual file on disk. You can also set a bunch of
defaults for each sound, such as volume offset, start time, etc. Then
when you want to play a sound in a game, you can refer to it by the
friendly name from your configuration file. You can also add entries
into your configuration file to set up sounds so they play based on
certain MPF events. (For example, play the sound "laser" every time
the event from a pop bumper being hit is posted.) You can also add
sounds to your show files so they play in-sync with lighting and
display effects. As we said, the current sound support is pretty
basic, but we have future plans for a lot of stuff, including: You
also have the option to setup multiple "tracks" for sound. Maybe you
have one track for background music, one for voice callouts, and one
for sound effects. Then when you play a sound you can specify which
track it will play on, and MPF will use the properties of the track to
make sure it plays properly. (The sound effects track might allow
multiple sounds to be played at once, while the voice track would want
to make sure only one sound is playing at a time.) You configure your
sound system in the ` `sound_system:``_section of your machine
configuration file. You add settings for individual sound files in the
` `sounds:``_section, and you can configure sounds to automatically
play when certain MPF events are posted in the `
`sound_player:``_section.

.. _sounds:: https://missionpinball.com/docs/configuration-file-reference/sounds/
.. _sound_player:: https://missionpinball.com/docs/configuration-file-reference/soundplayer/
.. _sound_system:: https://missionpinball.com/docs/configuration-file-reference/soundsystem/


