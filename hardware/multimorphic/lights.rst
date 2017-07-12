How to configure Matrix Lights (P-ROC/P3-ROC)
=============================================

.. include:: /not_updated_yet.rst

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/matrix_lights`                                                 |
+------------------------------------------------------------------------------+
| :doc:`/config/p_roc`                                                         |
+------------------------------------------------------------------------------+
| :doc:`/config/p3_roc`                                                        |
+------------------------------------------------------------------------------+

To configure matrix lights connected to a PD-8x8 and a P-ROC or P3-ROC, you can
follow the guides and instructions in the :doc:`/mechs/lights/index` docs.

However there are a few things to know about using matrix lights with a P3-ROC.

.. note::

   If you're using your P-ROC in an existing machine, then don't use the number
   settings here. Instead use the numbers from the existing machine section of
   the documentation. (link TODO)

number:
-------

Configure the number for each lamp in your matrix_lights: section with an entry
that contains a bunch of letters and numbers which specify the specific columns
and row outputs that make up each lamp. It’s probably easiest to look at an
example.

::

   matrix_lights:
      some_light:
         number: C-A2-B0-0:R-A2-B1-0

Notice there are two parts to the number, separated by a colon.

The first part is the column information:

* ``C`` means "Column"
* ``A2`` means "the PD-8x8 at Address 2"
* ``B0`` means "Bank 0"
* ``0`` means output "0"

The second part is the row information:

* ``R`` means "Row"
* ``A2`` means "the PD-8x8 at Address 2"
* ``B1`` means "Bank 1"
* ``0`` means input "0"

Luckily this is only something you have to work out once. :)

Fine tuning column strobe times
-------------------------------

The lamp matrix works by quickly cycling through the columns and then
activating the rows for the individual lamps that are supposed to be on in that
specific column.

Back in the day when only incandescent bulbs were used, this pretty much worked
the same everywhere and you didn't have to worry about any other settings.
However now that it's possible to use LEDs replacement bulbs in your lamp
matrices, and there are all sorts of LEDs like "anti-ghosting" and things like
that, you may want to fine-tune the timing of how the columns are activated.
You can do that in the ``p_roc:`` or ``p3_roc:`` sections of your machine-wide
config.

For P-ROC:

::

   p_roc:
      lamp_matrix_strobe_time: 100ms

For P3-ROC:

::

   p3_roc:
      lamp_matrix_strobe_time: 100ms

100ms is the default setting (which is used if you don't add this entry), but
you can play with this value to see how it affects your lights or LEDs.

This is a system-wide setting, so if you have multiple lamp matrices on
multiple PD-8x8 boards, then this setting will be used for all of them.
