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

This is an example:

.. code-block:: mpf-mc-config

   #! slides:
   #!   slide1: []
   #!   slide2: []
   #!   slide3: []
   slide_player:
     event1: slide1
     event2: slide2
     event3: slide3

See :doc:`/config_players/slide_player` for details.

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

.. code-block:: mpf-mc-config

   #! slides:
   #!   slide1: []
   slide_player:
     remove_slide_1:           # event name
       slide1:                 # slide name
         action: remove

You can also specify a transition for the removal, like this:

.. code-block:: mpf-mc-config

   #! slides:
   #!   slide1: []
   slide_player:
     remove_slide_1:           # event name
       slide1:                 # slide name
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

If a ``transition_out:`` is specified, it will be applied when the slide expires:

.. code-block:: mpf-mc-config

   slides:
     base:
       widgets:
         - type: text
           text: BASE SLIDE
           color: ff0000
           font_size: 100
     expire_slide:
       widgets:
         - type: text
           text: EXPIRE 5s
           color: purple
           y: 66%
       expire: 5s
       transition_out:
         type: wipe
         duration: 5s
   slide_player:
     mc_reset_complete.1: expire_slide
     mc_reset_complete.2: base

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
Single value, type: ``string``. Default: ``None``

You can specify the slide name here (instead of as key for the complete player).
There are reasons to use this but you won't need it in most cases.

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

.. code-block:: mpf-mc-config

   slides:
     base:
       widgets:
         - type: text
           text: BASE SLIDE
           color: ff0000
           font_size: 100
     top_slide:
       widgets:
         - type: text
           text: TOP SLIDE
           color: purple
           y: 66%

   slide_player:
     mc_reset_complete.1: top_slide
     mc_reset_complete.2: base
     mc_reset_complete.3:
       top_slide:
         action: remove
         transition:
           type: fade
           duration: 3s

Or you can specify a transition out when you remove the slide (with
``action: remove``).

There can only be one transition between slides, so if an outgoing slide has
a transition out set, and an incoming slide has a transition set, then the
incoming transition will take precedence.
