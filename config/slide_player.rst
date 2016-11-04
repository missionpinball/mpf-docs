slide_player:
=============

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

.. note:: This section can also be used in a show file in the ``slides:`` section of a step.

.. overview

The ``slide_player:`` section of your config is where you configure slides to be shown (or
removed) based on events being posted.

Note that the slide player is a :doc:`config_player </config_players/index>`, so everything
mentioned below is valid in the ``slide_player:`` section of a config file *and* in the ``slides:``
section of a show step.

Generically-speaking, the ``slide_player:`` section of your config file, or the ``slides:``
section of a show step, looks like this:

::

   event:
      slide_name:
         <settings>
   event:
      slide_name:
         <settings>
   event:
      slide_name:
         <settings>

That said, there are several different ways this config can actually be entered. Hopefully
having lots of options isn't too confusing! We can remove some if so. :)

First, there's a simple "express" config which is just `event:slide`, on one line, like this:

::

   slide_player:
      some_event: slide_1_awesome
      event2: slide2
      different_event: slide3

In the config above, when the event *some_event* is posted, *slide_1_awesome* will be shown
on the default display. When *event2* is posted, *slide2* will be shown, and when
*different_event* is posted, *slide3* will be shown.

This "express" config is down-and-dirty, no options, just show slides.

However you might want to add some additional options for when a slide is displayed. To
do this, instead of putting the slide name on the same line as the event, you put it
indented on the next line, followed below by more settings for how that slide is shown.

For example, the following config will show *slide_1* when *some_event* is posted, but it
will also override the defaul settings and show the slide on the display target called
*display1* and at a priority that's 200 higher than the base priority.

::

   slide_player:
      some_event:
         slide_1:
            target: display1
            priority: 200

Both of the examples so far assumed that you were using the slide player to show a slide
that had already been defined with its widgets and everything. However you can also define
slides right in-line in your slide player.

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

   #show_version=4

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


Optional settings
-----------------

The following sections are optional in the ``slide_player:`` section of your config. (If you don't include them, the default will be used).

action:
~~~~~~~
Single value, type: one of the following options: play, remove. Default: ``play``

Specifies what action should be taken. The default is ``play`` which means the slide is
displayed. You can also use ``action: remove`` to remove a slide.

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

persist:
~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

.. todo::
   Add description.

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

Speficies whether this slide should be shown. (It will only be shown if it's the highest
priority slide for that display.) If you set ``show: false``, then the slide will be
created and added to the display's collection of slides, but it won't be shown.

Note that if you add or remove a slide and the priority list is recalculated, whichever slide is the
highest priority will be shown. This ``show:`` option is sort of a one-time thing.
Really you should use priorities to control which slides are shown.

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


