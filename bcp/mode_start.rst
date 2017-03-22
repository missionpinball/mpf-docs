mode_start (BCP command)
========================

A game mode has just started. The mode is passed via the name parameter,
and the mode's priority is passed as an integer via the priority.

For example:

::

   `mode_start?name=base&priority=100`.

Origin
------
Pin controller

Parameters
----------

name
~~~~

Type: ``string``

The mode name.

priority
~~~~~~~~

Type: ``int``

The mode priority.

Response
--------
None
