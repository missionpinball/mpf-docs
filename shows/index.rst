Shows
=====

In MPF, *shows* are containers that hold steps of instructions for things that can be "played" in a certain order
with specific timings.

You can do almost anything in a step in a show, including setting the
color of LEDs, playing sounds, showing slides on the display, posting events, firing drivers, etc.

You're going to use shows a lot.

.. note:: Prior to MPF 0.30, "light shows" and "display shows" were two independent things. In MPF 0.30+, shows are
   now universal. There's only one type of show, and it can be used to do anything.

Shows are controlled and run by the MPF game engine, and if a show contains actions in a step for the media
controller, such as display or sound actions, then those actions are sent via BCP to the media controller when that
step is played.

Shows are configured via the YAML formatting just like config files. You can add the definitions for simple shows
into your config files directly, or you can create standalone shows files that you store in your machine's`shows` folder.

At this time, it's only possible to create and edit shows by editing the YAML files by hand. At some point we'll create
a graphical show editor, but that's probably a ways away. (Unless anyone wants to volunteer to write it?)

Read on for more info on how shows work:

.. toctree::
   :titlesonly:

   show_format
   show_content
   show_files
   shows_in_configs
   tokens