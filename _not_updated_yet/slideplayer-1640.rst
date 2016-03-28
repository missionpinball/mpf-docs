
The `slide_player:` section of your config file lets you configure
various `display elements`_ and `slides`_ that will automatically play
based on certain MPF events. This section is very similar to the
`sound_player:` and `show_player:` sections, except this one is for
displays. This sectioncan be used in your machine-wide config files.
This sectioncan be used in your mode-specific config files. Here's an
example:


::

    
    slide_player:
        player_score:
          - type: text
            text: "%score%"
            number_grouping: true
          - type: text
            text: "%player|number%"
            v_pos: bottom
            h_pos: left
            size: 5
          - type: text
            text: %player|ball%"
            v_pos: bottom
            h_pos: right
            size: 5
        tilt_hit:
            type: text
            text: WARNING
        player_add_success:
            type: text
            text: PLAYER %num% ADDED
            expire: 2s
        ball_live_added:
            type: text
            text: LET'S GO!
            expire: 2s
        balldevice_deadworld_ball_enter:
            type: text
            text: "BALLS LOCKED: %balls%"


First you create an entry called `slide_player:`. Then you create
subsections in there for MPF events, followed by one or more entries
for specific `display elements`_ (and their settings) that you'd like
to be displayed when that event is posted. Take a look at the
following section for a simple example:


::

    
        tilt_hit:
            type: text
            text: WARNING


What this does is when the event `tilt_hit` is posted, a display
element of type "Text" will be put on the display, and the text will
say "WARNING". Since no other settings are defined, the defaults (also
configurable in your configuration files) will be used. There are
several options for each display element, including:



type:
~~~~~

The `type:` can be any of the display element options `covered here`_.
The current options are *text*, *shape*, *image*, *animation*,
*movie*, *character_picker*, and *entered_chars*. Refer to the link
for details about the options you can use for each different type of
element. Note that *text* display elements can also include percent
signs to use dynamically-generated text. (See the section below on
dynamically-generated text for details.)



expire:
~~~~~~~

An `MPF time string`_(such as `2s` or `500ms`) that causes this slide
to automatically remove itself. Whatever next-highest priority slide
is will be displayed in its place. Note that if this slide enters via
a transition, the timer will start after the transition is complete.



slide_name:
~~~~~~~~~~~

A string name that you'd like to call the slide that is created. If a
slide already exists with this name and `clear_slide:` is set to
False, then these elements will be added to the existing slide. If you
don't specify a slide_name, then a new slide will be created with a
random name.



slide_priority:
~~~~~~~~~~~~~~~

The priority this slide will have. This has to be the same or greater
than whatever slide is currently showing or else this slide won't show
up. (It will still be created and will be shown later if the current
higher priority slide is removed.) If this ShowPlayer: section is
being configured as part of a mode config, the slide_priority entered
here will be added to the mode's base priority. (e.g. If the mode is
running at priority 300 and you specify `slide_priority: 1`, the slide
created will have a priority of 301.)



clear_slide:
~~~~~~~~~~~~

True/False as to whether the slide should be cleared (erased) before
these elements are added to it. This only applies when you specify a
slide name and when a slide already exists with that name.



clear_slides:
~~~~~~~~~~~~~

Clears all the slides created by the mode where this slide_player:
entry is. By default, MPF keeps at least one slide per mode unless the
slides were configured to expire or the mode ends. But what if you
want to clear all the slides from a mode but you don’t want to end
that mode? That's where the *clear_slides* option comes in. To use it,
just add `clear_slides: yes` to an event entry in `slide_player:`
section of a mode config file:


::

    
    slide_player
      some_event:
        clear_slides: yes


In the example above, when the event *some_event* is posted, all of
the slides that mode created will be removed.



persist_slide:
~~~~~~~~~~~~~~

True/False as to whether this should should persist after it's no
longer being shown. If True, then you can show this slide again by
calling it by name.



display:
~~~~~~~~

String name of the display that you'd like this slide to be shown on.
(Such as *DMD* or *window*.) If you don't specify a display then this
slide will be built for the default display.



transition:
~~~~~~~~~~~

If you want to apply a transition into this slide, you can add a
`transition:` entry with sub-settings that control the transition
itself.



Specifying multiple display elements for one event
--------------------------------------------------

If you want to add two elements to the display, note that you can
enter multiple items as long as they are all indented the same amount
and you add a dash ("-") to signify when the next item starts. For
example:


::

    
        ball_started:
          - type: Text
            text: "%score%"
            min_digits: 2
            number_grouping: true
          - type: Text
            text: PLAYER %number%
            v_pos: bottom
            h_pos: left
            size: 5
          - type: Text
            text: BALL %ball%
            v_pos: bottom
            h_pos: right
            size: 5
            transition:
                type: move_in
                direction: top


This entry puts three separate display elements on the display when
the `ball_started` event is posted.


+ A Text element with text that shows the current score,using the
  default size and position. Note that "%score%" is wrapped in quotation
  marks since its value starts with %, and that confuses the YAML
  parser. So we wrap it in quotes to tell the parser that the value is a
  string.
+ A Text element with text that says "PLAYER %number%" in the bottom
  left position, rendered at font size 5.
+ A Text element with text that says "BALL %ball%" in the bottom right
  position, rendered at font size 5.




On-the-fly text replacement with % signs
----------------------------------------

The *slide_player* entries in your config file are triggered by
events. Many events have keyword/value parameters passed along with
event itself when it was posted, and you can access the values of
those parameters with the text display elements in your
*slide_player*. To access event parameters in a text display element,
just add the parameter name surrounded with percent signs, like this:


::

    
    slide_player:
      player_add_success:
        type: text
        text: PLAYER %num% ADDED


Since the *player_add_success* event includes a parameter *num* which
is the player number, this will print *PLAYER 1 ADDED* (or whatever
the number of the new player is) when the *player_add_success* event
is posted. You can include % variables in-line with other text or by
themselves on their own lines. Note though that if you include them on
their own lines, a YAML value cannot start with a percent sign, so you
need to put it in quotes, like this:


::

    
    type: "%num%"


You can also include the values of player variables and machine
variables in your *slide_player* entries. See the documentation on the
`text display element`_ for more details.

.. _slides: https://missionpinball.com/docs/mpf-core-architecture/displays-dmd/slides/
.. _text display element: https://missionpinball.com/docs/mpf-core-architecture/displays-dmd/display-elements/text/
.. _display elements: https://missionpinball.com/docs/mpf-core-architecture/displays-dmd/display-elements/
.. _covered here: https://missionpinball.com/docs/displays/display-elements/
.. _MPF time string: https://missionpinball.com/docs/configuration-file-reference/entering-time-duration-values/


