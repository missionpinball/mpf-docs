
In the world of custom pinball, there's a lot of conversation around
"loop rates" and "machine speed" and things like that. MPF gives you
fine-grained control over how "fast" your machine runs, both in terms
of how fast MPF polls the pinball controller hardware and how often
MPF "wakes up" to do things. There are a lot of misconceptions about
these topics, so this page is meant to clear those up and explain
exactly how these concepts are implemented in MPF.



The MPF main loop
-----------------

There's a setting in the machine-wide config called `timing: hz:`
which controls how many times per second MPF "wakes up" to run its
main loop. The default value for this setting is 30, meaning that MPF
runs its main loop every 33ms. (Technically it's 33.333333ms, but
we'll use 33ms for simplicity.) Several things happen in this loop:


+ Any periodic system timers that should tick now are processed.
+ Any sleeping tasks that are scheduled to wake up are run.
+ Any delays that are ready to be processed are run
+ A machine variable called *tick_num* is incremented by 1.
+ An event called *timer_tick* is posted, which itself causes lots of
  things, including:

    + Light and display shows that need to advance are advanced
    + The display is updated
    + BCP messages are read from the incoming BCP queue
    + The switch controller processes delayed switch actions
    + Plus a few other things...



Once these actions are done, MPF goes back to sleep until it's time
for the main loop to run again. The amount of time MPF sleeps varies
depending on how long the previous loop actions took. For example, if
the MPF loop is set to run every 33ms and the loop took 6ms to
complete, then MPF will sleep for 27ms so the next loop starts on
time. MPF records its overall start and stop time, as well as tracking
the number of main loops that took place. When you stop MPF, it does
some quick math and shows what your target and actual loop rates were
on the console and in the log file, like this:


::

    
    INFO : Machine : Target MPF loop rate: 30 Hz
    INFO : Machine : Actual MPF loop rate: 30.13 Hz


It's a good practice to check to make sure these values are in the
same ballpark. (On very short runs of MPF it's possible to see loop
rates above the target due to the way the timing is started.) If you
have a target loop rate of 30 and an actual loop rate of 15, you know
you either need to lower your loop rate or buy faster hardware. :)



The hardware polling loop
-------------------------

Most "action" in a pinball machine happens because a switch changes
state. In pinball, we want the machine to respond "instantly" (or as
near-instantly as possible) to switch actions, so therefore * MPF does
not process switch changes in its main loop *. Rather there's a second
timer that runs while the main loop is sleeping to poll the pinball
controller hardware to receive any switch changes. That hardware
polling loop, by default, happens every 1 millisecond. (You can
control this via the `timing: hw_thread_sleep_ms:` machine wide config
setting which is set to "1" by default.) So while the main loop is
sleeping, MPF wakes up (every 1ms in this case) to poll the hardware
to see if there are any switch changes, and if so it services that
switch (by posting an event that that switch has changed and/or
processing and switch handlers that have been added for that switch).
If multiple switch events came in via a single hardware poll, MPF will
service them all, one-by-one, in the order they were received. Then
when MPF is done servicing those switches, it will go back to sleep
(for another 1ms), poll for new switches, go to sleep again, etc. When
the time for the main loop sleep is up, MPF will do a full wake-up and
run the main loop again.



What happens if a switch change happens while MPF is in its main loop?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

MPF does not poll the hardware for switch updates while the main loop
is running, so if a switch changes state while the main MPF loop is
doing it's thing, MPF won't process it until the main loop is done.
This is by design. The main reason for this is that while MPF is in
the process of running its main loop, it would be confusing if that
loop was interrupted to process another switch. So instead MPF just
runs its main loop as fast as it can, and then when its done it polls
the hardware again to see if anything switches changes while the main
loop was running. The main loop runs quickly—typically under 10ms—so
in practical terms this only means that the "delay" of processing
switches that changed while the main loop is running is 10ms or less.
We've gotten into arguments with people about whether this is
acceptable, but the reality is most humans see things as
"simultaneous" if they happen within 50ms or so of each other, so if
switch processing is delayed by 10ms or so, no human will notice. In
fact old Williams WPC hardware running at 2Mhz was much slower than
this in terms of how it read and processed switches, so if it wasn't a
problem for the past 30 years then it's not a problem now. :)



Why not just run the hardware polling as fast as possible?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Some people have questioned why MPF "sleeps" for 1ms between polling
the hardware for switch changes. Wouldn't it be better to poll the
hardware as fast as possible? Technically speaking, MPF can do that.
(Just set the `hw_thread_sleep_ms:` to 0. This will produce some
impressive numbers for your hardware loop rates that you can brag to
your friends about, but in reality it serves no practical purpose and
in fact makes things worse overall! Why is this worse? First, remember
that the default polling interval is every 1 millisecond, so if you
set the polling to 0ms then what do you gain really? Best case is you
shave a few tenths of a millisecond off the response time. So what?
Humans are slow. Second, and more importantly, if you run your
hardware polling loop as fast as possible, that means your MPF process
is going to consume 100% of your CPU (which makes sense since you're
telling it to run as fast as possible!) But that's bad for a few
reasons. First it means that your CPU is heating up and just running
full out 100% all the time. That is not good in terms of longevity of
your hardware. Second is it means that your OS will generally be
unresponsive since you essentially have a "bad" process that's trying
to take up as much CPU as it can. On many computers you'll see MPF
only take less than 10% of the CPU just by letting it "yield" to other
processes once a millisecond. Heck, you can even change that hardware
thread sleep time to 2 or 3 or 5ms with no perceivable difference in
performance and drop your CPU usage even more.



Viewing your actual hardware loop rate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When you stop MPF, the console will also show the average of how many
times it was able to poll the hardware per second. Again this is based
on MPF knowing how long it was running and then dividing that by the
number of times it polled the hardware. When you're using the virtual
hardware platform, you'll see really high numbers, like this:


::

    
    INFO : Machine : Hardware loop rate: 748.9 Hz


Physical hardware will be lower since there's delay in the USB bus,
but even with physical hardware you'll still see hardware polling over
100Hz which means there was only an average of 10ms delay from the
time a switch changed until MPF knew about it.



These two loops do not affect "instant" actions like flippers and pop
bumpers
-------

The other thing to keep in mind is that so-called "instant" response
actions—like the flipper buttons controlling the flippers or pop
bumper or slingshot switches activating those devices—are handled
directly by the pinball controller with no interaction required from
MPF or the host computer. All modern pinball controller hardware
support these types of instant-response rules. These rules are
constantly being updated, overwritten, added, and removed. For
example, when a ball starts, MPF will update the rules on the hardware
to enable these instant-response actions. When a ball ends, MPF
removes those rules. When the next ball starts, MPF enables those
rules again, etc. Instant action rules are based on switch actions. So
when a switch tied to a pop bumper is activated, the hardware
controller pulses the pop bumper coil. Then the next time that MPF
polls the hardware, it will receive notification that the pop bumper
switch as activated, and based on that MPF can process a score, update
the display, and play a sound. So in reality there might be a few
millisecond delay between the time the hardware controller fires the
pop bumper coil and when MPF processes it, but again this all happens
faster than humans can perceive. (Heck, the speed of sound is only
about 1 foot per millisecond, so there's even a 4ms delay from the
sound coming out of the speakers in the backbox until it reaches the
player's ears.) We did some experiments where we added a delay between
the flipper button press and the activation of a flipper, and for most
players we could take that delay all the way up to 30ms before people
even noticed. (Not that we recommend that, rather it was just to prove
a point that humans are slow!) The last thing to know about these
instant response rules in MPF is that while most people think of them
just in terms of flippers, pop bumpers, and slingshots, MPF actually
writes hardware action rules for anything that needs to happen
instantly, including things like kickbacks and diverters. So even if
you have a crazy slow MPF main loop rate of 10hz (meaning there is
100ms between loops), a fast-moving ball in front of a diverter will
still cause that diverter to fire in time because that's being
serviced by the pinball controller hardware rather than the MPF main
loop.



