Using "modes" to implement game logic
=====================================

One thing I found is that I tend to use modes as a sort of “super” logic block.
For example, the VC rules have a “manager’s choice” shot that leads to a ball
device. When the shot is lit, one of three things happens depending on what else
is going on (one for base game mode, another for when multiball is active, and a
third which is a timed mode). The shot may me lit or unlit in any of those three
scenarios, and the action I’m talking about should only happen when it’s lit,
otherwise it just scores some points and kicks out the ball.

I realized pretty quickly that the easiest way to handle this is to create a
mode called “managers_choice_lit” which is used to light the shot regardless of
what else is happening. When that mode starts, it enables the shot, turns on the
light, shows a slide that says the shot is lit, etc. I created a start event
“light_managers_choice” which is easy to post from wherever else I need in the
game to light the shot.

Then in order to handle the various chains of events that happen when that shot
is actually made, I created three more modes:

•	managers_choice_base (priority 301)
•	managers_choice_timed (priority 302)
•	managers_choice_multiball (priority 303)

Each of these modes looks for the managers_choice lit hit shot event and then
will do their award thing. What’s cool is they also each block the shot from the
lower down modes. This means that these shots can be stacked and running in any
various combination.

So the managers_choice_base mode is running at all times (with a start event of
ball_starting). That’s safe to run because it doesn’t do its award action unless
the managers choice lit hit event happens, and that shot is enabled in the
managers_choice_hit mode. In other words, managers_choice_base mode can be
running at all times, but it will only award the shot if the managers_choice_lit
mode is running.

Then if managers_choice_timed or managers_choice_multiball is running, they also
do their award thing based on the managers_choice lit hit shot event, so they
also can run any time but will not award the shot unless the managers_choice_lit
mode is running.

And since those two higher modes block the shot from lower modes, this means
that I don’t need complicated if/then logic to figure out which of the three
award options should be awarded when the shot is lit and hit.

And since the managers_choice_hit mode acts as an on/off switch for whether the
shot will be awarded, this means that I can safely start the
managers_choice_timed mode any time any other timed mode is running, and I can
start the managers_choice_multiball mode anytime multiball play is going on, and
they’ll each only do their award if the base managers_choice_lit is running and
the shot is made.


