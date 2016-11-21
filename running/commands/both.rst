mpf both (command-line utility)
===============================

Starts both the MPF game engine and the MPF Media Controller from a single command window with a single command. This
is effectively the same as running both ``mpf game`` and ``mpf mc``, but more convenient.

When you run ``mpf both``, the console log outputs from both MPF and MPF-MC will be mingled together in the console
window. However the log files in your machine's ``/logs`` folder will still be separate.

Also note that you can pass command line options to both MPF and MPF-MC after the "both" command, like this:

::

   mpf both -v

   mpf both -v -V -b

etc. See the ``game`` and ``mc`` command references for a full list of command line options.

To quit MPF and MPF-MC, either click in the graphical pop up window (so it has focus) and hit ``Esc``, or click in the
console window and press ``CTRL+C``.
