
You can use the `light_player:` section of your config files play
light shows and scripts based when certain MPF events happen. If you
add this section to yourmachine-wide config file, the entries herewill
always be active. If you enter it into a mode-specific config file,
entrieswill only be active while that mode is active. This sectioncan
be used in your machine-wide config files. This sectioncanbe used in
mode-specific config files. Here's an example:


::

    
    light_player:
        ball_save_active:
            lights: shoot_again
            script: flash
            tocks_per_sec: 4
            repeat: yes
        tilt_warning:
            led_tags: playfield
            script: flash_red
            key: tilt_warning
            tocks_per_sec: 10
        tilt_warning_expired:
            key: tilt_warning
            action: stop
        shot_ramp_made:
            show: left_side_big_flash
            tocks_per_sec: 10
            repeat: no


The Light Player setting above will apply a Light Script called
*flash* to the light *shoot_again*when the *ball_save_active*event is
posted. It will play that script at 4 tocks per second, and it will
repeat forever until it's stopped. It will also play the script
*flash_red*on all the LEDs tagged with *playfield*when the
*tilt_warning*event is posted. That script runs at 10 tocks per second
and willnot repeat. Finally, it will play a light show called
*left_side_big_flash* when the *shot_ramp_made* event is posted. That
show will also play at 10 tocks per second and will not repeat.
Specific settings for the `light_player:`are:



<event_name>:
~~~~~~~~~~~~~

The top-level entries under `light_player:` are the names of the
events that will activate the settings underneath them.



show:
~~~~~

The name of a light show that will be played when the *<event_name>*
is posted. Light shows contain lists of all the individual lights or
LEDs for each step. So if you enter a show here, then you do not need
to specify `lights`, `leds`, `light_tags`, or `led_tags`.



lights:
~~~~~~~

A list of one or more matrix lights (entered in MPF's `config list
format`_) that a lightscript will apply to.



leds:
~~~~~

A list of one or more LEDs (entered in MPF's `config list format`_)
that a lightscript will apply to.



light_tags:
~~~~~~~~~~~

A list of one or more tags for lights this light script will apply to.



led_tags:
~~~~~~~~~

A list of one or more tags for LEDsthis light script will apply to.



script:
~~~~~~~

The name of the script that will be applied to the lights, leds,
light_tags, and/or led_tags in this section. You define your scripts
in the ` `light_scripts:``_ section of your config file.



tocks_per_sec:
~~~~~~~~~~~~~~

How many tocks per second this light script or showshould play at.



repeat:
~~~~~~~

Whether this script or show should repeat.



action:
~~~~~~~

Specifies whether this option starts the show / script or stops it.
Options include:


+ `start` - starts the show or script. (This is the default implied
  value, so if you don't include an action: setting then `action: start`
  is implied.
+ `stop` - stops the show or script. In order to stop a show, you also
  need to include a `show:` entry with the name of the show you're
  stopping. In order to stop a script, you also need to include a `key:`
  entry with the name of the key you specified when you started the
  script.


Note that when you stop a show or script, you can optionally include
`reset: yes` and/or `hold: yes` as settings for that entry to reset
the show or script to the beginning and to hold the lights or LEDs in
their final states. If you don't specify these entries, the defaults
are `reset: yes` and `hold: no`.



key:
~~~~

You can enter an arbitrary text string as a "key" when you start
playing a script which you can then later use to stop that script.
This entry from the example above includes a key:


::

    
        tilt_warning:
            led_tags: playfield
            script: flash_red
            key: tilt_warning
            tocks_per_sec: 10


Why do you need a key? Unlike light shows, light scripts aren't
created for specific lights or LEDs—instead you specify them when you
play them. You might have a simple script called "flash" that you use
to cause a light to flash. When it comes time to stop that script, how
do you identify which light you want to stop it on? You might have 20
different lights flashing but you only want to stop one. This is where
the "key" comes in. When you play a script on a certain light, led,
list of lights/leds, or tags of lights/leds, you can optionally
specify a "key" that you can use to later stop that script on those
lights or LEDs. The key can be anything you want. In the example
above, we play our script called "flash_red" onall the LEDs tagged
with "playfield", and we give that a key called "tilt_warning". Then
we later stop that flashing when the event *tilt_warning_expired* is
posted:


::

    
        tilt_warning_expired:
            key: tilt_warning
            action: stop


We could have also just configured this script to play a few times and
stop on its own, like this:


::

    
        tilt_warning:
            led_tags: playfield
            script: flash_red
            tocks_per_sec: 10
            repeat: yes
            num_repeats: 3


In this case we used the `key:` just to show an example of how it
works.



Other show settings:
~~~~~~~~~~~~~~~~~~~~

When you're setting up a light show to play, you can enter any
settings for shows you want, including `repeat`, `priority`, `blend`,
`hold`, `tocks_per_sec`, `start_location`, and `num_repeats`. See the
documentation on `playing shows`_ for details.

.. _light_scripts:: https://missionpinball.com/docs/configuration-file-reference/lightscripts/
.. _config list format: https://missionpinball.com/docs/configuration-file-reference/adding-lists-and-lists-of-lists-to-config-files/
.. _playing shows: https://missionpinball.com/docs/game-programming/lighting/playing-shows/


