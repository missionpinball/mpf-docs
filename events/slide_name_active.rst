slide_(name)_active
===================

*MPF Event*

A slide called (name) has just become active, meaning that
it's now showing as the current slide.

This is useful for things like the widget_player where you want to
target a widget for a specific slide, but you can only do so if
that slide exists.

Note that this event will be posted anytime this slide is asked to
become the active slide, even if was already active.

Slide names do not take into account what display or slide frame
they're playing on, so be sure to create machine-wide unique names
when you're naming your slides.


Keyword arguments
-----------------

*None*
