MPF config files
================

MPF uses text-based config files to control the bulk of your game logic. In a
sense, your MPF "code" is actually these config files.

There are machine-wide config files which control machine-wide things (such as
hardware mappings, switches, lights, etc.) as well as mode-specific config files
that control what happens when a specific mode is running. (And you can stack
modes so you have a lot of them all doing different things at once.)

MPF also uses text-based files to control the "shows" which are the coordinated
sequences of lights, sounds, displays, etc.

The MPF config files use a file format called `YAML <http://www.yaml.org/spec/1.2/spec.html>`_
which is text-based and human readable. You can edit them in Notepad. YAML is
kind of like XML, though easier to read and write. It's kind of like INI files,
though more powerful.

We have a :doc:`detailed config file reference </config/index>`
that explains all the options for all the files, but for now we just want to
explain the basic concept of how these files work. (Feel free to browse through
the config file reference, but remember that it's a just a reference. You'll
actually learn how to use the config files via our tutorial and How To guides.
Learning MPF by reading the config file reference is like learning a foreign
language by reading a dictionary. :)

When you create your machine code in MPF, you'll actually create a folder which
will contain your config files. A super-simple snippet might look like this:

::

    game:
        balls_per_game: 3

Want a 5-ball game instead? Simple! Just change it:

::

    game:
        balls_per_game: 5

Ultimately your config files will be thousands of lines long (though you can
break them up into multiple files to help your sanity), but again, don't be
overwhelmed now. The tutorial will walk you through them step-by-step, and in
no time you'll have a playing pinball machine!
