
The Mission Pinball framework includes support for GI (general
illumination) strings which are common in existing Williams and Stern
machines. We allow you to specify GI String devices which you can then
enable, disable, or (if the hardware supports it) dim. (GI Strings
tend to be a relic of existing machines. Most new machines with RGB
LEDs just use more RGB LEDs for their GI strings which means that each
GI LED is individually controllable and color-able. So when you use a
P-ROC or FAST controller with a new custom machine, you wouldn't use
this GI string device type. GI Strings are actually kind of complex.
Many of them are AC (even in new machines), and some Williams WPC
machines include triacs (kind of like a transistor for AC) and "zero
cross" AC waveform detection circuits so they can sync their dimming
commands with the AC current wave. Later Williams WPC machines split
their GI into non-dimmable (which used still used AC) and switched
their dimmable to DC. Some machines also have "enable" relays that
must be activated first befor certain GI strings will work. The MPF
hides all this complexity from you. You just define your GI strings in
your machine configuration file and then you can enable, disable, and
dim the dimmable ones as you wish.



