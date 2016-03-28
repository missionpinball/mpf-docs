
Contains a list of the language translations that are available for
on-the-fly replacement of text strings, sound files, and animations.
This sectioncan be used in your machine-wide config files. This
section *cannot* be used in mode-specific config files.


::

    
    languages:
        french
        english


The list of languages in this entry represents the current language
options and the order they will be searched in whenever a language
replacement search is done. Note that these names are completely
arbitrary. They only have to match with the sections you have in your
TextStrings configuration. You could call them *adult*and
*family_friendly*if you wanted to use different text strings even
though they're all in English.



