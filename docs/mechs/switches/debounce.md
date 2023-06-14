---
title: Debouncing in Pinball Machines
---

# Debouncing in Pinball Machines


A pinball machine is a mechanical machine with a lot mechanical,
electronic and electromagnetical interferences. This has to be mitigated
on multiple levels to prevent unwanted effects:

1.  Prevent too much communication between hardware platform and CPU. A
    lot of switch changes could easily overflow the communication bus or
    starve the CPU/controller.
2.  Prevent too many switch events in the game. It is not uncommon to
    show slides or play sounds on a switch event. If this event occurs
    very often this may easily slow down your game.
3.  Prevent coils from pulsing too often. If a coil pulses on a switch
    hit and the switch activates constantly it might essentially be
    stuck on for the whole time which in the best case would only blow a
    fuse and in the worst case might burn down the machine.

As you can see there are multiple types of debouncing. We will explain
how to use those in the following:

## Switch Debouncing at the Hardware Level

To prevent too much communication between you hardware platform and your
CPU there is typically some switch debouncing at the hardware level.
This is what most electronic engineers will first think about when
taking about *debouncing*.

On the surface, switch *debounce* is pretty straightforward. Switches
are mechanical things, computers are fast, and your pinball software
wants to make sure a switch is actually in a new state before acting on
a switch.

Pinball controllers set debounce in different ways. For example, some
platforms (for instance, P-ROC, P3-ROC) say "a switch must be in a new
state for 2 consecutive reads" to be considered debounced, while other
platforms (e.g. FAST) focus on time-based durations rather than number
of reads, saying, "a switch must be in a new state for X milliseconds
before it's considered debounced." In practise, there is not much
difference between those two.

When considering switch debounce, the switch usually is supposed to be
active for the whole debounce time. So this could also be called
"minimum active time". Usually this time is in the range of two to
four milliseconds. The reason for that is that waiting for a minimum
active time induces some lag to the switch event.

Still, switch debounce is often disabled for hardware rules (e.g. for
pop bumpers or sling shots) to render them more responsive. However,
this also them more susceptible to interferences or phantom hits. For
that reason, in some platforms, even in that case a minimal debounce
time is enforced (around one millisecond).

There is very little reason to increase switch debounce time to more
than about four ms (see next section on what to do instead). Because if
you set your debounce times too long, then you risk switch events being
missed. (It would be annoying if a ball brushed a pop bumper and the
bumper not didn't fire.)

By default, MPF will enable switch debounce in all
[switches](../../config/switches.md). For
autofires such as pop bumpers or sling shots it will be disabled. You
can overwrite this using the `debounce` setting in your
[switches](../../config/switches.md).

## Preventing too many Switch Events in MPF

Depending on the type of switch you will see hits between five and fifty
milliseconds. So any switch debounce time above that will miss switch
hits. However, if you set your debounces too short, you risk getting
multiple switch events for what should have been a single switch event.
(Again it would be annoying if a ball hit a pop bumper and that bumper
fired once, but you actually got back multiple switch events which led
to multiple scores, multiple sound effects, etc.)

The solution to this is to combine switch debounce with a window to
ignore multiple hits. There are two ways to implement this.

### Ignore Window

The first and most used way is to define a period after registered hit
which ignores all further hits. This setting is called
`ignore_window_ms` in your
[switch config](../../config/switches.md). For
example, if you set `ignore_window_ms: 100`, then a switch is activated
once, then again 50ms later, the second activation will be ignored. The
timer is set based on the last switch hit that *activated* the switch,
so if another switch hit came in 105ms after the first (which would be
55ms after the second), it will also count.

In most cases you can easily set `ignore_window_ms` to a few hundred
milliseconds. This will not affect hardware rules. Use `recycle` on your
[coil](../../config/coils.md) instead.

This is what most javascript programmers understand when they hear
debouncing. Kind of related but also a bit different from what EEs
understand by it.

### Throttling

There is another technique which is commonly used in the javascript
works when working with computationally expensive callbacks which is
called throttling. The goal here is similar but the implementation is
differerent. Instead of having a window after each activation this
defines a maximum number of calls per time unit. For instance a maximum
of 10 calls per second. This would certainly also be possible in MPF but
is currently not supported. We think this would be inferior to
`ignore_window_ms` since it is more susceptible to bursts it might still
cause temporary lags. However, we might add this later to prevent
permanent problems with bad or bouncy switches.

## Preventing Coil Overheating

When enabling coils you usually use PWM to control the maximum power.
However, when pulsing coils they are often enabled without any PWM for a
while. This works fine for a single activation but might cause problems
when a switch is activated repeatedly (i.e. because of interferences).
In that case, the coil would be permanently pulsed and, thereby, enabled
all the time. That will hopefully only blow a fuse on that coil but
might as well burn down the machine. To prevent this there is `recycle`
on your [coil](../../config/coils.md). When set
to true it will prevent any further pulse for a certain time after a
pulse (similar to `ignore_window_ms` on the switch above). The duration
depends on your platform and might also be configurable.

## Understanding switch scanning loop speed

The other major factor which affects debounce involves the timing of how
the switches are read.

In all modern pinball platforms, a switch changing state doesn't
interrupt the controller. Instead, the controller reads the state of all
switches at a certain interval.

But even this varies from platform-to-platform, and even based on
whether you have matrix or direct switches. (More on this in a bit.)

The important thing, though, is that different controllers and different
types of switches are checked at different intervals. That could be
every millisecond, or every 1ms, or every 2ms... really it's up to the
controller and switch type as they're all different. Scanning speed
induces some delay and jitter to your debounce times. Refer to your
platform documentation for details.

In most cases switch matrixes are scanned slighly slower than direct
switches on a hardware platform. However, they are usually still fast
enough not to cause any problems with missed switches.
