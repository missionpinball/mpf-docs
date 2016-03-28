
In this How To guide, we're going to cover how you can setup a ball
device to lock balls towards multiball, and then how to actually start
the multiball. We'll also make sure that the locked balls are stored
on a "per-player" basis, which means this will all work even if one
player starts a multiball and empties out the ball device that was
holding the locked balls.



(A) Understanding the concepts
------------------------------

In this guide, we're going to assume that you have a ball device on
your playfield that is capable of holding multiple balls. Whenever a
ball enters a ball device, it posts an event called
*balldevice_<device_name>_ball_enter*. That event is posted as a
“relay” event which means it passes arguments (“balls” in this case).
A relay event means that each handler has the opportunity to
manipulate the args by returning some value which is different than
the value that came in, and that returned value is then passed to
additional handlers. It’s kind of like passing a token around that
handlers can change. So in the case of the ball device, it posts that
event along with the number of new balls, and if no registered
handlers “claim” that ball (by returning a token of fewer balls), then
the ball device just ejects it. So in your case, I see that the
bathtub is not configured as a ball device, probably because it was
just ejecting the ball right away and you wanted to lock it. So I
would add a method called “ball_entered_bathtub” or something which
you would register as a handler in your mode_start for
balldevice_bathtub_ball_enter” along with a “balls” parameter. Doing
this is nice BTW because you can use the settling time and everything
from the ball device rather than having to write that yourself. So
then in your ball_entered_bathtub method, you would have something
that checked the balls paramter to see how many balls entered, you
subtract the number you want to keep, and you end that method by with
something like this:


::

    
    return {'balls': 0}


(more details on relay methods are here:
`https://missionpinball.com/docs/mpf-core-architecture/events/`_) So
that will keep the ball in the bathtub, essentially locking it. Then
if you want to kick out another ball, you can call:


::

    
    self.machine.playfield.add_ball()


That will automatically kick another ball into play. There are
parameters you can use to specify how many balls, and the device, etc.
but by default it will be 1 ball from a ball device tagged with
‘ball_add_live’. (And if that’s your plunger lane, it will
automatically get one from the trough.) Now if you want the player to
manually hit the launch button, you need to call that with a
“trigger_event” parameter which would be the name of any event you
want which will trigger the ball to add. So that could be a tag
(sw_plunger) for example, like this:


::

    
    self.machine.playfield.add_ball(trigger='sw_plunger')


Now, notice that at no point yet did we increase the “balls in play”
count, since while you’re locking balls, there’s still only ever one
in play. So you can do this to lock the second ball too. For the third
ball lock, you’d want to add some logic that checks how many balls are
locked in your method that responds to a ball entering the bathtub.
(still return balls:0 so the bathtub doesn’t kick it out automatically
so you can play your slide show or whatever.) Then when that’s done,
change the balls_in_play to 3:


::

    
    self.machine.game.balls_in_play = 3


And then loop through ejecting them all one-by-one (which you can do
with the ball device logic, like this):


::

    
    self.machine.ball_devices.bathtub.eject()


Or you can eject multiples like:


::

    
    self.machine.ball_devices.bathtub.eject(3)


Or:


::

    
    self.machine.ball_devices.bathtub.eject_all()


Now.. what about multiple players with multiple locks? That’s where
you’d need to move to using a player variable to track the locked
balls instead of the physical count, which I see you have in your
code, so that’s great. So here’s putting it all together. This code is
very untested and I just dumped it our here, but you get the gist:


::

    
    def mode_start(self):
        ...
        self.add_mode_event_handler('balldevice_bathtub_ball_enter', self.ball_entered_bathtub)
        ....
    
    def ball_entered_bathtub(self, balls, **kwargs):
        self.player.lsb_balls_locked += 1
    
        if self.player.lsb_balls_locked == 3:
            self.start_multiball()
        else:
            self.machine.playfield.add_ball(trigger='sw_plunger')
    
        return {'balls': 0}
    
    def start_multiball(self):
        self.player.lsb_balls_locked = 0
        self.machine.game.balls_in_play = 3
        balls_from_trough = 3 - self.machine.ball_devices.bathtub.balls
        self.machine.ball_devices.bathtub.eject_all()
        self.machine.playfield.add_ball(balls_from_trough)


In your actual code you might add in a bunch of events to trigger
shows and slides and stuff, and you might have those shows call events
which move things along to the next step, but I think this shows the
gist of it? (And you have a diverter in there which I’m ignoring too..
but you get the idea?) BTW there are events for the number of balls in
play with paramters, so you could hook that and check to see if
there’s only one ball in play and end whatever scoring you have for
this multiball mode and stuff. So I need to write a tutorial but in
some ways I think I just did. :)

.. _https://missionpinball.com/docs/mpf-core-architecture/events/: https://missionpinball.com/docs/mpf-core-architecture/events/


