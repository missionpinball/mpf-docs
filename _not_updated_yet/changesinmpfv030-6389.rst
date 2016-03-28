
The next version of MPF will be v0.30. It's currently in active
development and is expected to be released in March with a preview
available in a few weeks. (`Details here.`_) The latest code for MPF
v0.30 is in the *dev* branch in GitHub which is available `here`_. The
latest *dev* code for MPF_MC (the MPF media controller) is available
`here`_. Neither of these two projects are ready for public use, but
you can check the commits to see what we're working on. We have been
very busy, with lots of commits every day to both projects. This
document was last updated Mar 4, 2016



Release Schedule
----------------

We hope to have a preview release of MPF 0.30 available by March 7.
We're hoping to get the final release out by March 31. Of course these
schedules may change depending on what comes up, but those are our
goals at this point.



What's new & changed in MPF 0.30
--------------------------------



Big Changes
~~~~~~~~~~~


+ Moved to Python 3.4 (from Python 2.7)
+ Separated the media controller component (mpf-mc) into a separate
  project. This way you won't have to download all the media controller
  prereqs if you're using the Unity media controller.
+ Completely rewritten media controller (like, from scratch), based on
  Kivy. (No more Pygame.) This is able to leverage the GPU, play modern
  video formats, and is all-around faster, better, and nicer than
  before.
+ Created a proper installer and registered it with PyPI, so you can
  install MPF simply by running `pip install mpf`.
+ Completely rewritten config file migrator that can now save comments
  and white space. This means the config migrator can now do everything.
+ Changed the way MPF starts. "mpf" is registered with your system, so
  you just switch to your machine folder and just run "mpf" to load that
  machine in MPF (or "mpf mc" to run the media controller, or "mpf
  migrate" to migrate your config files, etc.)
+ Light scripts have been combined into shows, and now shows are
  powerful and can be used to control anything (lights, LEDs, slides,
  sounds, coils, GI, etc.) Also you can put placeholder "tokens"
  anywhere in a show which are replaced in realtime with the parameters
  you pass to the show to run. (That's how shows replace light scripts,
  except they're much more powerful now because they work with anything,
  not just lights and LEDs.)




Other changes
~~~~~~~~~~~~~


+ New RGB Color class that supports other color layouts (HSV, HSL) and
  hardware LEDs that are not in RGB order (like BGR). Also named colors
  are supported, and you can redefine color names dynamically.
+ LED smooth fades which can be done in hardware, software, or both.
+ New MPF clock class replaces the existing timer_tick, events, and
  tasks in a way that is much more flexible and "smooths out" the CPU
  processing across the main loop.
+ Shows are changed from "tocks" to real-world time, with show steps
  that can be in absolute time or delta time (with mix-and-matching in
  shows)
+ All graphics can now use the GPU which gives us massive performance
  improvements and lowers CPU utilization.
+ Completely rewritten audio interface which supports all the
  important pinball concepts like ducking with custom per-sound ramps.
+ Completely rewritten asset manager which includes support for asset
  pools (one asset can have multiple files under the hood, so a single
  sound request can randomly return a sound from a pool, for example).
+ Display widgets can be added to existing slides, making display
  components easier to re-use (rather than having to build completely
  new slides all the time.)
+ Support for accelerometer-based tilts.
+ Ball search.
+ Servo support.
+ Improved ball device logic which makes it harder for MPF to get
  confused about where balls are.


.. _here: https://github.com/missionpinball/mpf_mc/tree/dev
.. _here: https://github.com/missionpinball/mpf/tree/dev
.. _Details here.: https://missionpinball.com/blog/2016/02/progress-towards-mpf-0-30-and-our-release-testing-plan/


