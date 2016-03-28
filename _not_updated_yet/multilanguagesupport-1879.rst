
MPF supports the ability to change the language of your pinball
machine. This can be used for actual languages, like changing it from
English to German, or it can be used to install "alternate" language
packs (like changing the language to "family friendly" which might
just replace a few text strings and audio callouts.The ability to
support multiple languages is built into the coreof MPF and it's
pretty easy to use.



Features of MPF's multi-language support
----------------------------------------


+ If you don't care about multiple languages, then the language
  systemstays out ofyour way. You don'thave to do anything weird or
  think about multi-language at all if you don't care.
+ If you later want to add multi-language support, it's easy, even if
  you didn't think about it when you were originally creating your game.
+ Creating the actual "translations" is alsoeasy, so you can send them
  out to non-technical translators and then plug their results right
  into your game.
+ The languagesystem can be used in novel ways for things other than
  actual languages.For example, rather than translating from one
  language to another, you canuse it to replace a few key elements to
  create a "family friendly" version of a game.
+ You canuse as much or as little of the language system as you want.
  So this means if you only want to use it for one or two things here
  and there, that's ok easy.
+ Translation settings arechangeable on the fly, so you can change the
  language of a machine from player-to-player (or even during a ball)
  without having to "reload" anything.
+ The multi-language system canbe able to control all aspects of the
  game which could contain language-specific things, including text,
  images, and animations, as well as sound and audio.
+ You can configure multiple languages in a hierarchy, so when a
  string that needs translating comes up, it can first look for it in
  Language 1, then Language 2, etc. until it finds it.




Working with text strings in multiple languages
-----------------------------------------------

You can configure text strings for alternate languages in the
`LanguageStrings:` section of your configuration file. Details on how
that works are in the `configuration file reference`_. To use the text
string language replacement system, all you have to do is wrap the
text you want replaced in parenthesis. You can do this anywhere—in
text elements that occur in show steps, in SlidePlayer elements in
your config file, etc. Basically anywhere you have a `text` setting,
instead of entering the text like this:


::

    
    text: GAME OVER


you instead enter it like this:


::

    
    text: (GAME OVER)


Doing that means that whenever that text is displayed, the language
module will look in its list of text strings for the current language
and see if it can find one for "GAME OVER". If it finds a match, it
will return the replacement text. If it doesn't find a match, it will
strip off the parenthesis and return the original text. A sample
`LanguageStrings:` section of your config file could look like this:


::

    
    LanguageStrings:
        French:
            GAME OVER: JEU TERMINÉ
        German:
            GAME OVER: SPIEL IST AUS
        Kid-friendly:
            GAME OVER: WE LOVE YOU SO MUCH!


(Note that the French translation has an accent mark, so be sure to
save your config file in UTF-8. Also be sure your font has a character
for that.)



Setting the current language
----------------------------

You configure the current language and the search order for alternate
languages in the ``Languages:` section`_ of your configuration file.
Right now that's something you have to do manually, but we'll soon
create MPF events so you can control all this from your shows and
config files.

.. _configuration file reference: https://missionpinball.com/docs/configuration-file-reference/languagestrings/
.. _`Languages:` section: https://missionpinball.com/docs/configuration-file-reference/languages/


