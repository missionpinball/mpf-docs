Tutorial step 18: Create an attract mode light show
===================================================

Once you add your lights or LEDs, you need a simple way to test them
to make sure they're working. We typically throw together a quick
attract mode light show so we can see some blinking lights as soon as
MPF boots up.

1. Create another show YAML file
--------------------------------

The easiest way to create a complex series of light actions is with
MPF's *show* functionality. This is the exact same type of show that
we use for the DMD loop, except this time we configure lights or LEDs
for each step instead of display elements. Show entries for lights and
LEDs are very similar, except with LEDs you specify full RGB values
whereas with lights you just specify whether they're on or off. So the
first thing to do is to create another show file in your attract mode
shows folders. Let's call this one ``attract_light_show.yaml``. Your
machine folder should now look like this:

2. Add some entries to your light show
--------------------------------------

There are all sorts of things you can do with a light show file that
you'll become familiar with as you get deeper into your game
configuration. For now we're just going to create a simple show that
cycles through three lights. We'll call them *light1*, *light2*, and
*light3*, though there's a good chance that you don't have lights with
those names in your machine so you'll have to change them to names
that actually exist for you. If you have Matrix Lights, add entries to
your ``attract_light_show.yaml`` file so that it looks something like
like this:

::

    #show_version=4
    - duration: 1
      lights:
        l_light2: 0
        l_light1: ff
    - duration: 1
      lights:
        l_light1: 0
        l_light2: ff
    - duration: 1
      lights:
        l_light2: 0
        l_light3: ff
    - duration: 1
      lights:
        l_light3: 0
        l_light2: ff

Matrix lights don't have color setting since their color is determined
by the color of the bulb and/or the color of the insert. So the ``0``
and ``ff`` values here just represent "off" (0) and "on" (255). If you
look at the four steps in this show, you'll see the first step turns
off *l_light2* and turns on *l_light1*, the next one turns *l_light2*
and turns off *l_light1*, etc. In other words, if this show runs in a
loop you'll get a never ending 1-2-3-2-1-2-3-2-1-2-3-2... pattern. If
you have RGB LEDs, then you can have some more fun and actually specify
different colors for each light at each step. For example, if you just
wanted to have a show that cycled three RGB LEDs through the colors of
the rainbow, you could create a show like this:

::

    #show_version=4
    - duration: 1
      leds:
        l_led1: red
        l_led2: red
        l_led3: ff0000
    - duration: 1
      leds:
        l_led1: ff6600
        l_led2: ff6600
        l_led3: ff6600
    - duration: 1
      leds:
        l_led1: ffcc00
        l_led2: ffcc00
        l_led3: ffcc00
    - duration: 1
      leds:
        l_led1: lime
        l_led2: 00ff00
        l_led3: 00ff00
    - duration: 1
      leds:
        l_led1: blue
        l_led2: 0000ff
        l_led3: 0000ff
    - duration: 1
      leds:
        l_led1: ff00aa
        l_led2: ff00aa
        l_led3: ff00aa

Obviously this is just the very beginning of what you can do. You can
create shows that are hundreds of steps involving dozens of lights.
(Notice that if you don't specify a change for a particular light for
a step then that light just stays at whatever it was before. In other
words, you only have to enter the new values for the lights that
change each step-—you don't have to enter all the lights from scratch
every step.)

3. Configure your show to play
------------------------------

This new show file is just like your existing display show, except this
one contains settings for lights or LEDs. So to get it to play, add it to
the ``show_player:`` section of your attract mode config file.

To do this, move the existing display show to the next line (and indented
under the event which triggers it). Then add a colon to the end of it, and add
the new show below it.

OLD:

::

   #config_version=4
   show_player:
     mode_attract_started: attract_display_loop

NEW:

::

   #config_version=4
   show_player:
     mode_attract_started:
       attract_display_loop:
       attract_light_show:

Save your machine config
file, save your light show file, and run your game. You should see
your light show start to play once the attract mode starts up.

4. Configure more light shows to all run at once
------------------------------------------------

Your simple little light show with two or three lights is a good first
step, but it's hardly what could be considered a "real" attract mode
light show. Unfortunately if you look at a real pinball machine, you
might be overwhelmed by all the crazy light action. But if you really
look closely, you'll realize that the super-complex looking light
shows on real pinball machines are just lots of little shows all
running at the same time. For example, look at how we can break down
the attract mode light show of *Demolition Man*:
https://www.youtube.com/watch?v=_h_rhHExmX4 So if we were creating the
attract mode light show like this for MPF, we would actually create
lots of little shows each with just a few lights in them. Then we'd
end up with a list of show files, like this:

+ flipper_red_flashing.yaml
+ purple_mode_sweep.yaml
+ inlane_alternating.yaml
+ random_flashing.yaml
+ car_chase_sweep.yaml
+ ramp_orbit_sweep.yaml
+ right_orbit_sweep.yaml
+ claw_sweep.yaml
+ mtl_sweep.yaml
+ center_ramp_sweep.yaml
+ standups_sweep.yaml

We'd probably make every step of every show have a duration of 1. Then in our
``show_player:`` configuration, we'd configure the list of shows to
play when the attract mode starts instead of just one. For example:

::

    show_player:
        mode_attract_started:
          flipper_red_flashing:
            speed: 2
          purple_mode_sweep:
            speed: 4
          inlane_alternating:
            speed: 3
          random_flashing:
            speed: 2
          car_chase_sweep:
            speed: 3
          ramp_orbit_sweep:
            speed: 5
    ...(truncated. you get the idea)
