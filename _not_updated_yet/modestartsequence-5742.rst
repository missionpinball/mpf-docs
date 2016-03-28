
Here's what happens when a mode starts:


#. One of the events in the mode's `start_events:` is posted.
#. The mode's `start()` method responds since it's registered as a
   handler for those events.

    #. If the mode is currently active, this process ends.
    #. If a *callback* kwarg is included in the event, it's saved for
       later use.
    #. Any *kwargs* that were attached to the event which started the mode
       are saved for later use.

#. Any devices that are configured in this mode's config that are not
   already created are created now.
#. Any events listed in the mode's `stop_events:` setting are
   registered and will call the mode's `stop()` method if they're posted.

    #. These events are registered with the priority of the mode +1, so
       they are called first.

#. Any registered mode *start_methods* are called one-by-one. These
   are called with the mode, the mode's config, and the mode's priority
   as *kwargs*.
#. Any device control_events from the mode config are registered
#. A queue event is posted called *mode_<mode_name>_starting* .
#. The mode's `_started()` method is the callback for the starting
   queue event and is called when that event is complete.
#. Mode timers are started.
#. An event *mode_<mode_name>_started* is posted.
#. The mode's `_mode_started_callback()` method is the callback for
   the started event, so it's called once that event is complete.
#. The mode's `mode_start()` method is called. (This is the method
   that can be subclassed to run custom mode code.)

    #. Any *kwargs* that were passed along with the event that started the
       mode are passed to the `mode_start()` method.

#. If a start *callback* was passed with the event that started the
   mode, it's called now.




