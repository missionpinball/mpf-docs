
The `scriptlets:` section of your machine configuration files is where
you specify the various scriptletsyou've installed into your game.
(What's a scriptlet? `Read here to find out.`_) This sectioncan be
used in your machine-wide config files. This sectioncan be used in
your mode-specific config files.


::

    
    scriptlets:
        attract.Attract
        bonus.Bonus
        modes.Multiball
        modes.InstantDeath


You can add as many scriptletas you want, with one per line. MPF will
look for scriptletin the `/scriptlets` folder in your machine files
location. The part of the name before the dot is the module name (i.e.
the file name), and the part after the dot is the class name in the
scriptletfile. (Note you can have more than one scriptletin the same
file, with each one being its own class. Just add them to the list
multiple times, one for each class.) For example, the first entry of
`attract.Attract` will load the `Attract()` class from the
`/scriptlets/attract.py` file.

.. _Read here to find out.: /docs/programming-guide/scriptlets/


