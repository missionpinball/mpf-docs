---
title: Mode Stop Sequence
---

# Mode Stop Sequence


Here's what happens behind-the-scenes when a mode stops.

1.  An event listed in the mode's `stop_events:` setting is posted.

2.  This is handled by the mode's `stop()` method.

    1.  If the mode is not active, this process ends.
    2.  If a *callback* argument was passed, it's saved now for later
        use
    3.  Other *kwargs* are saved for later use

3.  Switch handlers registered by that mode are removed.

4.  Timers set in that mode are stopped and removed.

5.  Delays set in that mode are cleared.

6.  An queue event is posted: *mode_<mode_name>_stopping*.

7.  Once that queue is clear, the mode's `_stopped()` method is called.

8.  Any mode *stop_methods* registered for that mode are called
    one-by-one. (mode stop_methods are based on anything that gets
    returned from the call to the mode's start_methods when the mode
    starts).

9.  An event *mode_<mode_name>_stopped* is posted.

10. Once any handlers for that event have finished, the mode's
    `_mode_stopped_callback()` method is called.

11. Mode event handlers are removed.

12. Devices that were created as part of this mode are removed.

13. The mode's `mode_stop()` method is called. (This is the method that
    can be subclassed in custom mode code for things you want to run
    when the mode stops.)

    1.  If *kwargs* were passed as part of the event in Step 1,
        they're included in the call to `mode_stop()`.

14. If a *callback* was saved in Step 2, it's called now.
