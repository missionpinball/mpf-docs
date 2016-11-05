Multimorphic (P-ROC & P3-ROC)
=============================

The P-ROC and P3-ROC are pinball hardware controllers created by Gerry
Stellenberg of Austin, Texas-based `Multimorphic <http://www.multimorphic.com/>`_.
The P-ROC controller is a "drop in" replacement in existing WPC and Stern
machines, whereas as the P3-ROC controller is designed to be used in new
machines. Multimorphic also has custom driver and interface boards that can be
used for new machines with either controller.

The P-ROC was introduced into the market in 2009, along with a basic
Python-based game framework called Pyprocgame (originally created by Gerry and
greatly improved by a guy named Adam Preble). Since then, many complete games
have been built on P-ROC and P3-ROC hardware, including The Big Lewbowski,
Cactus Canyon Continued, Buffy the Vampire Slayer, Predator, DeadPin, The
Matrix, and several others. (Multimorphic always has a big booth at the Chicago
Pinball Expo each October where you can  talk to many folks and see lots of
machines built using the P-ROC and P3-ROC controllers.)

MPF owes a lot to the P-ROC community because this is what we found in 2013
when we were randomly googling "build your own pinball machine", and the
creators of MPF spent a year programming for the P-ROC in Pyprocgame before we
decided to create our own framework in 2014.

MPF fully supports both the P3-ROC and the P-ROC. (MPF supports the P-ROC
operating with P-ROC driver boards as well as with Williams WPC and Stern S.A.M.
driver boards. We haven't tested with a Stern Whitestar machine yet but it
should work. Contact us for details if you'd like to help us test!)

More information about these controller boards (and ordering information) is
available at `pinballcontrollers.com <http://pinballcontrollers.com/>`_.
They also have an active `forum <http://www.pinballcontrollers.com/forum/>`_.

Multimorphic hardware options
-----------------------------

P-ROC
~~~~~
A pinball controller which can act like a "drop in" replacement for WPC, WPC-95,
Stern S.A.M., and Stern Whitesar machines. It can also be used with System 11
and Data East machines with the addition of the "Snux" driver board.

Includes 32 switch inputs directly on the board (more can be added by adding
additional input boards) and physical mono DMDs (via the standard 14-pin ribbon
cable).

P3-ROC
~~~~~~
Very similar to the P-ROC, except the P3-ROC only works with Multimorphic
driver boards (described below) and is designed to work with new machines
rather than existing ones like the P-ROC.

The P3-ROC does not have support for a mono DMD (though with MPF you can create a
virtual DMD on an LCD screen, use an LCD display outright (this is what The Big
Lewbowski does), or you can combine it with an RGB LED DMD controller for full
color RGB LED matrix displays.

The P3-ROC also includes a 3-axis accelerometer which MPF can use for tilts as
well as to detect whether the machine is level.

PD-16
~~~~~
A 16-channel driver board for the P-ROC or P3-ROC. You can add multiple PD-16s
to control up to 168 drivers.

PD-8x8
~~~~~~
An 8x8 switch matrix input board for the P-ROC. You can connect two of these to
create a 16x8 matrix for 128 switches total. (These switch inputs are in
addition to the 32 direct switch inputs on the P-ROC)

PD-LED
~~~~~~
Controls up to 84 individual LED elements, which can be used to control
individual single color LEDs, or combined into groups to control RGB LEDs. The
PD-LED works with both the P-ROC and P3-ROC.

Note that the PD-LED uses a "direct" connection method for LEDs, where each LED
has connections for each color element running back to the PD-LED. This is a
different architecture than the serial-controlled "Neo Pixel" type LEDs that
other hardware uses.

Also note that if you use a P-ROC or P3-ROC with MPF, you could optionally
choose to use an LED controller like the FadeCandy to control up to 512
separate RGB LEDs. It's just a matter of preference as to whether you want
direct connected or serial LEDs. MPF doesn't care either way. (And you can mix
and match.)

SW-16
~~~~~
A switch input board for the P3-ROC which allows you to connect up to 16 direct
switches (e.g. no switch matrix) to the P3-ROC. You can use multiple SW-16s to
support as many switches as you need (up to 256 total).

Using a P-ROC or P3-ROC with the MPF
------------------------------------

Using a P-ROC or P3-ROC with MPF is simple. All you need to do is to download
the FTDI driver (that's the USB driver for the board) from `here <http://www.ftdichip.com/Drivers/D2XX.htm>`_
for your platform. Everything else is built-in to MPF.

If you're familiar with the P-ROC or P3-ROC, pre-compiled versions of the
*libpinproc* and *pypinproc* libraries for Windows and Mac are included in the
MPF package, so you don't have to mess with that or compile anything when using
MPF.
