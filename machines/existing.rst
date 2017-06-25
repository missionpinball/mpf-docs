Controlling an existing machine with MPF
========================================

If you want to use MPF to write your own custom game code for an *existing*
Williams or Stern pinball machine, you replace the original CPU board in the
machine with a modern pinball controller board (called a *hardware controller*)
such as a :doc:`P-ROC</hardware/multimorphic/index>` or :doc:`FAST</hardware/fast/index>` Controller. That hardware
controller interfaces with the existing machine's driver boards to control the
coils, lights, and DMD, and it provides a "bridge" (via USB) to a host
computer running Python and the Mission Pinball Framework.

============================= ===== ==== ==== ======
Machine Type                  P-ROC FAST LISY Direct
============================= ===== ==== ==== ======
Williams / Bally / Midway WPC X     X
Williams / Bally System 11    X     X
Data East                     X     X
Stern S.A.M.                  X
Stern Whitestar               X
Stern SPIKE / SPIKE 2                         X
Gottlieb System 1                        X
Gottlieb System 80                       X
============================= ===== ==== ==== ======

Notes:

* "WPC" includes WPC-S and WPC-95, and machines made under the brands of
  Williams, Bally, and Midway. (A complete WPC game list is
  `here <http://www.pinwiki.com/wiki/index.php?title=Williams_WPC#Game_List>`_.)
* System 11 and Data East machines require the ":doc:`Snux</hardware/snux/index>`" replacement driver board in
  addition to the P-ROC or FAST controller.
* Since Stern SPIKE systems have a linux-based computer inside them already, so
  :doc:`MPF can directly connect to and control them via USB</hardware/spike/index>`.
  No additional hardware is needed.
* Gottlieb System 1 and 80 can be controlled using the
  :doc:`LISY platform</hardware/lisy/index>`

If you want to use MPF with an existing machine type that's not on the list above,
that's still possible, but you'd have to rewire the entire machine and use modern
control hardware. In other words, you strip the guts and keep all the hardware, and
the machine essentially becomes a home-brew machine on the inside and a retheme or
update on the outside. However, there might be an alternative not listed here so
we recommend you to ask in our :doc:`user forum</faq/help/index>`.
