Adjust coil hold power
======================

In MPF, a coil is said to be "held" (or "enabled") any time it's activated for
more than 255ms (since 255ms is the maximum pulse time for most platforms).

Most coils are only used in the "pulse" mode (slingshots, pop bumpers, trough
and ball device ejects, etc.).

However, some pinball devices need to hold a coil on for longer (flippers,
diverters, some older types of trough ball releases, etc.).

In MPF, you can adjust the power that's applied when these coils are held on
past their initial pulse point.

Single-wound versus dual-wound coil holds
-----------------------------------------

The way you configure coil holds depends on whether the coil in question is
a "single wound" or "dual wound" coil. See the
:doc:`dual_vs_single_wound` guide for details.

Adjusting single-wound coil "hold" strength
-------------------------------------------

Coils in MPF have a ``default_hold_power:`` setting which is used to control the
amount of power that's applied to the coil after the initial pulse time.

The default_hold_power setting is a value from 0.0-1.0, with 0 being 0% power
(off), and 1.0 being 100% power.

Consider the following example:

.. code-block:: mpf-config

   coils:
      some_coil:
         number:
         default_pulse_ms: 30
         default_hold_power: 0.250

In the example from a machine config file, the if the coil called
*some_coil* is enabled (turned on) then that coil will receive full (100%)
power for 30ms, and then after 30ms, the power drops down to 25%. The power will
stay at 25% until the coil is turned off.

Note that the pinball control hardware cannot vary the voltage or current
applied to a coil, rather it simulates lower power by rapidly pulsing the
power. The example of ``default_hold_power: 0.250`` would equate to 25% power,
which would mean the coil would get full power for 1ms, then it would get no
power for 3ms, then full power for 1ms, etc (details vary per platform).

The default_hold_power: setting is valid with every type of pinball control
system that MPF supports. However, some control systems have additional options
which you can use to fine-tune how the hold power is applied to a coil.

See the :doc:`hardware documentation for your platform </hardware/index>` for
links to specific coil settings your hardware might allow.

The big question is what default_hold_power: setting is appropriate for your
scenario? Unfortunately we don't have any good guidance for
what your default_hold_power: values should be. Really you can just start
with a value of 0.1 or 0.2 and then keep increasing it until your holds are
strong enough not to break their hold when a ball hits them.

Adjusting dual-wound coil "hold" strength
-----------------------------------------

If you have dual-wound coils then, the hold winding is designed to be held on,
for long periods of time so you can safely keep it on full strength solid and
don't have to mess with default_hold_power: settings.

The important caveat there is that the hold windings are designed around
certain voltages. So if you have a dual-wound coil from a Stern machine that
was designed to run at 48v, and you're using it in a new machine that's running
at 70v, you'd probably want to use a default_hold_power: setting that's lower.

Again, you'll need to play with the settings to see what makes sense, and always
choose the lowest one that works since if you have a setting that's too high,
you probably won't know it until it's too late and the coil has burned up.
