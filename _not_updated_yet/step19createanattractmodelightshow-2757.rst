
Once you add your lights or LEDs, you need a simple way to test them
to make sure they're working. We typically throw together a quick
attract mode light show so we can see some blinking lights as soon as
MPF boots up.



(A) Create a lightshow YAML file
--------------------------------

The easiest way to create a complex series of light actions is with
MPF's *show* functionality. This is the exact same type of show that
we use for the DMD loop, except this time we configure lights or LEDs
for each step instead of display elements. Show entries for lights and
LEDs are very similar, except with LEDs you specify full RGB values
whereas with lights you just specify whether they're on or off. So the
first thing to do is to create another show file in your attract mode
shows folders. Let's call this one `attract_light_show.yaml`. Your
machine folder should now look like this: ` `_



(B) Add some entries to your light show
---------------------------------------

There are all sorts of things you can do with a light show file that
you'll become familiar with as you get deeper into your game
configuration. Fornow we're just going to create a simple show that
cycles through three lights. We'll call them *light1*, *light2*, and
*light3*, though there's a good chance that you don't have lights with
those names in your machine so you'll have to change them to names
that actually exist for you. If you have Matrix Lights, add entries to
your `attract_light_show.yaml` file so that it looks something like
like this:


::

    
    - tocks: 1
      lights:
        l_light2: 0
        l_light1: ff
    - tocks: 1
      lights:
        l_light1: 0
        l_light2: ff
    - tocks: 1
      lights:
        l_light2: 0
        l_light3: ff
    - tocks: 1
      lights:
        l_light3: 0
        l_light2: ff


Matrix lightsdon't have color setting since their color is determined
by the color of the bulb and/or the color of the insert. So the `0`
and `ff` values here just represent "off" (0) and "on" (255). If you
look at the four steps in this show, you'll see the first step turns
off *l_light2* and turns on *l_light1*, the next one turns *l_light2*
and turns off *l_light1*, etc. In other words, if this show runs in a
loopyou'll get a never ending 1-2-3-2-1-2-3-2-1-2-3-2... pattern. If
you have RGB LEDs, thenyou can have some more fun and actually specify
different colors for each light at each step. For example, if you just
wanted to have a show that cycled three RGB LEDs through the colors of
the rainbow, you could create a show like this:


::

    
    - tocks: 1
      leds:
        l_led1: ff0000
        l_led2: ff0000
        l_led3: ff0000
    - tocks: 1
      leds:
        l_led1: ff6600
        l_led2: ff6600
        l_led3: ff6600
    - tocks: 1
      leds:
        l_led1: ffcc00
        l_led2: ffcc00
        l_led3: ffcc00
    - tocks: 1
      leds:
        l_led1: 00ff00
        l_led2: 00ff00
        l_led3: 00ff00
    - tocks: 1
      leds:
        l_led1: 0000ff
        l_led2: 0000ff
        l_led3: 0000ff
    - tocks: 1
      leds:
        l_led1: ff00aa
        l_led2: ff00aa
        l_led3: ff00aa


Obviously this is just the very beginning of what you can do. You can
create shows that are hundreds of steps involving dozens of lights.
(Notice that if you don't specify a change for a particular light for
a step then that light just stays at whatever it was before. In other
words, you only have to enter the new values for the lights that
change each step—you don't have to enter all the lights from scratch
every step.)



(C) Configure your light show to start by itself
------------------------------------------------

Once youcreate theshow, it just sits there, existing but not playing.
Youhave to tell it when to play and when to stop. You can do that in
the `light_player:` sectionof yourmachine config file. (Notice this is
different than the `show_player:` entry for the display show.) Create
that entry like this:


::

    
    light_player:
        mode_attract_started:
          - show: attract_light_show
            repeat: yes
            tocks_per_sec: 1


Like the DMD show, notice we also have the setting `tocks_per_sec: 1`.
Also notice the `tocks: 1` in each step of the
`attract_light_show.yaml` file. What's going on here is that MPF has
the ability to play back your light shows at any speed. (In other
words, the playback speed of a show is controlled when the show is
played, not when the show is built.) This is cool because it means you
can do things like making a show play faster and faster without having
to create a bunch of different shows for each playback speed. In this
particular case, each step of the light show is configured for 1 tock,
so each step will be equal duration. If you want your light show to
sit at one step longer than another, you could change the `tocks:`
setting for just that step. So that’s it! Save your machine config
file, save your light show file, and run your game. You should see
your light show start to play once the attract mode starts up.



(D) Configure more light shows to all run at once
-------------------------------------------------

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


We'd probably make every step of every show 1 tock. Then in our
`light_player:` configuration, we'd configure the list of shows to
play when the attract mode starts instead of just one. For example:


::

    
    light_player:
        mode_attract_started:
          - show: flipper_red_flashing
            repeat: yes
            tocks_per_sec: 2
          - show: purple_mode_sweep
            repeat: yes
            tocks_per_sec: 4
          - show: inlane_alternating
            repeat: yes
            tocks_per_sec: 3
          - show: random_flashing
            repeat: yes
            tocks_per_sec: 2
          - show: car_chase_sweep
            repeat: yes
            tocks_per_sec: 3
          - show: ramp_orbit_sweep
            repeat: yes
            tocks_per_sec: 5
    ...(truncated. you get the idea)




(E) Configure the shows to stop when the attract mode stops
-----------------------------------------------------------

At this point if you start a game, you'll see that the light shows
continue to run. That's because everything we set up in the light
player only has instructions for when the shows should start—it
doesn't say anything about them stopping. You can stop shows in a
similar way to how you start them. Create a sub-entry in your
*light_player:* section with the event name, but then instead of
settings to start shows, you add settings to stop them. So add an
entry for *mode_attract_stopped:*, and then create sub-entries for
each show. You don't need to add *repeat:* and *tocks_per_sec:*
settings since we don't care about those since we're stopping the
shows, but you do need to add *action:* stop to the light player knows
that entry is to stop them. (The default "action" is "start", which is
why you didn't have to enter an action to start your shows.) Here's an
example, again truncated:


::

    
    light_player:
        mode_attract_started:
          - show: flipper_red_flashing
            repeat: yes
            tocks_per_sec: 2
          - show: purple_mode_sweep
            repeat: yes
            tocks_per_sec: 4
        mode_attract_stopped:
          - show: flipper_red_flashing
            action: stop
          - show: purple_mode_sweep
            action: stop




