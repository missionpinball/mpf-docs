How to setup and use the virtual segment display emulator
=========================================================

This guide explains the basic steps to setup the virtual segment display emulator for your machine. Support for the
visual component of the virtual segment display emulator is part of the MPF media controller and only available if
you're using MPF-MC for your media controller.

1. Add your main display to your MPF config
-------------------------------------------

Add the segment display to your list of displays in your machine-wide config
file:

.. code-block:: mpf-mc-config

   displays:
     window:
       width: 600
       height: 200
   ##! test
   #! post show_slide_event
   #! advance_time_and_run .1

The example above contains a single display named "window" and has a size of
600x200. This will be the display that shows up on the computer
screen.

2. Add your window configuration
--------------------------------

The ``window:`` section of the machine-wide config holds the settings for the
on-screen display window. If you don't have this section, add it now.

You can make the width and height anything you want. In this case we're just
configuring it to be 600x200 with a window title of "Mission Pinball
Framework".

.. code-block:: mpf-mc-config

   window:
     width: 600
     height: 200
     title: Mission Pinball Framework
   ##! test
   #! post show_slide_event
   #! advance_time_and_run .1


3. Configure a window slide to show the on screen segment display
-----------------------------------------------------------------

Now we have a working on-screen window, but if you run ``mpf both`` now, your
on screen window will be blank because we haven't built any slides to show up.

So in this step, we're going to build a slide for the on-screen window that will
be shown when MPF starts. We'll add some widgets to that slide to make it look
like a segment display.

First, create a ``slides:`` section in your machine config (if you don't have
one already), and then create an entry for the slide that we want to show. In
this case, we've decided to name that slide "window_slide_1". (Of course you can
call this slide whatever you want.)

.. code-block:: mpf-mc-config

   slides:
     window_slide_1:
   ##! test
   #! post show_slide_event
   #! advance_time_and_run .1

Next we have to add some widgets to that slide. (Refer to the
:doc:`documentation on widgets </displays/widgets/index>` if you're not familiar
with widgets yet.)

The first widget will be a :doc:`segment display emulator widget </displays/widgets/segment_display_emulator/index>`
with a :doc:`glow effect </displays/widgets/display/effects>`
which is a widget which renders a emulation of a segment display:

.. code-block:: mpf-mc-config

   #! displays:
   #!   window:
   #!     width: 600
   #!     height: 200
   slides:
     window_slide_1:
     - type: segment_display_emulator
       name: display1
       character_count: 7
       character_slant_angle: 0
       character_spacing: 20
       segment_width: 0.11
       segment_interval: 0.04
       segment_off_color: 4b4c4a30
       segment_on_color: fe961bff
       side_bevel_enabled: true
       dot_enabled: true
       comma_enabled: true
       text: HELLO
       width: 600
       height: 150
       y: 100

   #! slide_player:
   #!   show_slide_event:
   #!     window_slide_1:
   #!       target: window
   ##! test
   #! post show_slide_event
   #! advance_time_and_run .1
   #! assert_slide_on_top window_slide_1 window

As you can see there are a lot of configuration options to modify the rendering of the segment display
segments/characters. This leads to a lot of very different looks for the resulting characters. One important
item to note is the name parameter of the segment display emulator must match the name of the hardware
segment display in MPF that we wish to connect to.

4. Configure the slide to show when MPF starts
----------------------------------------------

Now we have a nice slide with the virtual segment display on it, but if you run MPF, you
still won't see it because we didn't tell MPF to show that slide in the window.
So that's what we're doing here:

.. code-block:: mpf-mc-config

   #! displays:
   #!   window:
   #!     width: 600
   #!     height: 200
   #! slides:
   #!  window_slide_1:
   #!  - type: segment_display_emulator
   #!    name: display1
   #!    character_count: 7
   #!    character_slant_angle: 0
   #!    character_spacing: 20
   #!    segment_width: 0.11
   #!    segment_interval: 0.04
   #!    segment_off_color: 4b4c4a30
   #!    segment_on_color: fe961bff
   #!    side_bevel_enabled: true
   #!    dot_enabled: true
   #!    comma_enabled: true
   #!    text: HELLO
   #!    width: 600
   #!    height: 150
   #!    y: 100
   slide_player:
     init_done:
       window_slide_1:
         target: window
   ##! test
   #! advance_time_and_run .1
   #! assert_slide_on_top window_slide_1 window

If you don't have a slide_player: entry in your machine-wide config, go ahead
and add it now. Then create an entry for the :doc:`/events/init_done` event.
This is the event that the media controller posts when it's ready to be used,
so it's a good event for our use case.

Then under that event, create an entry to show the slide you just created in the
previous step.

5. Configure your virtual segment display "hardware"
----------------------------------------------------

At this point you have a simple display configured, and you have default content
showing up (the text "HELLO"). The final step is to add the configuration for your
virtual segment display "hardware" so that MPF can control your segment display
emulator as if it were a hardware display.

MPF contains a virtual hardware platform to allow it to run without physical hardware
connected (:doc:`/hardware/virtual/index`). This virtual platform contains code to
allow it to communicate with segment display emulator widgets as if it were a real
hardware display (in fact, you can develop your game using the virtual segment display
and easily migrate it to actual hardware later with few configuration changes).

The first step is to create a :doc:`/config/segment_displays` entry in your machine wide
config and add an entry for each segment display emulator widget (in this example we
created a single widget so we will only need one entry).

.. code-block:: mpf-config

   segment_displays:
     display1:
       number: 1

A couple of things to note in the above configuration. ``display1`` is the name we are
assigning to the segment display. This parameter value must match the one we assigned
to the``name`` parameter of the segment_display_emulator widget when it was created on
the slide previously (we used a value of ``display1``). Be sure these values match or
the communications between MPF and MPF-MC will not update the segment display widget
properly.

Repeat this process for each segment display emulator widget you configure.

Now we need to let MPF know to send changes to the segment displays to the virtual
segment display emulator in MPF-MC. This is accomplished using the
:doc:`/config/virtual_segment_display_connector` plugin.

.. code-block:: mpf-config

   virtual_segment_display_connector:
       segment_displays: display1

The ``segment_displays`` parameter contains a list of all the segment display names
you want to use in the connector to communicate with the segment display emulator
widgets in MPF-MC.

6. Update your virtual segment display using the segment_display_player
-----------------------------------------------------------------------

Now that the virtual segment display is configured in the hardware section, it is time
to configure the mechanism to update the text in the display. To do this, we use the
:doc:`/config_players/segment_display_player` (see also :doc:`/config/segment_display_player`).

.. code-block:: mpf-config

   segment_display_player:
     update_segment_display_hello:
       display1:
         text: "HELLO"
     update_segment_display_red:
       display1:
         action: set_color
         color: "FF0000"
     update_segment_display_score:
       display1:
         text: "{players[0].score:d}"

The segment display player establishes segment display updates that are triggered by events.
In the above example, the ``update_segment_display_hello`` event sets the segment display
text for display1 to ``HELLO``. The ``update_segment_display_red`` event sets the segment
display color to red for display1. Finally, the ``update_segment_display_score`` event sets
the text to the score for player 1 (this will update automatically as the score changes using
:doc:`/config/instructions/text_templates`).

Your virtual segment display should now be fully functional and ready for you to customize
further for your specific project.
