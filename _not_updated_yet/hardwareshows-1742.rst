
A hardware show is a show that takes place using pinball machine
hardware, including lights, LEDs, drivers (coils), GI, and/or
flashers. You'll ultimately have dozens (or maybe even hundreds) of
shows in your machine. Some of them might be simple, like when you
complete a final shot in a shot group then all of the group's lights
flash in sequence. Other shows will be complex, like when the player
hits wizard mode and everything is rocking out like crazy. The key to
remember with shows is that you can have multiple shows playing at
once. So something that might seem super complex at first could
actually be ten little shows all running at the same time rather than
one huge show. (This is also nice because then all your little shows
become sort of like "building blocks" you can combine in different
ways for future shows.) For example, the attract mode in a lot of
machines might look really complex at first, but if you break it down,
it's not too bad. For example, a typically attract mode might be built
of up lots of individual shows, such as:


+ A bunch of lights in a row cycle through in a pattern. That's one
  show.
+ A different group of lights in your lower lanes might pulse back and
  forth in their own pattern. That's another show.
+ A "wheel" of lights in the center of the playfield could rotate in
  their own show.
+ The DMD might display a series of text frames and animations (high
  scores, push start, logo of the machine and your company, etc.) That
  could be its own show.
+ You might have some sound effects that play during the attract mode
  every so often. Those could be their own show with two steps that
  repeat forever. (Step 1. Wait ten minutes. Step 2. Play sound.
  Repeat.)


You create show files in a YAML format (similar to your machine
configuration files) which you then put in a "shows" folder inside
your machine's folder. Then when you run MPF, all those shows are
loaded so you can play them at any time. Features of shows include:


+ A showcontroller handles playing, pausing, stopping, and resetting
  shows. One show controller for hardware shows runs in the MPF game
  engine, and another show controller for media shows runs in the MPF
  media player.
+ Add matrix lights, RGB LEDs, display information, sounds, events,
  and coil actions to each step of your show.
+ Play multiple shows at the same time. Play/pause/stop/restart
  individual ones, etc.
+ Play show files at any speed, including changing the playback speed
  of a show on the fly while it's playing. This means if you have a
  "wheel" of lights that you want to rotatefaster and faster, you only
  have to make one show yaml file and then you can keep on changing the
  playback rate.
+ Set repeats, like whether the show should play forever, or whether
  it repeats a fixed number of times and then stops.
+ Configure playlists (lists of shows). Each step in the playlist can
  be made up ofone or more shows, and you have precise control over how
  it moves to the next step. (After x seconds, after one of the shows
  plays through x times, etc.)
+ Set whether a show "blends" with whatever's running below it. So
  imagine you have an light that is on solid red, and then you play a
  show at a higher priority that flashes that same light between blue
  and off. If you have blend enabled, then when the light in the higher
  priority show is off, whatever the light wasset to in the lower
  priority show will "show through." (So you'd have the effect of the
  light alternating between red and blue.) If you have blend to False,
  then when the higher priority show turnsthat light off, it will be
  "off." In that case the light would flash between red and off.) If
  you're fading an light between off and a color, and you have
  enabledblending, then the fade will blend between whatever color is
  below it. It's very cool!
+ Specify the relative priority of a show, so if there areever two
  running shows that want to set the same light at the same time, the
  higher priority one will win. (The priorities only affect lights and
  LEDs, not show events or coils.)
+ Specify what happens when a show ends. Do the lights stay on in
  their last setting? Are they reset?


So now let's look at how you actually create a show file.



