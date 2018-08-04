Wiring and Connectors in Pinball Machines
=========================================

Usually there are two types of wires/connectors used in a pinball machine.
One for all low current connections (i.e. switches or logic) and one for
high current connections (i.e. coils).

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


Low Current/Logic Power
-----------------------

For logic power you don't need thick wires.
Typically, AWG 20-24 or 0.5mm^2 to 0.25mm^2 is used.
Connectors are usually 100 mil Molex connectors.
