---
title: Controlling an existing machine with MPF
---

# Controlling an existing machine with MPF

If you want to use MPF to write your own custom game code for an
*existing* pinball machine, some pinball controller allow you to replace the original
CPU board in the machine with a modern pinball controller board (called
a *hardware controller*). That hardware controller interfaces with
the existing machine's driver boards to control the coils, lights, and
DMD, and it provides a "bridge" (via USB) to a host computer running
Python and the Mission Pinball Framework.

| Machine Type                                                                         | FAST | P-ROC       | LISY | Direct |
|--------------------------------------------------------------------------------------|:----:|:-----------:|:----:|:------:|
| [Williams / Bally / Midway WPC](../hardware/existing_machines/wpc.md)                | :white_check_mark: | :white_check_mark: | |  |
| [Williams / Bally System 11](../hardware/existing_machines/system11.md)              | :white_check_mark: |      |        |
| [Data East](../hardware/existing_machines/data_east.md)                              |      |             |      |        |
| [Stern S.A.M.](../hardware/existing_machines/sam.md)                                 |      |             |      |        |
| [Stern Whitestar](../hardware/existing_machines/whitestar.md)                        |      |             |      |        |
| [Pinball 2000](../hardware/existing_machines/pinball2000.md)                         |      |             |      |        |
| [Stern SPIKE / SPIKE 2](../hardware/existing_machines/spike.md)                      |      |             |      | :white_check_mark: |
| [Gottlieb System 1](../hardware/existing_machines/gottlieb_system1.md)               |      |             | :white_check_mark: |        |
| [Gottlieb System 80](../hardware/existing_machines/gottlieb_system80.md)             |      |             | :white_check_mark: |        |
| [Bally/Stern w/ AS-2518-17 or AS-2518-35 MPU](../hardware/existing_machines/bally_stern_as_2518.md) | |   | :white_check_mark: |        |

Notes:

* "WPC" includes WPC-S and WPC-95, and machines made under the
    brands of Williams, Bally, and Midway. (A complete WPC game list is
    [here](http://www.pinwiki.com/wiki/index.php?title=Williams_WPC#Game_List).)
* Since Stern SPIKE systems have a linux-based computer inside them
    already, so
    [user forum</faq/help/index](MPF can directly connect to and control them via USB</hardware/spike). No additional hardware is needed.
* Gottlieb System 1 and 80 can be controlled using the
    [user forum</faq/help/index](LISY platform</hardware/lisy)
* Bally and Stern Games manufactured from 1977 to 1985 with MPU
    AS-2518-17 or AS-2518-35 can be controlled using
    [LISY35](../hardware/lisy/index.md)

If you want to use MPF with an existing machine type that's not on the
list above, that's still possible, but you'd have to rewire the entire
machine and use modern control hardware. In other words, you strip the
guts and keep all the hardware, and the machine essentially becomes a
homebrew machine on the inside and a retheme or update on the outside.
