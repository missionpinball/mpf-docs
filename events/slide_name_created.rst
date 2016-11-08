slide_(name)_created
====================

*MPF Event*

A slide called (name) has just been created.

This means that this slide now exists, but it's not necessarily the
active (showing) slide, depending on the priorities of the other slides
and/or what else is going on.

This is useful for things like the widget_player where you want to
target a widget for a specific slide, but you can only do so if
that slide exists.

Slide names do not take into account what display or slide frame
they're playing on, so be sure to create machine-wide unique names
when you're naming your slides.

Keyword arguments
-----------------

*None*
