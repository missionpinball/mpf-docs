
One of the goals of the Mission Pinball Framework is that we want to
get as much machine configuration as possible into the `machine
configuration files`_. It's our intention that maybe 80-to-90% of a
machine's "code" can be built out of the box just by configuring those
files. And so far we're pretty close. In addition to controlling
switches, lights, and coils, you can also use the configuration files
to set up shots, scoring, audio, DMD animations, events, and even game
modes. And you can further extend MPF without programming with plugins
for things like ball search, ball save, valid playfield, keyboard
interface, LCD displays, coins and credits, and lots of other
things—again all without having to write a single line of Python code.
That said, we recognize that to "finish" a game, you'll have to write
some custom Python code. Our goal is that these code snippets should
be easy to write and test, and (most importantly), they should not
require you to "hack" the framework code itself. (Not that we have a
problem with hacking—we love it! The problem though is if you hack the
MPF code then it's really difficult to reintegrate your hacks with the
official builds which are released every few weeks.) The decision as
to when to use config files versus when to use custom code is not a
black-or-white decision. Really it comes down to what you want to do,
what examples are out there, and how comfortable you are with Python.
Some people who love coding in Python just use MPF config files to get
the bare bones game up and running, while other people choose do as
much as they can in config files and to keep the custom coding to a
bare minimum. Regardless of where you fall on that spectrum, we tried
to build MPF to make it as easy as possible to mix in actual Python
code. We also created a few Python classes that hide a lot of the
complexity of MPF, meaning you can get your custom code integrated
with just some basic Python knowledge. There are two easy ways to add
custom Python code to your game project:


+ Sciptlets , which are "machine-wide" chunks of code that are always
  active.
+ Mode-specific code , which allow you to write custom Python code
  which is only active when a particular game mode is active.


As for when to use scriptlets versus mode-specific code, we tend to
use scriptlets for any custom code that will be used through MPF
(either in multiple game modes or when a game is not running). For
example, we used scriptlets to hold the Python code to control the
Claw in *Demolition Man*, the cannons in *Star Trek: The Next
Generation*, and the Dead World lock and crane unloader in *Judge
Dredd*.



Documentation of the MPF API
----------------------------

MPF's API (which is how you access various aspects of MPF via Python
code) is documented via `Sphinx`_-based documentation generated from
the docstrings in the code. It's available `online`_ or via `PDF`_.
(Note the API reference is different than the documentation you're
reading now.) You can also access the generated HTML pages via the `
*gh-pages* branch`_ of the MPF repo on GitHub.

.. _ branch: https://github.com/missionpinball/mpf/tree/gh-pages
.. _PDF: http://missionpinball.github.io/mpf/pdf/Mission%20Pinball%20Framework%20API%20Documentation.pdf
.. _Sphinx: http://sphinx-doc.org/
.. _online: /apidocs
.. _machine configuration files: /docs/configuration-file-reference/


