
The *Movie* `display element`_ is used for playing MPEG-1 movies to
the display. This is typically used for background loops or for cut
scenes. The animation and movie display elements are similar.
Animations can have transparencies and would typically be used for
characters or foreground objects, or for DMD animations where the file
size isn't too big. Note that today *MPF can only play movies encoded
in MPEG-1 format* . This is due to a limitation of Pygame (the Python
multimedia library that MPF uses). At this point it's easy enough to
use ffmpeg to convert whatever movies you want to play to the MPEG-1
format that MPF needs. Also note that the * Movies module is not
available on the Mac *. This is also due to Pygame, as the Mac version
of Pygame does not support movies. We will be moving MPF off of Pygame
in late 2015, but until then, you can only use MPEG-1 movies and can
you can't use movies on the Mac. Details on how to load movies are in
the configuration file reference in the ` `movies:``_ section. Movie
display elements use the same `positioning & placement settings`_ as
other display elements. There are also movie-specific settings,
including:



movie: (required)
~~~~~~~~~~~~~~~~~

The string name of the movie you want to play.



repeat:
~~~~~~~

True or False. (Or yes/no). If True, the movie will loop.



play_now:
~~~~~~~~~

Whether the movie should start playing right away, or whether it
should start paused and wait to be told when to start playing.



start_frame:
~~~~~~~~~~~~

The frame number you want the movie to start on. Default is 0. (The
beginning.)

.. _display element: https://missionpinball.com/docs/displays/display-elements/
.. _movies:: https://missionpinball.com/docs/configuration-file-reference/movies/
.. _ placement settings: https://missionpinball.com/docs/displays/display-elements/positioning/


