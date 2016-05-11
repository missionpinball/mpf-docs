What can you put in shows?
==========================

In the :doc:`<show_format>`_ page, we showed how *time* values work in shows and included some simple examples using
*LEDs*. However in MPF, you can put almost anything in shows, including:

* LEDs
* Lights
* Coil & drivers
* Sounds
* Slides (for the display)
* Shows (one show can spawn other shows and/or act like a playlist)
* Events
* Random events (randomly post an event from a list of events)
* Flashers
* GI (general illumination)
* BCP commands & triggers
* Widgets (to be added or removed from slides)

The full gamut of options for each of these things is available to you in a show step.

For example, you can configure LEDs to change color, set their fade, turn off, etc.
You can show slides on your display or DMD, or remove existing slides. You can post events
that trigger other shows or other things to happen. You can start and stop sounds and music.
The list goes on and on...

Technically-speaking, the list above is actually a list of things that MPF calls `config players </config_players/index>`_.

*Config players* in MPF have nothing to with the actual human players of your machine, rather, they are things that
"play" configurations.

Config players are used in the ``*_player:`` section of your config files *and* as steps in shows. For example, the
*LED player* is used to "play" a config to LEDs, and it's available to you outside of shows in the ``led_player:``
section of your config file as well as in the ``leds:`` section of a show.

That naming convention is the same for all the config players. You play sounds via the ``sound_player:`` section of a
config file or the ``sounds:`` section of a show. Slides are played via the ``slide_player:`` section of a config file
or the ``slides:`` section of a show, etc.

All of the individual config players are documented in the `config players </config_players/index>`_ section of the
documentation. You can read details about each config player there, as well as specific instructions for how to include
that kind of player in a show.