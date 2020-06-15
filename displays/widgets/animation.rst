How to animate display widgets
==============================

One of the features of MPF is that you can animate display widgets. Animating a widget means that you can change a
widget's properties over time. You can pretty much change any numeric property, including size, position, opacity, etc.

When animating widgets, you specify multiple properties to change at the same time, or a sequence of changes one after
the other (or both). You can also specify the duration of each step, the "easing" formula that affects the curve
(acceleration/deceleration) of the change, and whether the animation is a one-time thing or a repeating loop.

You can also configure animations to start playing as soon as the widget is created, or tie steps (or series of steps)
to MPF events, meaning a widget might be static, then the event "move_widget" is posted and it moves, then the event
"remove_widget" is posted and it's animated away.

This How To guide will show you how to do all of that.

1. Understanding animations in MPF
----------------------------------

MPF animations are properties of widgets. For example, here's a basic widget with no animations:

.. code-block:: mpf-mc-config

   slides:
     slide_1:
       widgets:
         - type: text
           text: MY TEXT
           color: red

To add animations to a widget, you simply add an ``animations:`` setting to that widget, and then under there you add
specific animation steps and settings. For example:

.. code-block:: mpf-mc-config

   slides:
     slide_1:
       widgets:
         - type: text
           text: MY TEXT
           color: red
           animations:
             show_slide:                   # animation trigger event
               - property: opacity         # name of the widget property we're animating
                 value: 1                  # target value of that property for this step
                 duration: .5s             # duration for this step (how long it takes to get there)
               - property: opacity         # second step in the animation (starts with a hyphen)
                 value: 0
                 duration: .5s
                 repeat: true              # added to the final step, tells this animation to repeat (loop)

In the example above, an ``animations:`` setting has been added to the widget. Then under there, you add
the name of the event you want to use to trigger this animation to start.
In this case, we use a special event called ``show_slide:`` which means these
animations are triggered when the slide is shown on a display.

Next, notice that under the event, there are two steps (each beginning with a hyphen and a space).

There are several settings you can specify in each step. (See the config file reference for animations for
details)

In this example, there are three settings for the first step:

::

                  - property: opacity
                    value: 1
                    duration: .5s

The **property** setting is the name of the widget's property that you want to animate. This can be almost any
numerical property of the widget, including ``x:``, ``y:``, ``opacity``, etc. (Different widget types have
different types of animatable properties. For example, on text widgets you can animate the ``font_size:``, on
various shape widgets you can animate the ``height:``, ``width:`` and ``rotation:``, etc.)

2. Relative animation values
----------------------------

Sometimes it is desirable to animate a value a relative amount from a widget's current value rather than specifying
an absolute target value.  This can be done using ``relative: True``.  With the ``relative:`` parameter set to
``True``, the new target value will set by adding the ``value:`` parameter to the widget's current ``property:``
value when the animation starts.  When ``relative:`` is set to ``False``, the animation target uses the actual
``value:`` property value as its destination.

The following example animates a widget 50 pixels in the ``x`` direction over one second from its current location,
 then -50 pixels in the ``y`` direction over another second followed by a 45 degree rotation over 500 ms:

::

                  - property: x
                    value: 50
                    relative: True
                    duration: 1s
                  - property: y
                    value: -50
                    relative: True
                    duration: 1s
                  - property: rotation
                    value: 45
                    relative: True
                    duration: 500ms

3. Animation trigger events
---------------------------

The animation trigger event (which is the ``show_slide:`` entry in the example
from the previous step is the name of the MPF event you want to use to start
the animation.

These are regular :doc:`MPF events </events/index>` and can be anything—a shot
being made, a switch hit, etc. (See the :doc:`event reference </events/index>`
for a full list of events.)

In most cases, however, you'll probably want to trigger an animation to start
playing when the slide is created, so in addition to being able to use any MPF
event, there are also a few special events (sometimes called "magic events")
that have special meaning here:

add_to_slide:
~~~~~~~~~~~~~
This event is triggered when a widget is added to a slide. This is useful when
you're using the :doc:`widget_player </config_players/widget_player>` to add
to new widget to an existing slide, and you want an animation to be applied to
that widget as soon as it's added.

remove_from_slide:
~~~~~~~~~~~~~~~~~~
This event is triggered when a widget is is removed from a slide.

pre_show_slide:
~~~~~~~~~~~~~~~
This event is triggered when the slide this widget is part of is about
to be shown. This doesn't necessarily get called when the slide is created or
when the ``slide_player:`` event happens, because if the slide is not the
highest priority slide, then the slide will be created but not shown. So this
event happens right before the slide is shown.

If there's an entrance transition, this method is called BEFORE the transition
starts. In other words, it means the animation will be playing as the slide
transition is happening.

show_slide:
~~~~~~~~~~~
This event is triggered when the slide this widget is part of has been shown and
is the current slide on the display.
This doesn't necessarily get called when the slide is created or
when the ``slide_player:`` event happens, because if the slide is not the
highest priority slide, then the slide will be created but not shown. So this
event happens right before the slide is shown.

If there's an entrance transition, this method is called AFTER the transition
starts. In other words, it means the animation will NOT be playing as the slide
transition is happening.

pre_slide_leave:
~~~~~~~~~~~~~~~~
This event is triggered by the current slide that's being shown on a display is
about to be replaced by another slide.

If there's an exit transition, this method is called BEFORE the transition
starts. In other words, it means the animation will be playing as the slide
transition is happening.

slide_leave:
~~~~~~~~~~~~
This event is triggered by the current slide that's being shown on a display is
has been replaced by another slide.

If there's an exit transition, this method is called AFTER the transition
starts. In other words, it means the animation will be NOT playing as the slide
transition is happening.

You might wonder what this is for, since what's the point of an animation if
the slide is not showing? This is useful if you want to pause or reset an
animation when the slide is not active. Then you can resume or restart the
animation with the "pre_show_slide" or "show_slide" event when the slide is
shown again.

slide_play:
~~~~~~~~~~~
This event is triggered when the slide this widget is part of is played
as part of a ``slide_player:`` "play" command, either via a standalone slide
player config or as a show step).

Other slide-related MPF events
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In addition to the seven special-purpose animation trigger events listed above,
there are three standard MPF events which are posted when slides are created,
when they become active, and when they're removed. See the events reference
for details on when these three events are posted.

* :doc:`slide_(slide_name)_created </events/slide_slide_created>`
* :doc:`slide_(slide_name)_active </events/slide_slide_active>`
* :doc:`slide_(slide_name)_removed </events/slide_slide_removed>`

4. Animating multiple properties at once
----------------------------------------

The example animation above includes two steps (one to set the opacity to 1 and the next to set it to 0).
By default steps are sequential, meaning that one step completes before the next one starts. However you can
add a ``timing: with_previous`` to an animation step which will make it so that step runs at the same time
as the step before it. This means you can animate multiple properties at once.

For example, to make the text grow and shrink while also fading on and off:

.. code-block:: mpf-mc-config

   slides:
     slide_1:
       widgets:
         - type: text
           text: MY TEXT
           color: red
           font_size: 50
           animations:
             show_slide:
               - property: opacity
                 value: 1
                 duration: .5s
               - property: font_size
                 value: 100
                 timing: with_previous         # makes this step run at the same time as the previous one
                 duration: .5s                 # specify a duration for each step, even when with_previous
               - property: opacity
                 value: 0
                 duration: .5s
                 repeat: true
               - property: font_size
                 value: 50
                 duration: .5s

Notice that the animation in the example above has 4 steps, but steps #2 and #4 have the setting ``timing: with_previous``.
You can chain together as many ``with_previous`` steps as you want. (The default setting for one step to run after the
previous one is ``timing: after_previous``, but since that's the default you don't need to explicitly add it.

Also note that all 4 steps above specify ``duration: .5s``. However you can make each step a different amount of time.
In fact you can even make multiple ``with_previous`` steps different durations (though the animation won't move on to
the next ``after_previous`` step until all the simultaneous steps are complete).

By the way, the example above is a widget that's part of a slide, but remember you can add animations to widgets
anywhere a widget is defined (in the slide properties, in a show step, as part of a
:doc:`named widget <reusable_widgets>`, as part of a ``widget_settings:`` override section in the ``widget_player:``,
etc.)

It is also possible to animate multiple properties in a single animation step by using a list in both the ``property:``
and ``value:`` parameters (there must be the same number of items in both lists).  The following example moves a widget
diagonally to the coordinate (10, 20) while rotating it 180 degrees over 5 seconds:

::

                  - property: x, y, rotation
                    value: 10, 20, 180
                    duration: 5s

5. Multi-step animations with different trigger events
------------------------------------------------------

So far all of the animation examples have been triggered on the ``show_slide``
event (which means they start animating as soon as the slide is shown).

You can create multiple event entries in the animation that cause different
animations to take place when different events occur. You can mix and match
these as much as you want, including mixing the "special" animation
trigger events with regular MPF events.

.. code-block:: mpf-mc-config

   slides:
     slide1:
       widgets:
         - type: text
           text: I'M GOING TO MOVE
           x: 50
           y: 50
       animations:
         move_up:
           property: y          # if there's just one animation step, we don't need the hyphen
           value: 100
         move_down:
           property: y
           value: 0
         move_right:
           property: x
           value: 100
         move_left:
           property: x
           value: 0
         move_home:
           - property: x
             value: 50
           - property: y
             value: 50
             timing: with_previous

In the above example, we have five different animation events configured. These are just regular MPF events which you
can use from logic blocks, shots, switch events, etc. When the event ``move_up`` is posted, this widget will move to the
top of the display (``x: 100``), when the ``move_left`` event is posted, it will move to the left of the screen, etc.

If ``move_home`` is posted, there are two steps in the animation which both run together to move the widget back to its
initial position.

Again, you can use any combination of properties and any number of steps for each event.

You can also use a property from your event.
For instance, you can move a widget based on a player variable:

.. code-block:: mpf-mc-config

   slides:
     slide1:
       widgets:
         - type: text
           text: I'M GOING TO MOVE
           x: 50
           y: 50
       animations:
         player_loops:           # this is posted when the player variable "loops" changes
           property: y
           value: (value)        # this is the value of loops

6. Looping and repeating animations
-----------------------------------

So far, every animation sequence we've looked at will just run through once and then stop. However, you can add
``repeat: true`` (or ``repeat: yes``) to the last step of an animation, and that
will cause that animation to loop back to the beginning and keep repeating.

Of course you can mix-and-match repeating animations with one time animations. For example:

.. code-block:: mpf-mc-config

   slides:
     slide1:
       widgets:
         - type: text
           text: BOO!
           y: -50
           font_size: 90
           animations:
             show_slide:
               property: y
               value: 50
               duration: 500ms
             pulse_boo:
               - property: font_size
                 value: 100
                 duration: 250ms
               - property: font_size
                 value: 90
                 duration: 250ms
                 repeat: true
             bye_boo:
               - property: y
                 value: 100
               - property: x
                 value: 150
                 timing: with_previous

In the example above, when the slide is shown (or when the widget is added if this config was in your ``widgets:``
section and you added it via a ``widget_player:`` entry), the widget will fly into the slide from the bottom (since the
initial y value is -50, it will start off the screen). Then when the ``pulse_boo`` event is posted, the two-step
animation which makes the font size bigger and smaller will starting playing and repeat forever. Finally when ``bye_boo``
is posted, the widget will fly off the screen to the upper right.

There is something special to consider when working with 360 degree rotations.
Setting the property rotation to 360 results in a complete turn of a widget.
However, attempting to repeat the 360 degree rotation appears to do nothing.
This is because of how Kivi handles 0 and 360 degrees.
When the rotation completes, the widget is at rotation 360 degrees.
Repeating the step fails to cause the widget to move because it is already at destination.
To create continuously rotating widgets, a two step process is required:

.. code-block:: mpf-mc-config

   slides:
     slide1:
       widgets:
         - type: text
           text: I'M GOING TO ROTATE
           x: 50
           y: 50
           animations:
             show_slide:
               - property: rotation
                 value: 0
                 relative: false
                 duration: 0
               - property: rotation
                 value: 360
                 relative: false
                 duration: 2s
                 repeat: true

   #! slide_player:
   #!   show_slide: slide1
   ##! test
   #! post show_slide

The first step creates a reset point setting the widget at 0 degrees. This assures that there is always a destination
to rotate to which is provided by the following step.

7. Inserting a "pause"
----------------------

Sometimes you might want to add a timed "pause" to an animation, where one step animates, then it pauses, then another
step animates.

The easiest way to do that is just to add a step where the property value in the step is the same as whatever value that
property is currently at. This is easy to do using a relative property value of 0 as shown in the following example.
So you still have the step in the animation, it just isn't doing anything since the widget's property is already at
the desired target value. For example:

.. code-block:: mpf-mc-config

   slides:
     slide1:
       widgets:
         - type: image
           image: flying_toaster
           y: -50
       animations:
         show_slide:
           - property: y
             value: 50
             duration: 1s
           - property: y
             value: 0
             relative: true
             duration: 2s
           - property: y
             value: 200

The the example above, the ``flying_toaster`` image will move in from the bottom of the screen (to ``y:50``) in 1 second,
then pause for 2 seconds (since ``y: 50`` again), then move out of the top of the screen in 1 second.

8. Easing
---------

You can also set "easing" values for each animation step which controls the formula that's used to interpolate the
current value to the target value over time. The default is ``linear`` which just does a constant motion (no
acceleration/deceleration) over time. Refer to the
:doc:`/displays/widgets/easing` for details on how this works and descriptions of all the options.

9. Creating reusable "named" animations
---------------------------------------

Much like :doc:`named widgets <reusable_widgets>`, you can also create pre-defined animations that you can easily
apply to any widget. You do this by adding those animations to the ``animations:`` section of your config, like this:

.. code-block:: mpf-mc-config

   animations:
     fade_in:
       property: opacity
       value: 1
       duration: 1s
     fade_out:
       property: opacity
       value: 0
       duration: 1s

Now you can use these animations, by name, in any widget or widget_player config where you would ordinarily define your
own animations.

For example, to configure a widget to fade in (assuming the widget was
initially created with ``opacity: 0``:

.. code-block:: mpf-mc-config

   widgets:
     hello_widget:
       - type: text
         text: HELLO
         animations:
           show_slide: fade_in

Again remember this can be done anywhere you configure an animation. So if you later wanted to fade that text out
when the event "timer_hurry_up_complete" is posted, you can do it like this:

.. code-block:: mpf-mc-config

   widgets:
     hello_widget:
       - type: text
         text: HELLO
         animations:
           show_slide: fade_in
           timer_hurry_up_complete: fade_out

10. Chaining multiple named animations together
-----------------------------------------------

When working with named animations, you can chain together multiple named
animations for a single event by specifying them as a list, like this:

.. code-block:: mpf-mc-config

   widgets:
     hello_widget:
       - type: text
         text: HELLO
         animations:
           some_event: fade_in, fade_out, pulse

Any animation with ``timing: with_previous`` in the first step will run with
the previous one, meaning you can create lots of little effects and
sub-animations and then combine them in reusable ways throughout your config.

You can even use the same animation over and over in a sequence to repeat
something a certain number of times. For example:

.. code-block:: mpf-mc-config

  animations:
    pulse:
      - property: opacity
        value: 0
        duration: 100ms
      - property: opacity
        value: 1
        duration: 100ms
        timing: after_previous
  widgets:
    widget1:
      - type: text
        text: HELLO
        animations:
          flash_3x: pulse, pulse, pulse

In the example above, when the MPF event "flash_3x" is posted, it will cause
widget1 to pulse three times.

11. Animating a progress bar
----------------------------

MPF can also animate progress bars or similar things.
In this example, we animate a progress bar based on the player variable
``progress`` by hooking the width of the bar to the event ``player_progress``
which is posted when the value changes:

.. code-block:: mpf-mc-config

   slides:
     green_slide:
       widgets:
         - type: rectangle
           y: 50
           z: 20
           anchor_x: left
           anchor_y: center
           width: 0
           height: 16
           corner_radius: 3
           corner_segments: 3
           color: 00FF00
           animations:
             player_progress:
               - property: width
                 value: (value)

