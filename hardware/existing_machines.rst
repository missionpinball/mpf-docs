Controlling an existing machine with MPF
========================================

If you want to use the MPF to write software for a real pinball machine, you
need some way to get your code onto the machine. Unfortunately you can't just
"install" MPF on a pinball machine. Most existing machines don't have normal
computers controlling them, rather, they're based on custom-built control
systems which run code compiled specifically for each platform.

Plus, a lot of pinball machines are old, meaning their hardware is weak by
today's standards. (For example, all those mid-90s Williams WPC games that we
love are powered by a Motorola 6809 CPU running at 2 MHz with 64 KB of RAM.
(Yeah, that's 64 *kilo* bytes, not megabytes.) So you're not getting the Mission
Pinball Framework on there.

(As a side note, if you want to write software which runs on the original 6809
Williams hardware, check out Brian Dominy's `FreeWPC project <http://freewpc.googlecode.com>`_.
You can use FreeWPC to write new game code in C++, compile it for the 6809, burn
it to a ROM chip, and replace your existing machine ROMs with your custom ones.
Crazy! And awesome!)

If you want to use MPF to write your own custom game code for an *existing*
Williams or Stern pinball machine, you replace the originalCPU board in the
machine with a modern pinball controller board (called a *hardware controller*)
such as a P-ROC or FAST Controller. That hardware
controller interfaces with the existing machine'sdriver boards to control the
coils, lights, and DMD, and it provides a "bridge" (via USB) to a host
computer running Python and the Mission Pinball Framework.

=============================       =====            ====
Machine Type                        P-ROC            FAST
=============================       =====            ====
Williams / Bally / Midway WPC       X                X
Williams / Bally System 11          X                X
Data East                           X                X
Stern S.A.M.                        X
Stern Whitestar                     X
==============================      =====            ====

See the :doc:`/howto/installation/wpc` guide for details for WPC machines. We'll
publish guides for the other types of machines soon.

Notes:

* "WPC" includes WPC-S and WPC-95, and machines made under the brands of
  Williams, Bally, and Midway. (A complete WPC game list is
  `here <http://www.pinwiki.com/wiki/index.php?title=Williams_WPC#Game_List>`_.)
* System 11 and Data East machines require the "Snux" replacement driver board.
