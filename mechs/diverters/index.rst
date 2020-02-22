Diverters
=========

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/diverters`                                                     |
+------------------------------------------------------------------------------+

.. contents::
   :local:

In MPF, a diverter (sometimes spelled "divertor") is anything that alters
the path of the ball based on the state it's in, including:

.. image:: /mechs/images/diverter1.jpg
.. image:: /mechs/images/diverter2.jpg

+ A traditional diverter which is a metal flap at the end of a rod,
  typically used on ramps to "divert" the ball one way or the other.
+ A coil-controlled post that pops up (or down) to let the ball either
  pass over it or bounce back in some other direction. (This is
  sometimes called an "up/down" post.)
+ A coil-controlled gate, typically which only allows the ball to flow
  through it in a single direction, but lifted out of the way via a coil
  when active which allows the ball to travel through it in both
  directions.
+ A "trap door" pop-up which captures the ball when it's up but lets
  the ball roll over it to another shot when it's down. (Like the trap
  door / basement in Theatre of Magic.)
+ A single drop target that blocks the entrance to a shot when it's up,
  such as in the back of the saucer in Attack from Mars or the ones that
  block the ramps in Ghostbusters.
+ Something else completely custom, such as the Ringmaster in Cirqus
  Voltaire. (When it's up the ball can hit it and drop down under the
  playfield, and when it's down the ball rolls over it and hits standup
  targets behind it.)

At this point you might be thinking, "Wait, you consider a trap door
or the Ringmaster to be a diverter?? What???" But if you think about it
from the perspective of pinball software, yeah, trap doors and the
Ringmaster *are* diverters because when then are not active, a ball
shot to them goes towards one place, and when they're active, a ball is
"diverted" to go somewhere else.

.. note::

    MPF's diverters are integrated with :doc:`/mechs/ball_devices/index` and MPF's
    ball management and routing system so they can be used to ensure that MPF is
    able to move balls to where they need to be.

Most diverters are held in their "on"
position as long as their driver coil enabled, and then when they're
disabled they return back to their off position. That said, some are
different. The Ringmaster has a motor which raises and lowers it, and drop
targets have coils that are just pulsed to raise/lower them, so this is not
a hard and fast rule.

So based on all that, let's look
at how the MPF actually handles diverters. At the most basic level,
most diverters are just a coil, so fundamentally we don't really need
to do anything special to control a diverter. As a game programmer you
just need to enable a coil. But if you want to program your game code
to control a diverter, there's a lot of glue you need to fully
integrate it into your machine, and that's the glue that we've pre-
written into our diverter device code.

For example, many diverters
attached to ramps do not hold their coils in the "on" position for the
entire time that they're on. Instead they use the ramp entry switch to
see when a ball is coming their way, and when one is they quickly
activate so they can catch the ball in time to divert it. They also
typically have a timeout where they deactivate themselves if they
don't actually see a ball get diverted, (like with a weak ramp shot
that trips the ramp entry switch but that isn't powerful enough to
make it all the way up the ramp to the diverter.)

MPF's diverter devices
also include support for automatic enabling and disabling (based on
events), and they include intelligence to know which target devices a
diverter will send a ball to when it's enabled or disabled.

Monitorable Properties
----------------------

For :doc:`dynamic values </config/instructions/dynamic_values>` and
:doc:`conditional events </events/overview/conditional>`,
the prefix for diverters is ``device.diverters.<name>``.

*active*
   Boolean (true/false) as to whether this diverter is actively on and
   in the powered state.

*enabled*
   Boolean (true/false) as to whether this diverter is enabled (meaning
   it will be activated when a ball approaches it).

*eject_state*
   Boolean (true/false) which shows whether this diverter will be activating
   to route a ball eject from an upstream ball device.

Related How To guides
---------------------

Dual Coil Diverter Example:
   In this example we use a standard flipper mechanism with a dual wound coil as a diverter. Much like a flipper, we'll want to control the main coil for enabling the diverter, and then the hold coil to hold it in the active position for as long as you need. 
   
First we need to define the coils in our hardware section: 

coils:
   c_diverter_upper_right_main:
        number: 25
        default_pulse_ms: 4
        default_hold_power: 0.2
   c_diverter_upper_right_hold:
        number: 26
        allow_enable: true

        
Next we'll define the dual wound coil for the diverter to use:

dual_wound_coils:
    c_diverter_dualcoil:
        hold_coil: c_diverter_upper_right_hold
        main_coil: c_diverter_upper_right_main

Then we define the Diverter itself:

diverters:
    ramp_diverter:
        activation_coil: c_diverter_dualcoil
        type: hold
        activation_time: .5s
        activation_switches: s_r_rampexit, s_l_rampexit
        enable_events: ball_started
        disable_events: ball_ended
        
        
 * :doc:`up_down_ramps`

Related Events
--------------

.. include:: /events/include_diverters.rst


.. toctree::

   up_down_ramps
   servo_as_diverter
   stepper_as_diverter
