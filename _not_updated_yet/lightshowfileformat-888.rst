
MPF light shows are created with`yaml files`_ which contain
instructions for what what different lights or LEDsshould do at
different times. (Note that light shows today only support matrix
lights and LEDs. In the future we'll add support for flashers and GI
strings.) You can also add event postings and coil firing to light
shows.



Details of the light show YAMLfile
----------------------------------

A light show file is a sequential listing of what things you want to
do at various time points. Each instruction in a show file plays for a
number of "tocks." So roughly speaking, your show file says, "Make
this light red for 2 tocks, then off for 3 tocks, then green for 8
tocks, then post event *foo*, then make this light blue, then fire
this coil then play this sound . . ." The term "tocks" was used
because we didn't want to use "ticks" because in MPF, the term "ticks"
is used to represent each "tick" of the machine loop. So we choose
"tocks" instead. We also chose "tocks" instead of "seconds" or
"milliseconds" because when you create a show.yaml file, the show file
has no sense of real world time. (So your show files don't say, "do
this for 100ms, then do this for 100ms," rather, they say "do this for
1 tock, then do this for 1 tock, then do this for 3 tocks, etc.") It's
not until you play your show that you specify your "playback" speed in
terms of "tocks per second." This gives you the flexibility to play
back a show at any speed and to change the speed of playback while a
show is playing. (And if you want to use tocks as ms, that's fine—just
always play back your shows at 1000 tocks per second and you're all
set.) The key is thatwhen you're creating a show, what's important is
that the ratio of tocks between your steps is what you want them to
be. Let's look at a simple show yaml file. This file "sweeps" left-to-
right-to-left between several RGB LEDson the playfield, turning each
one on red (ff0000), then off.


::

    
    - tocks: 1
      leds:
        left_lane: ff0000
        center_lane: 000000
    - tocks: 1
      leds:
        center_lane: ff0000
        left_lane: 000000
    - tocks: 1
      leds:
        right_lane: ff0000
        center_lane: 000000
    - tocks: 1
      leds:
        center_lane: ff0000
        right_lane: 000000


The line that begins with `- tocks:` is the beginning of each step in
the show. The showcontroller stays on that step for the number of
tocks specified (1, in this example), before moving to the next step.
Again, how long a tock is doesn't matter here (because you specify how
many tocks per second you want at runtime when you play the show). In
this case becauseeach step if the same duration as all the other
steps, each step will always play for the same amount of time. Another
important thing to note is that each step represents the instructions
that are actually sent to the hardware during that step. So in this
above example, if we only want one light on at a time, that's we're
using "000000" to turn "off" the light that was turned on red in the
prior step. If we didn't have all those "000000" entries then all the
lights would end up staying on. Also note in the above example that we
disable the center_lane light in the first step. We do that so that
this show is "loopable", since we want the center_lane to be turned
off in the first step but it's enabledred in the final step.



A note about YAML formatting
----------------------------

MPF's show files are in the YAML file format. Since this is the same
file format that's used for your machine config files, you're probably
at least somewhat aware of it. You're also probably aware that YAML
files can sometimes be finicky in terms of syntax, so make sure that
you keep in mind the following:


+ All indents *must* be done with spaces. No tabs.
+ The start of each step is `- tocks:`. The dash must be left-
  justified with no spaces in front of it, then you need a space before
  the word "tocks". So it's <dash><space><t><o><c><k><s><colon>.
+ The next line down ( `leds:`) in our example must have its first
  letterlined up with the first letter in the row above it. So you have
  to have two spaces, then the word "leds:".


If you run into any YAML formatting issues, you can always copy and
paste the shows from the Judge Dredd sample game as a starting point.



Controlling different types of items in your show
-------------------------------------------------

MPF show files can currently control fourdifferent types of things at
each step, including:


+ Matrix lights
+ RGB LEDs
+ Flashers
+ GI strings
+ Coils
+ Events


Let's look at each of these types of items one-by-one:



Matrix Lights
~~~~~~~~~~~~~

You control matrix lights via a `lights:` entry in your show file.
Under that you specify each light name as well as a 2-btye hex
representation of its value.


::

    
    - tocks: 1
      lights:
        l_pick_a_prize: ff
        l_extra_ball: ff
        l_right_start_feature: ff
    - tocks: 1
      lights:
        l_pick_a_prize: 0
        l_extra_ball: 0
        l_right_start_feature: 0


At this point the MPF does not support variable brightness for matrix
lights, so the only meaningful values here are `0` for off, and
anything non-zero for on. You can also control matrix lights based on
their "tag". Adding a tag (along with the tag name) to a step in the
show will apply the setting from that step to all the matrix lights
with that tag. You specify tags by adding an entry "tag|<tag_name:
into the step of the light show. (That's the text "tag", followed by
the vertical bar character, followed by the tag name, with no spaces.)
For example:


::

    
    - tocks: 1
      lights:
        tag|some_tag: 0


When you enter a tag name into a light show, MPF internally expands it
to all the lights that have that tag. So if you have previously turned
on a light by name in a step, and then you later use a tag to turn off
lights, then if that light has that tag it will also turn off even
though it was turned on individually.



RGB LEDs
~~~~~~~~

MPF lets you control RGB LEDs via the PD-LED board for P-ROC or the
built-in RGB LED channels on the FAST controller board. (We'll add
support for Fade Candy controllers too, but we haven't gotten to that
yet. To add RGB LEDs to a show, add a `leds:` entry to each step of
your show and specify your LEDs like this:


::

    
    - tocks: 1
      leds:
        beacon: ff0000-f1 # hex color with fade extension
    - tocks: 1
      leds:
        beacon: ffcc00 # hex color with no fade
    - tocks: 1
      leds:  
        beacon: 0, 255, 0, 2 # integer colors with fade
    - tocks: 1
      leds:
        beacon: 0, 255, 255  # integer colors with no fade


If you just specify a color, the show controller will change that LED
to that color instantly. You can also specify that the LED should fade
from its current color to the new color over some period of time by
adding a fade time to each entry. (This fade time is in tocks, with
the fade beginning where it's entered in your show file and ending
after the number of tocks has expired. Note that LEDs will always
respect their own default fade rates and your global fade rate, so if
you want to force an LED switch to that color instantly and ignore its
default fade, specify a fade time of 0. Finally, note from the example
above that there are two alternate notations you can use to specify
LED color and fade values. One is a hex string (with optional -f
extension for fades), and the other is a list of integers (three items
if you're just specifying the color in red, green, and blue, and four
items if you want to specify a fade). It doesn't matter which notation
you use, so go with whatever you're comfortable with. You can also set
colors of and fades of LEDs via tags. (See the note on using tags in
the Matrix Lights section above.) For example:


::

    
    - tocks: 1
      leds:
        tag|upper_playfield: 0




Flashers
~~~~~~~~

You can add flashers to your light show by adding a `flashers:`
section and then the name of each flasher. Flashers don't have any
additional options since you can't specify their color or duration of
flash:


::

    
    - tocks: 1 
      flashers:
        flasher1
        flasher2




GI Strings
~~~~~~~~~~

You can control GI strings in your light shows by adding a gis:
section to your show and then adding the name of each GI string as
well as an intensity value from 0-255. For GI strings that are not
dimmable, just use `ff` for on and `00` for off. For example:


::

    
    - tocks: 1
      gis:
        gi_back_panel: ff
        gi_upper_right: ff
        gi_upper_left: ff
        gi_lower_right: ff
        gi_lower_left: ff




Coils
~~~~~

You can include coil pulses in your shows which means the show
controller will pulse a the coil at that step of the show. Coils are
specified like this:


::

    
    - tocks: 1
      coils:
        c_knocker: pulse


Coil options are pretty simple. You add a `coils:` section to the step
in your show file, then add one or more coils under it in the format
`coil_name: pulse`. At this time MPF only supports pulsing coils, but
we will add the other methods (enable, disable, pwm, etc.) soon.



Events
~~~~~~

You can add events to your shows which cause the MPF to post events at
the show step where they're included. For example:


::

    
    - tocks: 1
      events:
        hello_world
        goodbye_guys


In this case, MPF will post two events, one called "hello_world" and
one called "goodbye_guys" at this step in the show.



Putting it all together
~~~~~~~~~~~~~~~~~~~~~~~

Remember that you can combine matrix lights, LEDs, flasher, GIs,
coils, and events into single shows (and even single steps within a
show):


::

    
    - tocks: 2
      leds:
        l_led0: ff0000
      lights:
        l_pick_a_prize: ff
        l_extra_ball: ff
        l_right_start_feature: ff
      flashers:
        upper_right
        upper_left
      gis:
        main_left: ff
    - tocks: 1
      leds:
        led0:00ff00
      lights:
        l_pick_a_prize: 00
      events:
        hello_event
      coils:
        c_left_slingshot: pulse


.. _yaml files: http://www.yaml.org/spec/1.2/spec.html


