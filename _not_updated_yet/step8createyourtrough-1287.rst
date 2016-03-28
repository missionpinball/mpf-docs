
At this point you have a flipping machine with a DMD, but you don't
have a "working" pinball machine since you can't start or play games.
All you can do is flip. So the next step in this tutorial is to get
your first two *ball devices* set up—your trough and plunger lane.
That will give MPF a basic understanding of where your balls are and
allow it to start moving through the game, player, and ball cycles.
(Once you have ball devices defined, an MPF core component called the
*`Ball Controller`_* is able to start tracking where your balls are at
all times.)



(A) Understanding what "devices" are
------------------------------------

The first step to setting up your ball devices is that you have to
understand what a ball device is. :) Broadly-speaking, a device in the
MPF world is a physical thing that's in your pinball machine. Back in
Step 4 we showed you how to add your flipper *devices* and we briefly
outlined what devices are. We also said there are low level,
*physical* devices (switches, coils, lights, LEDs, etc.) as well as
higher-level, *logical* devices that intelligently group together the
lower-level physical devices. A ball device is one of the logical
devices (like the flippers). Not every low-level hardware device will
be part of a higher level logical device—sometimes a switch is just a
switch—but in many cases your low level devices will end up being part
of something bigger. So to configure your first two ball devices (the
trough and the plunger lane), you'll first add the coils and switches
to their respective sections, then you'll group those building block
devices into higher level ball devices.



(B) Understand what "ball devices" are
--------------------------------------

A *`ball device`_* quite literally anything in a pinball machine that
holds a pinball (even for a moment), including your trough, the
plunger lane, playfield locks, VUKs, the gumball machines in *Twilight
Zone*, a kickout hole, etc. (Actually behind the scenes the playfield
is a ball device too, because when a ball is rolling around on it,
it's "in" the playfield device.) Your machine will most likely have
lots of ball devices. Turning around and looking at the *Judge Dredd*
machine behind me, I count eight(!) ball devices: the trough, the
right plunger lane, the left plunger lane, the Sniper VUK, the Hall of
Justice VUK, the Deadworld orbit thingy, the crane, and the playfield.
MPF keeps track of how many balls are in each ball device at all
times, and it assumes that any balls *not* in ball devices are either
in transit from one device to another, or they're stuck somewhere.
Most ball devices have a one-to-one ratio of ball switches to ball
capacity, so MPF can simply count how many switches are active to see
how many balls each device has at any given time. (Not all ball
devices have ball switches for every ball—the gumball machine in
*Twilight Zone* is a good example of this—but we'll get to that
later.) Ball devices support all sorts of settings and commands. They
can post events when balls enter or exit, you can configure counting
delays to account for balls bouncing around before they settle, you
can specify how devices confirm that balls have successfully ejected,
as well as dozens of other options that allow MPF to support every
known type of device in every pinball machine ever created.
(Seriously, if you find a ball device that you can't figure out how to
configure, `contact us`_ and we'll buildthe support for it.)



(C)Understanding "trough" ball devices
--------------------------------------

In modern pinball machines, the trough is the ball device that holds
balls after they've drained off the playfield. The act of a ball
entering a trough device usually triggers a *ball drain* event, and
when the game wants to launcha ball into play, it ejects a ball from
the trough (typically into another ball device like the plunger lane
or some sort of launch catapult). So when we're building the MPF
config for a new machine, the first ball device we create is the
trough. First, though, we should talk about what exactly a trough is.
A modern Stern- or Williams-style trough usually holds between 4 and 6
balls. The trough sits underneath the playfield so that a ball
entering it is gravity-fed and rolls down to the end of the line.
There's a switch (either a physical leaf switch or an opto switch) for
each ball position which lets the machine know how many balls are in
the trough, and there's a solenoid at the end that pulses to kick a
ball out of the trough and into the shooter lane. Most modern troughs
also have a switch in the upper position near the exit that's used to
detect if a ball falls back into the trough from the "exit"
side—something that tends to happen if your eject coil pulse is too
strong or too weak. (Too weak means the ball falls back in because it
didn't have enough oomph to make it out, and too strong means the ball
flies out too fast, bounces off the right edge rail of the plunger
lane, and lands back in the trough after the other balls have rolled
down into their new positions.) In MPF we refer to this as a "jam"
switch though it's also called a "ball stacked" or "up ball" switch
depending on whose manual you're reading. Here's a side-view diagram
of a modern style trough: ` `_ The diagram above does not show the
ball switches, but you get the idea.



If this trough diagram does not look like your trough...
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Of course not all troughs are the same. In older machines (most 1980s
machines, Williams System 11, and early WPC machines), the trough was
entirely above the playfield, and a second ball device (called the
"outhole") was responsible for receiving drained balls from the
playfield and ejecting them into the trough. If you have a classic
style outhole + trough combination that looks something like the
diagram below, you can see how to configure itvia `this "How To" guide
for 1980s-style troughs`_. ` `_ If you have a very old machine single
ball machine (almost all EMs and mostearly solid state machines) like
the diagram below, then you can typically configure your trough just
like a modern trough. (It's just that there's only one switch and one
coil, but everything in Steps (D) and (E) below still apply.)



(D)Adding your trough switch(es)
--------------------------------

Now that we've covered the background information of low-level
devices, logical devices, ball devices, and looked at some different
types of troughs, we're finally ready to build the actual
configuration for your trough. In this tutorial we're going to assume
you have a modern style trough device similar to the one shown above.
The first step is to add your trough's switches to the `switches:`
section of your config file and the trough's eject coil to the
`coils:` section. Let's start with the switches. Create an entry in
your `switches:` section for each switch in your trough, like this:


::

    
    switches:
        s_left_flipper:
            number: 00
        s_right_flipper:
            number: 01
        s_trough1:
            number: 02
        s_trough2:
            number: 03
        s_trough3:
            number: 04
        s_trough4:
            number: 05
        s_trough5:
            number: 06
        s_trough6:
            number: 07
        s_trough_jam:
            number: 08


Like the switches we added before, this tutorial just uses generic
numbers, but the actual numbers you enter need to reflect that actual
hardware numbers you have in your particular machine. They might be
something like `SD12` or `S62` or `2/5`. Refer to ` `switches:`
section of the configuration file reference`_ to see the exact number
pattern for your particular hardware controller and machine
combination. If your trough uses opto switches instead of mechanical
switches, then their states will be inverted. In other words they will
report "active" when there is no ball present and "inactive" when
there is a ball, so you need to add a further entry off `type: NC`
(normally closed) to tell MPF that this is a normally-closed switch
(meaning it's closed when there's no ball and open when there's a
ball.) Doing this means that MPF will automatically flip every reading
of that switch it gets, so in MPF a state of "1" (active) truly will
mean that the switch is active and there's a ball there. An example of
this will look like this:


::

    
        s_trough1:
            number: 02
            type: NC
        s_trough2:
            number: 03
            type: NC


It makes no difference which switch is which (in terms of whether
Switch 1 is on the left side or the right side). The actual switch
names don't really matter. We use s_ *trough1* through s_ *trough6*
plus s_ *trough_jam*, though you can call them s_ *ball_trough_1* or
s_ *trough_ball_1* or s_ *mr_potatohead*. (Just remember (1) you can
only use letters, numbers, and underscores, and your name can't start
with a number, (2) device names are not case-sensitive, and (3) we
recommend starting your switch names with "s_" to make it easier for
your editor to autocomplete them later.) Also, we should note, that
these names are the internal names that you'll use for these switches
in your game code and configuration file. When it comes time to create
"friendly" names for these switches which you'll expose via the
service menu, you can create plain-English labels with spaces and
capitalization everything. But that comes later. If you don't have a
trough jam switch that's fine, you would just enter your other
switches.



(E) Add your trough eject coil
------------------------------

Next, create an entry in your `coils:` section for your trough's eject
coil. Again, the name doesn't matter. We'll call this *c_trough_eject*
and enter it like this:


::

    
    coils:
        c_flipper_left_main: 
            number: 00
            pulse_ms: 20
        c_flipper_left_hold: 
            number: 01
        c_flipper_right_main: 
            number: 02
            pulse_ms: 20
        c_flipper_right_hold: 
            number: 03
        c_trough_eject:
            number: 04
            pulse_ms: 20


Again the exact number you enter will be dependent on how your coil is
physically connected to your pinball controller. Refer to the `
`coils:` section of the config file reference`_ for details. You'll
also note that we went ahead and entered a `pulse_ms:` value of 20
which will override the default pulse time of 10ms. It's hard to say
at this point what value you'll actually need. You can always adjust
this at any time. You can play with the exact values in a bit once we
finish getting everything set up.



(F) Add your "trough" ball device
---------------------------------

Next create a new top-level section (i.e. an entry with no spaces in
front of it) in your config file called b `all_devices:`. Then on the
next line, enter four spaces and create an entry called `trough:`,
like this:


::

    
    ball_devices:
        bd_trough:


This means that you're creating a ball device called *bd_trough* (or
whatever word you use for the setting with four spaces before it).
Again we use the preface *bd_* to indicate that this is a ball device
which makes it easier when we're referencing them later. Then under
your `bd_trough:` entry, type eight spaces and start entering the
configuration settings for your trough ball device:



(1) Add your trough switches
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create an entry called `ball_switches:` and then add a comma-separated
list of all the switches in your trough, like this: (At this point if
you have an editor that supports autocomplete then you'll really start
to appreciate why we preface our switch names with "s_"!


::

    
            ball_switches: s_trough1, s_trough2, s_trough3, s_trough4, s_trough5, s_trough6, s_trough_jam


So this is eight spaces, followed by the word "ball_switches", then a
colon, then a space, then the name of your first switch, comma, then
your second switch, comma, etc... Note that these switches can be in
any order. The key is that you're entering one switch for each
position that's used to detect whether a ball is in the trough at that
position. (That's why we also include the trough jam switch here,
since if that jam switch is active, that means there's a ball sitting
on top of another ball right near the exit of your trough.) The number
of switches you enter here will tell MPF how many balls your trough
can hold. When MPF wants to know how many ballsare in your trough, it
will check all these switches to see which ones are active, and the
total number active represents how many balls it's holding at that
moment.



(2) Add your entrance count delay
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Next add a setting called `entrance_count_delay:` followed by a time
entry. (This time entry can be in seconds or milliseconds and is
entered with the same formatting you would use to enter any time
duration setting in your config files as we explain `here`_.) This
setting tells MPF how long a ball switch has to be in a steady state
before it checks all the switches to see how many balls are in this
device. If we didn't have this delay then a ball entering a trough
would be chaos. (Imagine the physical switch changes when a ball
enters a trough. First the switch *trough6* would activate, then
*trough6* would become inactive a few milliseconds later, then
*trough5* activates, then *trough5* becomes inactive, then switch
*trough4* activates, etc. In our example we're going to use *300ms*
(which is probably fine for most cases). This means that whenever
anytrough switches change state, MPF will wait until they've all been
in a steady state for 300 ms before it actually counts them. If it
tries to count them before all the switches haven't changed in 300 ms,
it will abort the count and try again once they're all settled.


::

    
            entrance_count_delay: 300ms


MPF actually uses a default *entrance_count_delay:* time of 500ms, so
if you don't enter a setting here, it will use 500ms. So really you
can ignore this setting, but we wanted to mention it so you knew about
it.



(3) Add your eject coil
~~~~~~~~~~~~~~~~~~~~~~~

Next create a setting called `eject_coil:` which will be the name of
the coil that MPF should fire when it wants to eject a ball from this
ball device. This should be the name of the coil you just added above,
*c_trough_eject* in our case:


::

    
            eject_coil: c_trough_eject




(4) Add some tags to tell MPF about this device
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The final configuration setting you need to enter for your trough is a
list of tags which tell MPF certain things about this device. You can
add any tags to any device you want in MPF, and tags make grouping and
programming for certain devices easier later on. MPF also uses some
special tag names to tell it how it should treat certain devices. For
your trough, we're going to use a few special tags. First, we'll add a
tag called * trough * which tells MPF that this device wants to hold
as many balls as it can. (You need this tag even if you have one of
the System 11 or EM-style troughs.) This probably doesn't make sense
right now, which is fine, but without this tag then MPF won't know
what to do with all the balls that are sitting in the trough waiting
to be launched. This tag tells MPF that it's fine for this device to
hold lots of balls. Next you'll add a tag called * home * which tells
MPF that any balls in this device are considered to be in their "home"
positions. When MPF first starts up, and after a game ends, it will
automatically eject any balls from any devices that are not tagged
with "home." When a player tries to start a game, MPF will also make
sure all the balls in the machine are contained in devices tagged with
"home." (So if you're programming a machine like Star Trek: The Next
Generation which holds a ball in the upper playfield lock when a game
starts, you'd add a tag of `home` to that ball device too.) Finally,
you need to add a tag called * drain * which is used to tell MPF that
a ball entering this device means that a live ball has drained from
the playfield. At this point you might be wondering why you have to
enter all three of these tags. Why can't the simple `trough` tag be
enough to tell MPF that a ball entering it should trigger a drain and
that balls are home? This is due to the flexibility of MPF and the
nearly unlimited variations of pinball machine hardware in the world.
Some machines have multiple troughs. Some machines have drain devices
which aren't troughs. Some machines consider balls outside the trough
to be home. So even though these all might seem similar, just know
that for now you have to add `trough`, `home`, and `drain` tags to
your trough. You can specify the tags in any order, and your `tags:`
entry should look something like this:


::

    
            tags: trough, home, drain




(5) Enable debugging so you can see cool stuff in the log
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Finally, add an entry `debug: yes` to your trough which will cause MPF
to write detailed debugging information about this device to the log
file. You have to run MPF with the -v (verbose) option to see this.
This will come in handy in the future as you're trying to debug
things, and it's nice because you can just turn on debugging for the
things you're troubleshooting at that moment which helps keep the
debug log from filling up with too much gunk. At this point your
trough configuration should be complete! If you followed along
exactly, the `ball_devices:` section of your config file should look
something like this:


::

    
    ball_devices:
        bd_trough:
            ball_switches: s_trough1, s_trough2, s_trough3, s_trough4, s_trough5, s_trough6, s_trough_jam
            entrance_count_delay: 300ms
            eject_coil: c_trough_eject
            tags: trough, home, drain
            debug: yes




(G) Fire up your game and test
------------------------------

Unfortunately there are a few more things we need to configure before
you can play a full game, but if you want to test what you have so
far, you can launch MPF and drop a ball into your trough and you
should see some cool things in your log file. (If you don't have a
physical machine attaches then you can skip this step.) To do so,
launch theMPF core engine with the `-v` command line options so it
shows the verbose information in the log file, like this:


::

    
    python mpf.py your_machine -v


You don't have to launch the media controller this time since we're
just looking at the console output of the MPF core engine, though if
you want to run both MPF and the media controller than that's fine
too. Once your game is running, drop a ball into your trough and you
should see a whole bunch of trough switches changing between active
(State: 1) and inactive (State: 0). Now quit MPF and open the MPF log
file (the one with *mpf* in the name, not *mc*, since you want the log
file from the MPF core engine) and scroll to the bottom. You should
see all sorts of messages and events about the ball entering the
trough, including it updating its ball count, processing the newly-
entered ball, messages about the playfield ball count changing, etc.
You don't have to know what any of this means, but it's kind of cool
to see things happening! Here's an example of everything that happens
after a single ball switch is activated in the trough.


::

    
    2015-11-29 22:01:14,911 : INFO : SwitchController : <<<<< switch: s_trough1, State:1 >>>>>
    2015-11-29 22:01:14,913 : DEBUG : SwitchController : Found timed switch handler for k/v 1448863275.21 / {'callback': <bound method BallDevice._switch_changed of <ball_device.bd_trough>>, 'state': 1, 'switch_action': 's_trough1-1', 'ms': 300, 'callback_kwargs': {}, 'switch_name': 's_trough1', 'return_info': False}
    2015-11-29 22:01:14,914 : DEBUG : Events : ^^^^ Posted event 's_trough1_active'. Type: None, Callback: None, Args: {}
    2015-11-29 22:01:14,920 : DEBUG : Events : ============== EVENTS QUEUE =============
    2015-11-29 22:01:14,923 : DEBUG : Events : s_trough1_active, None, None, {}
    2015-11-29 22:01:14,926 : DEBUG : Events : =========================================
    2015-11-29 22:01:14,927 : DEBUG : Events : ^^^^ Processing event 's_trough1_active'. Type: None, Callback: None, Args: {}
    2015-11-29 22:01:14,927 : DEBUG : Events : vvvv Finished event 's_trough1_active'. Type: None. Callback: None. Args: {}
    2015-11-29 22:01:15,243 : DEBUG : SwitchController : Processing timed switch handler. Switch: s_trough1  State: 1, ms: 300
    2015-11-29 22:01:15,244 : DEBUG : ball_device.bd_trough : Counting balls
    2015-11-29 22:01:15,246 : DEBUG : ball_device.bd_trough : Confirmed active switch: s_trough1
    2015-11-29 22:01:15,246 : DEBUG : ball_device.bd_trough : Confirmed inactive switch: s_trough2
    2015-11-29 22:01:15,246 : DEBUG : ball_device.bd_trough : Confirmed inactive switch: s_trough3
    2015-11-29 22:01:15,247 : DEBUG : ball_device.bd_trough : Confirmed inactive switch: s_trough4
    2015-11-29 22:01:15,249 : DEBUG : ball_device.bd_trough : Confirmed inactive switch: s_trough5
    2015-11-29 22:01:15,250 : DEBUG : ball_device.bd_trough : Confirmed inactive switch: s_trough_jam
    2015-11-29 22:01:15,250 : DEBUG : ball_device.bd_trough : Counted 1 balls
    2015-11-29 22:01:15,253 : DEBUG : ball_device.bd_trough : Received 1 unexpected balls
    2015-11-29 22:01:15,256 : DEBUG : Events : ^^^^ Posted event 'balldevice_captured_from_playfield'. Type: None, Callback: None, Args: {'balls': 1}
    2015-11-29 22:01:15,257 : DEBUG : Events : ============== EVENTS QUEUE =============
    2015-11-29 22:01:15,257 : DEBUG : Events : balldevice_captured_from_playfield, None, None, {'balls': 1}
    2015-11-29 22:01:15,259 : DEBUG : Events : =========================================
    2015-11-29 22:01:15,262 : DEBUG : Events : ^^^^ Posted event 'balldevice_balls_available'. Type: boolean, Callback: None, Args: {}
    2015-11-29 22:01:15,263 : DEBUG : Events : ============== EVENTS QUEUE =============
    2015-11-29 22:01:15,263 : DEBUG : Events : balldevice_captured_from_playfield, None, None, {'balls': 1}
    2015-11-29 22:01:15,265 : DEBUG : Events : balldevice_balls_available, boolean, None, {}
    2015-11-29 22:01:15,272 : DEBUG : Events : =========================================
    2015-11-29 22:01:15,273 : DEBUG : ball_device.bd_trough : Processing 1 new balls
    2015-11-29 22:01:15,273 : DEBUG : Events : ^^^^ Posted event 'balldevice_bd_trough_ball_enter'. Type: relay, Callback: <bound method BallDevice._balls_added_callback of <ball_device.bd_trough>>, Args: {'device': <ball_device.bd_trough>, 'new_balls': 1, 'unclaimed_balls': 1}
    2015-11-29 22:01:15,275 : DEBUG : Events : ============== EVENTS QUEUE =============
    2015-11-29 22:01:15,276 : DEBUG : Events : balldevice_captured_from_playfield, None, None, {'balls': 1}
    2015-11-29 22:01:15,276 : DEBUG : Events : balldevice_balls_available, boolean, None, {}
    2015-11-29 22:01:15,278 : DEBUG : Events : balldevice_bd_trough_ball_enter, relay, <bound method BallDevice._balls_added_callback of <ball_device.bd_trough>>, {'device': <ball_device.bd_trough>, 'unclaimed_balls': 1, 'new_balls': 1}
    2015-11-29 22:01:15,279 : DEBUG : Events : =========================================
    2015-11-29 22:01:15,283 : DEBUG : Events : ^^^^ Posted event 'balldevice_bd_trough_ok_to_receive'. Type: None, Callback: None, Args: {'balls': 5}
    2015-11-29 22:01:15,289 : DEBUG : Events : ============== EVENTS QUEUE =============
    2015-11-29 22:01:15,289 : DEBUG : Events : balldevice_captured_from_playfield, None, None, {'balls': 1}
    2015-11-29 22:01:15,290 : DEBUG : Events : balldevice_balls_available, boolean, None, {}
    2015-11-29 22:01:15,292 : DEBUG : Events : balldevice_bd_trough_ball_enter, relay, <bound method BallDevice._balls_added_callback of <ball_device.bd_trough>>, {'device': <ball_device.bd_trough>, 'unclaimed_balls': 1, 'new_balls': 1}
    2015-11-29 22:01:15,296 : DEBUG : Events : balldevice_bd_trough_ok_to_receive, None, None, {'balls': 5}
    2015-11-29 22:01:15,298 : DEBUG : Events : =========================================
    2015-11-29 22:01:15,299 : DEBUG : Events : ^^^^ Processing event 'balldevice_captured_from_playfield'. Type: None, Callback: None, Args: {'balls': 1}
    2015-11-29 22:01:15,305 : DEBUG : Events : Playfield._ball_removed_handler (priority: 1) responding to event 'balldevice_captured_from_playfield' with args {'balls': 1}
    2015-11-29 22:01:15,309 : DEBUG : Events : ^^^^ Posted event 'sw_playfield_active'. Type: None, Callback: <bound method Playfield._ball_removed_handler2 of <playfield.playfield>>, Args: {'balls': 1}
    2015-11-29 22:01:15,313 : DEBUG : Events : ============== EVENTS QUEUE =============
    2015-11-29 22:01:15,315 : DEBUG : Events : balldevice_balls_available, boolean, None, {}
    2015-11-29 22:01:15,315 : DEBUG : Events : balldevice_bd_trough_ball_enter, relay, <bound method BallDevice._balls_added_callback of <ball_device.bd_trough>>, {'device': <ball_device.bd_trough>, 'unclaimed_balls': 1, 'new_balls': 1}
    2015-11-29 22:01:15,316 : DEBUG : Events : balldevice_bd_trough_ok_to_receive, None, None, {'balls': 5}
    2015-11-29 22:01:15,318 : DEBUG : Events : sw_playfield_active, None, <bound method Playfield._ball_removed_handler2 of <playfield.playfield>>, {'balls': 1}
    2015-11-29 22:01:15,319 : DEBUG : Events : =========================================
    2015-11-29 22:01:15,325 : DEBUG : Events : vvvv Finished event 'balldevice_captured_from_playfield'. Type: None. Callback: None. Args: {'balls': 1}
    2015-11-29 22:01:15,328 : DEBUG : Events : ^^^^ Processing event 'balldevice_balls_available'. Type: boolean, Callback: None, Args: {}
    2015-11-29 22:01:15,329 : DEBUG : Events : vvvv Finished event 'balldevice_balls_available'. Type: boolean. Callback: None. Args: {}
    2015-11-29 22:01:15,331 : DEBUG : Events : ^^^^ Processing event 'balldevice_bd_trough_ball_enter'. Type: relay, Callback: <bound method BallDevice._balls_added_callback of <ball_device.bd_trough>>, Args: {'device': <ball_device.bd_trough>, 'unclaimed_balls': 1, 'new_balls': 1}
    2015-11-29 22:01:15,332 : DEBUG : Events : BallController._ball_drained_handler (priority: 1) responding to event 'balldevice_bd_trough_ball_enter' with args {'device': <ball_device.bd_trough>, 'unclaimed_balls': 1, 'new_balls': 1}
    2015-11-29 22:01:15,334 : DEBUG : Events : ^^^^ Posted event 'ball_drain'. Type: relay, Callback: <bound method BallController._process_ball_drained of <mpf.system.ball_controller.BallController object at 0x020A6CF0>>, Args: {'device': <ball_device.bd_trough>, 'balls': 1}
    2015-11-29 22:01:15,344 : DEBUG : Events : ============== EVENTS QUEUE =============
    2015-11-29 22:01:15,345 : DEBUG : Events : balldevice_bd_trough_ok_to_receive, None, None, {'balls': 5}
    2015-11-29 22:01:15,346 : DEBUG : Events : sw_playfield_active, None, <bound method Playfield._ball_removed_handler2 of <playfield.playfield>>, {'balls': 1}
    2015-11-29 22:01:15,348 : DEBUG : Events : ball_drain, relay, <bound method BallController._process_ball_drained of <mpf.system.ball_controller.BallController object at 0x020A6CF0>>, {'device': <ball_device.bd_trough>, 'balls': 1}
    2015-11-29 22:01:15,352 : DEBUG : Events : =========================================
    2015-11-29 22:01:15,355 : DEBUG : Events : vvvv Finished event 'balldevice_bd_trough_ball_enter'. Type: relay. Callback: <bound method BallDevice._balls_added_callback of <ball_device.bd_trough>>. Args: {'device': <ball_device.bd_trough>, 'new_balls': 1, 'unclaimed_balls': 1}
    2015-11-29 22:01:15,358 : DEBUG : Events : ^^^^ Processing event 'balldevice_bd_trough_ok_to_receive'. Type: None, Callback: None, Args: {'balls': 5}
    2015-11-29 22:01:15,358 : DEBUG : Events : vvvv Finished event 'balldevice_bd_trough_ok_to_receive'. Type: None. Callback: None. Args: {'balls': 5}
    2015-11-29 22:01:15,362 : DEBUG : Events : ^^^^ Processing event 'sw_playfield_active'. Type: None, Callback: <bound method Playfield._ball_removed_handler2 of <playfield.playfield>>, Args: {'balls': 1}
    2015-11-29 22:01:15,371 : DEBUG : Events : Playfield.playfield_switch_hit (priority: 1) responding to event 'sw_playfield_active' with args {'balls': 1}
    2015-11-29 22:01:15,371 : DEBUG : Events : ^^^^ Posted event 'playfield_active'. Type: boolean, Callback: None, Args: {}
    2015-11-29 22:01:15,372 : DEBUG : Events : ============== EVENTS QUEUE =============
    2015-11-29 22:01:15,374 : DEBUG : Events : ball_drain, relay, <bound method BallController._process_ball_drained of <mpf.system.ball_controller.BallController object at 0x020A6CF0>>, {'device': <ball_device.bd_trough>, 'balls': 1}
    2015-11-29 22:01:15,375 : DEBUG : Events : playfield_active, boolean, None, {}
    2015-11-29 22:01:15,375 : DEBUG : Events : =========================================
    2015-11-29 22:01:15,375 : DEBUG : playfield : Playfield_active switch hit with no balls expected. glass_off_mode is enabled, so this will be ignored.
    2015-11-29 22:01:15,377 : DEBUG : Events : vvvv Finished event 'sw_playfield_active'. Type: None. Callback: <bound method Playfield._ball_removed_handler2 of <playfield.playfield>>. Args: {'balls': 1}
    2015-11-29 22:01:15,385 : DEBUG : Events : ^^^^ Processing event 'ball_drain'. Type: relay, Callback: <bound method BallController._process_ball_drained of <mpf.system.ball_controller.BallController object at 0x020A6CF0>>, Args: {'device': <ball_device.bd_trough>, 'balls': 1}
    2015-11-29 22:01:15,388 : DEBUG : Events : vvvv Finished event 'ball_drain'. Type: relay. Callback: <bound method BallController._process_ball_drained of <mpf.system.ball_controller.BallController object at 0x020A6CF0>>. Args: {'device': <ball_device.bd_trough>, 'balls': 1}
    2015-11-29 22:01:15,391 : DEBUG : Events : ^^^^ Processing event 'playfield_active'. Type: boolean, Callback: None, Args: {}
    2015-11-29 22:01:15,392 : DEBUG : Events : vvvv Finished event 'playfield_active'. Type: boolean. Callback: None. Args: {}
    2015-11-29 22:01:15,395 : DEBUG : playfield : 1 ball(s) removed from the playfield
    2015-11-29 22:01:15,397 : DEBUG : playfield : Ball count change. Prior: 0, Current: -1, Change: -1
    2015-11-29 22:01:15,398 : WARNING : playfield : Playfield balls went to -1. Resetting to 0, but FYI that something's weird
    2015-11-29 22:01:15,398 : DEBUG : playfield : New Ball Count: 0. (Prior count: 0)
    2015-11-29 22:01:15,404 : DEBUG : Events : ^^^^ Posted event 'playfield_ball_count_change'. Type: None, Callback: None, Args: {'balls': -1, 'change': -1}
    2015-11-29 22:01:15,411 : DEBUG : Events : ============== EVENTS QUEUE =============
    2015-11-29 22:01:15,413 : DEBUG : Events : playfield_ball_count_change, None, None, {'balls': -1, 'change': -1}
    2015-11-29 22:01:15,414 : DEBUG : Events : =========================================
    2015-11-29 22:01:15,414 : DEBUG : Events : ^^^^ Processing event 'playfield_ball_count_change'. Type: None, Callback: None, Args: {'balls': -1, 'change': -1}
    2015-11-29 22:01:15,415 : DEBUG : Events : vvvv Finished event 'playfield_ball_count_change'. Type: None. Callback: None. Args: {'balls': -1, 'change': -1}






(H) Add keyboard entries for your trough switches
-------------------------------------------------

While we're working with the trough config, let's create somekeyboard-
to-switch entries in your config file for your trough switches. You do
this just like how you created the entries you added in the Step 7.
For example (in your *keyboard:* section):


::

    
        1:
            switch: s_trough1
            toggle: true


The *toggle: true* setting for this keyboard entry sets up this key as
a "toggle" key meaning that it functions in a push on / push off kind
of way. (Without *toggle: true,* you'd have press and hold the key to
represent the ball activating the switch. With *toggle: true*, you tap
the key once to activate the switch, and tap it a second time to
deactivate it.) By the way, all of these true/false settings in the
config file give you a lot of leeway. You can enter the values as
*true*, *True*, *on*, or even *yes*, and you can use *No*, *no*,
*off*, *false*, etc. for "no" values. On important note about the
"toggle" function: The toggle function applies to keyboard keys, *not*
to switches. In other words in your physical machine, there is no
concept of a "toggle" style switch. The switch is open when it's open
and closed when it's closed. The toggle function only affects how
keyboard key behavior maps to switches in your machine. (If you really
want some fun, try using the toggle keys when you have a live machine
connected with balls in the trough. MPF will get really confused. :)
Now re-run MPFwith `-v -V` for verbose screen logging and tap the 1
key. (This time since we're using the keyboard interface and that
requires the graphical on-screen window from the media controller,
you'll need to launch both the MPF core engine and the media
controller.) After 300ms, (your entrance delay), you should see a
whole bunch of messages about a ball entering the trough. Now make
some more key entries for the trough and set them all to toggle. In
this example we'll set up one key for each regular ball switch in the
trough using the number keys.So now the *keyboard:* section of your
config file might look like this:


::

    
    keyboard:
        z:
            switch: s_left_flipper
        /:
            switch: s_right_flipper
        1:
            switch: s_trough1
            toggle: true
        2:
            switch: s_trough2
            toggle: true
        3:
            switch: s_trough3
            toggle: true
        4:
            switch: s_trough4
            toggle: true
        5:
            switch: s_trough5
            toggle: true
        6:
            switch: s_trough6
            toggle: true


You don't have to enter keyboard shortcuts for all the switches if you
don't want to. One should be fine for now.



(I) Configure yourvirtual hardware to start with balls in the trough
--------------------------------------------------------------------

If you're following along with virtual hardware, at some point you're
going to get annoyed because you'll have to press the 1 key every time
you runMPF to make it think there's a ball in the trough. (As you'll
soon learn, if you don't do this then MPF will think there are no
balls, so it won't start a game.) To get around that, you can add the
a new section to your config file called
`virtual_platform_start_active_switches:` . (Sorry this entry name is
hilariously long. We tried couldn't really think of any other name
that accurately described what it does.) Is its name implies,
*virtual_platform_start_active_switches:* lets you list the names of
switches that you want to start in the "active" state when you're
running MPF with the virtual or smart virtual platform interfaces. The
reason these only work with the virtual platforms is because if you're
running MPF while connected to a physical pinball machine, it doesn't
really make sense to tell MPF which switches are active since MPF can
read the actual switches from the physical machine. So you can add
this section to your config file, but MPF only reads this section when
you're running with one of the virtual hardware interfaces. To use it,
simply add the section along with a list of the switches you want to
start active. For example:


::

    
    virtual_platform_start_active_switches:
        s_trough1
        s_trough2
        s_trough3
        s_trough4
        s_trough5
        s_trough6


Note that you don't actually have to have *keyboard:* entries for any
of these *virtual_platform_start_active_switches* for switches. If you
do, though, and if those keyboard entries are set to *toggle: true*,
then that just means the switches will start out in the active state,
and the first time you hit the key associated with a switch, the
switch will change from active to inactive.



(J) Troubleshooting if something didn't work
--------------------------------------------

If you've gotten this far and your trough isn't working right, there
are a few things you can try (depending on what your problem is). If
your log file shows a number of balls contained in your trough that
doesn't match how many balls you actually have, that either means that
(1) you didn't add all the ball switches to the *ball_switches:*
section of the trough configuration, or (2) your trough uses opto
switches but you didn't add *type: NC* to each switch's configuration,
or (3) you're using a physical machine but a switch isn't adjusted
properly so the ball is not actually activating it. (Seriously, we
can't tell you how many times that's happened! We've also found that
on some machines, if you only have one ball in the trough that the
single ball isn't heavy enough to roll over the top of the eject coil
shaft. In that case we just add a few more balls to the machine and it
seems to take care of it.) Either way, if you have a ball in the
trough, theswitch entry in your log should showthat the switch is
active ( *State:1*), like this:


::

    
    2014-10-27 20:05:29,891 : SwitchController : <<<<< switch: trough1, State:1 >>>>>


If you see State:1 immediately followed by another entry with State:0,
that means the ball isn't activating the switch even though it might
be in the trough. If you get a YAML error, a "KeyError", or some other
weird MPF error, make sure that all the switch and coil names you
added to your trough configurationexactly match the switch and coil
names in the `switches:` and `coils:` sections of your config file
(including the same capitalization). Also make sure that all your
names are allowable names, meaning they are only letters, numbers, and
the underscore, and that none of your names start with a number.
Finally.make sure your YAML file is formatted properly, with spaces
(not tabs) and that you have no space to the left of your colons and
that you do have a space to the right of your colons, like this: ` `_
At this point your trough is ready to go! Next we have to configure
your plunger lane.



Check out the complete config.yaml file so far
----------------------------------------------

If you want to see a complete `config.yaml` file up to this point,
it’s available in the MPF package at
`<your_mpf_root>/machine_files/tutorial/config/step8.yaml`. (You need
to rename this file to `config.yaml` to use it.) And remember if
you're using physical hardware, your coil and switch numbers will be
different than the ones in the sample file, since you'll need to
configure them based on your driver boards' actual inputs and outputs.

.. _Ball Controller: https://missionpinball.com/docs/mpf-core-architecture/system-modules/ball-controller-system-module/
.. _ section of the configuration file reference: https://missionpinball.com/docs/configuration-file-reference/switches/
.. _ section of the config file reference: https://missionpinball.com/docs/configuration-file-reference/coils/
.. _contact us: https://missionpinball.com/about/
.. _here: https://missionpinball.com/docs/configuration-file-reference/important-config-file-concepts/entering-time-duration-values/
.. _ball device: https://missionpinball.com/docs/mpf-core-architecture/devices/logical-devices/ball-device/
.. _this "How To" guide for 1980s-style troughs: https://missionpinball.com/docs/howto/configure-1980s-style-trough/


