---
title: Game Logic
---

# Game Logic


Most (potentially all) of your game logic can be configured in the MPF
config files. For classical language programmers new to MPF, an
introduction to how the framework handles logical decisions may be
helpful. All game logic is tied to event posts. Mostly, this is achieved
through config file programming of timers, shots, counters, multiballs,
accruals, etc.... These prebuilt modules (listed below) listen for
events to be posted then read the state of the hardware and/or perform
manipulations on player or device variables. In turn these modules issue
their own event posts which drive the behavior or other modules and
devices to start and stop modes, control diverts, set bonus multipliers
and everything else game related.

A question beginners may have is "How do I tell MPF to perform an
action when two or more conditions are met simultaneously?" In an event
driven framework this is not the correct way to conseptualize the logic.
Again, nothing game related happens without being driven by a posted
event. Because events only exist as a descrete moments in time, it does
not work to attempt (pseudocode) logic such as IF event1 and event2 then
post event3. Nevertheless, MPF provides a flexible and robust mechanism
for performing logic on events. This is where Conditional Events come
in.

In brief, the the way conditional events work is by telling MPF to
process a particular event if and only if additional conditions are met.
These conditions (listed inside curly brackets) can relate to player
variables (such as score) machine variables (such as credit) or device
variables (such as timer ticks or number of balls locked). See
<conditional/index> for specific examples.

With this flexibility in mind, Here is a list of pre-built game logic
modules containing the description, how to guides, links to tutorials,
event listings, and configuration

!!! note

    Most of the "How To" guides for these sections still need to be
    written.

* [Achievements](achievements)
* [Ball Holds](ball_holds.md)
* [Ball
Locks](ball_locks)
* [Ball Saves](ball_saves)
* [Ball Search](ball_search)
* [Ball Start and End Behavior](ball_start_end.md)
* [Ball Tracking](ball_tracking.md)
* [Bonus](bonus)
* [Coins & Credits](credits.md)
* [Combo Switches](combo_switches.md)
* [Extra Balls](extra_balls.md)
* [High Scores](high_scores)
* [Logic Blocks](logic_blocks)
* [Match Mode](match_mode.md)
* [Modes](modes)
* [Multiballs](multiballs)
* [Player Variables](players.md)
* [Replays](replays.md)
* [Timed Switches](timed_switches.md)
* [Timers](timers.md)
* [Service Mode](service_mode.md)
* [Shots](shots)
* [Skill Shot](skill_shot.md)
* [Video Modes](video_modes.md)
* [Scoring](scoring)
* [Tilt](tilt)
