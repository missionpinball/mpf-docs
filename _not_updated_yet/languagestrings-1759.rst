
The `language_strings:` section of your config file has a list of text
strings that will be replaced for a certain language. This sectioncan
be used in your machine-wide config files. This section *cannot* be
used in mode-specific config files.


::

    
    language_strings:
        french:
            press start: APPUYEZ SUR START
            free play: JEU GRATUIT
            player: JOUEUR
            ball: BALLE
        german:
            press start: START DRÜKEN
            free play: FREISPIEL
            player: SPIELER
            ball: BALL


The layout of this section of your config file should be pretty
obvious. By the way we don't speak French *or* German, sowe used
Google Translate for these just to make examples. They're more to
prove the point. :) Note that in order to support the U with the
umlaut in"DRÜKEN"then you need to save the config file as UTF-8. Also
you need to make sure that your font has a glyph for those characters.
(The current default font we use with MPF does not. It's on our to-do
list though.)



