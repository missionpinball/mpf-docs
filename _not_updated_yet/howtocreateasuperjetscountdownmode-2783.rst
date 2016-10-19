
Warning: This How To guide has not yet been updated for MPF 0.21 (the
current version). If you're reading this now and you'd like to add
this to your game, send me an email (brian@missionpinball.com) and
I'll get it updated. While we're working on game modes, let's create
one more before we move on to other things. In this step, we're going
to create a "super jets" mode. This is something that's pretty common,
where each hit to a pop bumper is worth a small amount of points
initially, but after a lot of hits (usually 75 or so), you get "super
jets" which makes each pop bumper hit worth a lot more. So in our
tutorial, let's make our pop bumpers worth 500 points each for the
first 15 hits (picking a small number to make testing easier, but you
can change it to 75 once everything is working), and then after that,
"super jets" will be enabled and each hit will be worth 5,000 points.
We also want the count (and the super jet status) to persist from
ball-to-ball. (In other words, if our player gets 5 hits their first
ball, they'll enter their second ball only needing 10 more hits
instead of the full 15.) If you don't have pop bumpers, you can still
follow along with this tutorial. Maybe configure slingshots instead?
Or just any standup targets?



(A) Create yourpop bumpers
--------------------------

A pop bumper is typically made up of one switch and one coil. As you
can imagine, you add your switches and coils to the `switches:` and
`coils:` section of your machine config file just like any other
switch and coil. For example (just showing the pop bumper-related
entries):


::

    
    switches:
        pop_left:
            switch: pop_left
            number: 31
            tags: playfield_active, pop
        pop_right:
            switch: pop_right
            number: 32
            tags: playfield_active, pop
        pop_upper:
            switch: pop_upper
            number: 33
            tags: playfield_active, pop
    coils:
        pop_left:
            coil: pop_left
            number: 11
            pulse_ms: 20
        pop_right:
            coil: pop_right
            number: 12
            pulse_ms: 20
        pop_upper:
            coil: pop_upper
            number: 13
            pulse_ms: 20


Of course remember that your coil and switch numbers will be different
(and might have different formatting) depending on your hardware
platform. If everything you're doing is virtual and all your numbers
are fake, then just pick the next three numbers for each. Also if
you're virtual, you might want to pick three keyboard keys to map to
your pop bumpers so you can test out what we're doing here. Once you
have your switches and coils in your machine configuration, you need
to create your pop bumper devices which are what cause the coil to
automatically pulse when the switch is activated. In MPF, these are
called *Autofire* devices (`more info`_), and you configure them in
the ` `autofire_coils:` section`_ of your machine config file:


::

    
    autofire_coils:
        pop_left:
            switch: pop_left
            coil: pop_left
        pop_right:
            switch: pop_right
            coil: pop_right
        pop_upper:
            switch: pop_upper
            coil: pop_upper


Note that autofire coil devices automatically enable and disable
themselves when balls start and stop.



(B) Create twosuper jets modes
------------------------------

Now that your pop bumpers are all set, let's create a pair of game
modes that we'll use to create the super jets functionality. Why two?
We'll use one to track the progress towards the super jets, and
another which will take over once the super jets are actually active.
You might be wondering if two modes is really necessary? Certainly
it's possible to build this with one mode, but really it doesn't
matter. Modes don't add any overhead, and they don't slow things down.
You can have dozens or hundreds running at once. So yeah, maybe we
could put the progress tracker towards super jets in the base game
mode, but that feels like the super jets would be polluting that mode.
And yeah, maybe we could figure out how to create one mode which
tracks the super jets progress and then stops tracking it once super
jets are active, but again, meh. Why struggle with that? Two modes
makes it easy and it doesn't hurt anything. Anyway, the two modes
we're going to create are called *super_jets_phase_0* and
*super_jets_phase_1*. Phase 0 will be the mode that will be enabled by
default. It's where the jets will be worth 500 points each, and it's
where we will be tracking the progress of our 15 hits. Then once we
get that, the phase 0 mode will stop and the phase 1 mode will start.
The phase one mode will assign 5,000 points per hit. (And if we wanted
to, we could create a phase 2 mode which would be even more points per
hit that the phase 1 mode could track... and so on....) The first step
is to add the two folders for the two modes to the modes folder in
your game and then to create the empty mode configfiles as you did
when you made your previous modes: ` `_ In the super jets phase 0 mode
configuration, ( `super_jets_phase_0.yaml`), let's set it up like
this:


::

    
    mode:
        start_events: ball_starting
        stop_events: super_jets_phase_1_start
        priority: 300


Then for your super jets phase 1 mode ( `super_jets_phase_1.yaml`),
let's configure it like this:


::

    
    mode:
        start_events: super_jets_phase_1_start
        priority: 300




(C) Configure a counter to track progress towards super jets
------------------------------------------------------------

Another MPF component we haven't covered in the tutorial yet is
something called *Logic Blocks*. Logic Blocks are like logical "glue"
you can add to your config files that can cause certain events to
happen based on other events happening. There are three types of logic
blocks: sequence, counter, and accrual. (More information is available
in the `Logic Blocks section of our Game Logic documentation`_, as
well as in the `LogicBlocks section`_ of the configuration file
reference.) In our super jets mode, we'll be using a logic block
called *counter* which watches for how many times a certain event
happens, and once a threshold is hit, it posts another event. So in
our case, we're going configure the counter to watch for the events
posted by the pop bumpers being hit, and after 15 of them, we're going
to post an event that starts the super jets. We'll configure our
counter logic block like this (in our `super_jets_phase_0.yaml` mode
config file):


::

    
    logic_blocks:
        counters:
            super_jets:
                count_events: sw_pop
                starting_count: 15
                count_complete_value: 0
                direction: down
                events_when_complete: super_jets_phase_1_start




(D) Add the two modes to the machine-wide modes list
----------------------------------------------------

Don't forget to add these two new modes to the list of modes this game
uses in your machine-wide config.yaml file. The Modes: section of that
file should now look like this:


::

    
    modes:
       - base
       - skill_shot
       - super_jets_phase_0
       - super_jets_phase_1




(E) Configure scoring for the two super jet modes
-------------------------------------------------

Remember we want a pop bumper hit to be worth 500 points ordinarily
(in "phase 0" mode) and 5,000 points in super jut ("phase 1") mode. So
let's create those two scoring entries now. First, in your
`super_jets_phase_0.yaml` file, add the following section:


::

    
    scoring:
        sw_pop:
            Score: 500


Then in you `super_jets_phase_1.yaml` file:


::

    
    scoring:
        sw_pop:
            Score: 5000




(F) Test it out
---------------

Save your two config files and then run your game. Once you press
start, you should see your score increase by 500 points for the first
15 hits of the pop bumpers. Then on the 16th hit, you should see that
you get 5000 points (and 5000 for every hit after that). You'll also
notice in the log file that the *super_jets_phase_0* mode stops and
the *super_jets_phase_1* mode startson the 16th hit.



(G)More to come...
------------------

We have a bit more to finish in this step, including:


+ Displaying a count down to super jets on the display
+ Getting the super jets mode to automatically be active once it's be
  achieved when a new ball starts


.. _Logic Blocks section of our Game Logic documentation: https://missionpinball.com/docs/game-logic-rules/
.. _ section: https://missionpinball.com/docs/configuration-file-reference/autofire-coils/
.. _more info: https://missionpinball.com/docs/mechs/autofire-coil/
.. _LogicBlocks section: https://missionpinball.com/docs/configuration-file-reference/logicblocks/


