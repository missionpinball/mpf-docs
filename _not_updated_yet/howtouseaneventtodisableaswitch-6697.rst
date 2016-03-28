
Question from the forum:
I have a coil that can be fired by either switch A or switch B.
However, if the drop bank is completed, then I need to disable switch
A until switch B is triggered. Then it reverts back to using either
switch again. Also, the coil needs to hold for about a second. Right
now I have a mode watching for the switches to be activated. Then it
fires and holds the coil as it should. Is there a way in MPF to
disable a switch or to tell the mode to stop watching that switch
until another event happens? Is there a better way to do this? Thanks!
Here's how we'll handle this. We're going to do this by writing some
custom Python code. It's probably possible to do it in config files
with logic blocks and stuff, but this is one of the scenarios where
it's much faster and less confusing just to write it in Python. First,
we have to decide whether we'll register switch handlers to talk to
the Switch Controller and watch for the switches to change, or whether
we'll look for the events that are posted when a switch is activated.
(Remember that all switches post an event <switchname>_active when
they're activated. We're going to use the event method here. Why? Two
reasons. First, when you write code for modes, the Mode parent class
automatically cleans up and removes any event handlers you've
registered in that mode when the mode stops. So that means you don't
have to worry about doing that yourself. Second, registering for
events is the more "MPF-way" to do things. Using events means this
code can be easily changed to work with any event. (For example, maybe
you want to look for shot completion events instead of raw switch
hits. In that case it would be the same code, just looking for
different events. So let's setup the code now. First create the
skeleton for your mode code if you don't have it yet. We'll call this
mode "Alien":

::

    
    from mpf.system.mode import Mode
    
    class Alien(Mode):


For this demonstration, let's assume the drop target bank is called "
*drop_targets_1*", and the switches are *switch_a* and *switch_b*. The
way we're going to do this is to create two modes of operation. One is
when either switch can be hit to fire the coil, and the second is
while the blocking is in place and it's waiting for *switch_b* to
triggered. So first let's create a method that actually fires our
coil. We'll use the driver method timed_enable() which lets you to
fire a coil for a set time that's longer than 255ms (since 255ms is
the maximum pulse time.


::

    
    def fire_coil(self, **kwargs):
        self.machine.coils['some_coil'].timed_enable(1000)


Next let's add a method called *disable_blocking()* that allows both
*switch_a* and *switch_b* to fire the coil:


::

    
    def disable_blocking(self):
        self.add_mode_event_handler(event='switch_a_active',
                                    handler=self.fire_coil)
        self.add_mode_event_handler(event='switch_b_active',
                                    handler=self.fire_coil)


Then we'll created a method called enable_blocking() which removes all
the events with self.fire_coil() as their callback and then re-sets up
switch_a to fire the coil:


::

    
    def enable_blocking(self):
        self.machine.events.remove_handler(self.fire_coil)
        self.add_mode_event_handler(event='switch_b_active',
                                    handler=self.fire_coil)


Finally, add an entry to your *mode_start()* method to start with
either blocking enabled or disabled, like this:


::

    
    def mode_start(self, **kwargs):
        self.disable_blocking()


The complete code should look like this:


::

    
    from mpf.system.mode import Mode
    
    class Alien(Mode):
        def mode_start(self, **kwargs):
            self.disable_blocking()
        def fire_coil(self, **kwargs):
            self.machine.coils['some_coil'].timed_enable(1000)
    
    
        def disable_blocking(self):
            self.add_mode_event_handler(event='switch_a_active',
                                        handler=self.fire_coil)
            self.add_mode_event_handler(event='switch_b_active',
                                        handler=self.fire_coil)
        def enable_blocking(self):
            self.machine.events.remove_handler(self.fire_coil)
            self.add_mode_event_handler(event='switch_b_active',
                                        handler=self.fire_coil)


So now we have a coil that is fired for one second if either
*switch_a* or *switch_b* is hit, and then after either switch is hit
and the coil is fired, the "blocking" is enabled and only *switch_b*
works. But this isn't quite what the question asked. In the question,
there's an external trigger event (the drop target bank being
completed) that triggers the blocking to start. So we need to change
the code a bit. In MPF, when a drop target bank is completed, it post
an event *<drop_target_bank_name>_down*. So in this case with
*drop_targets_1*, we're looking for an event *drop_targets_1_down*. So
change our *mode_start()* method so it looks for that event, and then
it enables the blocking when it happens. (Note that we keep
`self.disable_blocking()` in there because we still need to set it up
to look for both *switch_a* and *switch_b* events.)


::

    
    def mode_start(self, **kwargs):
        self.disable_blocking()
        self.add_mode_event_handler(event='drop_targets_1_down',
                                    handler=self.enable_blocking)


The only other change we could make here is what happens when
*switch_b* is hit while the blocking is enabled? Currently this code
fires the coil for 1 second. But maybe you don't want *switch_b* to
fire the coil when blocking is enabled, and instead you want it to
just remove the blocking? Simple! Just change your `enable_blocking()`
method handler for *switch_b* to be `self.disable_blocking` instead of
`self.fire_coil`. So now your mode code looks like this:


::

    
    from mpf.system.mode import Mode
    
    class Alien(Mode):
    
        def mode_start(self, **kwargs):
            self.disable_blocking()
            self.add_mode_event_handler(event='drop_targets_1_down',
                                        handler=self.enable_blocking)
    
        def fire_coil(self, **kwargs):
            self.machine.coils['some_coil'].timed_enable(1000)
    
        def disable_blocking(self, **kwargs):
            self.add_mode_event_handler(event='switch_a_active',
                                        handler=self.fire_coil)
    
            self.add_mode_event_handler(event='switch_b_active',
                                        handler=self.fire_coil)
    
        def enable_blocking(self, **kwargs):
            self.machine.events.remove_handler(self.fire_coil)
    
            self.add_mode_event_handler(event='switch_b_active',
                                        handler=self.disable_blocking)


We're almost there, except there's one thing that's still not quit
right. The problem now is that when the mode starts, both *switch_a*
and *switch_b* are active to fire the coil. Then when the drop target
bank is completed, blocking is enabled and the switches no longer fire
the coil. So far, so good. But when *switch_b* is hit at this point,
it will call `self.disable_blocking()` which will register *switch_a*
and switch_b to fire the coil (which is good), but *switch_b* is still
registered to also *disable_blocking*, which probably isn't right. (It
should be that only the drop target bank being completed disables
blocking.) So we need to remove the *event_handler* for *switch_b* in
our `disable_blocking(`) method, meaning our new complete code looks
like this:


::

    
    from mpf.system.mode import Mode
    
    class Alien(Mode):
    
        def mode_start(self, **kwargs):
            self.disable_blocking()
            self.add_mode_event_handler(event='drop_targets_1_down',
                                        handler=self.enable_blocking)
    
        def fire_coil(self, **kwargs):
            self.machine.coils['some_coil'].timed_enable(1000)
    
        def disable_blocking(self, **kwargs):
            self.add_mode_event_handler(event='switch_a_active',
                                        handler=self.fire_coil)
    
            self.add_mode_event_handler(event='switch_b_active',
                                        handler=self.fire_coil)
            self.machine.events.remove_handler(self.disable_blocking)
    
        def enable_blocking(self, **kwargs):
            self.machine.events.remove_handler(self.fire_coil)
    
            self.add_mode_event_handler(event='switch_b_active',
                                        handler=self.disable_blocking)


So there you have it! You can use these techniques in your own game
code to set up complex scenarios and logic based on events and
switches. It seems like a lot at first, but once you break it down
step-by-step as we've done here, you see it's not too bad. A few
notes:


+ You can safely remove an event handler even if no handlers are
  registered. For example, this code called `disable_blocking()` when
  the mode starts, and that code will remove the event handlers
  registered for `disable_blocking()`. The first time this is called
  there will not be any handlers for that callback, but that's ok.
+ Since the event handlers are registered via
  `self.add_mode_event_handler()` versus the machine-wide
  `self.machine.events.add_handler()`, they will automatically be
  removed when the mode stops, so you don't have to worry about removing
  them yourself.
+ When you add event handlers, notice that you do not include
  parenthesis in the method you specify as your handler. Why? Because in
  Python, when you add parenthesis, that means you're calling that
  method right there. In our handlers, we just want to pass the method
  as the handler, rather than calling it on the spot, which is why there
  are no parenthesis there.




