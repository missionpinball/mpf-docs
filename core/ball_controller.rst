Ball Controller
===============

The Ball Controller is responsible for knowing where all the balls in the
machine are at any given time. It lives in the *mpf/core/ball_controller.py*
module. The ball controller keeps track of which balls are in which ball
devices, how many balls are known and are missing, and tracking balls that drain
from the playfield. The ball controller also makes sure that all the balls are
in their "home" positions before a game can start, and it's responsible for
moving balls into position as needed.
