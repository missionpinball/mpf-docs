---
title: Loops / Orbits / Ramps
---

# Loops / Orbits / Ramps


Related Config File Sections:

* [sequence_shots:](../config/sequence_shots.md)
* [sound_player:](../config/sound_player.md)

Ramps, loops or orbits usually contain two switches. One at the entry
and one to signal success. To detect only shots where both switches were
hit in order you can use
[sequence_shots](../config/sequence_shots.md).

[TODO: Add a picture of an orbit](../about/help.md)

``` mpf-config
switches:
  s_ramp_entry:
    number: 1
  s_ramp_success:
    number: 2
sequence_shots:
  ramp:
    switch_sequence: s_ramp_entry, s_ramp_success
    sequence_timeout: 3s
```

Additionally, most machines usually play a sound once the entry is hit
to signal the player that he hit the ramp and another sound on success
to indicate that the ball made it. You can use
[sound_player:](../config/sound_player.md) to achieve that. In
this example you would use the events `s_ramp_entry_active` and
`ramp_hit` to play the sounds:

``` mpf-config
sound_player:
  s_ramp_entry_active: indicate_ramp
  s_ramp_success: indicate_ramp_success
```
