---
title: Power Entry Board
---

# Power Entry Board


This board can be used to fan out your power rails. See
[Voltages and Power in Pinball Machines](../voltages_and_power/index.md) for
details.

![image](../images/multimorphic_Power_Entry.png)

The Multimorphic Power Filter board serves four purposes. 1. It serves
as a central connection point for 230V/110V AC and all your PSUs using
connectors J1, J2 or J3. 2. It provides a bank of capacitors to buffer
current surges on the high voltage rail. 3. It provides safety relay
control of the high voltage rail. 4. It connects the ground (negative)
terminals of each of the power supplies to prevent a differential in
ground levels between the coil supply and the logic supply which is a
common cause of unstable operation.

The Multimorphic Power Entry Board allows connections for up to four DC
rails:

* 5V
* 12V
* 15V
* High Voltage (HV)

You might use different voltages but the LEDs might operate outside the
spec in this case (consult the manual).

DC Outputs are J11 to J17. DC Inputs are J6 to J9. J10 will turn on HV
on the ouput. You should connect it to your door switch to cut high
power when the door is opened. Make sure that J10 is closed during
development or HV will be off.
