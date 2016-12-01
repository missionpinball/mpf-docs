mc_ready
========

*MPF Event*

Posted when the MPF-MC is available to start showing slides and
playing sounds.

Note that this event does not mean the MC is done loading. Instead it's
posted at the earliest possible moment that the core MC components are
available, meaning you can trigger "boot" slides from this event (which
could in turn be used to show asset loading status, boot progress,
etc.)

If you want to show slides that require images or video loaded from
disk, use the event "init_done" instead which is posted once all the
assets set to "preload" have been loaded.

*This event does not have any keyword arguments*
