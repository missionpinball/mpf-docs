Specifying Colors in Config Files
=================================

Colors in config files can be specified by name (like "red") or by hex value ("ff0000").

You can see a list of valid color names (and their respective colors) `here <http://htmlcolorcodes.com/color-names/>`_.

In addition to the 140 standard named colors, MPF adds the following color options:

* ``off`` - maps (0,0,0) which is more intuitive than "black" when you're working with LEDs.
* ``on`` - turns on an LED with that LED's ``default_color:`` setting. (Default is "white" if you don't specify a color.)

If you specify a color by hex value, do *not* put a ``#`` in it, since YAML files use those for comments which
are ignored.

* CORRECT: ``color: ff0000``
* WRONG: ``color: #ff0000``
