ball_search_stopped (MPF event)
===============================

The ball search process has been disabled. This event is posted any time ball
search stops, regardless of whether it found a ball or gave up. (If the ball
search failed to find the ball, it will also post the *ball_search_failed*
event.)

Keyword arguments: None
