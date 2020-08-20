Wiring and Connectors in Pinball Machines
=========================================

Usually there are two types of wires/connectors used in a pinball machine.
One for all low current connections (i.e. switches or logic) and one for
high current connections (i.e. coils).
See :doc:`voltages_and_power` for details about the different voltages and
power requirements.

.. warning::

   If you are unsure ask a professional electric engineer. This guide does not
   provide all information needed to design and operate a
   high-voltage/high-current system in a pinball machine. Use this at your own
   risk. Electricity can be dangerous and might kill you or burn down your
   house.

High Current
------------

High currents require proper wires and connectors.
Otherwise stuff might get hot and start a fire.
This applies to coils and in some cases also to lights (if you power
more than one light with a wire).
In general, everything above 1A current should use thick wires.

For high current wires you usually want to use AWG 18 or smaller (thicker).
The metric equivalent would be 1mm^2 or more.
Also consider the resistance per meter/inch of your wire and calculate the
voltage drop in advance.

Your connectors should also be spec'd for your expected current.
Most 100 mil Molex connectors allow up to 1A which definitely is not enough
for coils.
For that reason, 156 mil Molex connectors are used for coils.
Usually, they are spec'd for 7A (depends on housing and crimp).
If you need more than 7A use multiple pins.

Molex part numbers (KK series):

* 2 positions: 09-50-3021
* 3 positions: 09-50-3031
* 4 positions: 09-50-3041
* 5 positions: 09-50-3051
* 6 positions: 09-50-3061
* 8 positions: 09-50-3081
* 9 positions: 09-50-3091
* 10 positions: 09-50-3101
* 11 positions: 09-50-3111
* 12 positions: 09-50-3121
* Crimps: 39-00-0342 or 08-52-0072

Low Current/Logic Power
-----------------------

For logic power you don't need thick wires.
Typically, AWG 20-24 or 0.5mm^2 to 0.25mm^2 is used.
Connectors are usually 100 mil Molex connectors.

Molex part numbers (KK series):

* 2 positions: 22-01-2027
* 3 positions: 22-01-2037
* 4 positions: 22-01-2047
* 5 positions: 22-01-2057
* 6 positions: 22-01-2067
* 9 positions: 22-01-2097
* 10 positions: 22-01-2107
* 11 positions: 22-01-2117
* 12 positions: 22-01-2127
* Crimps: 08-51-0108 or 08-50-0114

There are also a lot of very cheap no-name replacements for 100 mil KK which
work just fine since there should not be any high current on those connectors.

Wire-to-Wire Connections
------------------------

While most of the wiring in a pinball machine involves Wire-to-Board connections as referenced above, you may also find yourself needing to make wire-to-wire connections with modular connectors. For this purpose, the standard size connector is the .093” Molex connector from the “Standard .093" Pin and Socket Connectors” series. These connectors and crimps are generally rated for 250V/14A.

For AWG 18-22 wires, use the following Molex parts (Note: there are not housings for 5, 7, 8, 10, 11, 13 or 14 circuit options):

* 1 position: 03-09-1011 (receptacle/female) / 03-09-2011 (plug/male)
* 2 positions: 03-09-1022 (receptacle/female) / 03-09-2022 (plug/male)
* 3 positions: 03-09-1032 (receptacle/female) / 03-09-2032 (plug/male)
* 4 positions: 03-09-1042 (receptacle/female) / 03-09-2042 (plug/male)
* 6 positions: 03-09-1064 (receptacle/female) / 03-09-2062 (plug/male)
* 9 positions: 03-09-1094 (receptacle/female) / 03-09-2092 (plug/male)
* 12 positions: 03-09-1126 (receptacle/female) / 03-09-2122 (plug/male)
* 15 positions: 03-09-1157 (receptacle/female) / 03-09-2159 (plug/male)
* Pin (male) crimp: 02-09-1118
* Socket (female) crimp: 02-09-1119
* Pin extractor: Molex 0011030006 or GC Electronics W-HT-2038
* Recommended crimping tool: IWISS SN-28B

Note: While you can purchase large quantities of the crimp pins above on a reel/tape for a slightly cheaper price, you then have to cut off the side wings on each pin while being careful not to cut too much off or the pins will not lock inside the housings. For people new to crimping, this can be a frustrating experience so the “loose/bag” option listed above (02-09-1118 and 02-09-1119) is generally worth the extra .02 or .03 per crimp terminal.

Sourcing Connectors
-------------------

Those connectors and crimps can be purchased from Digikey or Mouser.
Additionally, you can buy those at your pinball supplier but they tend to be
quite pricy.

Power Distribution Boards
-------------------------

Your power rails will fan out below the playfield to various mechs and boards.
The simplest solution to implement this are terminal blocks which work fine
but make it hard to disconnect stuff temporarily.
Luckily, various boards exist to solve this issue:

* Spooky/PBL Power Distribution board (part number: #600-0224-00)
* FAST Playfield Interchange Board
* Multimorphic Power Distribution board (part number: PCBA-0031-0003)
