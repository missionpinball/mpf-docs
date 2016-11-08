Case insensitivity in config files
==================================

Setting names config files are not case sensitive. This was done to prevent confusion
as people would typically miss case settings. For example, in MPF
prior to version 0.17, the following would work:

::

    SlidePlayer:

While the following would not:

::

    Slideplayer:

What happens internally is that all the
settings (i.e. the "keys" of the key/value pairs in config files) are
converted to lowercase internally. We believe that this should not be
a problem and in fact should be transparent to most game programmers.
We also have attempted to make sure that all functions that reference
objects that are set up in the config files also convert their
references to lower case. For example, if you have a coil defined like
this:

::

    coils:
      flipperLeftMain:
        number: ...

And then later you refer to it via your code as

::

    self.machine.coils['flipperLeftMain']

That will still work because the device collection object that holds
the list of coils will convert the incoming request to lowercase. All
that said, there's one "gotcha" with this. The case insensitivity
means that you cannot differentiate between devices bases solely on
case differences. For example, in versions of MPF prior to 0.17, it
was perfectly valid to define lane lights based on uppercase letters.
For example, the three lights that make up "W", "I", and "N" lanes
could have been defined as ``lane_Win``, ``lane_wIn``, and ``lane_wiN``
previously. Starting with MPF 0.17, you'll have to differentiate them
in some other way. (For example, ``lane_win_w``, ``lane_win_i``, and
``lane_win_n``. We believe this change was for the better, but we're
always open to options. If you believe we should change this behavior,
please start a discussion in our MPF Development forum.
