mc_ready (MPF event)
====================

Posted when the MPF-MC is available to start showing slides and
playing sounds.

Note that this event does not mean the MC is done loading. Instead it's
posted at the earliest possible moment that the core MC components are
available, meaning you can trigger "boot" slides from this event (which
could in turn be used to show asset loading status, boot progress,
etc.)


Keyword arguments: None
