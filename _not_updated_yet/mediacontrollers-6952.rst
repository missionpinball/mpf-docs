
The MPF project separates out the "`core engine`_" from the "media
controller." These are literally two completely separate processes
that run. (So when you "run MPF" on your computer, you'll actually
have two programs running at the same time—the MPF core engine and a
media controller.) The game engine and the media controller talk to
each other via a TCP socket with a protocol we invented called "BCP"
(for "`Backbox Control Protocol`_"). Here's a diagram that shows what
the MPF game engine is responsible for versus what the media
controller is responsible for: ` `_



Media Controller Options
------------------------

When you use MPF, there are currently two media controller options.


+ There's a built-in Python-based media controller that we call "The
  MPF Media Controller." This is the default option that most people
  use. You can use this for DMD or LCD-based games, and it can play high
  def video and work with HD displays.
+ There's an advanced media controller based on Unity 3D which you can
  use if you want complete control over the display and audio
  experience. Using this option requires programming and knowledge of
  Unity 3D.




.. _core engine: https://missionpinball.com/docs/mpf-game-engine/
.. _Backbox Control Protocol: https://missionpinball.com/docs/mpf-core-architecture/media-controllers/bcp1-0-spec/


