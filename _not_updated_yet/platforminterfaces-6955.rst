
The Mission Pinball Framework is "platform agnostic," meaning it can
be used to control pinball machines via several different hardware
pinball controllers, including:


+ FAST Pinball Nano Controller
+ FAST Pinball Core Controller
+ FAST Pinball WPC Controller
+ Multimorphic P-ROC
+ Multimorphic P3-ROC
+ Mark Sunnuck's (Snux) System 11 interface board


MPF can also directly control other types of hardware devices,
including:


+ Fadecandy (an option to control RGB LEDs)
+ OpenPixel Control hardware (for RGB LEDs and DMX lighting)
+ SmartMatrix controllers (for RGB LED matrix-based displays)


We'll continue to add support for future platforms as the needs arise.
(Most likely the open source Open Pinball Project (OPP) controllers
will be next, though in theory MPF can talk to just about anything.)
Control of each of these different types of hardware is done via a
platform interface (found in the *mpf/platform* folder) and is
completely transparent to you. Often times switching hardware
platforms is as simple as making a few lines of changes in your
configuration files and MPF does the rest. MPF can communicate with
multiple platforms at the same time. For example, you might use a
P-ROC to control your switches and coils, a FadeCandy to control RGB
LEDs, and a SmartMatrix controller to control a color RGB LED DMD. You
can do this all at the same time and that's fine. MPF's platform
interfaces contain the "low-level" driver code from the various
hardware makers which is translated back-and-forth to a format that
MPF can use. For example, pulsing driver #20 for 30 milliseconds via a
P-ROC requires a Python command that looks like this:


::

    
    self.proc.driver_pulse(20, 30)


On a FAST pinball controller, the same command is done by sending the
following string to a virtual serial port:


::

    
    DN:14,89,00,10,1e,ff,00,00


Don't be mislead by the apparent complexity of the FAST interface. The
FAST interface includes all the settings, including pulse strength and
recycle time, in a single command, whereas the P-ROC uses separate
commands for each. The point is that we read and understand all the
details of the hardware interfaces so you don't have to. :)



