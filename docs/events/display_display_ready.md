---
title: [display](../index.md)(name)_ready
---

# [display](../index.md)(name)_ready


*MPF-MC Event*

The display target called (name) is now ready and available to show
slides. This event is useful with display widgets where you want to add
a display to an existing slide which shows some content, but you need to
make sure the display exists before showing a slide. So if you have a
display called "overlay", then you can add it to a slide however you
want, and when it's added, the event "display_overlay_ready" will be
posted, and then you can use that event in your slide_player to trigger
the first slide you want to show. Note that this event is posted by
MPF-MC and will not exist on the MPF side. So you can use this event for
slide_player, widget_player, etc., but not to start shows or other
things controlled by MPF.

*This event does not have any keyword arguments*

Event is posted by [displays:](../config/displays.md)
