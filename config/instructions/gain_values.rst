How to enter gain values in config files
========================================

The sound-related items in your config files contain various volume settings that may be specified
as a gain value.  MPF gives you the flexibility to specify gain values as simple numeric values
between 0.0 and 1.0 or as a decibel string between -inf and 0.0 db.  Individuals with audio or
video editing experience may be more comfortable working with decibel values.

Entering a simple numeric gain value
------------------------------------

To enter a simple numeric gain value, simply enter a number between 0.0 and 1.0 with no appended
label string.  Some examples:

.. code-block:: yaml

   volume: 0.1334

   volume: 1.0

   volume: 0.0

Entering a gain value in decibels
---------------------------------

To enter a gain value in decibels, enter your value between -inf and 0.0 and add a “db” after your
value. (This can be uppercase or lowercase, and you can put a space in between your value and
the letters if you want.)

**Note**: -inf indicates the minimum gain value (equivalent to 0.0 in
a simple numeric gain value) and should not contain a “db” suffix.  For all other decibel values if
you do not enter the “db” suffix after your value, then MPF will read in the gain value as a simple
numeric gain value between 0.0 and 1.0.

Some examples:

.. code-block:: yaml

   volume: -17.5db

   volume: 0.0 db

   volume: -inf

It makes no difference whether you enter your gain values in simple numeric format or decibels,
as MPF will convert everything to simple gain values under-the-hood when it reads in your
configuration files.
