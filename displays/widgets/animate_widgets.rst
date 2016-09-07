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

::

   slides:
      slide_1:
         widgets:
            - type: text
              text: MY TEXT
              color: red

To add animations to a widget, you simply add an ``animations:`` setting to that widget, and then under there you add
specific animation steps and settings. For example:

::

   slides:
      slide_1:
         widgets:
            - type: text
              text: MY TEXT
              color: red
              animations:
                entrance:                  # animation trigger event
                  - property: opacity      # name of the widget property we're animating
                    value: 1               # target value of that property for this step
                    duration: .5s          # duration for this step (how long it takes to get there)
                  - property: opacity      # second step in the animation (starts with a hyphen)
                    value: 0
                    duration: .5s
                    repeat: true           # added to the final step, tells this animation to repeat (loop)

In the example above, an ``animations:`` setting has been added to the widget. Then under there, you add
the name of the event you want to use to trigger this animation to start. In this case a special event
called ``entrance:`` was used, which is a fake event name that makes this animation start immediately once
the widget is created.

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
various shape widgets you can animate the ``height:`` and ``width:``, etc.

Pretty much the only thing you can't animate at this point is rotation (since MPF doesn't currently
support widget rotation. That's a future feature we'll have to add).

2. Animating multiple properties at once
----------------------------------------

The example animation above includes two steps (one to set the opacity to 1 and the next to set it to 0).
By default steps are sequential, meaning that one step completes before the next one starts. However you can
add a ``timing: with_previous`` to an animation step which will make it so that step runs at the same time
as the step before it. This means you can animate multiple properties at once.

For example, to make the text grow and shrink while also fading on and off:

::

   slides:
      slide_1:
         widgets:
            - type: text
              text: MY TEXT
              color: red
              font_size: 50
              animations:
                entrance:
                  - property: opacity
                    value: 1
                    duration: .5s
                  - property: font_size
                    value: 100
                    timing: with_previous      # makes this step run at the same time as the previous one
                    duration: .5s              # specify a duration for each step, even when with_previous
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

3. Multi-step animations with different trigger events
------------------------------------------------------

So far all of the animation examples have been triggered on the ``entrance`` event which means they start animating as
soon as the widget is added to the slide (or as soon as the slide is created if the widget is part of the slide
definition).

However the real power of animations is that you can create steps in the animation that are played based on any MPF
event. To do that, just enter multiple events in the ``animations:`` section of a widget. For example:

::

   slides:
      slide1:
         widgets:
            - type: text
              text: I'M GOING TO MOVE
              x: 50
              y: 50
         animations:
            move_up:
               property: y      # if there's just one animation step, we don't need the hyphen
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

4. Looping and repeating animations
-----------------------------------

So far, every animation sequence we've looked at will just run through once and then stop. However, you can add
``repeat: true`` to the last step of an animation, and that will cause that animation to loop back to the beginning and
keep repeating.

Of course you can mix-and-match repeating animations with one time animations. For example:

::

   slides:
      slide1:
         widgets:
          - type: text
            text: BOO!
            y: -50
            font_size: 90
          animations:
            entrance:
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

5. Inserting a "pause"
----------------------

Sometimes you might want to add a timed "pause" to an animation, where one step animates, then it pauses, then another
step animates.

The easiest way to do that is just to add a step where the property value in the step is the same as whatever value that
property is currently at. So you still have the step in the animation, it just isn't doing anything since the widget's
property is already there. For example:

::

   slides:
      slide1:
         widgets:
            - type: image
              image: flying_toaster
              y: -50
         animations:
            entrance:
             - property: y
               value: 50
               duration: 1s
             - property: y
               value: 50
               duration: 2s
             - property: y
               value: 200

The the example above, the ``flying_toaster`` image will move in from the bottom of the screen (to ``y:50``) in 1 second,
then pause for 2 seconds (since ``y: 50`` again), then move out of the top of the screen in 1 second.

6. Easing
---------

You can also set "easing" values for each animation step which controls the formula that's used to interpolate the
current value to the target value over time. The default is ``linear`` which just does a constant motion (no
acceleration/deceleration) over time. Refer to the :doc:`/displays/easing`
for details on how this works and descriptions of all the options.

7. Named animations
-------------------

Much like :doc:`named widgets <reusable_widgets>`, you can also create pre-defined animations that you can easily
apply to any widget. You do this by adding those animations to the ``animations:`` section of your config, like this:

::

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

For example, to configure a widget to fade in:

::

   widgets:
      hello_widget:
         - type: text
           text: HELLO
           animations:
             entrance:
               named_animation: fade_in

Again remember this can be done anywhere you configure an animation. So if you later wanted to fade that text out:
