slide_player:
=============

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`shows </shows/index>`                                       | **YES** |
+----------------------------------------------------------------------------+---------+

The ``slide_player:`` section of your config is where you configure slides to be shown (or
removed) based on events being posted.

Note that the slide player is a :doc:`config_player </config_players/index>`, so everything
mentioned below is valid in the ``slide_player:`` section of a config file *and* in the ``slides:``
section of a show step.

Full instructions on how to use the slide_player are included in the
:doc:`/displays/slides/showing_slides` guide. The documentation here is for
reference later.

Generically-speaking, there are two formats you can use for slide_player
entries: "express" and "full" configs. Express configs will look like this:

.. code-block:: yaml

   slide_player:
      event1: slide1
      event2: slide2
      event3: slide3

Full configs will look like this:

.. code-block:: yaml

   slide_player:
      event1:
         slide1:
            <settings>
      event2:
         slide2:
            <settings>
      event3:
         slide3:
            <settings>

In both cases, these configurations are saying, "When *event1* is posted,
show *slide1*. When *event2* is posted, show *slide2*. Etc."

This "express" config is down-and-dirty, with no options, to just show slides.
The full config lets you specify additional options (based on the settings
detailed below).

For example, the following config will show *slide_1* when *some_event* is posted, but it
will also override the default settings and show the slide on the display target called
*display1* and at a priority that's 200 higher than the base priority.

::

   slide_player:
      some_event:
         slide_1:
            target: display1
            priority: 200

Showing dynamically-created slides
----------------------------------

Both of the examples so far assumed that you were using the slide player to show a slide
that had already been defined in the :doc:`/config/slides` section if your config.
However you can also define slides right in-line in your slide player.

The following config will show a slide called *slide_1* when the *some_event* is posted,
but it assumes that *slide_1* does not yet exist, and it contains a list of widgets (one
text widget and one rectangle widget) which will be added to that slide.

Note that slide names are global in MPF, so if you already had a slide defined called
*slide_1* and you redefine it in your slide player like the example below, this new slide
will become *slide_1* and the old one will be gone.

::

   slide_player:
      some_event:
         slide_1:
            widgets:
            - type: text
              text: I AM A TEXT WIDGET
            - type: rectangle
              width: 200
              height: 100
              color: red

You can also mix-and-match defining a slide in the slide player as well as adjusting
properties of how the slide is shown. Just add multiple settings, like this:

::

   slide_player:
      some_event:
         slide_1:
            target: display2
            widgets:
            - type: text
              text: I AM A TEXT WIDGET
            - type: rectangle
              width: 200
              height: 100
              color: red
            transition: wipe

Remember that these slide player settings can also be used in show steps (in a ``slides:``
section). Any of the examples above apply, you just don't include the event name, like this:

::

   #show_version=5

   - time: 0
     slides: slide1
   - time: +3
     slides: slide2
   - time: +3
     slides:
       slide3:          # newly-defined slide here
         widgets:
           - type: text
             text: I AM SLIDE 3 IN THIS SHOW
             color: lime
   - time: +3
     slides:
       slide4:
         transition:
           type: move_out
           duration: 1s
           direction: up

Here's a list of all the valid settings for individual slides in the ``slide_player:``
section of your config file or the ``slides:`` section of a show. Note that all of these
are optional. Any that you do not include will be automatically added with the default
values applied.

Settings
--------

The following sections are optional in the ``slide_player:`` section of your config. (If you don't include them, the default will be used).

action:
~~~~~~~
Single value, type: one of the following options: play, remove. Default: ``play``

``play``
   Makes the slide active. Note that the actual slide shown on a display will
   be whichever active slide has the highest priority, so depending on what
   other slides are active, this action might not technically show the slide.

   Also note that if a transition is specified (either in the slide definition
   or the ``transition:`` section here, then than transition will be used when
   showing this slide.

``remove``
   Removes the slide from the list of active slides. If this slide is the
   highest priority slide that's currently showing, then the next-highest
   priority slide will be shown in its place.

   If a ``transition_out:`` setting is used, then that transition will be
   used here.

For example, to remove *slide1* when the event *remove_slide_1* is posted:

::

   slide_player:
      remove_slide_1:          # event name
         slide1:               # slide name
            action: remove

You can also specify a transition for the removal, like this:

::

   slide_player:
      remove_slide_1:          # event name
         slide1:               # slide name
            action: remove
            transition: fade

expire:
~~~~~~~
Single value, type: ``time string (secs)`` (:doc:`Instructions for entering time strings) </config/instructions/time_strings>` . Default: ``None``

Specifies that this slide should automatically be removed after the time has passed.
When it's removed, whichever slide is the next-highest priority will be shown.

The expiration timer starts immediately, so if the slide you're displaying here doesn't
end up being shown because it's not the highest-priority slide, the timer is still running
in the background, and the slide will still be removed when the timer expires.

If a ``transition_out:`` is specified, it will be applied when the slide expires.

force:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

Forces this slide to be shown, even if it's not the highest priority. Note that if you
add or remove a slide and the priority list is recalculated, whichever slide is the
highest priority will be shown. This ``force:`` option is sort of a one-time thing.
Really you should use priorities to control which slides are shown.

priority:
~~~~~~~~~
Single value, type: ``integer``. Default: ``None``

An adjustment to the priority of the slide that will be shown.

In MPF, all slides have a priority. Only one slide is show on a display at a time, and
the slide with the highest priority is automatically shown. If that slide is removed, the
next-highest priority slide is shown.

If you have a ``slide_player:`` section in a mode-based config file, then slides shown
will automatically have the priority of the mode. (``slide_player:`` sections from your
machine-wide config file use priority ``0``.) However you can adjust the priority
of a slide (up or down) by adding a ``priority:`` setting with a positive or negative
value.

If a slide is being shown as part of a show, the slide will have the priority set to
whatever the priority of the show is (which itself is also the priority of the mode unless
you adjust it)

show:
~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``True``

Specifies whether this slide should be shown. (It will only be shown if it's the highest
priority slide for that display.) If you set ``show: false``, then the slide will be
created and added to the display's collection of slides, but it won't be shown.

Note that if you add or remove a slide and the priority list is recalculated, whichever slide is the
highest priority will be shown. This ``show:`` option is sort of a one-time thing.
Really you should use priorities to control which slides are shown.

slide:
~~~~~~


:doc:`/about/help_us_to_write_it`

target:
~~~~~~~
Single value, type: ``string``. Default: ``None``

Specifies the display target this slide will be shown on. If you do not specify a target,
then the slide will be shown on the default display.

In MPF, display targets are the names of the displays themselves. However there is also
a *slide_frame* widget (literally a widget which you add to a slide which holds other
slides, kind of line picture-in-picture). When you add a slide_frame to a slide, you
give it a name, and that name is added to the list of valid targets.

So really the ``target:`` here is either the name of a display, or the name of a slide_frmae
where you want this slide to be displayed.

transition:
~~~~~~~~~~~

A sub-configuration of key/value pairs that make up the incoming transition
that will be used when this slide is shown. See the :doc:`/displays/slides/transitions`
documentation for details.

Note that you can also configure a transition when the slide is defined
in the :doc:`/config/slides` section of your config if you want to use the
same transition every time for a slide and don't want to always have to
define it here.

If you specify a transition in both places, the transition in the slide_player
or show will take precedence.


transition_out:
~~~~~~~~~~~~~~~

A sub-configuration of key/value pairs that make up the incoming transition
that will be used when this slide is removed. See the :doc:`/displays/slides/transitions`
documentation for details.

Note that you can add a transition out to the slide player when a slide
is shown, and it will be "attached" to the slide and used when that slide
is removed (either with the slide player or when a new slide is created with
a higher priority than it).

Or you can specify a transition out when you remove the slide (with
``action: remove``).

There can only be one transition between slides, so if an outgoing slide has
a transition out set, and an incoming slide has a transition set, then the
incoming transition will take precedence.
