Adding custom code to your game
===============================

While one of the goals of MPF is to allow you to do as much of your game's
configuration as possible with the config files, we recognize that many
people will want to mix in some custom code to their machines.

Fortunately that's easy to do, and you don't have to "hack" MPF or
break anything to make it happen!

The amount of custom code you use is up to you, depending on your
personal preferences, your comfort with Python, and what exactly
you want to do with your machine.

Some people will use the config files for 99% of their machine, and
only add a little custom code here and there. Others will only want
to use the configs for the "basic" stuff and then write all their
game logic in Python. Either option is fine with us! (See the
:doc:`/start/dsl_vs_programming` guide for a more detailed discussion
of this.

When you decide that you want to add some custom Python code into
your game, there are three ways you can do this:

+ :doc:`Mode-specific code <mode_code>`, which allows you to write custom
  Python code which is only active when a particular game mode is active.
+ :doc:`Sciptlets <scriptlets>`, which are "machine-wide" chunks of code that
  are always active.
+ :doc:`Placeholders </config/instructions/placeholder>` &
  :doc:`conditional events </events/overview/conditional>`.
