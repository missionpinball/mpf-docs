Switch debounce theory
======================

*MPF Tech Note*

There's a lot of confusion around how "debounce" works in pinball machines and
in MPF, mainly because different hardware platforms do things in very different
ways. So this tech note will explain the different ways that debounce works,
how MPF deals with it, and the technical back stories.

Understanding debounce
----------------------

On the surface, switch *debounce* is pretty straightforward. Switches are
mechanical things, computers are fast, and your pinball software wants to make
sure a switch is actually in a new state before acting on a switch.

Pinball controllers set debounce in different ways. For example, some platforms
(P-ROC, P3-ROC) say "a switch must be in a new state for 2 consecutive reads"
to be considered debounced, while other platforms (FAST) focus on time-based
durations rather than number of reads, saying, "a switch must be in a new state
for X milliseconds before it's considered debounced."

When discussing debounce, a lot of people tend to fixate on how "long" the
debounce is (10ms, 30ms, etc.), and conversations devolve into arguments about
switch lag and human perception, the "feel" of "instant", etc.

But the "lag" of a switch response is only part of the conversation about
debounce times.

The other important thing is if you set your debounce times too long, then you
risk switch events being missed. (It would be annoying if a ball brushed
a pop bumper and the bumper not didn't fire.)

If you set your debounces too short, you risk getting multiple switch events for
what should have been a single switch event. (Again it would be annoying if a
ball hit a pop bumper and that bumper fired once, but you actually got back
multiple switch events which led to multiple scores, multiple sound effects,
etc.)

Understanding switch scanning loop speed
----------------------------------------

The other major factor which affects debounce involves the timing of how the
switches are read.

In all modern pinball platforms, a switch changing state doesn't interrupt the
controller. Instead, the controller reads the state of all switches at a certain
interval.

But even this varies from platform-to-platform, and even based on whether you
have matrix or direct switches. (More on this in a bit.)

The important thing, though, is that different controllers and different types
of switches are checked at different intervals. That could be every millisecond,
or every 2ms, or every 8ms... really it's up to the controller and switch type
as they're all different.

Debounce + switch scanning loop speed = confusion!
--------------------------------------------------

Now combine the two previous concepts, and you quickly see we have some complex
scenarios about how "debounce" *really* works.

For example, let's start with a switch on a platform that defines debounce as
two consecutive reads of the same state. How does that translate into real-world
time? In other words, how long does that switch need to be active before the
controller considers it to be active?

We can't answer that question until we understand the switch scanning loop
speed.

For example, if the controller hardware steps through each switch poll at 1ms
intervals, that means it polls the direct switches, then 1ms later is polls
column 1, then 1ms, column 2, 1ms, column 3, etc.

So in the case of an 8x8 matrix with a single bank of direct switches, the
status of each switch is polled every 9ms.

Now imagine you have a switch configured for no debounce. How long does that
switch have to be in the new state to be considered changed?

If the switch changes state at the exact perfect instant that its column is
being read, then the active time for that switch is essentially instant.

However, if that switch's column is read, then 1ms later that switch goes active,
then 7ms after that the switch goes inactive again--all that happened within the
9ms polling "gap".

In other words, you could have a switch which was technically active for 7ms,
but the pinball controller completely missed it!

Same for debouncing. If debouncing needs a switch to be in the active state for
two consecutive reads to be considered active, and the switch polling loop only
poll that switch's column, then you could actually have a switch that was active
for 17ms (1ms less than 9ms * 2 reads), and the switch would not be seen as
active!

So, again using a 9ms polling loop as an example:

=============  ====================  ======================================
Type           Min time to activate  Max time that still might not activate
=============  ====================  ======================================
Debounced      10ms                  17ms
Not Debounced  1ms                   7ms
=============  ====================  ======================================

Matrix versus direct switches
-----------------------------

These longer loop times between switch reads are a necessity when switch matrices
are used. After all, you can only step through the matrix so fast before running
into FCC issues.

In theory, "direct" switches could mean the switches could be polled more often.
However, just because a switch is called a "direct" switch doesn't automatically
mean that it's polled more often.

For example, on the P-ROC, the direct switches are essentially like an extra 1x8
switch matrix where the "column" is always active. But the reads of the direct
switches are slotted into the timing of the reads of the matrix switches, meaning
P-ROC direct switches are not read any faster or more often than matrix switches.

(The P3-ROC uses SW-16 switch boards with 2 banks of direct switches each. I'm
awaiting confirmation to see how the timing works on those.)

FAST hardware switches connected to FAST I/O boards are direct as well. However
since each I/O board has its own processor on it, those switches are polled every
1ms.

(When FAST releases a switch matrix daughter board, those columns will need to
be strobed 1-by-1, meaning FAST matrix switches will have longer polling intervals
than FAST direct switches.)

Putting it all together
-----------------------

The P-ROC hardware allows for two debounce settings: *on* and *off*. Debounce
*on* means the switch must be in the same state for two consecutive reads before
the switch change event is sent to the host, and debounce *off* means the switch
event will be sent to the host as soon as it changes.

The polling interval on the P-ROC is configurable, and you also need to take into
consideration how big your matrix is (do you have 8 or 9 columns), how many
direct switches you have, etc.

FAST hardware accepts debounce settings based on milliseconds, e.g. "How many ms
does a switch have to be in the new state before a change event is sent to the
host?"

Putting it all together this means that on a P-ROC, *debounce off* is not the
same thing as as *debounce 0* on a FAST controller.

Depending on your hardware, *debounce off* on a P-ROC could still mean it takes
7ms (or more) for a switch to register, and *debounce on* on a P-ROC means that
it could take 17ms (or more) for a switch to register.

So if you have a FAST controller with a direct switch connected to a FAST I/O
board, setting (for example) *debounce 5ms* does *not* mean the FAST controller
is going to be "slower" to respond than a P-ROC that's set to *debounce off*.

This also shows why the recommendation in the P-ROC community has historically
been to set *debounce off* on autofire rules, since *debounce on* would mean a
switch could potentially have to be activated for 17ms (or more, again,
depending on the size of the matrix and other things). It's also why FAST has
been recommending 10ms for "instant" response and 30ms for "regular" switches.
(Which, if you don't like 10ms/30ms, you could change to 7ms/20ms, or whatever
you want.)

The point is that FAST's 10ms/30ms isn't actually that different than P-ROC's
off/on settings when you actually dig under the hood and see how the timing
works.
