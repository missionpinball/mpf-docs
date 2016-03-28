Shows
=====

*Shows* in MPF are timed series of actions that take place. A show typically has more than one step, and each "step"
defines actions that take place on that step. You can do almost anything in a step in a show, including setting the
color of LEDs, playing sounds, showing slides on the display, posting events, firing drivers, etc.

.. note:: Prior to MPF 0.30, "light shows" and "display shows" were two independent things. In MPF 0.30, shows are
   now universal. There's only one type of show, and it can be used to do anything.

Shows are controlled and run by the MPF core engine, and if a show contains actions in a step for the media
controller, such as display or sound actions, then those actions are sent via BCP to the media controller when that
step is played.

Shows are configured via the YAML formatting just like config files. You can add the definitions for simple shows
into your config files directly, or you can create standalone shows files that will go in your `shows` folder.

At this time, it's only possible to create and edit shows by editing the YAML files by hand. At some point we'll create
a graphical show editor, but that's probably a ways away. (Unless anyone wants to volunteer to write it?)

.. toctree::

   show_format
   show_files
   shows_in_configs
   replacement_tokens