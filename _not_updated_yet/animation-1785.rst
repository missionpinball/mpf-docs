
The *Animation*`display element`_ is used to display and play an
animation. Details on how to load animationsare in the configuration
file reference for the ` `Animations:`section`_. Animationdisplay
elements use the same `positioning & placement settings`_ as other
display elements. There are also animation-specific settings,
including:



animation: (required)
~~~~~~~~~~~~~~~~~~~~~

The string name of the animationyou want to play.



start_frame:
~~~~~~~~~~~~

What frame number the animation should start on. The first frame is
Frame 0. Default is 0.



fps:
~~~~

How many frames per second the animation will play at. Default is 10,
but that default is completely arbitrary and you really should set
this to whatever your animation is meant to be played at.



repeat:
~~~~~~~

True/False as to whether this animation repeats when it reaches the
end. Default is False.



drop_frames:
~~~~~~~~~~~~

True/False which controls whether this animation should drop frames if
it gets behind. If True, the animation will always stay "current",
even if it has to skipsome frames to stay on time. If False, the
animation will play every frame, even if it means that it slows down.
Default is True.



play_now:
~~~~~~~~~

True/False as to whether this animation should start playing
immediately. If False, the animation will load and display the
start_frame and wait to be played manually. Default is True.



width:
~~~~~~

Used to change the width of the animation. Not yet implemented.



height:
~~~~~~~

Used to change the heightof the animation. Not yet implemented.

.. _display element: https://missionpinball.com/docs/displays/display-elements/
.. _ placement settings: https://missionpinball.com/docs/displays/display-elements/positioning/
.. _section: https://missionpinball.com/docs/configuration-file-reference/animations/


