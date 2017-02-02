Controlling an existing machine with MPF
========================================

If you want to use MPF to write your own custom game code for an *existing*
Williams or Stern pinball machine, you replace the original CPU board in the
machine with a modern pinball controller board (called a *hardware controller*)
such as a P-ROC or FAST Controller. That hardware
controller interfaces with the existing machine's driver boards to control the
coils, lights, and DMD, and it provides a "bridge" (via USB) to a host
computer running Python and the Mission Pinball Framework.

============================= ===== ==== ======
Machine Type                  P-ROC FAST Direct
============================= ===== ==== ======
Williams / Bally / Midway WPC X     X
Williams / Bally System 11    X     X
Data East                     X     X
Stern S.A.M.                  X
Stern Whitestar               X
Stern SPIKE / SPIKE 2                    X
============================= ===== ==== ======

Notes:

* "WPC" includes WPC-S and WPC-95, and machines made under the brands of
  Williams, Bally, and Midway. (A complete WPC game list is
  `here <http://www.pinwiki.com/wiki/index.php?title=Williams_WPC#Game_List>`_.)
* System 11 and Data East machines require the "Snux" replacement driver board in
  addition to the P-ROC or FAST controller.
* Since Stern SPIKE systems have a linux-based computer inside them already, MPF
  can directly connect to and control them via USB. No additional hardware is needed.

If you want to use MPF with an existing machine type that's not on the list above,
that's still possible, but you'd have to rewire the entire machine and use modern
control hardware. In other words, you strip the guts and keep all the hardware, and
the machine essentially becomes a home-brew machine on the inside and a retheme or
update on the outside.
