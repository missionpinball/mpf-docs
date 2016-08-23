Mode Stop Sequence
==================

Here's what happens behind-the-scenes when a mode stops.


#. An event listed in the mode's `stop_events:` setting is posted.
#. This is handled by the mode's `stop()` method.

    #. If the mode is not active, this process ends.
    #. If a *callback* argument was passed, it's saved now for later use
    #. Other *kwargs* are saved for later use

#. Switch handlers registered by that mode are removed.
#. Timers set in that mode are stopped and removed.
#. Delays set in that mode are cleared.
#. An queue event is posted: * mode_<mode_name>_stopping *.
#. Once that queue is clear, the mode's `_stopped()` method is called.
#. Any mode *stop_methods* registered for that mode are called one-by-
   one. (mode stop_methods are based on anything that gets returned from
   the call to the mode's start_methods when the mode starts).
#. An event *mode_<mode_name>_stopped* is posted.
#. Once any handlers for that event have finished, the mode's
   `_mode_stopped_callback()` method is called.
#. Mode event handlers are removed.
#. Devices that were created as part of this mode are removed.
#. The mode's `mode_stop()` method is called. (This is the method that
   can be subclassed in custom mode code for things you want to run when
   the mode stops.)

    #. If *kwargs* were passed as part of the event in Step 1, they're
       included in the call to `mode_stop()`.

#. If a *callback* was saved in Step 2, it's called now.




