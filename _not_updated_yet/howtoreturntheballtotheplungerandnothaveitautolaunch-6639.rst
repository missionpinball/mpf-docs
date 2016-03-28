
Some pinball machines have an option where a diverter or other shot
can return the ball to the plunger lane. By default, MPF will auto
launch any balls that enter devices that are not configured for some
"action" to handle the ball, so if you have an eject coil in your
plunger lane and a ball goes there during a game, MPF will eject that
ball. This How To guide explains how you can change that behavior. In
it, we'll assume the ball device is called *plunger*, though in your
machine you'd change that to whatever your plunger device is called.
(A) Setup your mode code This functionality requires custom mode code,
so if you haven't set that up for the mode where you want this to
happen, do that now. (This doesn't have to be a special mode per se.
You could add it to your base game mode.) (B) Add an event handler to
look for the ball entering the plunger. In the mode_start() method of
your mode code, add an event handler to watch for a ball entering your
plunger device. Then in that handler, you'll return {'balls': 0} which
will tell MPF that your code is "claiming" the ball that just entered.
(You're literally changing the value of "unclaimed" balls to zero.
This is like telling MPF, "Hey. It's ok. I got this."


::

    
    def mode_start(self, **kwargs):
        self.machine.events.add_handler(
            event='balldevice_plunger_ball_enter',
            handler=self._ball_entered_plunger)
    
    def _ball_entered_plunger(self, **kwargs):
        self.machine.ball_devices['plunger'].setup_player_controlled_eject()
        return {'balls': 0}


(C) Setup the new player eject request



