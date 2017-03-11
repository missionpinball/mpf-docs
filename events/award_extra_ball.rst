award_extra_ball
================

*MPF Event*

This is an event you can post which will immediately award the
player an extra ball (assuming they're within the limits of max
extra balls, etc.). This event will in turn post the
extra_ball_awarded event if the extra ball is able to be awarded.

Note that if you want to just light the extra ball, but not award it
right away, then use the :doc:`award_lit_extra_ball` event instead.

Also note that if an extra ball is lit, this event will NOT unlight
or decrement the lit extra ball count. If you want to do that, use the
:doc:`award_lit_extra_ball` instead.

*This event does not have any keyword arguments*
