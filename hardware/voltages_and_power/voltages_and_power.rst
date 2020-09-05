Voltages and Power
==================

A pinball machine uses multiple different voltages for different purposes.
You need at least one power supply unit (PSU) to transform the AC power
to multiple DC rails.
See :doc:`wiring_and_connectors` for more details on the wire thickness and
connectors to use for the different power rails below.

.. warning::

   If you are unsure ask a professional electric engineer. This guide does not
   provide all information needed to design and operate a
   high-voltage/high-current system in a pinball machine. Use this at your own
   risk. Electricity can be dangerous and might kill you or burn down your
   house.


Primary side - 230/110V
-----------------------

At the mains your machine usually runs at 230V or 110V depending on the region.
Some PSUs are able to work with both voltages.
Sometimes there is a switch to select the input voltage.
In other cases a PSU might only work with a certain input voltage.
Make sure to check this before connecting the PSU to the mains.

In case you run a traditional transformer you usually have to wire the windings
differently depending on the input voltage.
If you get this wrong the output voltages might be different or the transformer
may burst into flames.

In any case it is a good idea and common practise to add a fuse before your PSU
or transformer in case anything goes wrong.
This is for your own safety and for the safety of your neighborhood because
if stuff starts burning it might cause a lot of damage.

High Voltage - 48V to 80V
-------------------------

High voltage (HV) is used to drive coils in your machine.
In modern machines 48V is used which technically classifies as low voltage
in most countries around the world (it is still not safe to touch and can kill
you).
This is preferred if you start a new design as PSUs for 48V are readily
available at a good price.
Most machines use supplies with around 6A to 10A.

Older machines used transformers with 70V to 80V.
Those are more expensive, heavier and harder to get nowadays.
They are generally not recommended for new designs.
If you want to produce a machine this will also be harder to certify in most
countries.
Some people use 24V supplies which technically works but is not recommended
because coils tend to be quite weak and unreliable in those settings.

A large capacitor might help to keep this rail stable since pulsing and PWMing
coil causes large electric and magnetic spikes.
In some cases a PSU might turn off while driving coils without a capacitor on
this rail.
In other cases pulses might be unstable because the voltage will drop too much
during the pulse (seems to be common with 24V supplies).
If you are increasing pulse times and there seems to be no change in the power
of the coil you are likely experiencing the second issue.
Adding large capacitors or using a power entry board (see below) is recommended
in those cases.

You want to use at least one fuse on the HV rail to prevent coils from burning.
Most coils will start burning after a while if you enable them permanently
without PWM (see ``hold_power`` in :doc:`/config/coils` for details).
You do not want that. Instead the fuse should trip and cut the power.
It might be wise to use multiple fuses (e.g. one per bank of coils).

Common power supplies for 48V:

* Meanwell SP320-48 - Used by Stern Spike (not recommended because it is a bit
  too weak)
* Meanwell RSP500-48 - Used by Stern Spike 1 (starting from Ghostbusters) and
  Spike 2
* Meanwell SE-600-48 - Used by Spooky

Common power supplies for 70V - 80V (not recommended for new designs):

* AnTek PS-4N70R5R12 - 70V + unregulated 5V and unregulated 12V


Light Power
-----------

Your lights will require a lot of power.
Depending on the type of light the voltage might differ.
Traditional incandescent bulbs need something around 12V to 24V.
LEDs usually run at 5V (sometimes 12V).
Make sure to understand how much power you need for your lights.
Then calculate which wires, connectors, PSU and fuses you need.
This is very likely a high-current setup and standard connectors with thin
wires will certainly cause problems (or fire) in your machine.

For instance, every LED will draw around 20mA. Triple that for RGB LEDs.
With 80 RGB LEDs for inserts and 80 RGB GIs you will end up at 10A power or 50W.
Most connectors are rated for less than 10A and you will see some voltage drop
with thin wires (check the resistance).

Make sure this is properly fused since this may easily burn down your machine.

Common power supplies:

* Standard ATX power supplies - Work well but you might have to cut the connectors
* Meanwell SP/MW for 12V or 24V - Precalculate your current and get one with some headroom

Display Power
-------------

RGB DMDs usually need either 5V or 12V and might draw a few amps at full
brightness.
Traditional DMDs might need very high voltages.
Definitely ask a professional before getting started with traditional DMDs.

As with any power rail: Add a fuse.

Common power supplies (for 12V):

* Standard ATX power supplies
* Meanwell RD65A - A cheap 5V and 12V supply

Logic Power
-----------

In most cases this will be 5V and 12V.
Most systems use 12V for switches and 5V to power logic components.
In most cases you don't need many amps on those rails.
It might be wise to run separate 12/5V rails for logic components and
light/display power to prevent problems with interferences.

As with other rails: Add a fuse to be safe.

Common power supplies (for 12V):

* Standard ATX power supplies
* Meanwell RD65A - A cheap 5V and 12V supply

PC Power
--------

Most machines run embedded PCs which come with their own PSU.
Sometimes they run off 5V (such as the Raspberry Pi).
Others use standard ATX power supplies.
See :doc:`/finalization/power` for details about power on/off.

Electromagnetic Compatibility EMC/EMI
-------------------------------------

You need to make sure that your machine complies with regulations and will
not disturb police radios/air traffic control or your neighbors Wifi.
Especially pulsing or PWMing coils will cause a lot of interferences.
This might cause RF emissions and make you a lot of enemies.
The most important step to mitigate EMI is to run your power and return wire
in parallel and make them the same length.
There will be a magnetic field between HV and GND to your coil when current
flows.
If current changes, the field will change and you will transmit signal which
is what you want to avoid.
Additionally, add free flow diodes to your coils to prevent self-induction
voltage from travelling back to your driver board and PSU (which will transmit
another signal).

EMC is a complex topic. If in doubt consult an electic engineer.


Common Ground
-------------

.. warning::

   It is very important to connect all grounds if you use multiple PSUs.
   We cannot stress this enough.
   Not ensuring this will be very dangerous!

In general, it is preferred to connect the ground at the PSUs than below
the playfield.
Then run a separate ground for each power rail from the PSU to the playfield.

Interferences on the ground of the HV rail might cause problems in other rails.
Especially for serial LEDs and logic power.
In case you run into those problems consult with an electric engineer.
The right capacitors and the right wiring might help with this case for example.

Common "ground" generally refers to the neutral wire of your PSU which should
not be confused with ground/electric earth.
See :doc:`ground_and_appliance_classes` for details about ground vs neutral.

Power Filter Boards
-------------------

Some vendors sell power filter boards which help you to build your different
power rails.
Additionally, those boards allow you to disconnect components at a central
location.
Usually, those boards will also connect all ground for you.

Some common boards:

* :doc:`Multimorphic Power Entry Board </hardware/multimorphic/power_entry>`
* :doc:`FAST Power Filter Board </hardware/fast/power_filter>`
* Spooky/PBL Power Entry Board (part number: #600-0253-00)
* `OPP Power Filter Board  <http://pinballmakers.com/wiki/index.php/OPP#Power_Filter_Board>`_
* Stern Spike Power Distribution Board (part number: 520-5343-01)
