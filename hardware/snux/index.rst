Snux System 11 Driver Board
===========================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/hardware`                                                      |
+------------------------------------------------------------------------------+
| :doc:`/config/snux`                                                          |
+------------------------------------------------------------------------------+
| :doc:`/config/system11`                                                      |
+------------------------------------------------------------------------------+
| :doc:`/config/switches`                                                      |
+------------------------------------------------------------------------------+
| :doc:`/config/coils`                                                         |
+------------------------------------------------------------------------------+


MPF can be used with Williams System 11 machines. (Also since Data
East's system was a clone of Williams System 11, everything here also
applies to those machines.) This How To guide walks you through the
process of buying the hardware you need and configuring MPF to work
with it.



(A) Understand the challenges of System 11 hardware
---------------------------------------------------

The original System 11 Williams/Bally hardware (and the Data East
clone) was created in a time when computing resources were scarce and
hardware was expensive. It's sort of a "crossover" between the early
solid state machines of the '80s and the more modern WPC machines.
Because of this, there are a lot of, umm... "quirks" to the design
which were necessary at the time but which may seem a bit strange in
today's world. Even though we tend to lump all "System 11" machines
into a single category, there were actually four different generations
of System 11 machines, called System 11, System 11A, System 11B, and
System 11C. (And just to make things even more fun, some changes were
made part way through System 11B.) So technically-speaking there are
actually five different types of System 11 machines out there!

Flippers
^^^^^^^^

On modern WPC pinball machines, flipper buttons are just regular
switches that send their inputs to the CPU, and flipper coils are just
regular coils that are controlled by the CPU. Typical flippers in MPF
are configured via the flippers: section of the config file, and when
flippers are enabled, hardware rules are written to the pinball
controller to allow them to be fired "instantly" when the flipper
buttons are hit. Back in the days of System 11, the CPUs in those
machines didn't have enough horsepower to constantly poll the status
of the flipper buttons and to drive the flippers in software while
also doing everything else the CPU needed to do to run the game. So
instant, System 11 machines had the flipper buttons directly connected
to the flipper coils, meaning that hitting the flipper button would
activate the flipper coil directly without any intervention of the
CPU. Of course the machine still needed a way to enable or disable the
flippers, since the flippers needed to be disabled when a game was not
going on and when the player tilted. To do this, System 11 machines
used a "flipper enable" relay. This was a mechanical relay connected
to a driver output on the driver board. When that driver was enabled,
the relay was energized and the flippers worked. When that relay was
disabled, the relay de-energized, the electrical connection to the
flipper buttons was broken, and the flippers stopped working. While
this meant that the CPU didn't have to directly control the flippers,
it also meant that many modern conveniences are not available on that
hardware. For example, on modern machines you can control the strength
of the flipper by adjusting the pulse times of the flipper coils with
millisecond-level accuracy. But these older machines gave full power
to the flipper until the flipper bat hit the end-of-stroke (EOS)
switch, and that switch mechanically cut off power to the high-power
winding (while keeping power enabled on the low-power hold winding).
So in those days, changing the strength of a flipper was done by
physically swapping out the flipper coil with a stronger or weaker
one.



"Special" Solenoids
^^^^^^^^^^^^^^^^^^^

Flippers are not the only types of devices that require instant
response in pinball machines. They also need instant response action
for slingshots, pop bumpers, and (sometimes) diverters. In many System
11 machines, these types of devices were also controlled by the
flipper enable relay. So when that relay was enabled, it enabled not
just the flippers but also the pop bumpers and slingshots. Of course
pop bumpers and slingshots are a bit different than flippers:


+ The CPU needs to know when pop bumpers and slingshots are hit so it
  can assign points, flash lights, play sounds, etc.
+ The CPU needs to be able to manually fire pop bumpers and slingshots
  for things like ball search and the coil test options in the operators
  menu.


In other words, it seems that pop bumpers and slingshots really need
to be controlled the "new" way since the CPU needs to know when
they're hit and the CPU needs to be able to manually fire them. But of
course firing a pop bumper or slingshot when their switch is hit needs
to happen instantly, and as we just discussed, that was not possible
in the System 11 days. So how did they get around it? System 11
machines call these types of solenoids *special solenoids* (that is
literally what they're called in the manual) because they're actually
controllable via two different ways:


+ When the flipper enable relay is enabled, a hit to these devices'
  switches creates a direct electrical connection to their coils which
  fires them.
+ These devices' coils also have a second (additional) control input
  which lets the CPU fire them from the service test menu or for ball
  search.


Furthermore you'll also notice that there are switches in the switch
matrix for many of these devices which are used to let the CPU know
that these devices have been hit to assign points and to do effects.
At this point you might think, "Great! So these devices have CPU-
controlled coils, and they have switches in the switch matrix, so I
can just set them up like regular devices since I'm using modern
hardware!" Not so fast. In many System 11 machines, the switches in
the switch matrix which tell the CPU that a pop bumper or slingshot
has been hit are not the same switches that fire the coil! For
example, the switch attached to the skirt of the pop bumper that the
ball hits is a high-voltage switch that is physically connected to the
pop bumper's coil. The CPU does not see that switch at all. When that
switch is hit (if the flipper enable relay is active), then it grounds
the connection to the coil and the coil fires. When the coil fires,
its shaft hits a second switch underneath, and that's the switch that
is connected to the switch matrix and the CPU. (And actually there's a
third switch under there too which is the EOS switch which cuts power
to the coil after it's been fired.) So in reality, yeah, you may see a
switch in the switch matrix for a pop bumper, but that switch is not,
"Hey the pop bumper skirt switch was hit, so fire the pop bumper now,"
rather, that switch is, "Hey the pop bumper just fired. Just FYI." The
exact details of how these special solenoids work depends on the
specific machine and which version of System 11 it is. For example,
some devices (like pop bumpers and slingshots) should always be on
whenever the flippers are enabled, so the flipper enable relay enables
them too. Other devices (like diverters) should only be active
sometimes, so they have their own enable driver (which is like the
flipper enable relay, but separate from it) so they can be controlled
individually.



The A/C Relay & Switched Solenoids
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

But wait! There's more! System 11 machines also have this concept of
the A/C relay. This is not A/C in the terms of alternating current. It
has nothing to do with that. It's actually used to control things
called A-side and C-side devices. The basic concept is that since the
driver circuitry was expensive, Williams decided they could get double
their "bang for their buck" by connecting two devices so a single
output. So you might see on a schematic that a single driver output is
connected to both a ball kickout coil and a flasher. Then there was a
relay (called the A/C relay, or sometimes the C-select relay)
connected in there too. If the A/C relay was in the A position, then
firing that driver would fire the coil connected to the A side of that
output, and if the A/C relay was in the C position, then firing that
driver would fire the device connected to the C side of that output.
This worked because they had a single A/C relay that was connected to
an entire bank of 8 drivers. So they could actually control 16
different devices (8 drivers with two devices each) from just 9 driver
outputs (8 drivers plus 1 for the A/C relay). They were also smart
about what types of devices they connected to each side of the relay.
System 11 machines put the "important" devices on the A side (things
that interact with the ball on the playfield, like diverters, kickout
holes, motors, etc.), and they put the "less important" things on the
C side (flashers and the knocker coil). So this means they will
constantly enable and disable the A/C relay to do different effects,
but if two things need to happen at exactly the same time, they can
service the A-side first (since those are the important ones) and then
flip the relay to the C-side and pick those up after a few hundred
milliseconds of delay.



Controlled Solenoids
^^^^^^^^^^^^^^^^^^^^

In addition to switched, controlled, and flipper solenoids, System 11
machines also included what they called "controlled" solenoids which
was their name for normal, modern-style solenoids. So in addition to
all the craziness of the other control schemes, some solenoids were
regular. No special switches. No special handling. Just regular
solenoids.



GI (General Illumination)
^^^^^^^^^^^^^^^^^^^^^^^^^

In WPC machines, GI strings are controlled via separate GI drivers
(which are alternating current and which may or may not be dimmable).
In System 11, GI strings were regular driver outputs, just like any
solenoid. The catch is that most (maybe all?) GI strings on System 11
machines are "backwards" in the sense that the GI is on when the
driver is disabled, and you enable the driver to turn off the GI. This
was done because the GI is almost always on all the time, though there
are periods when you might want to turn it off for special effects. So
to save on wear of the relays and make things simpler, in System 11
machines, the GI is just always on until the CPU turns it off.



Putting it all together
^^^^^^^^^^^^^^^^^^^^^^^

If you look at the solenoid table in the operators manual of a System
11 machine, you'll see that all the drivers fall into these
categories. Some are are switched, some are controlled, some are
flippers, and some are special. Check out the solenoid table from
PinBot. Note that the first 16 solenoids are the A/C switched
solenoids, and there are two coils for each number 1-8 with an "A" and
"C" suffix denoting which side they're on. Then the next 8 (numbers
9-16) are controlled solenoids. These are the regular modern-style
drivers which also include the GI (remember they're active off) and
important flashers they don't want to share with A/C switched drivers.
Then you have the next batch 17-22 which are the special solenoids
that are enabled when the flipper enable relay is enabled, but they
can also be manually controlled for ball search and testing. And
finally you have the left and right flipper solenoids which don't have
numbers because they're not connected to the driver board. Also notice
solenoid 14 is the "Solenoid Select Relay." That's the A/C select
which when inactive means that drivers 1-8 are connected to the A-side
devices, and when active means drivers 1-8 are connected to the C-side
devices.



(B) The Snux board
------------------

Okay, so now that you're caught up with the intricacies of System 11
hardware, how do you actually control this via MPF? The usual way you
control an existing machine is to remove the original CPU board and to
replace it with either a P-ROC controller. The new pinball
controller plugs into the backbox and uses the existing driver board.
The problem with System 11 is that unlike more modern machines, the
System 11 CPU board and driver board were actually combined into one
single huge board. So when you take out the CPU board, you also lose
the driver board. This means if you put a P-ROC controller
into a System 11 machine, you don't have a driver board. :( This is
where the Snux board comes in. The Snux board (which is our name for
it) is a System 11 driver board created by Mark Sunnucks. (His online
handle is Snux which is why we call it the Snux board.) Mark developed
this board a few years ago because he wanted to control an F-14
machine with a P-ROC. The Snux board can be thought of kind of like
the WPC power driver board except that it's made to work with System
11 machines instead of WPC machines. Since the original System 11
combo CPU board / driver board was so huge, when you remove it from
your System 11 machine there's plenty of room to put the Snux board
and a P-ROC controller in it's place. The Snux board
connects to the P-ROC controller via the standard
34-pin ribbon cable, and then it has all the connectors (in their
proper locations) to connect the existing wiring connectors from the
System 11 machine to it. So in order
to control a System 11 machine with MPF, you need to get a Snux board.
Mark has a day job and built this board as a hobby, but he sells them
to other folks who are interested in modernizing System 11 machines.
Mark lives in the UK, so the exact price you pay depends on the exchange rate,
shipping to your country but it's around $180 US (Then you
also have to buy a P-ROC to drive it.) You can
contact Mark via PM (on Pinside as Snux). In addition to the board there are
3 or 4 cables you'll need, Mark can advise.

Displays
^^^^^^^^

All System 11 machines used various combinations of segment displays
and these cannot be directly controlled via the P-ROC.  If you do want to use
the original segment displays, Jim at mypinballs.com sells an adaptor board
that will connect between the P-ROC and the displays.   Otherwise you can use the
various other display options that MPF provides.


(C) Understand how MPF works with the Snux board
------------------------------------------------

Once you have your P-ROC controller and the Snux board
installed in your System 11 machine, you need to build your machine-
wide configuration file for your machine. MPF has a *Snux* interface
which is actually implemented as a platform overlay. A platform
overlay, in MPF, is like a second layer that sits on top of the
regular platform interface and modifies the way it works. So since the
Snux board works with the P-ROC controller, the main
platform interface MPF uses is the P-ROC platform.
Then the Snux platform overlay layers on top of it to handle the
special cases that arise when using the P-ROC with
a Snux board. (For example, automatically controlling the A/C relay to
make sure it's in the right position when an A-side or C-side driver
is activated, and preventing the activation of C-side drivers when the
A/C relay is in the A position and vice-versa.) The Snux driver
overlay completely hides the nuances of the System 11 hardware from
you. You can freely enable, disable, or pulse any A-side or C-side
driver you want, and MPF will automatically control the A/C relay and
make sure it's in the proper position. Since A-side drivers are more
important in the machine, MPF will always give them priority. If
simultaneous requests for an A-side and C-side driver come in at the
same time, MPF will service the A-side driver and add the C-side
driver to a queue, and then when the A-side driver is done, MPF will
flip the relay to the C-side and then service the C-side driver.
Similarly if drivers on the C-side are active and an A-side request
comes in, MPF will deactivate the C-side drivers, flip the relay, and
then service the A-side drivers. The takeaways from this are (1)
A-side drivers always have priority, and (2) the handling of the A/C
relay is automatic.



(D) System 11-specific MPF configuration
----------------------------------------

Once you have your hardware setup, there are a few things you need to
do in your config file.



1. Configure your hardware interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The first thing to do is to configure your hardware options in the
hardware section of your machine-wide config. You configure the main
platform as *p_roc*, but then for *driverboards* you
configure it as *snux*, like this:


.. code-block:: mpf-config

   hardware:
     platform: virtual
     driverboards: wpc
     coils: snux
     switches: snux

2. Configure snux options
^^^^^^^^^^^^^^^^^^^^^^^^^

The MPF machine-wide config file contains a few options for the Snux
driverboard. These options are set in the default *mpfconfig.yaml*
file which means you don't have to add them to your own config file,
but we're including them here just for completeness:


.. code-block:: mpf-config

   coils:
     c_diag_led_driver:
       number: c24
       default_hold_power: 1.0

   snux:
     diag_led_driver: c_diag_led_driver

The Snux board maps driver ``c_diag_led_driver`` which is driver 24
to the "diag" LED on the board.
When you power on your
machine, the diag LED is off. Then when MPF connects to the board,
this LED turns on solid. Finally when MPF is done loading and it
starts the main machine loop, this LED flashes twice per second. If
this LED stops flashing, that means MPF crashed. :)

3. Configure system11 options
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Next you need to add a system11: section to your machine-wide config
and specific some System 11 options. At this point you might be
wondering, "Why aren't these options in the snux section?" The reason
is that the settings in the snux section apply to the Snux board
itself, whereas the settings in this system11 section apply to any
System 11 machine that MPF might control. Of course at this point,
that's only possible via the Snux board, but they're technically
separate settings since the architecture allows for future System 11
boards that may exist at some point.  Here's the system11
configuration section from Pin*Bot:


.. code-block:: mpf-config

    system11:
      ac_relay_delay_ms: 75
      ac_relay_driver_number: c14

The *ac_relay_delay_ms* is the number of milliseconds MPF waits before
and after flipping the A/C select relay to allow for it to fully
switch positions. For example, if you have a C-side driver active and
you need to activate an A-side driver, MPF cannot simply deactivate
the A/C relay and the C-side device and activate the A-side device all
at the same time. If it does then power will "leak" from one side to
the other as the relay is transitioning. So what actually happens in
this scenario is that MPF will deactivate the C-side devices, then
wait 75ms for them to really be "off", then deactivate the A/C relay,
then wait another 75ms for the relay to flip, then activate the A-side
device. We did some experimentation with different delay times. On
Pin*Bot, 50ms was definitely too short as we'd see some weak flashes
from C-side flashers connected to A-side devices we were activating on
the transition. 75ms seems fine, though really this is all faster than
humans can perceive (and C-side devices aren't as time sensitive), so
even setting this to 100ms is probably fine. 75ms is the default if
you don't add this section to your config. The
*ac_relay_driver_number* is the driver (with a "C" added to it) from
the manual for the A/C select relay. Be sure you check the A/C relay
driver number from your manual. It's different in the two System 11
machines we tested. (C14 in *Pin*Bot* and C12 in *Jokerz!*) Also it's
labeled differently in different manuals. In the *Jokerz!* manual it's
called the "A/C Select Relay," and in the *Pin*Bot* manual it's called
the "Solenoid Select Relay."


4. Enable flippers
^^^^^^^^^^^^^^^^^^

The Snux board uses driver 23 to enable the flippers:

.. code-block:: mpf-config

   digital_outputs:
     flipper_enable_relay:
       number: c23
       type: driver
       enable_events: ball_started
       disable_events: ball_will_end

You can change the events when the flipper should enable and disable.
By default we will enable the flippers on ball start and disable them on
ball end.

5. Configuring driver numbers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: /hardware/voltages_and_power/common_ground_warning.rst

When you configure coils, flashers, and gis in your MPF hardware
config, you can enter the numbers straight out of the operators
manual. The only thing to note here is that you must add a "C" to the
beginning of the driver number (even for flashers and GI), since
that's what triggers MPF to do a WPC-style lookup to convert the
driver number to the internal hardware number the platform uses. (It's
an WPC-style lookup since the Snux driver board emulates a WPC driver
board.) Also for switched solenoids which use the A/C relay, you also
need to add an "A" or a "C" to the end of the driver number. Here's a
snippet (incomplete) from the *Pin*Bot* machine-wide config file:


.. code-block:: mpf-config

    coils:
      outhole:
        number: c01a
      knocker:
        number: c01c
      trough:
        number: c02a
      visor_motor:
        number: c13
        allow_enable: true
      upper_pf_and_topper_1:
        number: c02c
      left_insert_bottom:
        number: c03c
      right_insert_bottom:
        number: c04c
      lower_pf_and_topper_2:
        number: c05c
      energy:
        number: c06c
      left_playfield:
        number: c07c
      sun:
        number: c08c
      robot_face_insert_bottom:
        number: c09
      topper_3:
        number: c15
      topper_4:
        number: c16

Again, don't forgot the "a" or the "c" at the end of the switched
solenoids, since that's how MPF knows it needs to use the A/C relay
logic for those devices!



6. Configure lamps
^^^^^^^^^^^^^^^^^^

Configuring the numbers for matrix lamps is pretty straightforward and
something you can also use the manual for. The format for lamp number
is the letter "L" followed by the column, then the row. In other
words, light number L25 is the light in column 2, row 5. This is a bit
confusing because these are not the numbers that the lamps use in the
manual! The lights in the lamp matrix table are simply numbered from 1
to 64. So you need to use the chart in the manual to get the column
and row positions, not to get the actual light numbers! (When Williams
switched to WPC, they switched to lamp numbers based on the column and
row. So in WPC machines, the lamps in column 1 are numbers 11-18, the
lamps in column 2 are 21-28, etc. System 11 numbers would be 1-8 for
column 1, 9-16 for column 2, etc. Basically since System 11 machines
have an 8x8 lamp matrix, there should be no numbers 9 or 0 anywhere in
your lamp numbers. Here's a snippet of the configuration from Pin*Bot:


.. code-block:: mpf-config

    lights:
      game_over_backbox:
        number: L11
      match_backbox:
        number: L12
      bip_backbox:
        number: L13
      mouth1_backbox:
        number: L14
      mouth2_backbox:
        number: L15
      mouth3_backbox:
        number: L16
      mouth4_backbox:
        number: L17
      mouth5_backbox:
        number: L18
      bonus_2x:
        number: L21
      bonus_3x:
        number: L22

Again, don't forget that they should all start with "L", and they're
based on the positions in the matrix, not on the numbers from the
manual.



7. Configure switches
^^^^^^^^^^^^^^^^^^^^^

Switch numbering in System 11 machines is the same as lamp numbering,
except the numbers start with "S". Again the numeric portion of the
number is based on the column/row, not the switch number in the
manual. So even though the manual says that the switch in column 5,
row 6 is number 38, you actually enter "L56". Here's another snippet
from *Pin*Bot*:


.. code-block:: mpf-config

   switches:
     left_outlane:
       number: S24
       label: Left Outlane
       tags: playfield_active
     left_inlane:
       number: S25
       label: Left Inlane
       tags: playfield_active
     right_inlane:
       number: S26
       label: Right Inlane
       tags: playfield_active
     right_outlane:
       number: S27
       label: Right Outlane
       tags: playfield_active

You might have to do some detective work to figure out where the
switches are and how they work. For example, remember that switches
from slingshots or pop bumpers are most likely activated by the
physical action of the device's coil, not by the switch above the
playfield. So on Pin*Bot hitting the pop bumper skirt does not
activate the pop bumper switch, but manually pushing the pop bumper
ring down with your fingers will activate that switch. Also you might
see switches with names along the lines of "Right Lane Change." If the
lane change in that machine is activated by a slingshot, then most
likely the Right Lane Change switch is under the playfield and
activated by the physical slingshot arm hitting it. Same for flipper-
controlled lane changes. You'll have to hunt to see whether there's a
second switch in the flipper EOS stack under the playfield or perhaps
a second switch in the stack behind the flipper button.


8. Create your System 11-style trough
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Troughs in System 11 machines are not like troughs in modern machines.
Rather than a single ball device which acts as the drain as well as
the feeder to the plunger lane, System 11 machines have two separate
devices with two solenoids. One device is typically called the
"outhole" (or "drain") which receives the ball from the playfield, and
it kicks the ball over to the trough where the ball is stored. Then
the trough has a second coil which kicks the ball into the plunger
lane when it needs it. We have a separate How To guide which details how to setup a System 11 1980s-
style trough, link below (since many games do this, even ones that aren't System
11), so you can read that for more details. The result though will
look something like this:


.. code-block:: mpf-config

   #! switches:
   #!   outhole:
   #!     number: 1
   #!   trough1:
   #!     number: 2
   #!   trough2:
   #!     number: 3
   #!   plunger_lane:
   #!     number: 4
   #! coils:
   #!   outhole:
   #!     number: 1
   #!   trough:
   #!     number: 2
   ball_devices:
     outhole:
       ball_switches: outhole
       eject_coil: outhole
       confirm_eject_type: target
       eject_targets: trough
       tags: drain
     trough:
       ball_switches: trough1, trough2
       eject_coil: trough
       eject_targets: plunger_lane
       tags: home, trough
     plunger_lane:
       ball_switches: plunger_lane
       mechanical_eject: true
       eject_timeouts: 3s

The key is that you're setting up a "chain" of devices (from *outhole*
to *trough* to *plunger lane*), and you're breaking up the special
tags so that each device is tagged with it's exact role. (And hey! Now
you know why these are all separate tags in MPF instead of a single
tag called "trough".)

See :doc:`Setting up a System 11 Style Trough </mechs/troughs/two_coil_multiple_switches>` for details.


(E) Final Steps and additional information
------------------------------------------

MPF's System 11 interface is new, and we haven't yet built a complete
game using it. There are most likely things that we haven't thought of
yet, so if you're using MPF with a System 11 machine, please post to
the forum if you find anything that's weird or that doesn't work as
expected.

`Snux on Pinside <https://pinside.com/pinball/community/pinsiders/snux>`_.


This is an example code block with the main Sys11 elements in.

.. code-block:: mpf-config

   hardware:
     platform: virtual
     driverboards: wpc
     coils: snux
     switches: snux

   system11:
     ac_relay_delay_ms: 75
     ac_relay_driver: c_ac_relay

   snux:
     diag_led_driver: c_diag_led_driver

   digital_outputs:
     flipper_enable_relay:
       number: c23
       type: driver
       enable_events: ball_started
       disable_events: ball_will_end

   coils:
     c_diag_led_driver:
       number: c24
       default_hold_power: 1.0
     c_ac_relay:
       number: c25
       default_hold_power: 1.0
     c_side_a1:
       number: c11a
     c_side_a2:
       number: c12a
       default_hold_power: 0.5
     c_side_c1:
       number: c11c
     c_side_c2:
       number: c12c
       default_hold_power: 0.5

What if it did not work?
------------------------

Have a look at our :doc:`hardware troubleshooting guide </hardware/troubleshooting_hardware>`.
