Game Logic
==========

Most (potentially all) of your game logic can be configured in the MPF
config files. For classical language programmers new to MPF, an introduction
to how the framework handles logical decisions may be helpful. All game logic
is tied to event posts. Mostly, this is achieved through config file programming
of timers, shots, counters, multiballs, accruals, etc....  These prebuilt
modules (listed below) listen for events to be posted then read the state of the
hardware and/or perform manipulations on player or device variables. In turn
these modules issue their own event posts which drive the behavior or other
modules and devices to start and stop modes, control diverts, set bonus
multipliers and everything else game related.

A question beginners may have is "How do I tell MPF to perform an action when
two or more conditions are met simultaneously?" In an event driven framework
this is not the correct way to conseptualize the logic. Again, nothing game related
happens without being driven by a posted event. Because events only exist as a
descrete moments in time, it does not work to attempt (pseudocode) logic such as
IF event1 and event2 then post event3. Nevertheless, MPF provides a flexible and
robust mechanism for performing logic on events. This is where Conditional Events
come in.

In brief, the the way conditional events work is by telling MPF to process a
particular event if and only if additional conditions are met. These conditions
(listed inside curly brackets) can relate to player variables (such as score)
machine variables (such as credit) or device variables (such as timer ticks
or number of balls locked). See <conditional/index> for specific examples.

With this flexibility in mind, Here is a list of pre-built game logic modules
containing the description, how to guides, links to tutorials, event listings,
and configuration

.. note:: Most of the "How To" guides for these sections still need to be written.

.. toctree::
   :titlesonly:

   Achievements <achievements/index>
   Ball Holds <ball_holds/index>
   Ball Locks <ball_locks/index>
   Ball Saves <ball_saves/index>
   Ball Search <ball_search/index>
   Ball Start and End Behaviour <ball_start_end/index>
   Ball Tracking <ball_tracking/index>
   Bonus <bonus/index>
   Coins & Credits <credits/index>
   Combo Switches <combo_switches/index>
   Extra Balls <extra_balls/index>
   High Scores <high_scores/index>
   Logic Blocks <logic_blocks/index>
   Match Mode <match_mode/index>
   Modes <modes/index>
   Multiballs <multiballs/index>
   Player Variables <players/index>
   Replays <replays/index>
   Timed Switches <timed_switches/index>
   Timers <timers/index>
   Service Mode <service_mode/index>
   Shots <shots/index>
   Skill Shot <skill_shot/index>
   Video Modes <video_modes/index>
   Scoring <scoring/index>
   Tilt <tilt/index>

