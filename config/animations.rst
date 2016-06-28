animations:
===========

*Config file section*

.. include:: _machine_config_yes.rst
.. include:: _mode_config_yes.rst

.. overview

The ``animations:`` section of your config is where you list the reusable "named" animations.

Note that while you can add animations in both the machine-wide and a mode-specific
config, the list of animations is global, meaning that any animation is available in any
mode, and you can't have two different animations with the same name.

For example:

::

   animations:
     fade_in:
       property: opacity
       value: 1
       duration: 1s
     fade_out:
       property: opacity
       value: 0
       duration: 1s

The above example defines animations named ``fade_in`` and ``fade_out`` that you can use, by name, in any widget or
widget_player config where you would ordinarily define your own animations.

See the :doc:`/howto/display/animate_widgets` for more details.
