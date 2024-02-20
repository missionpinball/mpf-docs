---
title: Mode Start Sequence
---

# Mode Start Sequence


Here's what happens when a mode starts:

1.  One of the events in the mode's `start_events:` is posted.

2.  The mode's `start()` method responds since it's registered as a
    handler for those events.

    1.  If the mode is currently active, this process ends.
    2.  If a *callback* kwarg is included in the event, it's saved
        for later use.
    3.  Any *kwargs* that were attached to the event which started the
        mode are saved for later use.

3.  Any devices that are configured in this mode's config that are not
    already created are created now.

4.  Any events listed in the mode's `stop_events:` setting are
    registered and will call the mode's `stop()` method if they're
    posted.

    1.  These events are registered with the priority of the mode +1,
        so they are called first.

5.  Any registered mode *start_methods* are called one-by-one. These are
    called with the mode, the mode's config, and the mode's priority
    as *kwargs*.

6.  Any device control_events from the mode config are registered

7.  A queue event is posted called *mode_\(mode_name\)_starting* .

8.  The mode's `_started()` method is the callback for the starting
    queue event and is called when that event is complete.

9.  Mode timers are started.

10. An event *mode_\(mode_name\)_started* is posted.

11. The mode's `_mode_started_callback()` method is the callback for
    the started event, so it's called once that event is complete.

12. The mode's `mode_start()` method is called. (This is the method
    that can be subclassed to run custom mode code.)

    1.  Any *kwargs* that were passed along with the event that
        started the mode are passed to the `mode_start()` method.

13. If a start *callback* was passed with the event that started the
    mode, it's called now.
