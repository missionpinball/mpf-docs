---
title: Using MPF with existing pinball machines (Williams, Stern,
  Gottlieb, etc.)
---

# Controlling Pinball Machines with MPF

There are three options when it comes to using MPF with a pinball
machine:

* Build your own new machine completely from scratch.
* Rewrite the rules for an existing machine, which means you don't
    change the physical hardware at all, rather, you just update the
    software.
* "Retheme" an existing machine, which means you reuse all of the
    mechanical and electrical components of an existing machine, but you
    strip down and replace all the artwork to transform it into
    something else. (And you rewrite all the rules for your new theme.)

Here are more details on each option. The "rewrite the rules" and
"retheme" options above are combined below into the "controlling an
existing machine" section:

MPF supports all kinds of pinball machines. In this section, we
highlight how to connect and configure existing machines with MPF.

* [Williams, Bally, Midway WPC, WPC-S, WPC-95](wpc.md)
* [Williams, Bally System 11](system11.md)
* [Gottlieb System 1](gottlieb_system1.md)
* [Gottlieb System 80](gottlieb_system80.md)
* [Data East](data_east.md)
* [Stern Whitestar](whitestar.md)
* [Stern SAM](sam.md)
* [Stern SPIKE / SPIKE 2](spike.md)
* [Pinball 2000](pinball2000.md)
* [Williams System 3 to 9](williams_system3_to_9.md)
* [Bally/Stern with AS-2518-17 or AS-2518-35 MPU](bally_stern_as_2518.md)

If you want to use MPF to write your own custom game code for an
*existing* pinball machine, some pinball controller allow you to replace the original
CPU board in the machine with a modern pinball controller board (called
a *hardware controller*). That hardware controller interfaces with
the existing machine's driver boards to control the coils, lights, and
DMD, and it provides a "bridge" (via USB) to a host computer running
Python and the Mission Pinball Framework.

| Machine Type                                                                         | FAST | P-ROC       | LISY | Direct |
|--------------------------------------------------------------------------------------|:----:|:-----------:|:----:|:------:|
| [Williams / Bally / Midway WPC](wpc.md)                | :white_check_mark: | :white_check_mark: | |  |
| [Williams / Bally System 11](system11.md)              | :white_check_mark: |      |        |
| [Data East](data_east.md)                              |      |             |      |        |
| [Stern S.A.M.](sam.md)                                 |      |             |      |        |
| [Stern Whitestar](whitestar.md)                        |      |             |      |        |
| [Pinball 2000](pinball2000.md)                         |      |             |      |        |
| [Stern SPIKE / SPIKE 2](spike.md)                      |      |             |      | :white_check_mark: |
| [Gottlieb System 1](gottlieb_system1.md)               |      |             | :white_check_mark: |        |
| [Gottlieb System 80](gottlieb_system80.md)             |      |             | :white_check_mark: |        |
| [Bally/Stern w/ AS-2518-17 or AS-2518-35 MPU](bally_stern_as_2518.md) | |   | :white_check_mark: |        |

Notes:

* "WPC" includes WPC-S and WPC-95, and machines made under the
    brands of Williams, Bally, and Midway. (A complete WPC game list is
    [here](http://www.pinwiki.com/wiki/index.php?title=Williams_WPC#Game_List).)
* Since Stern SPIKE systems have a linux-based computer inside them
    already, so can directly connect to and control them via USB. No additional hardware is needed.
* Gottlieb System 1 and 80 can be controlled using the
    LISY platform
* Bally and Stern Games manufactured from 1977 to 1985 with MPU
    AS-2518-17 or AS-2518-35 can be controlled using
    [LISY35](../hardware/lisy/index.md)

If you want to use MPF with an existing machine type that's not on the
list above, that's still possible, but you'd have to rewire the entire
machine and use modern control hardware. In other words, you strip the
guts and keep all the hardware, and the machine essentially becomes a
homebrew machine on the inside and a retheme or update on the outside.
