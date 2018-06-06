Text Templates
==============

Text templates can contain python format strings to show
:doc:`text placeholder <dynamic_values>`.

This is an example which will show the player 1 score of the previous game
as number:

::

   Player 1 score: {machine.player1_score:d}

Current score (during a game only):

::

   Score {current_player.score:d}

Any :doc:`variable <dynamic_values>` needs to be enclosed in ``{}``.
Either you can use ``{variable}`` or ``{variable:format_string}``.
Any `python format string https://docs.python.org/3/library/string.html#string-formatting`_
will work here.

Common format strings
---------------------

Assuming ``variable`` has a value of 1337.

Alignment and Padding
~~~~~~~~~~~~~~~~~~~~~

Left aligned and padded to 10 characters:

::

   {variable:10}

Output:

::

   "1337      "


Right aligned and padded to 10 characters with zeros:

::

   {variable:0>10}

Output:

::

   "0000001337"

Centered and padded to 10 characters with spaces:

::

   {variable:^10}

Output:

::

   "   1337   "

Number as float (2 decimals):

::

   {variable:5.2f}


Output:

::

   " 1337.00"


Number as integer:

::

   {variable:5d}


Output:

::

   " 1337"

Truncating long strings
~~~~~~~~~~~~~~~~~~~~~~~

Centered and padded to 10 characters with spaces:

::

   {variable:.3}

Output:

::

   "133"
