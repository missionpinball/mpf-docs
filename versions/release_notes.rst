MPF Release Notes
=================
Here's the history of the various release versions and changes of the Mission
Pinball Framework. (Patch releases and bug fixes are not included in this list.)

0.52
----

Released: February 02, 2019

This is a 0.51 maintenance release with cleanups and some refactorings.
There should not be any breaking changes but a lot of bug fixes.

.. rubric:: MPF

New Features
^^^^^^^^^^^^

-  `OSC platform to control external lights <https://github.com/missionpinball/mpf/pull/1260>`__ - jab based on `request in forum <https://groups.google.com/forum/#!topic/mpf-users/8JZbb_X__Rc>`__
-  `Validate variables in variable\_player <https://github.com/missionpinball/mpf/pull/1261>`__ - jab based on `config in example <https://groups.google.com/forum/#!topic/mpf-users/v4b75FEQU70>`__
-  `Placeholders for shots and shot\_groups <https://github.com/missionpinball/mpf/pull/1262>`__ - jab based on `question from mike wiz <https://groups.google.com/forum/#!topic/mpf-users/_EBF2tkfabI>`__
-  `Better error messages for placeholders <https://github.com/missionpinball/mpf/commit/418b210e0e2bf847dcd66dbec5950d277828080c>`__ - jab
-  `Show proper error when fadecandy server is not running <https://github.com/missionpinball/mpf/pull/1263>`__ - jab based on request from Brian Cox
-  `Nicer output on startup errors <https://github.com/missionpinball/mpf/commit/55f449407d832e0bfa6f3403c19a3572ea621ee2>`__ - jab
-  `Show shutdown reason on exit of MPF <https://github.com/missionpinball/mpf/pull/1265>`__ - jab
-  `Show import error for pinproc <https://github.com/missionpinball/mpf/pull/1267>`__ - jab
-  `Upstream Raspberry Pi DMD support <https://github.com/missionpinball/mpf/pull/1269>`__ - jab based on `external platform from Michael Betz <https://github.com/yetifrisstlama/Fan-Tas-Tic-platform>`__
-  `Support for Spike Trough via SPI Bit Bang <https://github.com/missionpinball/mpf/pull/1270>`__ - jab
-  `Move libpinproc to a separate thread <https://github.com/missionpinball/mpf/pull/1195>`__ - jab
-  `Score Queues for SS style scoring <https://github.com/missionpinball/mpf/pull/1273>`__ - jab based on `request in forum <https://groups.google.com/forum/#!topic/mpf-users/4Ecj6xtveHo>`__
-  `Check for OPP firmware mismatch on start <https://github.com/missionpinball/mpf/pull/1276>`__ - jab based on `bug report in forum <https://groups.google.com/forum/#!topic/mpf-users/umg2ZmDElog>`__
-  `Evaluate placeholders from service cli <https://github.com/missionpinball/mpf/pull/1277>`__ - jab
-  `Improve USB latency for I2C in pypinproc <https://github.com/missionpinball/pypinproc/pull/5>`__ - jab based on suggestion by rosh
-  `Only enable AC relay by default during the game. Keep it off in attract <https://github.com/missionpinball/mpf/pull/1289>`__ - snux
-  `Ball Routing device to route balls to certain devices <https://github.com/missionpinball/mpf/pull/1291>`__ - jab
-  `Support for the Pololu Tic stepper controller <https://github.com/missionpinball/mpf/pull/1293>`__ - wolfmarsh
-  `Update Smartmatrix Teensy Code Example for New Cookie <https://github.com/missionpinball/mpf/pull/1295>`__ - aaronmatthies and eli
-  `Placeholders in event\_player based on event parameters <https://github.com/missionpinball/mpf/pull/1297>`__ - avanwinkle
-  `Update ruamel yaml parser <https://github.com/missionpinball/mpf/pull/1298>`__ - jab
-  `Use newer cython to support Python 3.7 <https://github.com/missionpinball/mpf-debian-installer/commit/532d8757c078ef568b6a9d3473a1db63d35e84ef>`__ - jab
-  `Add Python 3.7 support to MPF <https://github.com/missionpinball/mpf/pull/1300>`__ - jab

Bug fixes & code improvements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  `Fix audio problems <https://github.com/missionpinball/mpf-mc/commit/7751cef626cae7fe0eeba2c4138f7ab6bb7d8982>`__ - jab (based on `0.50 fix <https://github.com/missionpinball/mpf-mc/commit/e9d7f3aac92489ba8f987807aad5584938d77891#diff-b1084838e78cf0dc54bddd5026e1f747>`__)
-  `Fix name clashes between multiple anonymous slides <https://github.com/missionpinball/mpf-mc/pull/359>`__ - jab based on bug report by pinballpeople
-  `Properly support external platforms in MC <https://github.com/missionpinball/mpf-mc/pull/361>`__ - jab based on `report by TheLegoMoviePinball <https://groups.google.com/forum/#!topic/mpf-users/okl8PjXrlWI>`__
-  `Honour -a and -A option when loading config\_spec in MPF <https://github.com/missionpinball/mpf/pull/1280>`__ and `MC <https://github.com/missionpinball/mpf-mc/pull/362>`__ - jab based on `report by TheLegoMoviePinball <https://groups.google.com/forum/#!topic/mpf-users/okl8PjXrlWI>`__
-  `Honour slide parameter in inactive slides <https://github.com/missionpinball/mpf-mc/pull/363>`__ - avanwinkle
-  `Fix iMC startup crash <https://github.com/missionpinball/mpf-mc/pull/364>`__ - jab based on `report by snux <https://groups.google.com/forum/#!topic/mpf-users/YLrh6RKlx0s>`__
-  `Remove use\_sound\_setting from default options <https://github.com/missionpinball/mpf-mc/pull/367>`__ - avanwinkle

.. rubric:: MPF-MC

New Features
^^^^^^^^^^^^

-  `Add a segment display font <https://github.com/missionpinball/mpf-mc/commit/0dadad10eeaf01188e92016c90006ebb8b5b5933>`__ - jab based on `example from BorgDog <https://groups.google.com/forum/#!topic/mpf-users/1wzjCo5pL0U>`__
-  `Conditionals on add\_to\_slide animations <https://github.com/missionpinball/mpf-mc/pull/357>`__ - avanwinkle

Bug fixes & code improvements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  `Fix audio problems <https://github.com/missionpinball/mpf-mc/commit/7751cef626cae7fe0eeba2c4138f7ab6bb7d8982>`__ - jab (based on `0.50 fix <https://github.com/missionpinball/mpf-mc/commit/e9d7f3aac92489ba8f987807aad5584938d77891#diff-b1084838e78cf0dc54bddd5026e1f747>`__)
-  `Fix name clashes between multiple anonymous slides <https://github.com/missionpinball/mpf-mc/pull/359>`__ - jab based on bug report by pinballpeople
-  `Properly support external platforms in MC <https://github.com/missionpinball/mpf-mc/pull/361>`__ - jab based on `report by TheLegoMoviePinball <https://groups.google.com/forum/#!topic/mpf-users/okl8PjXrlWI>`__
-  `Honour -a and -A option when loading config\_spec in MPF <https://github.com/missionpinball/mpf/pull/1280>`__ and `MC <https://github.com/missionpinball/mpf-mc/pull/362>`__ - jab based on `report by TheLegoMoviePinball <https://groups.google.com/forum/#!topic/mpf-users/okl8PjXrlWI>`__
-  `Honour slide parameter in inactive slides <https://github.com/missionpinball/mpf-mc/pull/363>`__ - avanwinkle
-  `Fix iMC startup crash <https://github.com/missionpinball/mpf-mc/pull/364>`__ - jab based on `report by snux <https://groups.google.com/forum/#!topic/mpf-users/YLrh6RKlx0s>`__
-  `Remove use\_sound\_setting from default options <https://github.com/missionpinball/mpf-mc/pull/367>`__ - avanwinkle


.. rubric:: MPF Documentation

-  `How to change the size of switches and light in the MPF monitor <https://github.com/missionpinball/mpf-docs/commit/78bcd64254da3710423d5791ce6a067857c9c348>`__ - jab based on questions from Jack Danger and Dan
-  `Document StepStick stepper drivers in MPF <https://github.com/missionpinball/mpf-docs/commit/5f6b117f9e0cdae26514dc0e4d5846b83277a9e8>`__ - jab based on `request from Tom <https://groups.google.com/forum/#!topic/mpf-users/ZgssCKBzvnA>`__
-  `How to show virtual segment displays in MC <https://github.com/missionpinball/mpf-docs/commit/bda3bb1c11dbe3ea63c5d151299ab81f6c9ea7be>`__ - jab based on `example from BorgDog <https://groups.google.com/forum/#!topic/mpf-users/1wzjCo5pL0U>`__
-  `How to use multiple displays <https://github.com/missionpinball/mpf-docs/commit/a608639b21ff9cd62692fc12c7b05b8dc1ff5ee5>`__ - jab based on `question in forum by Chris B and Snux <https://groups.google.com/forum/#!topic/mpf-users/2kjoLF_q9KA>`__
-  `Credits mode tutorial <https://github.com/missionpinball/mpf-docs/commit/2df9021bd09fae9b6023ff9113c344ced45f5a22>`__ - jab based on old tutorial
-  `Tutorial on debugging memory leaks <https://github.com/missionpinball/mpf-docs/commit/e49caefff47f8b1af3642f946c1cc4d4c43f3a74>`__ - jab based on question from Brian Cox
-  `Document RPi DMD platform <https://github.com/missionpinball/mpf-docs/commit/d075be91f5592ead66469227186b0495b32d975d>`__ - jab
-  `How to subscribe variables in config players <https://github.com/missionpinball/mpf-docs/commit/b3c95c884cc2e622a6c017421216bb8ab4fa85c5>`__ - jab based on `question <https://groups.google.com/forum/#!topic/mpf-users/nLnz5rM3Uus>`__
-  `Documenting the snux platform <https://github.com/missionpinball/mpf-docs/pull/193>`__ - snux
-  `How to use a Stern Spike Trough in other platforms than Stern Spike <https://github.com/missionpinball/mpf-docs/commit/e285f58d46253262f54d10ab7837a835ad3cd608>`__ - jab
-  `How to use Solid State Style Score Queues <https://github.com/missionpinball/mpf-docs/commit/e1bd78aa1e2b4b13de609134f141e1fea44d69a6>`__ - jab based on `request in forum <https://groups.google.com/forum/#!topic/mpf-users/4Ecj6xtveHo>`__
-  `Document event handler priorities <https://github.com/missionpinball/mpf-docs/commit/b2b8e270d0dfb9b862190b60fa8e744e8e524905>`__ - jab
-  `How to use multiple locks in a multiball <https://github.com/missionpinball/mpf-docs/commit/6ddb559e013c5a187dba99d293d2df88a74bf223>`__ - jab
-  Monitorable properties for `shots <https://github.com/missionpinball/mpf/pull/1287>`__ and `shot\_groups <https://github.com/missionpinball/mpf-docs/commit/f2b1833153fb391d6316ed8afb18761eaa580854>`__ - jab based on `question by snux <https://groups.google.com/forum/#!topic/mpf-users/cVnmhJIN1tM>`__
-  `Document recycle settings for more platforms <https://github.com/missionpinball/mpf-docs/commit/cec753171700165814d0853684e6ac9c6357df76>`__ - jab based on `question by Cole M <https://groups.google.com/forum/#!topic/mpf-users/qGVVwTbYnrA>`__
-  `Explain logic and modes in MPF <https://github.com/missionpinball/mpf-docs/pull/197>`__ - colemanomartin
-  `Notes on case-sensitivity <https://github.com/missionpinball/mpf-docs/pull/195>`__ - colemanomartin
-  `Explain A and C side preference in System11/Snux <https://github.com/missionpinball/mpf-docs/pull/194>`__ - snux
-  `Fix typos <https://github.com/missionpinball/mpf-docs/pull/196>`__ - travisbmartin
-  `Document monitorable properties and event in logic blocks <https://github.com/missionpinball/mpf-docs/commit/7a03143a5ebf571f6092ebf4b28a7b7282420584>`__ - jab
-  `Example for conditionals in log <https://github.com/missionpinball/mpf-docs/commit/34e8403e29d3292d82ff768bac95c400f16191c4>`__ - jab
-  `Update Smartmatrix documentation for new cookie <https://github.com/missionpinball/mpf-docs/pull/198>`__ - aaronmatthies
-  `Document start/launcher/tournament buttons <https://github.com/missionpinball/mpf-docs/commit/1073eb379d827037f094123d73d4180ab433d8e3>`__ - jab
-  Document part numbers and voltages for `bulbs, flashers <https://github.com/missionpinball/mpf-docs/commit/59c62c471e8c9237b33bfa424f192eb332d8d500>`__, `GIs and popbumpers <https://github.com/missionpinball/mpf-docs/commit/ddfa77cfbfd6fa37ecf2b36f911d4220f84a9d8f>`__ and `LEDs <https://github.com/missionpinball/mpf-docs/commit/24bbc32b25a75580d9407a12676d12cd14af9136>`__ - jab
-  `Up-Down ramps <https://github.com/missionpinball/mpf-docs/commit/79166be8691b92e2c8f3a77c0f76ce299ad56759>`__ - jab
-  `Updated Mac Install Instructions <https://github.com/missionpinball/mpf-docs/pull/200>`__ - avanwinkle
-  `Image for WS2812 LEDs <https://github.com/missionpinball/mpf-docs/pull/199>`__ - kylenahas


0.51
----

Released: November 24, 2018

This is a 0.50 maintenance release with cleanups and some refactorings.
Breaking changes in common features are minimal but some minor changes might be
required in some cases (e.g. we removed some defunctional options).
It comes with lots of performance improvements and new settings for
production machines.

.. rubric:: MPF

New Features
^^^^^^^^^^^^

-  `Configurable match number <https://github.com/missionpinball/mpf/pull/1150>`__ - jab
-  `Support I2C on the RPi via pigpio <https://github.com/missionpinball/mpf/pull/1159>`__ - jab
-  `Improve event order <https://github.com/missionpinball/mpf/pull/1160>`__ - jab
-  `Refactor accelerometers <https://github.com/missionpinball/mpf/issues/1155>`__ - jab (breaking change)
-  `Support burst IRs and local inputs/outputs on the P3-Roc <https://github.com/missionpinball/mpf/pull/1167>`__ - jab
-  `Validate P-Roc direct input numbers <https://github.com/missionpinball/mpf/pull/1172>`__ - jab
-  `Rename scriptlets to custom\_code <https://github.com/missionpinball/mpf/pull/1148>`__ - jab
-  `Add json logging <https://github.com/missionpinball/mpf/pull/1178>`__ - muffler-aus
-  `Improve startup performance <https://github.com/missionpinball/mpf/pull/1179>`__ - jab
-  `Allow lists of flashers <https://github.com/missionpinball/mpf/pull/1183>`__ - avanwinkle
-  `Prevent spaces in event handlers <https://github.com/missionpinball/mpf/pull/1191>`__ - avanwinkle (breaking change)
-  `Allow float in timers <https://github.com/missionpinball/mpf/issues/1187>`__ - jab
-  `Major performance improvements for switch handlers <https://github.com/missionpinball/mpf/pull/1196>`__ - jab
-  `Major performance improvements in lights and shows <https://github.com/missionpinball/mpf/commit/9148c8ebc568706d1c30ef2a64710993c05d2aec>`__ - jab
-  `Add option to disable sound output <https://github.com/missionpinball/mpf/pull/1199>`__ - avanwinkle
-  `Support multiple I2C servo controllers <https://github.com/missionpinball/mpf/pull/1206>`__ - jab (breaking change)
-  `Improve performance without logging <https://github.com/missionpinball/mpf/commit/b870147b3031f4ab5cea90911269013b8d86f3ac>`__ - jab
-  `Add support for P3-Roc burst optos <https://github.com/missionpinball/mpf/commit/c98832f4e175a4cc2d1de0c546a3b9d65432aedb>`__ - jab
-  `Allow users to disable ball search rounds <https://github.com/missionpinball/mpf/commit/2ded24ac3076c877a53ed575205fe124378888e0>`__ - jab
-  `Define alignment for segment displays <https://github.com/missionpinball/mpf/issues/1201>`__ - jab
-  `Add restart\_events to shots and shot groups <https://github.com/missionpinball/mpf/pull/1213>`__ - avanwinkle
-  `Add placeholder support to event\_player <https://github.com/missionpinball/mpf/pull/1212>`__ - avanwinkle
-  `Prevent warnings during init and batch incandescant update for OPP <https://github.com/missionpinball/mpf/pull/1220>`__ - jab
-  `Improve FAST behaviour during MPF init <https://github.com/missionpinball/mpf/pull/1221>`__ - jab
-  `Entrance switch ignore window <https://github.com/missionpinball/mpf/pull/1216>`__ - avanwinkle
-  `Improved README.md for the MPF project <https://github.com/missionpinball/mpf/pull/1219>`__ - austinbgill
-  `Prevent bad switch config for drop\_targets, shots and autofires <https://github.com/missionpinball/mpf/pull/1227>`__ - jab
-  `Validate that ball\_count for multiballs is the right range <https://github.com/missionpinball/mpf/pull/1229>`__ - jab based on `question from Alex <https://groups.google.com/forum/#!topic/mpf-users/jQTwpofBysA>`__
-  `Allow variable\_players outside game modes for machine variables <https://github.com/missionpinball/mpf/pull/1231>`__ - jab
-  `Only reset drop target banks if a target is down <https://github.com/missionpinball/mpf/pull/1236>`__ - jab based on `request from Mark M <https://groups.google.com/forum/#!topic/mpf-users/kHq3dM1PMyo>`__
-  `Add support for flipper tapping for OPP <https://github.com/missionpinball/mpf/pull/1238>`__ - jab and Hugh based on `forums discussion <https://groups.google.com/forum/#!topic/mpf-users/pKfmv_lmuDc>`__
-  `Serial LEDs support for PD-LED <https://github.com/missionpinball/mpf/pull/1239>`__ - jab with help from gstellenberg
-  `Only send lamp updates when lamps change in LISY <https://github.com/missionpinball/mpf/commit/a4cd700c488f9290bd4a62cb198d188d75c30da2>`__ - jab
-  `mpf test can now parse example/tests from rst files <https://github.com/missionpinball/mpf/commit/89f05214e22bce03b7bcb2047600a11f338053ab>`__ - jab
-  `sw\_flip\_events and sw\_release\_events for flipper to flip from software <https://github.com/missionpinball/mpf/commit/9a1e6c0f41ccf53645d02804dd0f66eb387a1ee8>`__ - jab based on `request from Philip D <https://groups.google.com/forum/#!topic/mpf-users/76BQAtIfsZc>`__
-  `Add event handlers to start game and add players <https://github.com/missionpinball/mpf/pull/1244>`__ - jab based on `request from Cole M <https://groups.google.com/forum/#!topic/mpf-users/vuUJMdSI2_A>`__
-  `Add new mode\_will\_start hook for custom code <https://github.com/missionpinball/mpf/pull/1247>`__ - Lamoraldus based on `discussion in forum <https://groups.google.com/forum/#!topic/mpf-users/D0W3pacTGUg>`__
-  `Support external platforms via entry\_points <https://github.com/missionpinball/mpf/pull/1248>`__ - jab
-  `Refresh Smartmatrix DMDs periodically <https://github.com/missionpinball/mpf/pull/1250>`__ - jab
-  `Support Servos on PD-LED <https://github.com/missionpinball/mpf/pull/1253>`__ - jab with help from gstellenberg (`announcement <https://www.multimorphic.com/news/servo-and-stepper-motor-control-in-pd-led-v3/>`__)
-  `Support Steppers on PD-LED/New stepper device interface <https://github.com/missionpinball/mpf/pull/1255>`__ - jab with help from gstellenberg
-  `Support config specs for external platforms via entry\_points <https://github.com/missionpinball/mpf/pull/1252>`__ - jab

Bug fixes & code improvements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  `Prevent crash on empty machine vars in MC <https://github.com/missionpinball/mpf/pull/1151>`__ - jab
-  `Sync shows with sync\_ms on stop <https://github.com/missionpinball/mpf/pull/1169>`__ - jab
-  `Fix pulse on drop target reset <https://github.com/missionpinball/mpf/issues/1176>`__ - jab
-  `Prevent flicker on show replace <https://github.com/missionpinball/mpf/pull/1175>`__ - jab
-  `Fix logging verbosity <https://github.com/missionpinball/mpf/pull/1197>`__ - avanwinkle
-  `Fix placeholder crash <https://github.com/missionpinball/mpf/issues/1202>`__ - jab
-  `Restore diverter state after ball search <https://github.com/missionpinball/mpf/pull/1209>`__ - jab
-  `Fix debug flag in P-Roc and P3-Roc <https://github.com/missionpinball/mpf/commit/015fc4d8508ffadf9324100a5d9280dd4e781b49>`__ - jab
-  `Prevent achivements from enabling after restoring state <https://github.com/missionpinball/mpf/pull/1211>`__ - avanwinkle
-  `Fix ms vs sec in timer pause <https://github.com/missionpinball/mpf/pull/1214>`__ - avanwinkle
-  `Fix mode events when starting/stopping mode from BCP <https://github.com/missionpinball/mpf/issues/1215>`__ - jab based on `report by Travis Martin <https://groups.google.com/forum/#!topic/mpf-users/u48fOP3TIx0>`__
-  `Fix display\_light\_player crash when used in mode <https://github.com/missionpinball/mpf/pull/1224>`__ - jab
-  `Fix crash in BCP with MPF Monitor <https://github.com/missionpinball/mpf/pull/1226>`__ - jab based on `report from alex <https://groups.google.com/forum/#!topic/mpf-users/4anGZjhW7i4>`__
-  `Fix pulse calculation error in Stern Spike <https://github.com/missionpinball/mpf/commit/09f236a40b462cc7e3ea5b7043831b0b8ff1badf>`__ - jab
-  `Actually use poll\_hz in lisy section <https://github.com/missionpinball/mpf/pull/1240>`__ - jab
-  `Prevent broken flipper rules when using multiple flipper devices in FAST/OPP <https://github.com/missionpinball/mpf/commit/16b1a5dc5fd4d3f25764f27e9a0043e1c99f4144>`__ - jab
-  `Prevent lags in LISY <https://github.com/missionpinball/mpf/pull/1249>`__ - jab


.. rubric:: MPF-MC

New Features
^^^^^^^^^^^^

-  `Disable multi touch <https://github.com/missionpinball/mpf-mc/commit/f4c19ea3ddb8a3d76351f4c7555abb35f5dae722>`__ - qcapen
-  `Add json logging to MC <https://github.com/missionpinball/mpf-mc/pull/335>`__ - mfulleratlassian
-  `Improve startup performance <https://github.com/missionpinball/mpf-mc/pull/337>`__ - jab
-  `Add animations based on event parameters <https://github.com/missionpinball/mpf-mc/commit/fc60d636409ed50ba2e8f9c03695b7b01c45d09d>`__ - jab
-  `Add option to disable sound output <https://github.com/missionpinball/mpf-mc/pull/340>`__ - avanwinkle
-  `Rename mc\_scriptlets to mc\_custom\_code <https://github.com/missionpinball/mpf-mc/pull/347>`__ - jab
-  `Support other channel orders than RGB for all RGB DMDs <https://github.com/missionpinball/mpf-mc/issues/345>`__ - jab based on `request from Cadrion <https://groups.google.com/forum/#!topic/mpf-users/1EtJxmAZiow>`__
-  `Update kivy to version 1.10.1 <https://github.com/missionpinball/mpf-mc/pull/346>`__ - jab
-  `Support multiple (stacked) style values for widgets <https://github.com/missionpinball/mpf-mc/pull/349>`__ - avanwinkle
-  `Better error when showing images too early <https://github.com/missionpinball/mpf-mc/pull/350>`__ - jab based on `question from Brian C <https://groups.google.com/forum/#!topic/mpf-users/iMivocg70BQ>`__
-  `Allow widget styles to set z values <https://github.com/missionpinball/mpf-mc/pull/351>`__ - avanwinkle
-  `Update kivy dependencies <https://github.com/missionpinball/mpf-mc/pull/354>`__ - jab
-  `Reusing named widgets <https://github.com/missionpinball/mpf-mc/pull/353>`__ - avanwinkle

Bug fixes & code improvements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  `Properly update text widgets on text change <https://github.com/missionpinball/mpf-mc/pull/326>`__ - MarkInc666
-  `Fix crash on empty machine var <https://github.com/missionpinball/mpf-mc/pull/328>`__ - jab
-  `Reset animation on remove of image <https://github.com/missionpinball/mpf-mc/pull/332>`__ - jab
-  `Fix iMC crash <https://github.com/missionpinball/mpf-mc/commit/947ba86af2a9ea148a33674a60ee5f2184527948>`__ - jab
-  `Fix widget leaks <https://github.com/missionpinball/mpf-mc/commit/5ce7e23579718892b09405bcca3ebb41be31ca8d>`__ - jab
-  `Fix playlist crash <https://github.com/missionpinball/mpf-mc/commit/a3dadfc1bf0e7cce7ef80c86561e86ba0492aee9>`__ - qcapen
-  `Fix that you cannot edit the last highscore character <https://github.com/missionpinball/mpf-mc/issues/338>`__ - jab
-  `Prevent multiple text handlers/Improve performance <https://github.com/missionpinball/mpf-mc/pull/342>`__ - avanwinkle
-  `Fix depreation warnings in kivy scale <https://github.com/missionpinball/mpf-mc/pull/343>`__ - avanwinkle
-  `Fix iMC initialisation <https://github.com/missionpinball/mpf-mc/pull/352>`__ - avanwinkle

.. rubric:: MPF-Monitor

New Features
^^^^^^^^^^^^

-  `Add config option for device size in monitor <https://github.com/missionpinball/mpf-monitor/commit/a348117131ae93904ef8c265eb4253b225876a8e>`__ - jab
-  `Improve monitor performance <https://github.com/missionpinball/mpf-monitor/commit/6e70bf76462a0bb21a4d272a5a4057aa3b67d3c9>`__ - jab

Bug fixes & code improvements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  `Fix bcp crashes <https://github.com/missionpinball/mpf-monitor/commit/436133dfbef1f8d67d4845f101bab2bc536bc6b6>`__ - jab
-  `Obey machine path <https://github.com/missionpinball/mpf-monitor/pull/18>`__ - John

.. rubric:: MPF Documentation

-  `Document state\_machines <https://github.com/missionpinball/mpf-docs/commit/d42223c9d1c1c1c96dd6b2770ec6b9515e88db26>`__ - jab
-  `Document hardware\_sound\_player for older machines <https://github.com/missionpinball/mpf-docs/commit/6c7a3773b820162211bae1e9f84cf7ddb70c07fe>`__ - jab
-  `Document bitmap\_fonts <https://github.com/missionpinball/mpf-docs/commit/32266404b229aa6079d265a37b08880ae0147bc1>`__ - qcapen
-  `Document motors and digital\_outputs <https://github.com/missionpinball/mpf-docs/commit/12fb5c757881b7e90c4a59721023f56e9a96cfb6>`__ - jab
-  `Document SPIKE DMDs <https://github.com/missionpinball/mpf-docs/commit/59222b3524cefab73ae5283edaef9295e2ff41ef>`__ - jab
-  `Example for logic blocks <https://github.com/missionpinball/mpf-docs/commit/7770a5b66e5c5a0dff88c546f26133fa3a7a8f58>`__ - jab
-  `Add documentation on game design <https://github.com/missionpinball/mpf-docs/commit/3c755828ac89c2e658255fe6676b29491bee51b0>`__ - jab
-  `Update I2C accelerometer documentation <https://github.com/missionpinball/mpf-docs/commit/aeb6cc6d8946fb1b2e665594571405e05bae9426>`__ - jab
-  `Add mode examples <https://github.com/missionpinball/mpf-docs/commit/bdbe69e10327358b0699721bf809c2d16a547445>`__ - jab
-  `Improved windows install instructions for the monitor <https://github.com/missionpinball/mpf-docs/commit/cb5ec4c2b8f4970706e871cb66471397799d5592>`__ - sliderpoint
-  `Document burst IR and direct inputs/ouputs on the P3-Roc <https://github.com/missionpinball/mpf-docs/commit/1089bda9177ff54526c0888caaceb16d3b1439ad>`__ - jab
-  `Fix smartmatrix documentation <https://github.com/missionpinball/mpf-docs/pull/154>`__ - driskel
-  `Document tilt mode <https://github.com/missionpinball/mpf-docs/commit/05401391f8c33a22366f7b3a18b506c5bf65c08e>`__ - jab
-  Document `conditionals <https://github.com/missionpinball/mpf-docs/commit/273322ef0f8e08b1f52d73bba15a2a2c384ebecf>`__ and `placeholders <https://github.com/missionpinball/mpf-docs/commit/4b57f15a11c77a941490ef3e56cf8f1b4c27a991>`__ - jab
-  `Document multipliers in scoring <https://github.com/missionpinball/mpf-docs/commit/d0c5c3408f1d26e86185e73dc1360ad1be1e9cfa>`__ - jab
-  `Document color correction <https://github.com/missionpinball/mpf-docs/commit/889fb39e75e8ff69d541169a2bd29bf9b22b3763>`__ - jab
-  `Document spinners <https://github.com/missionpinball/mpf-docs/commit/6525fd67f43d7f73c21193905dba3155d553498c>`__ - jab
-  `Document shows on ball start/end <https://github.com/missionpinball/mpf-docs/commit/6a431f184e7104550790edcc7cfde7a68f9deb8a>`__ - jab
-  `Document bonus mode <https://github.com/missionpinball/mpf-docs/commit/4100fb8f2a46c68bae6ca75f2100fd04c17c326d>`__ - jab
-  `Howto on ball save on ball start <https://github.com/missionpinball/mpf-docs/commit/c4b7fa497f35857eaf638532e26411ab38096d7c>`__ - jab
-  `Document high score mode <https://github.com/missionpinball/mpf-docs/commit/98572da7c502302248042cb34178cc9537e5beb0>`__ - jab
-  `Document MPF service cli <https://github.com/missionpinball/mpf-docs/commit/3a3c06f3f8e9331ce147f351575817058db5a2fa>`__ - jab
-  `Document credits mode <https://github.com/missionpinball/mpf-docs/commit/98deb6d540a92ff793a9ab7632b30ed1b02ba82e>`__ - jab
-  `Document common machine types <https://github.com/missionpinball/mpf-docs/commit/9176ba41c3ff9bc881e1297cc050de6cb889dd0b>`__ - jab
-  `Document LISY <https://github.com/missionpinball/mpf-docs/commit/94cacad09ed830c22122538549543671fd5cd217>`__ - jab
-  `Document common modes in MPF <https://github.com/missionpinball/mpf-docs/commit/7e63be2b75572e453096f89ea182e907f0091bba>`__ - jab
-  `Add RPi debug notes on sound/video <https://github.com/missionpinball/mpf-docs/pull/155>`__ - matirwin
-  `Document match mode <https://github.com/missionpinball/mpf-docs/commit/bee6d74ab69827eda548ad3a881fc06b2c0d1603>`__ - jab
-  `How to use udev to ensure persistent devices on linux <https://github.com/missionpinball/mpf-docs/commit/f5e15e224786fd7cfdc95c40b69ade0f97893ec8>`__ - jab
-  `Document text placeholders <https://github.com/missionpinball/mpf-docs/commit/0bca0610df3f8b6ae17d7a52fc1ef1a3c015baf3>`__ - jab
-  `Add examples for animations based on player vars <https://github.com/missionpinball/mpf-docs/commit/357ac2fbb8f581c4cdbb9076637067efdc9618d0>`__ - jab
-  `Add light examples <https://github.com/missionpinball/mpf-docs/commit/6585b62fdcf4032a7e6b19ec59992ce71e4dc5eb>`__ - jab
-  `Clarify monitorable properties <https://github.com/missionpinball/mpf-docs/pull/159>`__ - avanwinkle
-  `Added a guide on mode layering <https://github.com/missionpinball/mpf-docs/pull/161>`__ - avanwinkle
-  `Document how to run MPF in production <https://github.com/missionpinball/mpf-docs/commit/d44450ed89509f4cf6e92e86f5efe0e6350a9cbf>`__ - jab
-  Improve `light\_strips <https://github.com/missionpinball/mpf-docs/commit/2a8028faca8a9a8193b5ff7adf5e8619b9cb5355>`__, `ball\_holds <https://github.com/missionpinball/mpf-docs/commit/edb91230b88616c3380f29dab31bbff2e9996eb4>`__, `image\_widgets <https://github.com/missionpinball/mpf-docs/commit/892051e8a7a10fe5a334be49b2319a4729ee262d>`__, `widget\_styles <https://github.com/missionpinball/mpf-docs/commit/539c2bdeb947fabf2c6bea3574925f9d5d9e573c>`__, `switch\_player <https://github.com/missionpinball/mpf-docs/commit/9b35a8849e1dc2a5f8b613eb57ca7bbd2984b1e9>`__, `drop\_target\_banks <https://github.com/missionpinball/mpf-docs/commit/10901bfbeb3e8b982aa4c3b406f783c8fbf08d10>`__, `drop\_targets <https://github.com/missionpinball/mpf-docs/commit/1a2f2b83daafa402d1efe99e7eb920c591f524f4>`__, `logic\_blocks <https://github.com/missionpinball/mpf-docs/commit/1522debd55ccab6492670d5943dc6e4b4aa3bc97>`__, `coil\_player <https://github.com/missionpinball/mpf-docs/commit/fe54283f9b651934e54071d846d1a08014772757>`__, `counters <https://github.com/missionpinball/mpf-docs/commit/d292c016bc0b9205815b5898245c0aca1a35583a>`__, `switches <https://github.com/missionpinball/mpf-docs/commit/c6234540fddaf0cfe36ac10a7f0b701a0e6f9a76>`__, `ball\_devices <https://github.com/missionpinball/mpf-docs/commit/2099814c58b1b3d0f5f8a3d401a3d67e71bd2da2>`__, `PSUs <https://github.com/missionpinball/mpf-docs/commit/e928ea5803faf6300b675e16ad1d60b05f0b27f9>`__, `coils <https://github.com/missionpinball/mpf-docs/commit/fadd5fbec22d372b32488b00389cabebc229af75>`__, `smart\_virtual\_platforms <https://github.com/missionpinball/mpf-docs/commit/065235cb3b45164d29c74e6db25567232c546fc2>`__, `multi\_balls <https://github.com/missionpinball/mpf-docs/commit/7586913dea15b574c4d8536f13073a53d623e407>`__, `light\_rings <https://github.com/missionpinball/mpf-docs/commit/36b9df88ec31ec7f510bd21d3bde67e17df34e94>`__ and `more <https://github.com/missionpinball/mpf-docs/commit/44a6b57b4a372408eedbf6636d57a5f34366ecee>`__ - jab
-  `Document volatages in pinball machines <https://github.com/missionpinball/mpf-docs/commit/970f51c50496d6870836cb3a06c89e381fd4ef5b>`__ - jab
-  `Documentation about EMC/EMI and common ground <https://github.com/missionpinball/mpf-docs/commit/531977dc4254e24916025bfc6cd17c82a8526510>`__ - jab
-  `Document FAST power filter board <https://github.com/missionpinball/mpf-docs/commit/e794a3a31bd69c91a9c56231de60ef3e84d7db49>`__ - jab
-  `Document Multimorphic power entry board <https://github.com/missionpinball/mpf-docs/commit/9e40e42b6763a9188a880a308bed2446c934d60f>`__ - jab
-  `Document servo sequences <https://github.com/missionpinball/mpf-docs/commit/08c4d51beb16ddc2efcc7e0b2b72bf6e51b57c93>`__ - jab
-  Images for `targets <https://github.com/missionpinball/mpf-docs/commit/3b4cb68e5959270026008244caa52387fd27d2ab>`__ and `FAST and Multimorphic <https://github.com/missionpinball/mpf-docs/commit/54bb1ec5c56349d3bed89d7ce3017fa019460d76>`__, `drop\_targets and optos <https://github.com/missionpinball/mpf-docs/commit/6385cc1f6c81e8728d0ddc084b8a5629e5b357a8>`__, `switches, spinners and magnets <https://github.com/missionpinball/mpf-docs/commit/6192c7e9aecefa6adad948d7d13e39c6946fe63b>`__, `vari-targets <https://github.com/missionpinball/mpf-docs/commit/5b4eee25b464ac71ce9527b6553b28504700b3bb>`__ - with help from the fast slack
-  `Add part numbers for optos and switches <https://github.com/missionpinball/mpf-docs/commit/73dd80bd24a4f1b15a2b7b53df87e5dd8e41711e>`__ - jab
-  `Add common PSU part numbers <https://github.com/missionpinball/mpf-docs/commit/d759882df0a083382bc8d77a5c78dff1702359bf>`__ - jab
-  `Document uninstall <https://github.com/missionpinball/mpf-docs/pull/168>`__ - colemanomartin
-  `Document how to cancel a show using flipper\_cancel events <https://github.com/missionpinball/mpf-docs/commit/acb6c6ba2efaaba8b5a93e71f229772f8b6c96a9>`__ - mwiz
-  `Document wiring and voltages <https://github.com/missionpinball/mpf-docs/commit/a7a70a8b3c454f725edb5773fceadf77659f2584>`__ - jab
-  `Mode corrections <https://github.com/missionpinball/mpf-docs/pull/169>`__ - mwseiden
-  `Document electrical details of optos <https://github.com/missionpinball/mpf-docs/commit/7c06de742a730449b9d82e32a864b9fcfa3684d2>`__ - jab
-  `Update shot group profiles documentation <https://github.com/missionpinball/mpf-docs/pull/171>`__ - avanwinkle
-  `Document how to use player variables with counters <https://github.com/missionpinball/mpf-docs/pull/172>`__ - mwseiden
-  `Document appliance classes and common ground <https://github.com/missionpinball/mpf-docs/commit/44c15465db97108d93fad1637c43a3778afdd4aa>`__ - jab
-  `Added examples for PD-LED <https://github.com/missionpinball/mpf-docs/commit/a57ddb305abf8b4738e355143be1222d6c763b6b>`__ - jab
-  `Document appliance classes and common ground <https://github.com/missionpinball/mpf-docs/commit/44c15465db97108d93fad1637c43a3778afdd4aa>`__ - jab
-  `Added examples for PD-LED <https://github.com/missionpinball/mpf-docs/commit/a57ddb305abf8b4738e355143be1222d6c763b6b>`__ - jab
-  `Improved bonus mode documentation <https://github.com/missionpinball/mpf-docs/pull/173>`__ - avanwinkle
-  `Document ball and game end mode blocking <https://github.com/missionpinball/mpf-docs/commit/fd7112356a26413abe27a0e0cb3980f586f3a6c9>`__ - jab inspired by Lynn
-  `Extra ball based on score example <https://github.com/missionpinball/mpf-docs/commit/2d8e6b7d073f6904564896ca485b3f3c69951027>`__ - jab based on `example from Lynn <https://groups.google.com/forum/#!topic/mpf-users/cOQKDQIIu-g>`__
-  `How to use high score mode in EMs <https://github.com/missionpinball/mpf-docs/commit/318541ee4349776e5fb4660fcd44b29104f1a842>`__ - jab based on `example from Lynn <https://groups.google.com/forum/#!topic/mpf-users/cOQKDQIIu-g>`__
-  `Document RGB DMD channel\_order parameter <https://github.com/missionpinball/mpf-docs/commit/a21bcae7b7be032c918a987fdb32cda8ee2a567e>`__ - jab
-  `Added example of game mode which increases multiplier when lanes are complete <https://github.com/missionpinball/mpf-docs/pull/176>`__ - travisbmartin
-  `No longer claim Python 3.4 support - it is EOL <https://github.com/missionpinball/mpf-docs/commit/1639e5b62f221b6a525b3ca39da6b68dd2d88752>`__ - jab
-  `Document PC power on/off <https://github.com/missionpinball/mpf-docs/commit/8bb7de3ce54153c8e7afbc3fdb992b13bb000409>`__ - jab
-  `Typos <https://github.com/missionpinball/mpf-docs/pull/177>`__, `Typos <https://github.com/missionpinball/mpf-docs/pull/178>`__ - travisbmartin
-  `Improve skill shot example to prevent race condition and add timeout <https://github.com/missionpinball/mpf-docs/commit/063dd00c2b9f0db50b099528e3f2d948c7e40f28>`__ - jab based on `question from mike wiz <https://groups.google.com/forum/#!topic/mpf-users/Fxuh95wxmjY>`__
-  `Document scoring based on logic blocks <https://github.com/missionpinball/mpf-docs/commit/a843d366bed107544aebf2198f80f07a501adb5b>`__ - jab based on `question from alex <https://groups.google.com/forum/#!topic/mpf-users/3mShvjtjfPU>`__
-  `Describe how to debug crashes with GDB <https://github.com/missionpinball/mpf-docs/commit/27a7c31b524f2a1890c97e6dbc86e08811e31e38>`__ - jab
-  `How to tune eject\_timeouts in ball devices <https://github.com/missionpinball/mpf-docs/commit/ec7477e5a9c3e03adf24473599c2c2909db0a75a>`__ - jab
-  `Understanding tags in MPF <https://github.com/missionpinball/mpf-docs/pull/179>`__ - cfbenn
-  `Example for using MC with multiple screens <https://github.com/missionpinball/mpf-docs/commit/2d62878bc2a04d699e81fd12fad77d1ad4b13a52>`__ - jab based on example from Brian Cox/cfbenn/qcapen
-  `Document how to use machine and player variables from code <https://github.com/missionpinball/mpf/pull/1232>`__ - jab
-  `Document multiple styles for widgets <https://github.com/missionpinball/mpf-docs/pull/180>`__ - avanwinkle
-  `Document how to use start button for mode selection without added new players <https://github.com/missionpinball/mpf-docs/commit/946426c043a34af7cccd48027fa06fa658799019>`__ - jab based on `example provided by alex <https://groups.google.com/forum/#!topic/mpf-users/e3emzNIxZp0>`__
-  `Document which hardware rules are used in MPF <https://github.com/missionpinball/mpf-docs/commit/d9d95dd66795e2301731eacbc7e1bb7932374f99>`__ - jab based on `discussion in the forum <https://groups.google.com/forum/#!topic/mpf-users/pKfmv_lmuDc>`__
-  `Document Molex KK part numbers for connectors <https://github.com/missionpinball/mpf-docs/commit/4214b32a82f9b4115a6ce831c57ce315fc536578>`__ - jab
-  `Document how to maintain a stable high voltage rail <https://github.com/missionpinball/mpf-docs/commit/c1eada55c0c52b009a18b2d5d14431d4d6fce6d6>`__ - jab based on `suggestion by Hugh in discussion <https://groups.google.com/forum/#!topic/mpf-users/7-E62qVTkGA>`__
-  `Common events and example for shots <https://github.com/missionpinball/mpf-docs/commit/2a9a918f6469f9b7b34d08348184fc4925ede93b>`__ - jab based on `question from Alex <https://groups.google.com/forum/#!topic/mpf-users/-BUnwqkcIBE>`__
-  `Autogenerated event lists for events <https://github.com/missionpinball/mpf-docs/commit/08bcd6ae2f11ef4f762976d041338f654c2fe33c>`__ - jab
-  `Initial documentation for sequence\_shots <https://github.com/missionpinball/mpf-docs/commit/c5fe46c93b3f27bd588d305cf194ddbe201d808c>`__ - jab
-  `Fixed typos <https://github.com/missionpinball/mpf-docs/pull/181>`__ - travisbmartin
-  `Weak flippers mode <https://github.com/missionpinball/mpf-docs/commit/e13d593671e9e523f78e964ee655a00cae9dad34>`__ - jab based `question by Brian C and Philip D <https://groups.google.com/forum/#!topic/mpf-users/51HrIM0IQrI>`__
-  `Document how to use widgets from code <https://github.com/missionpinball/mpf/pull/1243>`__ - cloudjor
-  `Extend event documentation for game\_start <https://github.com/missionpinball/mpf/pull/1242>`__ - colemanomartin
-  `Doctor Who carousel example <https://github.com/missionpinball/mpf-docs/pull/183>`__ - travisbmartin
-  `Document sw\_flip\_events and sw\_release\_events <https://github.com/missionpinball/mpf-docs/commit/96f0fc5158a5e12d21dffdb12760d64ed3f2b069>`__ - jab
-  `Example game mode with multiple shots which need to be active a the same time <https://github.com/missionpinball/mpf-docs/commit/d6cf7fb5b43844a0425837bb677f473055f213b2>`__ - jab and improvements by `coleman <https://github.com/missionpinball/mpf-docs/pull/184>`__ based on `question by Cole M <https://groups.google.com/forum/#!topic/mpf-users/QnJ_1Hkd-Mk>`__
-  `Cookbook/tutorial for a super jets mode <https://github.com/missionpinball/mpf-docs/pull/185>`__ - travisbmartin
-  `Document how to send data from MPF to MPF-MC in custom code <https://github.com/missionpinball/mpf/pull/1245>`__ - cloudjor
-  `Added a minimal OSC plugin <https://github.com/missionpinball/mpf/pull/1200>`__ - jab
-  `Fix typos and links <https://github.com/missionpinball/mpf-docs/pull/187>`__ - zach27
-  `Notes on using multiple playfields <https://github.com/missionpinball/mpf-docs/commit/ddcc16252cc783a4aab42c5f372085349914e10f>`__ - jab based on `discussion in forum <https://groups.google.com/forum/#!topic/mpf-users/tnmvTI9J_O8>`__
-  `Animating a progress bar <https://github.com/missionpinball/mpf-docs/commit/b272f836598d13562f41f99007f27f13278a0f9d>`__ - based on `discussion in forum <https://groups.google.com/forum/#!topic/mpf-users/n2Shn9wDfUc>`__
-  `Adding a picture of a drop target bank <https://github.com/missionpinball/mpf-docs/commit/38e8e8bba4ffaead3c6c0e5a1f88300c570aa312>`__ - coleman
-  `Fix typos <https://github.com/missionpinball/mpf-docs/pull/188>`__ - travisbmartin
-  `Update stepper documentation <https://github.com/missionpinball/mpf-docs/commit/6f588482e0fe51a112052a16c1cd2a587d35e7c5>`__ - jab
-  `Document PD-LED steppers, servos and serial LEDs <https://github.com/missionpinball/mpf-docs/commit/324a5cfc77061a6756f99d8a62b0ad1148aa843c>`__ - jab


.. rubric:: Others

New Features
^^^^^^^^^^^^

-  `Experimental external Philips Hue platform <https://github.com/missionpinball/mpf-hue-platform>`__ - jab based on `code from Philip D <https://groups.google.com/forum/#!topic/mpf-users/e5dv9j71BUE>`__

0.50
----

Released: April 23, 2018

.. rubric:: MPF

New Features
^^^^^^^^^^^^

* Consolidated LEDs, matrix lights, GI, and flashers into a single "light" device. Much cleaner, less code,
  and unified features across all light types.
* Added RGBA color support (RGB colors plus an alpha channel)
* Hardware fade support for all light (fade-in and fade-out).
* Added segmented displays support
* Added LISY hardware platform support (for Gottlieb System 1 and System 80 machines)
* Added MyPinballs 7 segment display support
* Added P-Roc alphanumeric displays support
* Added Raspberry Pi as a platform (remote via ethernet or local using pigpio)
* Added stepper motor device
* Added motor device (with position and/or end switches)
* Added Trinamics Steprocker platform
* Added SPIKE DMD support
* Support for FAST RGB DMD support
* Added digital output support (either mapped as drivers or lights)
* Added native I2C support on linux (via SMBus)
* Added NXP MMA8451 accelerometer support (via I2C)
* Support fuzz testing (to find crashes in a machine without playing it)
* Added PSU support to manage maximum power usage.
  Coil pulses can specify a maximum delay which is used to reorder pulses
  (used by ball devices, score reels and drop targets).
* Improved and broke out game lifecycle events (will start, starting, started, etc.) for game, ball, and turn starts
  and stops.
* Made many more settings "templatable"
* Logging to syslog
* Cleaned up and simplified shots
* Added Text UI
* Added replay credits
* Added developer documentation website (developer.missionpinball.org)
* Added support for custom named colors
* Added pluggable ejectors and ball counters in ball devices
* Added "mpf service" command to spawn a service cli (similar to service mode or SPIKE game cli)
* Added "mpf hardware scan" to enumerate all hardware platforms
* Added "mpf hardware update_firmware" to send firmware updates to all hardware platforms

Bug fixes & code improvements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Support for Python 3.5 and 3.6 on Windows (including P-ROC libraries)
* Much more type checking
* Improved logic around how playfields are marked active
* Improved how device monitors work
* Improved and added config template values
* Improved multiball locks
* Improved machine variable internals
* Improved ball tracking
* Improved ball handling in ball devices
* Improved Stern SPIKE platform
* Refactored mode device loading, config validation, and config player loading
* Renamed "scoring" to "variable_player"
* Improved high score mode
* More robust score reels
* Performance improvements for fadecandy LED updates
* Performance improvements for smartmatrix devices (separate sender thread)


.. rubric:: MPF-MC

New Features
^^^^^^^^^^^^

* Major display refactoring
* Bitmap fonts
* Relative animation values
* Added widget rotation & scale animations
* Animation values respect initial anchor points
* Simplified, consolidated, & unified DMD, color DMD, and slide frame widgets into displays and display widgets
* New 'sound_loop' audio track type optimized for live looping music control driven by events.  This specialized
  audio track type can synchronize playback of multiple looping sounds simultaneously in layers and provides
  gapless switching to a new set of loops. It is designed to build music that dynamically changes based on events
  in your game.  Only supports in-memory sounds (no streaming).
* New 'sound_loop_set' asset type. A sound_loop_set is an asset used to play sounds in a sound_loop track that is
  basically a grouping of one or more sound assets.  The sounds in a loop set are arranged in layers. The master
  layer contains the sound that establishes the length of the entire loop set. Whenever the sound in the master
  layer loops, all other sounds in the sound_loop_set will also loop back to the beginning.
* New 'sound_loop_player' config_player. The sound_loop_player is a config player that is used to control the
  playback of sound_loop_sets in a sound_loop audio track. The track_player can also be used with a sound_loop
  track to control volume and playback state.
* New 'playlist' audio track type is designed to provide a comprehensive set of music playing capabilities that
  include named playlists, playback mode (sequence, random, etc.), cross-fades between sounds/songs/playlists,
  and more.
* New 'playlist' asset type. A playlist is an asset used to group and play sound assets on a playlist track. A
  playlist is basically an ordered group of sounds/songs typically used to playback music.
* New 'playlist_player' config player. The playlist_player is a config player that is used to control the playback
  of playlists (and their component sounds) in a playlist track.  The track_player can also be used with a playlist
  track to control volume and playback state.
* New sound 'about_to_finish' events (configurable for each sound). These post events at a specified time before
  the sound ends.
* New display_light_player to use your playfield lights as display in MC.
  Also supports transparency to overlay a graphic/animation above your light shows.

Bug fixes & code improvements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Support for Python 3.5 and 3.6 on Windows
* Significant performance improvements
* Fixed many leaks (especially widgets)
* Animation steps can be run simultaneously
* Bail out when a video codec is missing
* Refactored the entire audio engine code (broke audio_interface.pyx into many different files, individual
  source files for each track type and base class, eliminated .pxi files and established use of .pxd files)
* Switched back to SDL_Mixer for main audio playback, mixing, and in-memory sound asset loading functions
  (provide more reliable and faster loading of .ogg and .flac files)
* Allow unlimited sound asset event markers (previously only allowed a fixed number)

.. rubric:: MPF-Monitor

New Features
^^^^^^^^^^^^

* Device list shows all monitorable attributes

Bug fixes & code improvements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Improved performance of light updates/Smooth light shows


0.33
----

Released: April 10, 2017

.. rubric:: MPF

New Features
^^^^^^^^^^^^

* "Ball hold" device (Temporarily hold a ball while something else is happening)
* "Multiball lock" device (Track ball locks towards multiball, including virtual
  locks, across balls and players)
* Multiball "add a ball" feature
* Added support for Stern SPIKE platform
* :doc:`Revamped logging </config/logging>`
* Additional achievements control events
* BCP ports & interfaces are now configurable
* Drop target "keep up" feature (PWMs reset coil to "lock" target up)
* "Async" events (Events that wait for all handlers to finish before continuing)
* Additional multiball events
* More functions for people building games to use to write tests
* Built-in modes with code can have their code overloaded
* Added score reels to the smart virtual platform
* Allow machine variables to be set via BCP
* Allow setting default high scores
* Add "early save" events to ball saves
* Add all monitorable device properties to conditional events
* Use placeholders in mode timer start & end values
* More options for bonus (hurry ups, skip slides with 0 value, placeholders for score calculations, etc.)
* Improved ball search
* OPP - support for firmware 2.0 and dual wound coils
* MC scriptlets for video modes and code on the MC side
* Support for conditional events
* Template variables which are evaluated during runtime and can use
  placeholders (timers, logic_blocks, tilt, scoring, bonus_mode, and more)
* Early ball save
* Advanced bonus_mode
* TimedSwitch device - built-in event for flipper cradling and releasing
* Asynchronous logging - This is especially important on windows because
  logging previously slowed down the game. However, also important in production
  when under high I/O load or with slow discs.
* Timers work outside of the game now
* New "mpf diagnosis" command
* Scoring to machine variables
* Scoring for other players
* Weights in random_event_player
* Unlimited delay in ball_save to allow video modes or mode selection
* Added Machine vars for all kinds of versions
* Drop Target keep up support
* Multiball add a ball support
* New multiball_lock device which handles virtual saves for multiplayer game
* Allow BCP to bind on all IPs


Bug fixes & code improvements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* A lot of miscellaneous bug fixes
* Exiting service mode always put the machine back on free play
* Fixed a ball lock crash
* File loader will not try to load temp files
* Manual plunger in smart virtual platform now works properly
* Refactored ball devices to allow for different types of ball counters & be more robust for
  unexpected ball situations and different types of eject failures
* Made achievements and achievement groups smarter and more robust (also backported to 0.32)
* Improved log messages for BCP encoding errors
* "Hz" setting is gone (since MPF is now tickless)
* Active eject process trackers are canceled on shutdown
* Randomizer now works with a single element
* Fixed a bunch of small things that caused crashes
* Changed default on-screen DMD pixel settings
* Removed OSC plug-in since it hasn't worked in over a year and no one uses it
* Better errors on invalid configs
* Catching a lot more config problems
* Improved ball search. Drop Target reset no longer resets ball search
* Better start/stop procedures for modes. no more event races
* Improved extra ball
* Better yaml parsing for unescaped strings
* Performance improvements through better fast paths and offloading of logging
  from the synchronous path
* BCP version 1.1 with synchronisation during reset
* Improved handling of ball devices with entrance_switch
* Force UTF-8 for configs on windows
* Better errors when loading assets


.. rubric:: MPF-MC

New Features
^^^^^^^^^^^^

* Added a camera widget (live video)
* Allow placeholders and settings
* Added keyboard debugging
* Added warnings if window size & display size aspect ratios are not the same
* MPF-MC now checks to make sure the MPF version it's talking to is compatible
* Change the default display size to 800x600 if a displays: section is not in the config
* Re-vamped Mac installation procedure. It's now a "real" install and does not use
  MPF.app anymore.
* Added a "volume" machine variable
* Added Interactive Media Controller (iMC)
* Added "anchor_y: baseline" option for text widgets
* Added gamma setting for physical DMDs
* Added new relative animation target values


Bug fixes & code improvements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Improved sound asset loading speed (uses SDL_Mixer for loading to memory rather than GStreamer)
* Sound assets can be loaded while videos are playing
* Sound assets can be located in sub-folders as many levels deep as desired (not just a single
  level)
* Fixed points widget
* Improvements to automated testing on Travis
* widget_player positioning fixed
* Better error messages for malformed slide configs
* Prevent crash in text widget when empty and back is selected
* Changes to support BCP 1.1


0.32
----

Released: Dec 1, 2016

.. rubric:: MPF

* Improved :doc:`achievements </game_logic/achievements/index>` and added
  :doc:`achievement groups </game_logic/achievements/achievement_groups>`.
* Added relay events and relay queues
* Improved :doc:`smart virtual platform </hardware/virtual/smart_virtual>`
* Improved support for :doc:`System 11 </mechs/troughs/two_coil_multiple_switches>`
  and :doc:`Gottlieb System 3 style </mechs/troughs/two_coil_one_switch>`
  troughs (including using the ball drain as a ball storage location to get one
  additional ball capacity with no hardware changes).
* Verify that duplicate sections don't exist in config files
* Check that event handlers are properly formatted before they're registered
* Added conditional events (handlers that only fire if certain conditions are
  met)
* You can :doc:`set starting values for player variables </config/player_vars>`
* Fixed the :doc:`physical mono DMD </displays/display/dmd>` and
  :doc:`physical RGB (color) DMD </displays/display/rgb_dmd>`
* Added :doc:`multiball lost event </events/multiball_name_lost_ball>`
* Allow devices to have inline config specs
* Added shots with events
* Better OPP platform parsing
* Fixed & improved the high score mode
* Improved service mode
* Added options for "random" events (force next, force all, save per-player, etc.)
* Added events to the BCP monitor (meaning they can be viewed in the MPF Monitor app)
* Added ``-f`` command line option to force all assets to load on boot for testing purposes
* Added scoring options (add, replace, block)
* Use color "on" for LED default colors
* Allow multiple config player entries to fire from the same event
* Ensure that events created by the MC are sent to MPF
* Added machine vars for P-ROC and FAST hardware revisions
* Added :doc:`combo switches </game_logic/combo_switches/index>` (for "flipper cancel", two-button skill shots, etc.)
* Lots of little bug fixes...

.. rubric:: MPF-MC

* Fixed the widget z-order layering bug (this has been backported to 0.31).
  Widget orders are now higher value z: settings are on top of lower value ones.
* Negative z: values are no longer used to target parent slide frames. Instead,
  ``target: (name)`` is used.
* Cleaned up debug logging so BCP frames are not included in it by default
* Events that are natively posted in the MC are now sent to MPF
* Fixed a bug to ensure that the slide_active event is only posted once per frame
* Fixed a bug that prevented slide frames from being animated
* Fixed a bug where videos were not stopping
* Allow the same slide to be used on multiple displays
* Switch to GStreamer instead of SDL_Mixer for loading and streaming sounds. (SDL2 still used for all sound output.)
* Sound file streaming is now supported from any track (streamed from disk instead of preloaded into memory)
* New "track_player" config controls sounds at the track-level (fade, volume, play, pause, stop, etc.)
* Custom loading & unloading events at the individual sound level.
* Lots of little bug fixes...

0.31
----

Released: Sept 19, 2016

.. rubric:: MPF

* MPF is now "tickless", meaning everything runs faster, but with less overhead
* Improved flow control for FAST hardware serial communication
* Improved BCP communications
* Improved serial communications for all devices which use serial
* Additional options for ball saves
* Removed many threads which makes everything simpler and faster under the hood
* Improved "virtual" and "smart virtual" platforms
* Prevent broken data files from crashing MPF
* Added a basic service mode (this is just a start, much more to come)
* Detect balls that jump between playfields
* Prevent duplicate rules being written to P-ROC and P3-ROC controllers
* Allow mode config files to be broken into multiple files
* Allow multiple multiball modes to run at once and add options for how it tracks them
* Allow ball locks to wait for a ball to drain before releasing their locked balls
* Added the ability to use matrix lamps/LEDs at individual channels for RGB LEDs
* Re-added high score mode (Which was in 0.21 and removed in 0.30)
* OPP platform improvements
* Improved error messages for config file errors
* Improved the way the "mpf both" command works on all platforms
* Added ability to step backwards in shows
* Refactored and improved show player
* Added ball search for servos
* Added default colors to RGB LEDs
* Added support for nested shows
* Added the "LED Group" device (am easily-configured strip of LEDs which can be strobed, pulsed, etc.)
* Added kickback mechanisms
* Added magnets
* Added blocking show queues
* Many bug fixes...

.. rubric:: MPF-MC

* Audio library improvements (sound fading, markers, start position, instance limiting,
  ducking improvements)
* Allow widget events based on when slides are shown, hidden, etc.
* Improved error if you try to target a widget to an invalid slide
* Added default DMD fonts
* Many bug fixes...

0.30
----

Released: July 15, 2016

* Python 3 required
* Mac OS X support
* The Media Controller is now a separate package from MPF
* The MPF-MC has been completely rewritten from scratch (based on Kivy, SDL2,
  OpenGL, and Gstreamer)
* GPU is used for graphics
* Brand-new audio interface specifically written for pinball audio, which
  includes advanced feature like ducking, attack, attenuation, etc.
* Proper Python package installers, and inclusion in PyPI so install can be done
  via *pip*.
* System-wide *mpf* launcher utility with pluggable commands
* New MPF clock module replaces the old timing and timers
* All shows are driven by MPF
* Show content is "played" by the standard config_players
* Playlists become shows
* "Tocks" are gone, shows now operate on real-world time
* Light scripts are gone, replaced by placeholder "tokens" in shows
* Named colors
* Hardware accelerated LED fades
* Asset Pools
* Ball Search
* Accelerometer-based tilts
* Servo support
* Text string support
* Player achievements

0.21
----

Released: Dec 1, 2015

* SmartMatrix "real" RGB LED Color DMD support.
* System 11 support.
* High Score mode.
* Credits mode.
* Tilt mode.
* Smart virtual platform. (This is the new default platform.)
* New display elements: Character Picker and Entered Characters.
* Devices can be created and changed per mode.
* Machine variables.
* Untracked player variables.
* Central config processor, data manager, file manager, and file
  interfaces. This paves the way for config files in formats other than
  YAML.
* Added support for combo manual/auto plungers.
* Events for ball collection process.
* Driver-enabled devices.
* External light shows, controllable via BCP. (Thanks Quinn Capen!)
* Created a starter game machine config template you can use for your
  own machines.
* Started adding unit tests. (We're at the very beginning of this, but
  we have full coverage of the ball device, the event manager, and the
  tutorial configuration files.)
* Rewritten driver/coil device interface.
* Rewritten ball device and ball controller code. (Thanks Jan
  Kantert!)
* Rewritten score controller.
* Rewritten display & slides modules.
* Many improvements and features added to ball saves.
* Python 2.7 is now required. (Previous releases would also run on
  Python 2.6)
* Logic blocks can now persist between balls
* Fixed & enhanced the asset loading process.
* Many improvements and features added to modes and the mode
  controller
* Multiple config files can be chained together at the command line
* Improved text display element.
* Improved event manager and event dispatch queue
* Moved all utility functions to their own class.

0.20
----

Sept 14, 2015

* The *targets* and *shots* modules have been combined into a single
  module called *shots*.
* The new shots module adds several new features, including:

  * Shots can be members of more than one shot group, and added and
    removed dynamically.
  * Sequence shots can track more than one simultaneous sequences. (e.g.
    two balls going into an orbit at essentially the same time will now
    count as two shots made.)
  * Shots are mode-aware and will automatically enable or disable
    themselves based on modes starting and stopping.

* Modes now work outside of a game.

  * “Machine modes” have been removed. Attract and game machine modes
    are now regular modes.
  * This makes it easier to have always-running modes (volume control,
    coin door open, coin & credit tracking).
  * This makes it possible to configure custom branching of mode-flow
    logic. (i.e. long-press the start button to load a different game
    mode, etc.)

* Significant performance improvements for both starting MPF and
  starting a game:

  * Reading the initial states of switches on a P-ROC is significantly
    faster.
  * The auditor now waits a few seconds before writing its audit file,
    and it does it as a separate thread. Previously this was slowing down
    the game start and player rotation events.
  * The way modules that need to track “all” the switches (like the
    auditor and OSC) was changed and now it doesn’t bog things down.

* A device manager now manages all devices. (This will enable future
  GUI apps to easily be able to browse the device tree.)
* Devices can be “hot added” and removed while MPF is running. This
  includes automatic support to add and remove devices per mode.
* All device configuration is specified and validated via a central
  configuration service. This has several advantages:

  * The config files are now validated as they’re loaded. For example,
    if there a device has a settings entry for “switches”, MPF will now
    validate that the strings you enter in the are actual switch names. It
    will give you a smart error if not.
  * This paves the way for supporting config files in formats other than
    YAML. (JSON, XML, INI, etc.)
  * This led to the removal of about 500 lines of code since all the
    config processing was done manually in each module before.
  * The config processing is more efficient and less-error prone since
    it’s not written from scratch for each module.
  * There’s now a master list (in `mpfconfig.yaml`) of all config
    settings for all device types.
  * The config processor and validator can run as a service to support
    the back-end business logic behind future GUI tools which could be
    used to build machines.
  * If you’re configuration has an unrecognized setting, the config
    validator will load the config file migrator to tell you what the
    updated name is for the section it doesn’t recognized.

* Shot rotation has been improved:

  * You can now specify the states of shots you’d like to include or
    exclude. (i.e. only rotate between incomplete shots.)
  * You can specify custom rotation patterns (i.e. a “sweep” back-and-
    forth instead of a simple left or right rotation)

* A ball lock device was added to make it easy to specify ball locks.
* A multiball device was added.
* A simple ball save device was added.
* Created a “random_event_player” that lets you trigger random events
  based on another event being posted.
* Centralized debugging
* Drop targets and drop target banks have been simplified and
  separated from shots.
* The states of switches tagged with ‘player’ will be passed to the
  game start mode, allowing branching based on which combinations of
  switches were held in when the start button was pressed. (The amount
  of time the start button was held in for is also sent.)
* Official support for multiple playfields via config files
* Added x, y, and z positions to lights and leds
* Exposed wait queue events to mode configs, allowing code-less
  creation of modes that can hook into game flow (bonus, etc.)

0.19
----

Released: August 6, 2015

* Completely rewritten target and drop target device module,
  including:

  * Per-player state tracking for targets
  * Target “profiles” that control how targets behave, completely
    integrated with the mode system

* Light show “sync_ms” which allows new light shows to sync up with
  existing running shows.
* Timed switch events can be set up via the config files.
* Added “recycle_time” to switches. (Switches can be configured to not
  report multiple events until a cool-down time has passed.)
* Created an events_player module
* Player variables in slides automatically update themselves when they
  change. (No more need to find an event to tie the slide to in order
  for it to update!)
* Device control events exposed via the config files
* Automatic control of GI
* Activation and deactivation events can be automatically created for
  every switch.
* Allow multiple playfield objects to be created at once (for head-to-
  head pinball)
* Added support for FAST Pinball’s new WPC controller
* Added a Linuxshell script to launch mc.py and mpf.py
* Created the config file migration tool
* Added per-timer debug loggers
* Standardization of many non-standard config file naming conventions
* Color logging to LEDs
* Added P3-ROC switch test tool
* Added reset to mode timer action list
* Added restart feature to mode timers
* Flipper Device: Add debug logging to rules
* FAST:Added minimum firmware version checking for IO boards
* Added “restart” method to logic blocks
* Text display element min_digits
* Allow system modules to be replaced and subclassed
* Added configurable event names for switch tag events
* Added callback kwargs to switch handlers
* Added light and LED reset on machine mode start
* Added default machine and mode delay managers

0.18
----

Released: June 2, 2015

* FadeCandy and Open Pixel Control (OPC) support. This means you can
  use a FadeCandy or other OPC devices to control the LEDs in your
  machine.
* Rewritten FAST platform interface. It’s now “driverless,” meaning
  you no longer need to download and compile drivers to make it work.
* Added support to allow multiple hardware platforms to be used at
  once. (e.g. LEDs can be from a FadeCandy while coils are from a
  P-ROC.) You can even use multiple different platform interfaces for
  the same types of devices at once (e.g. some LEDs are FadeCandy and
  others are FAST).
* Added support for GI and flashers to light shows
* Added activation and deactivation events to switches
* Added support for sounds in media shows
* Added per-sound volume control
* Added support for P-ROC / P3-ROC non-debounced switches
* Exceptions and bugs that causeMPF to crash are now captured in the
  log file. (This will be great for troubleshooting since you can just
  send your log. No more needing to capture a screenshot of the crash.)
* If a child thread crashes, MPF will also crash. (Previously child
  threads were crashing but people didn’t know it, so things were
  breaking but it was hard to tell why.)
* MPF can now be used without switches or coils defined. (Makes
  getting started even easier.)
* “Preload” assets loading process is tracked as MPF boots, allowing
  display to show a countdown of the asset loading process
* Added *restart_on_complete* to mode timers
* Smarter handling of player-controlled eject requests while existing
  eject requests are in progress
* *eject_all()* returns *True* if it was able to eject any balls
* Playfield “add ball” requests are queued if there’s a current player
  eject request in progress
* Created a smarter asset loading process
* The attract mode start is held until all the “preload” assets are
  loaded
* Updated how the game controller tracks balls in play

0.17
----

Released: May 4, 2015

* Broke MPF into two pieces: The MPF core engine and the MPF media
  player
* Added support for the Backbox Control Protocol (BCP)
* Added device-specific debugging for LEDs.
* Added version control to config files.
* Added volume control.
* Switches that you want to start active when using virtual hardware
  are now added to the `virtual platform start active switches:` section
  instead of being a property of the `keyboard:` entry.
* Converted several former plugins to system modules, including shots,
  scoring, bcp, and logic blocks.
* General performance improvements. (Running MPF on my machine used to
  take about 50% CPU. Now it’s down to 15%.)

0.16
----

Released: April 9, 2015

* Added slide "expire" time settings to the Slide Player.
* Added *Demo Man* as the sample game code.
* Added start_time configuration parameter for music in the
  StreamTrack
* Added the SocketEvents plugin
* Created the LightScripts and LightPlayer functionality.
* Change light script "time" to "tocks"
* Created a centralized config processing module

0.15
----

Released: March 9, 2015

* Added support for game modes.
* Converted several existing modules to be mode-specific, including:

  * LogicBlocks
  * SoundPlayer
  * SlidePlayer
  * ShowPlayer
  * Scoring
  * Shots

* Created an Asset Manager and converted the images, animations,
  sound, and show modules to use it instead of each handling their own
  assets.
* Created an asset loader which creates a background thread to load
  each type of asset.
* Added an AssetDefaults section to the asset loader to specify per-
  folder asset settings
* Created a universal player variable system
* Added movie support (for playing MPEG videos on the LCD and DMD).
  They're available as a standard display element type which means they
  can be positioned, layered as backgrounds, etc.
* Created a generic ModeTimers class that can be used for timed modes
  and goals. (With variable count rates, support for counting up and
  down, multiple actions which can start, stop, pause, and add time,
  etc.)
* Changed logic blocks so they maintain all their states and progress
  on a per-user basis.
* Added a "double zero" text filter. (Used to show zero-value scores
  as "00" instead of "0".)
* Updated the display code so that it doesn't show a slide until all
  that slides assets have been loaded.
* Renamed the "sphinx" folder to "docs".
* Broke the three phases of machine initialization into 5 phases.
* Created the mode timer
* Renamed the "HitCounter" logic block to "Counter" and updated it to
  be more flexible so it can track general player-specific counts (both
  up and down), for example, total shots made, combos, progress towards
  goals, etc.
* Changed window section of config so it uses the slide builder.
* Added the ability to control lights and LEDs by tag name in shows.
* Modified the switch controller so events from undefined switches
  simply log a warning rather than raises an exception and halting MPF.

0.14
----

Released: February 9, 2015

* Completely rewritten ball controller.
* Completely rewritten ball device code.
* Major updates to the diverter device code.
* Creation of a new playfield module that's responsible for managing
  the playfield and any balls loose on it.
* Completely rewrote the "player eject" logic. (This is what happens
  when the game needs to wait for the player to push a button to eject a
  ball from a device.)
* The ball search code was moved from the game controller to the
  playfield device module.
* Different types of events were broken out into their own methods.
  For example, to post a boolean event, instead of calling
  `event.post(type='boolean')`, you now use `event.post_boolean()`.
  There are similar new methods for other event types, like
  `post_relay()` and `post_queue()`.
* Added a debug option for ball devices which enables extra debug
  logging for problem devices.
* Tilt status was removed from the machine controller. (It was
  inappropriate there. Tilt is a game-specific thing, not a machine-
  specific thing.)
* Virtual Platform: default NC switch states fixed

0.13
----

Released: January 16, 2015

* Major update to the sound system, including:

  * Support for multiple sound tracks ("voice", "sfx", "music", etc.),
    each with their own channels, settings, volume, etc.
  * Using background threads to automatically load sound files from disk
    in the background without slowing down the main game loop.
  * Support for streaming sounds from disk versus preloading the entire
    sounds in memory.
  * Support for sound priorities and queues, so sounds can pre-empt
    other sounds if they have a higher priority.
  * System-wide volume control with settable steps.

* Support for the v1.0 update of FAST Pinball's libfastpinball
  library. (Basically we updated the FAST platform interface to support
  their latest firmware and drivers)
* Support for flashers. (Previously flashers were just driven like any
  other driver. Now they are their own device with their own flasher-
  specific settings.)
* Game Controller: Changed the player rotate routine to be driven from
  the game_started event so the player object isn't actually set up
  until the game has finished being set up.
* Pygame: Moved the Pygame event loop to the machine controller and
  out of the window manager. This lets us use Pygame events even if we
  don't have an on screen window. (This is needed for the sound system.)
* Display: Moved the SlideBuilder instantiation earlier in the boot
  process so it's available to other modules who want to use it when
  they're starting up. This will let us get the "loading" screen up
  earlier in the boot process.
* Switch Controller: Added a method to dump the initial active states
  of switches to the log. This is needed for our automated log playback
  utility so it can set the initial switches properly.
* Ball Devices: fixed a typo on the cancel ball request event

0.12
----

Released: December 31, 2014

* Added full display and DMD support, with support for physical DMDs,
  on screen virtual DMDs, color DMDs, and high res LCD displays.
* Added transitions which flip between display slides with cool
  effects.
* Added decorators which are used to "decorate" display elements (make
  them blink, etc.)
* Added display support to shows so that shows can now combine display
  and lighting effects
* Added a Slide Builder which can assemble slides from text, image,
  animation, and shapes from shows and the config files.
* Added a SlidePlayer config setting which can show slides based on
  MPF events
* Modified the Virtual DMD display element so that it can render on
  screen DMDs that look more like real pixelated DMDs
* Added a font manager that lets you define font names and specify
  default settings (sizes, antialias, color, etc.)
* Added TrueType font support
* Added support for stand image types to be displayed on the DMD
* Added .dmd file type support for images and animations
* Addedthe OSC Sender tool
* Added the Font Tester tool
* Added the multi-language module which can replace text strings with
  alternate versions for multi-language environments and other (e.g.
  "family-friendly") text replacements
* Improved the diverter devices so they have knowledge of what ball
  devices and diverters are upstream and downstream, allowing them to
  automatically activate and deactivate based on where balls need to go.
* Improved the ball device class so ball devices are smarter about how
  they interact with target devices. (e.g. a ball device will
  automatically eject a ball if its target device wants a ball.)
* Added support for the P3-ROC
* Added many more events
* Modified displays so they can each have independent refresh rates

0.11
----

Released: December 1, 2014

* Created a Display Controller module which is responsible for
  handling all interactions with all types of displays, including DMD,
  LCD, alphanumeric, 7-segment, etc.
* Created a DMD display module which controls both physical DMDs as
  well as on screen representations of physical DMDs
* Created a Window Manager, a centralized module which manages the on
  screen window, including full screen and resizable support
* P-ROC platform interface: Built the DMD control code
* FAST platform interface: Built the DMD control code
* Switched from Pyglet to Pygame
* Created a Sound Controller
* Created a Game Sounds plug-in that lets you control which sounds are
  played and looped based on MPF events
* Added PD-LED support
* Added support for P3-ROC SW-16 switch boards
* Switch Controller: Added verify_switches() method which verifies
  that switches are in the hardware state that MPF expects.
* Switch Controller: Adding logging so it can track when duplicate
  switch events were received
* LEDs: added on() and off() methods and "default color" support
* Ball Device: created _ball_added_to_feeder() and made it so the
  device watches for a ball entering and will request it if it needs it.
* Changed the command line options so you don't have to specify the
  .yaml extension for your configuration file
* Changed the command line options so you (optionally) don't have to
  specify the "machine_files" folder location
* Created default machine_files folder location settings in the config
  file
* Added support for absolute or relative paths in the command line
  options
* Added support for X/Y coordinates to LEDs and Lights for future
  light show mapping awesomeness.
* Created an early, early version of the Playfield Lights display
  interface which lets you "play" Pygame shows on your playfield lights
* Added system default font support
* Added a player number parameter to the player_add_success event
* Added a default MPF background image for the on screen window
* Added many more default settings to the system default
  mpfconfig.yaml file
* Virtual platform interface: Updated it so that it works when
  hardware DMDs are specified in the config files

0.10
----

Released: October 25, 2014

* Added enable_events, disable_events, and reset_events to devices.
* Removed the First Flips plug-in. (Since the thing above replaces it)
* Added support for network switches and drivers for FAST Pinball
  controllers.
* Added support for multiple USB connections to FAST Pinball
  controllers to separate main controller traffic from RGB LED traffic.
* Changed default debounce on and off times to 20ms for FAST Pinball
  controllers.
* Individual targets hit in target groups will now post events
* Changed the default show priority to 1 so it will restore lights
  that weren’t set with a priority by default
* Driver: Added a power parameter to driver.pulse()
* Score Reel: Added resync events to individual reels
* Score Reel: Changed repeat_pulse_ms config setting to
  repeat_pulse_time.
* Score Reel: Changed hw_confirm_ms config setting to hw_confirm_time.
* Changed default pulse time for all coils to 10ms
* Coils: (Fast): Added separate debounce_on and debounce_off settings
* Info Lights: Forced game_over light to off when game starts
* LEDs: Added force parameter to the off() method

0.9
---

Released: October 7, 2014

* Added a “Logic Blocks” plug-in which lets game programmers build
  flowchart-like game logic with the config files. No Python programming
  required!
* Created a “First Flips” plug-in which you can use to get your
  machine flipping as fast as possible. (This was written as part of our
  Step-by-Step Tutorial for getting started with MPF.)
* Added Tilt and Slam Tilt support. (This is built via our Logic
  Blocks, so they’re very advanced, supporting grouping multiple quick
  hits as a single hit, settling time (to make sure the plumb bob is not
  still swinging when the next ball is started, etc.).
* Added Extra Ball / Shoot Again support
* Created OSC interfaces for /audits
* MAJOR rewrite to the ball controller and ball device modules
* Created a non-instrumented optimized software loop which is as lean
  as possible if you’re running your game on a slow computer. (I’m
  looking at you Raspberry Pi!) Note: other single board computers are
  fine, like the BeagleBone Black or the ODOID, but man the Pi is slow.
* Added the ability to pull “data” from MPF via the OSC interface, so
  we can put player scores, ball in player, etc. on an iPhone, iPad, or
  Android device.
* Added an OSC audit interface so you can view audit data via your
  mobile device.
* Created an “Info Lights” plug-in which turns on or off lights
  automatically based on things that happen in the game. (Which player
  is up, current ball, tilt, game over, etc.) This is typically used in
  EM games, but of course the plug-in can be used wherever you need it.
* Finished the code for our Big Shot EM-to-SS conversion. This is
  included as a sample game in MPF, so you can see our config files and
* Logic Blocks which can be helpful when creating your own game.
* Fixed up drop targets to support the new lit/unlit scheme
* Added support for default states to targets and target groups (stand
  ups, rollovers, drop targets, etc.), including events that are posted
  when they are hit while lit or unlit, and the ability to light or
  unlight them via events
* Added Start Button press parameters which are automatically sent to
  the game when the start button is pressed. This is for things like how
  long the button was held and what other buttons where active at the
  time. (Start * Right Flipper, etc.)
* Added a “pre-load check) to plug-ins that allows them to test
  whether they’re able to run before they load and only load if
  everything checks out. (This means that a plug-in will no longer crash
  if a required Python module is missing.)
* Added ‘no_audit’ tag support. (If you add ‘no_audit’ as a tag to a
  switch, then the Auditor will not include that switch in the audit
  logs.)
* Created Action Events for shutting down the machine and added
  shutdown tag support (so you can cleanly shut down the machine simply
  by posting and event or pressing a button which is tagged with
  “shutdown”)
* Added performance data logging to the machine run loop (so it now
  tracks the percentage of time spent doing MPF tasks, hardware tasks,
  and idle).
* Added a reload() method to Shows which causes that show to reload
  itself from disk. This is nice for testing shows since you can reload
  them without having to restart the machine each time.
* Added support for null steps in shows (literally a step that
  performs no action). This makes it easier to get timing right for
  music shows.
* Added the ability to force a light or LED to move to a given state,
  regardless of its current priority or cache.
* Added a method to test whether a device is valid. This will be used
  for our config file validator
* Added option for restart on long start button press
* Added option to allow game start with loose balls
* Score reels maintain a valid status, allowing other modules to know
  whether the score reels are showing the right data or not.
* Score reels now post an event when they’re resyncing, allowing other
  modules to act on it. (For example the score reel controller uses this
  to turn off the lights for a score reel while it’s resyncing.)
* Added option to remove all handlers for an event regardless of what
  their registered \**kwargs are.
* Added mpf command line options for verbose to console and optimized
  loops. (Now we can support different logging levels to the console and
  log file, meaning you can configure it so you only see important
  things on the console but you can see everything in the log file.)
* Added light on/off action events
* Added action events and methods to award the extra ball
* Created ball device disable_auto_eject() and enable_auto_eject()
  methods. This is how we handle player-controlled ejects (like when a
  ball starts or they’re launching a ball out of a cannon).
* Changed scoring from “shots” to “events”
* Changed the hardware rules for clearing a rule so it disables any
  drivers that were currently active from that rule
* Updated are_balls_gathered() so that if you pass it a tag which
  doesn’t exist, it always returns True
* Added management of switch handlers to machine modes so they can be
  automatically removed
* Changed switch handlers so they process delays from new handlers
  that are added
* Removed “standup” target device type (it was redundant with
  “target”)
* Moved auditor, scoring, and shots out of system and into plugins

0.8
---

Released: September 15, 2015

* Platform support for FAST Pinball hardware
* RGB LED support, including settings colors and fades
* Created target and target group device drivers for drop targets,
  standups, and rollovers (including events on complete, lit shot
  rotation, etc.)
* Created an OSC interface to view & control your pinball machine from
  OSC client software running on a phone or tablet
* Changed our “light controller” to a “show controller” and added
  support for things other than lights (like coils and events). So now a
  show can be a coordinated series of lights, RGB LEDs, coil firings,
  and events.
* Created an “event triggers” plugin which lets you configure series
  of switches that trigger events, including custom timings, decays, and
  resets. (We use this for our titlt functionality but it’s useful in
  other ways too.)
* Created the auditor module
* Created an intelligent diverter device driver (with hardware switch
  trigger integration)
* Created GI device drivers
* Created a system-wide MPF ‘defaults’ configuration file
* Created templates for new machines, new scriptlets, and new plugins
* Modified the on screen window to become a “real” LCD display plugin.
* Renamed “hacklets” to “scriptlets”
* Created a scriptlet parent class to make them even easier to use
* Broke the hardware module into “platforms” and “devices”
* Major rewrite of how the machine controller loads system modules and
  devices
* Shows now auto load
* Added the ability to attach handlers to lights so you can receive
  notifications of light status changes
* Reworked the EM score reel update process to simplify and streamline
  it

0.7
---

Released: September 4, 2014

* Support for lights and light shows.
* An on-screen display of game metrics like score, player, and ball
  number.
* A “hacklet” extension architecture which lets you add python code to
  finish up the “last 10%” of your game that you can’t control via the
  machine configuration files.
* A formal plug-in architecture which allows easy creation and
  modification of plug-ins that will survive core MPF framework updates.
* Cleaned up the machine flow and made that controllable via the
  config files
* Changed the -x command line option so it doesn’t use fakepinproc,
  got rid of the p_roc methods that detected fakepinproc. (Now even with
  the P-ROC platform it will use our virtual platform interface when no
  physical hardware is present. This means you don’t need pyprocgame to
  use fakepinproc.
* Changed the command line options to break out machine root from
  config files
* Moved command line options to their own python dictionary
* Changed time.clock() back to time.time() since clock was not real
  world which affected the light shows
* Created new events to capture start and stop of machine flow modes
* Added light support to P-ROC platform interface
* Reorganized the machine files into machine-specific subfolders
* Created an int_to_pwm() static method in Timing

0.6
---

Released: August 19, 2014

* Addition of a Shot Controller, allowing you to configure and group
  switches which become shots in the machine. (Read more about the
  concept of shots in our blog post from last week.)
* Addition of a Scoring Controller, allowing you to map score values
  to shots (and general scoring support for the machine).
* Addition of the Score Reel Controller, Score Reel devices, and Score
  Reel Group devices for mechanical score reels in EM-style machines.
  (Details here.)Switched entire framework timing over to real time
  system clock times (time.clock()) instead of ticks (for delays, tasks,
  switch waits, etc.)
* Changed ball controller that if it counts more balls than it thought
  it had, it will invoke ball_found()
* Changed the switch controller so it will ignore new switch events if
  they come in with the current status the switch already is
* The switch controller will ignore repeat switch events from the
  hardware if they are the same state that the switch was in before
* Added chime support for EM-style machines
* Changed game_start event to a queue
* Change game_start event name to game_starting (some of these entries
  might seem trivial, but I also use this list to track the changes I
  need to make to the documentation)
* Created a queue for adding new tasks so our set won’t change while
  iterating

0.5
---

Released: August 5, 2014

* Created a single device parent class that’s used for all devices.
* Rewrote and cleaned up devices. Now coils, switches, and lights are
  all devices, as are the more complex ones.
* Added “events” to the keyboard interface. This means you can use the
  keyboard to post MPF events (along with parameters).
* Separated out ball live confirmation and valid playfield
* Built a bunch of valid playfield methods
* Changed ball_add_live_request from direct calls to events so they’d
  be slotted in properly
* Broke valid playfield out into its own module
* Made the ball device “entrance” switch work
* Built a quick “coil test” mode
* Added kwargs to event handlers (meaning you can register a handler
  with kwargs)
* Figured out how to handle the “first time” counts of ball devices
* Added checks to attract mode to make sure all balls are home, and to
  the ball controller to prevent game start if all balls are not home
* Changed ejects to events. (So if you want to request that a device
  ejects a ball, you post an event rather than calling the device)
* Changed the balldevice_name_eject_request to be the event you use to
  call it, rather than the notification of the eject attempt.
* Created a get_status() method for ball devices
* Created a gather_balls() method and wrote the code that will send
  all the balls home before a game can be started.
* Updated stage_ball() code so it didn’t ask for another ball if there
  was already an eject in progress
* Moved detection of how balls fall back in out of devices and into
  the events that watch for the entrance
* Create player and event based ejects. (This is a system to allow
  players or events to eject balls from ball devices. Useful for cannons
  like in STTNG.)
* Got stealth and auto eject out of the ball device code since they
  shouldn’t care about that.
* Rewrote a lot of the ball device stuff.
* Added a manual eject capability for devices without eject coils
* Moved around some things between the ball controller and ball
  devices so that everything lives where it ‘makes sense’
* Added method to check whether an event has any handlers registered
  for it.
* Ball devices now post events based on tags when balls enter them
* Ball devices can now eject their ball if no event is registered.
  This will prevent balls from getting “stuck” in unconfigured devices
  and will make prototyping on new machines faster.
* Changed event logging to show “friendly” names of handlers
* Converted flippers to use a config dictionary instead of variables
* Cleaned up the eject confirmation and valid playfield functionality
* Added a remove_switch_handler method to the switch controller

0.4
---

Released: July 25, 2014

* MAJOR rewrite of how the hardware platform modules interact with the
  framework’s hardware module and how hardware is configured in general.
  It’s way simpler and cleaner now. :)
* Created a parent class for Devices
* Cleaned up the way hardware objects use their parent class
* Fixed the ball controller so it doesn’t get confused on the initial
  count after machine start up.
* Cleaned up switch processing and added a logical parameter so we
  only have to do all the conversion for NC or NO in one place
* Renamed the none interface to virtual. Rewrote it with the new
  platform interface way of working.
* Added support for holdPatter in coils
* Change add_live() to use tags instead of the plunger device
* Made it so many things, like ball search, autofires, etc. would not
  crash the machine if they weren’t there.

0.3
---

Released: July 16, 2014

* Changed the way config files are loaded by making Config a normal
  section of any config file instead of using a special initial
  configuration file that did nothing but point to additional files.
  Details here.
* Created a virtualhardware platform for virtual / software only
  testing that does not require P-ROC or FAST drivers.

0.2
---

Released: July 11, 2014

* Added docstring documentation
* Added /sphinx folder and got the sphinx html docs included
* Created the first version of the documentation

0.1
---

Released: June 27, 2014

* Command line parameters to select real or fake (simulated)
  controller hardware.
* Command line parameters to select logging level
* Command line parameters to select the location of the initial config
  file
* Reads an initial config file which is a list of additional config
  files
* Processes those config files in order to build a config dictionary
* All platform-specific hardware code is isolated into its own module.
  Config files specify which platform is used. All game code is
  100%interchangeable between platforms.
* Game loop runs with configurable loop rate. System timer tick event
  is raised every tick.
* Periodic and one-time use timers can be setup
* Switches, Coils, Lamps, and LEDs are read in and configured from the
  config files
* Switch events are read from the hardware
* Driver commands can be sent to the hardware
* Autofire drivers are automatically configured from the config files.
  They can be enabled, disabled, and reconfigured as needed.
* Flippers are automatically configured based on config files. They
  can use EOS or not, and be based on two coils (main/hold) or one coil
  with pulse+pwm. Multiple coils can be connected to the same switch,
  and vice-versa.
* The computer keyboard can be used to simulate switch presses. Key
  map configuration information is stored in the config dictionary. It
  supports momentary, toggle (push on / push off), and inverted (key
  press = open) key modes. Also supports combo key mapping (Shift, Ctrl,
  etc.)
* A switch controller receives all notifications of debounced hardware
  switch events.
* Can specify timed switch modes that trigger certain methods. (i.e.
  do blah() when switch_1 is active for 500ms.)
* Event manager handles system events, including registering handlers,
  priorities, aborting events, and maintaining a queue.
