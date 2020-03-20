Power Management in Software
============================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/psus`                                                          |
+------------------------------------------------------------------------------+
| :doc:`/config/coils`                                                         |
+------------------------------------------------------------------------------+

MPF will try to prevent concurrent pulses on the same power supply unit to
reduce the maximum current draw.
This is important for certain switching power supplies since they might just
shutdown on over current.
However, MPF will not mess with any timing critical things such as slings, pops
or flippers as they are controlled by hardware rules.
Instead MPF will delay resets of drop target, ejects of ball devices or
advancing of score reels for up to a few milliseconds (configurable).
You won't notice this in your machine but it makes eject power much more
consistent and drop target resets more reliable.
Without this kind of magic most score reels won't work at all because if you
pulse 15 coils at once none of them will move.

By default MPF assumes that you have only one single power supply unit for all
your coils.
If this is not true you can configure multiple PSUs and assign them to coils:

.. code-block:: mpf-config

   psus:
     default:  # this is configured by default
       voltage: 48
     psu_12v:
       voltage: 12

   coils:
     c_score_reel_1k_p1:
       psu: psu_12v
       number:
     c_score_reel_100_p1:
       psu: psu_12v
       number:
     c_score_reel_10_p1:
       psu: psu_12v
       number:
     c_score_reel_1_p1:
       psu: psu_12v
       number:

This way MPF will sequentialize those coils independently from your coils
on the other PSU.

To give your PSU some breathing room MPF will apply some spacing between two
pulses.
This can be configured using ``release_wait_ms``:

.. code-block:: mpf-config

   psus:
     default:
       voltage: 48
       release_wait_ms: 50    # defaults to 10ms
