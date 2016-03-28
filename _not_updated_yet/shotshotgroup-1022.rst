
Broadly speaking, a shot is anything the player shoots at during a
game. It could be a standup target, a lane, a ramp, a loop, a drop
target, a pop bumper, a toy, etc. Many shots in MPF have lights or
LEDs associated with them that indicate what “state” the shot is in.
(e.g. “shoot the flashing targets” or “hit the lit ramp” could mean
“hit the target that’s in the *flashing* state”, or “hit the ramp
that’s in the *lit* state”.) Shots in MPF are similar to other devices
we’ve worked with (like autofires and ball devices) where you group
together switches, lights, and/or LEDs into the things we call
*shots*. (Not every shot has a light or LED associated with it.) You
can even configure shots that are based on series of switches that
must be hit in the right order within a certain time frame. For
example, you might have an orbit shot with three switches:
*orbit_left*, *orbit_top*, and *orbit_right*. You could configure one
shot called *left_orbit* that’s triggered when the switches
*orbit_left*, *orbit_center*, and *orbit_right* are hit (in that
order) within 3 seconds, and you could configure a second shot called
*right_orbit* that’s triggered when the switches *orbit_right*,
*orbit_center*, and *orbit_left* are hit within 3 seconds. (So, same
switches, but two different shots depending on the order they’re hit.)
You can also group multiple shots together into a shot group. For
example, you might have three lanes at the top of your playfield, each
with a rollover switch and a light. In that case you’d configure each
of them as a separate shot. Then you could create a shot group that
grouped all three of the shots together into a logical group. A shot
group lets you do cool things, like trigger an event when all of the
member shots are in the same state (increase Bonus X when all three
shots are “lit”), and you can setup things like “shot rotation” that
rotates the state of the member shots left or right (lane change via
the flipper buttons, for example).



