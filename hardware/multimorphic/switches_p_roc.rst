How to configure switches (P-ROC)
=================================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/switches`                                                      |
+------------------------------------------------------------------------------+

To configure switches on a P-ROC, you can follow the guides and instructions in
the :doc:`/mechs/switches/index` docs.

.. image:: /hardware/images/multimorphic_p_roc.png

However there are a few things to know about using switches with a P-ROC.

number:
-------

Switches are directly connected to the P-ROC board itself. There are two
types of switches—matrix and direct—and they each have a different number
format.

.. note::

   If you're using your P-ROC in an existing machine, then don't use the number
   settings here. Instead use the numbers from the
   :doc:`existing machine section </hardware/existing_machines/index>`
   of the documentation.

Direct Switches
^^^^^^^^^^^^^^^

The P-ROC has 32 direct switch inputs (which are switches that are directly
connected to the P-ROC that do not require a switch matrix). Direct switches
are numbered 0-31. (See the P-ROC documentation for the connector mappings.)

Direct switches are configured in your machine config file by starting the
number with "SD", like this:

.. code-block:: mpf-config

   switches:
     my_switch:
       number: SD0
     my_other_switch:
       number: SD1
     another_switch:
       number: SD12

Matrix Switches
^^^^^^^^^^^^^^^

If you're using a switch matrix, then the switch numbers are entered using
the column number, then a slash, then the row number.

.. code-block:: mpf-config

   switches:
     my_switch:
       number: 0/0    # column 0, row 0
     my_other_switch:
       number: 0/1    # column 0, row 1
     another_switch:
       number: 3/4    # column 3, row 4

Mixing and matching direct and matrix switches
----------------------------------------------

You can mix-and-match direct and matrix switches. However you should be
aware of the hardware limitations of combining both. The P-ROC gives you the
ability for ONE of the following:

* 32 direct switches and an 8x8 (64 switches) matrix
* 24 direct switches and an 8x16 (128 switches) matrix

Basically the P-ROC has the ability to repurpose 8 of the direct switch inputs
as row inputs to extend the switch matrix from 8 to 16 rows. This means
that valid values are:

* Direct switches, ``SD0`` - ``SD31``
* Matrix switches, ``0/0`` - ``7/7``

OR

* Direct switches, ``SD8`` - ``SD31``
* Matrix switches, ``0/0`` - ``7/15``

In other words, if any switch uses a row number (the number after the slash)
greater than 7, then you can't use direct switches 0 through 7.

The configuration of this is automatic based on the numbers you use, but
currently there is no error checking to ensure that SD0 - SD7 are not used if
you have any switch which a row that's 8-15.

Choosing direct versus matrix switches
--------------------------------------

The only difference between direct and matrix switches is in how they're wired.
Matrix switches use less wire, but require diodes on the switches and are
harder to troubleshoot. Direct switches are easier to wire, but they require
more wire and you're limited to 24 (or 32) of them.

If you're using :doc:`opto switches </mechs/switches/optos>` then you must
connect the IR receivers to direct switch inputs, since the direct switch
inputs are always powered.

There's a misconception that direct switches are "faster" than matrix switches.
That is false. The P-ROC scans the 8 columns of the matrix (one at a time),
then it reads the direct switches, then the matrix switches again, then the
directs, etc. So from a practical sense, the directly switches are really like
a single column matrix with either 24 or 32 rows, and they're scanned after the
rows of the matrix are scanned. So whether a switch is direct or in the matrix
doesn't affect the scanning speed or response time of the switch.

Debounce options
----------------

The P-ROC has the ability to configure :doc:`debounce settings </mechs/switches/debounce>`
for switches. A non-debounced switch which report its state change immediately,
while a debounced switch will report its state change after it's been in the
new state for two consecutive reads.

By default, MPF will enable debouncing in both directions (open and close) for
all switches. However you can override this on a per-switch basis with a
switch's ``debounce:`` setting.

Valid options are ``normal``, ``quick``, and ``auto``.

To disable debouncing for a switch, add ``debounce: quick`` to the switch
config, like this:

.. code-block:: mpf-config

   switches:
     my_switch:
       number: 0/0
       debounce: quick

To force debouncing to always be used (which is also the default on the P-ROC,
so not really needed), configure it like this:

.. code-block:: mpf-config

   switches:
     my_switch:
       number: 0/0
       debounce: normal

What if it did not work?
------------------------

Have a look at our
:doc:`troubleshooting guide for the P/P3-Roc <troubleshooting>`.
