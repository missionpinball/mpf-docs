Controlling an existing machine with MPF
========================================

If you want to use MPF to write your own custom game code for an *existing*
Williams or Stern pinball machine, you replace the original CPU board in the
machine with a modern pinball controller board (called a *hardware controller*)
such as a :doc:`P-ROC</hardware/multimorphic/index>` Controller (but not P3-Roc).
That hardware
controller interfaces with the existing machine's driver boards to control the
coils, lights, and DMD, and it provides a "bridge" (via USB) to a host
computer running Python and the Mission Pinball Framework.

==================================================================================================== ===== ==== === ======
Machine Type                                                                                         P-ROC LISY APC Direct
==================================================================================================== ===== ==== === ======
:doc:`Williams / Bally / Midway WPC </hardware/existing_machines/wpc>`                               X     X
:doc:`Williams / Bally System 11 </hardware/existing_machines/system11>`                             X          X
:doc:`Data East </hardware/existing_machines/data_east>`                                             X
:doc:`Stern S.A.M. </hardware/existing_machines/sam>`                                                X
:doc:`Stern Whitestar </hardware/existing_machines/whitestar>`                                       X
:doc:`Pinball 2000 </hardware/existing_machines/pinball2000>`                                        X
:doc:`Stern SPIKE / SPIKE 2  </hardware/existing_machines/spike>`                                                   X
:doc:`Gottlieb System 1 </hardware/existing_machines/gottlieb_system1>`                                    X
:doc:`Gottlieb System 80 </hardware/existing_machines/gottlieb_system80>`                                  X
:doc:`Bally/Stern w/ AS-2518-17 or AS-2518-35 MPU </hardware/existing_machines/bally_stern_as_2518>`       X
==================================================================================================== ===== ==== === ======

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
* Bally and Stern Games manufactured from 1977 to 1985 with MPU AS-2518-17 or
  AS-2518-35 can be controlled using :doc:`LISY35 </hardware/lisy/index>`

If you want to use MPF with an existing machine type that's not on the list above,
that's still possible, but you'd have to rewire the entire machine and use modern
control hardware. In other words, you strip the guts and keep all the hardware, and
the machine essentially becomes a home-brew machine on the inside and a retheme or
update on the outside. However, there might be an alternative not listed here so
we recommend you to ask in our :doc:`user forum</faq/help/index>`.
