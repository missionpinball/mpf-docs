light_segment_displays:
=======================

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **NO**  |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``platform_settings:`` of your ``segment_displays`` section is where you
map segment displays to lights when using the
:doc:`light segment displays platform </hardware/light_segment_displays/index>`.

.. config


Required settings
-----------------

The following sections are required in the ``light_segment_displays:`` section of your config:

lights:
~~~~~~~
List of one (or more) values, each is a type: dictionary consisting of ``string`` : string name of a :doc:`lights <lights>` device.

In this setting you provide a list of mapping for each segment.
This is an example for a two 7-segment display:

.. code-block:: mpf-config

   #! hardware:
   #!   segment_displays: light_segment_displays
   #! lights:
   #!   segment1_a:
   #!     number: 1
   #!   segment1_b:
   #!     number: 2
   #!   segment1_c:
   #!     number: 3
   #!   segment1_d:
   #!     number: 4
   #!   segment1_e:
   #!     number: 5
   #!   segment1_f:
   #!     number: 6
   #!   segment1_g:
   #!     number: 7
   #!   segment2_a:
   #!     number: 8
   #!   segment2_b:
   #!     number: 9
   #!   segment2_c:
   #!     number: 10
   #!   segment2_d:
   #!     number: 11
   #!   segment2_e:
   #!     number: 12
   #!   segment2_f:
   #!     number: 13
   #!   segment2_g:
   #!     number: 14
   segment_displays:
     display1:
       number: 1
       platform_settings:
         lights:
           - a: segment1_a
             b: segment1_b
             c: segment1_c
             d: segment1_d
             e: segment1_e
             f: segment1_f
             g: segment1_g
           - a: segment2_a
             b: segment2_b
             c: segment2_c
             d: segment2_d
             e: segment2_e
             f: segment2_f
             g: segment2_g
         type: 7segment

type:
~~~~~
Single value, type: one of the following options: 7segment, bcd, 14segment, 16segment.

The type of your hardware segment display.
This is used to calculate the mapping from text to segment.

The mapping is different per type:

For 7segment your segments are: a, b, c, d, e, f, g and dp (see: `7-Segment Displays in Wikipedia <https://en.wikipedia.org/wiki/Seven-segment_display_character_representations>`_ for details)
For BCD your segments are: x0, x1, x2, x3 and dp (see: `Binary Coded Decimal in Wikipedia <https://en.wikipedia.org/wiki/Binary-coded_decimal>`_ for details)
For 14segment your segments are: l, m, n, k, j, h, g2, g1, f, e, d, c, b, a and dp (see: `14 Segment Displays in Wikipedia <https://en.wikipedia.org/wiki/Fourteen-segment_display>`_ for details)
For 16segment your segments are: u, t, s, r, p, n, m, k, h, g, f, e, d, c, b, a and dp (see: `16 Segment Displays in Wikipedia <https://en.wikipedia.org/wiki/Sixteen-segment_display>`_ for details)

dp is an optional decimal point per display.


Related How To guides
---------------------

* :doc:`/hardware/light_segment_displays/index`
* :doc:`/displays/display/alpha_numeric`
* :doc:`/hardware/segment_display_platforms`
