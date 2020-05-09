How to configure servos (FAST Pinball)
======================================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/servos`                                                        |
+------------------------------------------------------------------------------+

You can drive servos from any FAST IO board by adding the FAST Servo Controller
daughter board to it. You then configure and use the servos like normal. The
only real "FAST-specific" thing is the number.

number:
-------

The number of the servo requires a bit of math. Each FAST IO board "reserves"
six slots for daughter board accessories (regardless of whether there's a
daughter board there are not). So the numbers go like this:

* First board in the chain (Board 0), numbers 0, 1, 2, 3, 4, 5
* Second board in the chain (Board 1), numbers 6, 7, 8, 9, 10, 11
* Third board in the chain (Board 2), numbers 12, 13, 14, 15, 16, 17
* Fourth board in the chain (Board 3), numbers 18, 19, 20, 21, 22, 23
* etc.

So to figure out the number for your servo, first figure out which board it's
plugged into, then look at which connection on that board it uses, then figure
out the number based on the list above.

By default, standalone numbers like this have to be entered in hex format, so
once you find your number, enter it as the hex equivalent:

======= ===
Regular Hex
======= ===
0       0
1       1
2       2
3       3
4       4
5       5
6       6
7       7
8       8
9       9
10      a
11      b
12      c
13      d
14      e
15      f
16      10
17      11
18      12
19      13
20      14
21      15
22      16
23      17
======= ===

If you don't want to mess with all this hex stuff, you can set the config
number format to "int" via the ``fast: config_number_format:`` setting. See
the :doc:`/config/fast` section of the config file reference for details.

What if it did not work?
------------------------

Have a look at our :doc:`FAST troubleshooting guide <troubleshooting>`.
