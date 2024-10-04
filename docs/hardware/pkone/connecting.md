---
title: Connecting PKONE to your Computer
---

# Connecting PKONE to your Computer


This page is about connecting the PKONE system to your computer. It
roughly covers connecting the bus between the boards.

## PKONE Nano

Connect your PKONE NANO controller to your PC using USB.

![image](/docs/hardware/images/pkone-nano.png)

Then connect the OUT port of your NANO to the IN port of your first
board (Extension or Lightshow). Consequently, connect the OUT port of
the first board to the IN port of your second board (etc.). Be sure each
Extension board or Lightshow board has a unique Address ID set using the
Address ID switches on each board. Finally, be sure the last board in
the chain has the CANBUS Protocol Termination Jumper set to properly
terminate the bus.

Notes:

* Address ID values are numbered starting with zero (Extension
    boards have addresses 0 to 7 while Lightshow boards have addresses
    0 to 3).
* An Extension board cannot have the same Address ID number as a
    Lightshow board (all connected boards must have unique Address ID
    values).
* You do not have to chain the boards in the same order as their
    Address ID numbers.
