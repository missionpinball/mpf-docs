
MPF supports coils (also called solenoids or drivers). There are
several actions you can perform on coils, including:


+ Pulse: A predefined 'pulse' of a certain number of milliseconds is
  sent to the coil. This is how most coils in pinball machines work,
  including slingshots, pop bumpers, the trough eject coil, ball
  poppers, drop target reset and knockdown coils, ball launch plungers,
  etc. Pulses can be from 1 to 255 milliseconds.
+ Enable: A coil is enabled (i.e. held in the "on") position. This is
  used for some types of coils that are designed to be held on, such as
  the flipper "hold" windings as well as certain diverters and coil-
  controlled gates. Note that you should never "enable" a coil that
  isn't designed to be enabled. If you just turn on a regular coil and
  hold it on, it will overheat and burn out. So make sure you only
  enable coils that are meant to be enabled. (In fact to protect against
  this, you have to specifically configure an "allow enable" setting for
  each coil you want to enable. We put this into MPF as a safety
  precaution to make sure you don't accidentally enable a coil that
  isn't designed for it.
+ Timed Enable: This is like a pulse that lasts longer than 255ms.
  It's useful for things like diverters (where you may want them to
  enable for a few seconds at a time). Under the hood this actually
  implements an *enable* command with a delay scheduled to automatically
  disable the device when the time ends.
+ Disable: This is simple. It just disables (i.e. "turns off" a coil)




Configuring your coils
----------------------

Coilsare configured in the ` `coils:` section`_of the machine
configuration file.



Step-by-step tutorial for coils
-------------------------------

The step-by-step tutorial covers coils in the following sections:
`Step 4. Get flipping!`_

.. _ section: https://missionpinball.com/docs/configuration-file-reference/coils/
.. _Step 4. Get flipping!: https://missionpinball.com/docs/tutorial/get-flipping/


