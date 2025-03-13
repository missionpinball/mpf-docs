---
title: display_(name)_initialized
---

# display_(name)\_initialized


*MPF-MC Event*

Event is posted by [displays:](../config/displays.md)

The display called (name) has been initialized. This event is generated
in the MC, so it won't be sent to MPF if the MC is started up and ready
first.

This event is part of the MPF-MC boot process and is not particularly
useful for game developers. If you want to show a "boot" slide as
early as possible, use the *mc_ready* event.

*This event does not have any keyword arguments*
