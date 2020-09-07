How to use MPF with Stern SPIKE / SPIKE 2 machines
==================================================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/hardware`                                                      |
+------------------------------------------------------------------------------+
| :doc:`/config/spike`                                                         |
+------------------------------------------------------------------------------+

If you haven't done so already, be sure to read the :doc:`/start/index` page
to understand how MPF talks to physical pinball machines in general.

Stern pinball machines from early 2015 (Wrestlemania) onwards use a control
system called SPIKE (or SPIKE 2 from Batman 66 onwards). The complete list
of SPIKE machines is available in IPDB (click here for `SPIKE <http://ipdb.org/search.pl?searchtype=advanced&mpu=61>`_
and `SPIKE 2 <http://ipdb.org/search.pl?searchtype=advanced&mpu=65>`_ machines).

You can read all about how SPIKE works in the operators manuals for the games, but the important
thing to know here is that SPIKE machines essentially have a full linux
computer inside them (the "SPIKE CPU Node") which runs the game code from an SD card.

If you want to use MPF to control or power a Stern SPIKE system, you can
make some small changes to the SD card to enable external control and then
connect the computer running MPF to the CPU Node via USB.

.. note:: When you use MPF with a Stern SPIKE machine, MPF itself does not run
   "on" the SPIKE CPU Node. Rather you still run MPF on a host computer (your
   laptop, a Raspberry Pi, a mini-ATX motherboard in the machine, etc.), and it
   connects to the SPIKE CPU node via a serial or USB connection to control the
   machine.

Doing so gives you full control of the machine. You can read the states of switches,
fire coils, set LEDs, etc. Then you can use MPF to write your own game code, just
like any other platform.

Note that you *cannot* access any of the existing Stern game rules, code, or assets (videos,
images, sounds, etc.) All of that is compiled into the original game code on the SD
card and protected by copyright. So if you just want to do a "small tweak" to the
rules of a Stern SPIKE machine, then MPF is not the right tool for that. Instead MPF
would be used to completely rewrite the game from scratch, either to write a different
version for the existing machine or to retheme the machine into something of your
own creation.

.. note:: The MPF to Stern SPIKE bridge & support is new and EXPERIMENTAL.
   Much of this will change in the next weeks and months as we get more real world
   experience with it.

.. warning:: It's possible that using the MPF SPIKE bridge will void your warranty.
   For example, maybe you build a config or MPF contains a bug that holds a coil on
   too long and it burns up your machine. Use it at your own risk. It's also possible
   that you will not void your warranty. We are not lawyers and don't know.

.. warning:: If you break or corrupt your original SD card with your Stern game code
   on it, you may have to get a new one from Stern support. Again, proceed at your
   own risk only if you know what you're doing.

Fundamentally, using MPF with a Stern SPIKE system is like putting a P-ROC in a
Williams WPC machine. All it does is expose the hardware to a computer which you
can then control, and you're on your own in terms of rules and assets and code
and everything. The advantage of using a SPIKE machine is you don't have to buy a
$325 P-ROC, and you can swap back-and-forth between the original rules and your own
code by changing an SD card versus having to unplug and re-plug a bunch of wires to
swap out a board.

Stern SPIKE features that work today
------------------------------------

* :doc:`Coils / drivers <drivers>`
* :doc:`Switches <switches>`
* :doc:`LEDs & GIs <leds>`
* :doc:`Backbox LEDs <leds>`
* Hardware Rules (flippers, pop bumpers, slingshots, etc.)
* :doc:`DMDs <dmds>`
* :doc:`Steppers <steppers>`

How does the MPF SPIKE interface work?
--------------------------------------

Here's a more technical overview of how MPF talks to a Stern SPIKE machine. You don't
have to read this section if you don't care.

Stern SPIKE hardware is a series of node boards that are connected via Cat-5 cables
which is known as the SPIKE node bus. The CPU running the game code from the SD card
on the CPU node sends commands to individual node boards to actuate drivers and set
LEDs and stuff like that, and it receives switch state updates from node boards with
switches attached.

When you use a Stern SPIKE machine with MPF, you install a piece of software called
the "MPF SPIKE Bridge" on the SD card (ideally you first make a copy of your existing
SD card and keep the original in a safe place), and then when the machine powers on,
instead of running the existing game code from the SD card, the CPU runs the MPF SPIKE
bridge software.

.. image:: /hardware/images/spike_bridge.png

The MPF SPIKE bridge is fairly simple. Essentially all it does is relay messages from
the SPIKE node bus to the debug port on the CPU node, and it also accepts commands
sent via the debug port and retransmits them to the node bus.

So in order to connect a computer running MPF to the Stern SPIKE machine, you buy
a small USB-to-serial adapter (Amazon.com has them for under $10) and connect one
end of it to the CPU node's debug header, and you plug the other end into your computer
which is running MPF. (That can be Windows, Mac, Linux, Raspberry Pi, etc. Just a regular
computer running the regular version of MPF.)

From there you just configure MPF like regular. You set the platform to "spike", you
set the port that your USB-to-serial adapter is using, and you set all your coils,
switches, and LEDs based on their node board & IDs from the operator's manual.

If you ever want to go back to the original game code from Stern, then just swap out
the SD card with the MPF SPIKE Bridge on it and replace it with the original card from
Stern and you're all set.

Stern SPIKE features that do not work (yet)!
--------------------------------------------


Sound
^^^^^

Currently if you want to use sound (which of course you do), the way
to do it is to use the sound card in the computer running MPF and
speakers connected there.

The SPIKE system has sound capabilities, and it would be nice to be
able to use it along with its existing speakers and amps, but
the way MPF connects via the debug port does not allow for enough
bandwidth for us to do sound this way.

This is something that might change in the future, or perhaps we
can find an easy way to connect the sound output from the computer
to the SPIKE amp.

Servos
^^^^^^

Once we get access to a SPIKE machine with servos, we'll get
support for them added.

Small LCD from WWE
^^^^^^^^^^^^^^^^^^

WWE LEs have a small playfield LCD which is controlled via the SPIKE
node bus. MPF does not yet support this, though of course you could
use any HDMI display connected to the machine running MPF.

.. toctree::
   :titlesonly:

   Installing the MPF SPIKE bridge on the SD card <mpf-spike-bridge>
   Connecting your computer <connection>
   Configuring MPF for SPIKE <config>
   Coils & Drivers <drivers>
   LEDs, GI, & Backbox lights <leds>
   DMDs <dmds>
   Switches <switches>
   Steppers <steppers>
   troubleshooting
