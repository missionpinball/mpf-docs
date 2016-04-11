slide_player: (config setting)
==============================

The ``slide_player:`` section of your machine or mode config file is used to
"play" slides on a display. It can be used to show existing slides (calling
them by name), or to create and/or display new slides. It can also be used to
hide and/or remove slides.

.. include:: _machine_config_yes.rst
.. include:: _mode_config_yes.rst

The slide_player functionality is part of the MPF MC, so if you're using a
different media controller, such as the Unity 3D backbox server, then the
slide_player wouldn't exist for you.

Note that any slides that were created in a mode config file will be removed
when that mode stops. If the active slide for a display was created from a mode
config, then that slide will also be removed and the display will automatically
show the next-highest priority slide that exists for it.

Using slides in shows
---------------------

Like every config player in MPF, you can use the slide player in show files and
show configs in addition to using them in your machine and mode config files.
To do this, just add a ``slides:`` section to your step in the show file. Other
than that, every sub-setting is identical to what's covered below.

There are several different ways you can use the slide player, so we'll step
through the various options one-by-one.

Showing a named slide
---------------------
The first way to use the slide_player is to use it to show a slide that has
been previously defined but that does not exist as an active slide. In other
words, this shows a slide, based on its name, from the ``slides:`` section of
your config file. (Note that slides in MPF are "universal", meaning that there's
a single list of slide names and slide configs, so any mode can show any slide,
regardless of where that slide was defined.)

To show a slide by name in a config file, just add the event you want to use
to trigger the slide, and then the name of the slide. For example:

::

  slide_player:
    some_event: your_slide

The above configuration will show the slide called *your_slide* on the default
display target when the event called *some_event* is posted.

You can add as many event/slide combinations as you want in the slide_player:
section, like this:

::

  slide_player:
    some_event: your_slide
    ball_search_started: ball_search_started
    collecting_balls: please_wait_notice
    jackpot: jackpot_slide_1

You can also use a similar configuration to show slides as steps in shows, for
example:

::

  - time: 1s
    slides: your_slide

In the show, you'll notice there is no *event* to trigger the slide, because
since it's in a show, the slide is shown when it gets to that step in the show,
rather than it being triggered by an event.

All of these examples were pretty basic. They just "show the slide" and that's
it. But what if you want to use additional options to show the slide, like to
target a slide to a specific display, or to add a transition?

Showing a named slide with additional options
---------------------------------------------
Notice that in the above examples, we put the event name and the slide name on
the same line, like event:slide. If you want to add additional options to
control how the slide is displayed, you can instead put the slide name on the
line below (and indented) from the event, and then under there, you can add
as many options as you want.

For example, to show a slide with options in a config file, you would do
something like this:

::

  slide_player:
    some_event:
      your_slide:
        target: window
        transition: fade
        priority: 100

In this case, *some_event* is the event that triggers this slide, *your_slide*
is the name of the slide to show, and *target*, *transition*, and *priority* are
additional options that control how this slide is shown. (See the *slide_player
settings*) section a bit further down to see the list of options that are
available and how they work.

Again, you can configure different slides to play on different events in the
same ``slide_player:`` section of a config file, like this:

::

  slide_player:
    some_event:
      your_slide:
        target: window
        transition: fade
        priority: 100``
    some_other_event:
      other_slide:
        transition: move_in
        priority: 200

The above configuration would show the slide called *your_slide* when the event
*some_event* was posted (using the settings below it), and it would show the
slide *other_slide* when the event *some_other_event* was posted.

You can also mix and match the "simple" slide play commands from the previous
section with slides that have additional options, like this:

::

  slide_player:
    some_event:
      your_slide:
        target: window
        transition: fade
        priority: 100``
    some_other_event:
      other_slide:
        transition: move_in
        priority: 200
    a_third_event: yet_another_slide

If you want to play a slide in a show, but with additional options, you'd add
something like this to the step in the show file:

::

  - time: 1s
    slides:
      your_slide:
        target: window
        transition: fade
        priority: 100

Mixing and matching things here is nice if you want to show two different slides
on two different display targets in the same step of a show:

::

  - time: 1s
    slides:
      your_slide:
        target: window
      a_different_slide:
        target: dmd

Adding and showing a slide
--------------------------
So far, all the examples we've shown have been used to play existing slides that
have already been defined in the ``slides:`` section of your config file. But
you can also define new slides right inside your slide_player. (This is offered
as a matter of convenience. Personally we feel like it might be confusing to
define some slides in your ``slides:`` section and to define other slides
right in-line in your ``slide_player:`` config, but really the choice is up to
you.)

In MPF, every slide needs a name. So even if you define a new slide right in
your ``slide_player:`` section, you still need to give it a name. For example,
the following config will create a new slide called *some_new_slide_name* when
the event *some_event* is posted, and that new slide will have two text widgets.
(See the documentation on the ``slides:`` configuration for details about how to
define slides.)

::

  slide_player:
    some_event:
      some_new_slide_name:
        - type: text
          text: MY SLIDE
        - type: text
          y: 33%
          text: IS COOL

Here's a similar entry from a show file that shows how you can create and show
slides from within the show itself. In this case, a slide called
*some_new_slide_name* will be created (and shown) when this step of the show is
played.

::

  - time: 1s
    slides:
      some_new_slide_name:
        - type: text
          text: MY SLIDE
        - type: text
          y: 33%
          text: IS COOL

Note that any slides you create this way are "real" slides, and will be
available to be used elsewhere in your configs just like any slide that was
created in the ``slides:`` section of your config files. Also, like any slides,
these slides will be removed when a mode ends if they were created from within a
config file or show that was from a mode.

Adding and showing a slide with additional options
--------------------------------------------------
You can also specify additional options for showing a newly-created slide. In
this case, you'd move the widgets list under a section called ``widgets:``, and
then you can also add additional options (from the settings list below) which
control how a slide is displayed.

Here's an example of doing this from within a config file:

::

  slide_player:
    some_new_slide_name:
      widgets:
      - type: text
        text: MY SLIDE
      - type: text
        y: 33%
        text: IS COOL
      target: window
      transition: move_in

And here's how you'd do this from within a step in a show:

::

  - time: 1s
    slides:
      some_new_slide_name:
        widgets:
        - type: text
          text: MY SLIDE
        - type: text
          y: 33%
          text: IS COOL
        target: window
        transition: move_in


Here's a list of the additional options you can use when you work with slides in
either the ``slide_player:`` section of a config file or the ``slides:`` section
of a show file.


Settings & options
------------------

expire:
~~~~~~~
Single value, type: time string (will be converted to seconds). Default: None

Configures the slide to *expire*, meaning it will be automatically removed after
the time expires, and the display will show whatever the next-highest priority
slide is.

Note that this expiration timer runs regardless of whether the slide is actually
showing (since maybe a different mode is showing a slide on the display with a
higher priority).

Times here are entered in the standard MPF time string format, like
``expire: 2s`` or ``expire: 500ms``.


force:
~~~~~~
Single value, type: boolean (Yes/No or True/False). Default: False

True/false setting which "forces" this slide to be shown, regardless of its
priority and the priority of whatever other current slide is on the display.

Note that this forcing is a one-time thing, as any subsequent slides that are
played might play on top of it. If you really want a slide to show and not to
be overridden, you can use the *priority* setting.


priority:
~~~~~~~~~
Single value, type: integer. Default: None

Used to adjust (up or down) the priority of this slide. By default, slides are
played with the priority of the mode (for ``slide_player:`` sections from
configs) or the priority of the show (for ``slides:`` sections from shows), so
this *priority* setting is applied on top of that.

For example, if you have a mode running at priority 200, and then you have a
slide set to ``priority: 100`` in the ``slide_player:`` section of that mode
config, then that slide is displayed with priority 300.

You can also use negative values (like ``priority: -100``) to lower the
relative priority of a slide.

Note that if you have a ``slide_player:`` section in your machine-wide config
files, its base priority is zero.


show:
~~~~~
Single value, type: boolean (Yes/No or True/False). Default: True

True/false setting that lets you add an active slide to the display without
actually showing it right away.


target:
~~~~~~~
Single value, type: string. Default: None

Let's you specific the *display target* this slide will be shown on. This is
only needed if you have more than one display, or if you have a "picture in
picture" style slide which has subsections which are other slides.

To use the target, you specify the target name, such as ``target: window`` or
``target: upper_left_quadrant``.

Targets must be previously defined in order for them to work here. If you don't
specify a target, then the default display target is used.


transition:
~~~~~~~~~~~
.. todo::
   Need to add details here.

Used to specify a transition (move_in, fade, etc.) for how which animated
transition effect will be used to move from the current slide to this slide. If
you play a slide that will not be shown (which would happen if you play a slide
at a lower priority than the current slide that's being shown), then this
transition effect will not be shown since the new slide you're playing here will
be added to the display in the background.


widgets:
~~~~~~~~
.. todo::
   Need to add details here.

Lets you specify a list of widgets that will be added to a slide when you're
using the slide_player to define and name a new slide rather than just showing
an existing already-defined slide. See the slides documentation for details.

