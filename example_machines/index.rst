Example Machine Projects you can learn from
===========================================

The mpf-examples project
------------------------

This repo doesn't have an installer,
rather, you just download it and start using the examples it contains.

Each software repository in GitHub has several "branches". (Think of these
kind of like versions.) The mpf-examples repository has branches that
match the version of MPF. For example, the 0.21 branch of the mpf-examples
repository has examples for MPF 0.21, the 0.30 branch has examples for
MPF 0.30, etc.

Since the documentation you're reading here is for MPF |version|, download
a zip file of the 0.31 branch of MPF examples here:
`here <https://github.com/missionpinball/mpf-examples/archive/0.31.zip>`_.

Unzip the file to any location you want. It doesn't have
to be in the same folder as MPF. (In fact when you installed MPF, it
was installed to some system folder that you probably can't even find.
So for these example files, just put them somewhere easy.)

Download the version that matches your version of MPF:

* 0.21.x <https://github.com/missionpinball/mpf-examples/archive/0.21.zip>`_.
* 0.30.x <https://github.com/missionpinball/mpf-examples/archive/0.30.zip>`_.
* 0.31.x <https://github.com/missionpinball/mpf-examples/archive/0.31.zip>`_.
* 0.32.x <https://github.com/missionpinball/mpf-examples/archive/0.32.x.zip>`_.
* dev <https://github.com/missionpinball/mpf-examples/archive/dev.zip>`_.

``aztec``

   Aztec machine rewired for FAST Pinball contoll system

``big_shot``

   1974 Gottlieb Big Shot, rewired for a P-ROC with PD-16 and PD-8x8 driver boards. We showed off this machine at
   the Chicago Pinball Expo in 2013. It's cool because it still uses the original score reels and stuff, and you
   can't really tell that it's running MPF from the outside.

``bullseye``

   A Game Plan Bullseye 301 that has been completely rewired and connected to a FAST Pinball controller


``demo_man``

   Williams Demolition Man. This config is pretty basic, but you can play complete games and it has some simple shots,
   scoring, and modes. It also contains custom code to run the Cryro Claw.

``hurricane``

   Williams Hurricane. This config is very basic, essentially just the hardware and device mappings.

``indy``

   Williams Indiana Jones: The Pinball Adventure. This config is very basic, essentially just the hardware and device mappings.

``jd``

   Williams Judge Dredd. This config is very basic, essentially just the hardware and device mappings.

``jokerz``

   Williams Jokerz, written for a P-ROC using a Snux System 11 driver board.

``mc_demo``

   A standalone demo config you can look at for various MPF-MC (Media Controller) examples. You can run this without
   the MPF game engine—just switch to the ``mc_demo`` folder and run ``mpf mc``.

``pinbot``

   Williams Pin*Bot, written for a P-ROC using a Snux System 11 driver board.

``sega_space_shuttle``

   A Sega Space Shuttle that has been completely rewired and connected to a FAST Pinball controller.

``stle``

   A Stern Star Trek machine, using a P-ROC along with the original driver boards. The LEDs do not work in this
   config (since the P-ROC in a Stern SAM system does not support the Stern RGB LEDs).

``sttng``

   A Williams Star Trek: The Next Generation machine. This config is pretty basic, but the hardware and devices are
   complete.

``tutorial`` (and several ``tutorial_step_XX`` folders)

   Contains the config files used in the :doc:`/tutorial/index`.

``wpc_template``

   A template config you can use for WPC machines (with either a P-ROC or FAST WPC controller).

Brooks 'n Dunn
--------------

One of the projects we took on in 2015 was to rewire and build and MPF config for Gottlieb's Brooks 'n Dunn. (BnD).
BnD was the machine that Gottlieb was working on when they shut down in 1996.

This config is probably the most complete of any MPF project that's publicly available. However it contains lots of
licensed assets (music, videos, images, etc.) that are not in the public repo. This means you won't be able to
actually run it, but you can look through the configs (which are well commented) to see how we do things.

The BnD repo is at https://github.com/gabeknuth/bnd
