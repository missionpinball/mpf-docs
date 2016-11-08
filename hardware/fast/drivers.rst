How to configure coils/drivers/magnets (FAST Pinball)
=====================================================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/fast`                                                          |
+------------------------------------------------------------------------------+
| :doc:`/config/coils`                                                         |
+------------------------------------------------------------------------------+

To configure coils, drivers, motors, and/or magnets (basically anything connected to an
IO board's driver outputs) with FAST Pinball hardware, you can follow the guides
and instructions in the :doc:`/mechs/coils/index` docs.

However there are a few things to know and some additional options you get
with FAST hardware that is discussed here.

number:
-------

When you're using FAST IO boards, drivers plug into individual IO boards.
Then the IO boards are connected together in a loop.

The ``number:`` setting for each driver is its board's position number in the
chain, then the dash, then the driver output number. Note that the position
number starts with zero, so the first IO board in the chain is 0, the second
is 1, etc.

::

   coils:
      my_coil:
         number: 0-0  # first board, driver 0
      some_other_coil:
         number: 2-14  # third board, driver 14

Notes:

   * The first board in the chain is board 0.
   * The boards are counted in the direction of the "out" connector on the
     controller board.
   * Different models of IO boards have different numbers of drivers, and
     MPF will make sure that the numbers work for each type of board. (e.g.
     a driver number 10 isn't valid on an 0804 board since that board only has
     4 drivers numbered 0-3).

Also note that prior versions of MPF just numbered all the drivers in one
continuous sequence from the first board through the last, but that was
confusing. You can still do that if you want (in either hex or integer format),
but we feel the board-input format is much easier to understand.

Pulse Power
-----------

In the :doc:`/mechs/coils/index` section of the documentation, we talked about
:doc:`how adjusting a coil's pulse time can affect its strength </mechs/coils/pulse_power>`.
Adjusting the coil's pulse times still assumes that 100% power will be applied
to that coil during that pulse time.

However, FAST Pinball controllers allow you to specify the power that's applied
to the coil during the initial pulse time. This is similar to the
:doc:`/mechs/coils/hold_power`, except it applies to the initial pulse time
instead of the extended hold time.

You can configure the pulse power by adding a ``pulse_power:`` setting to
a coil definition and then specifying the power value from 0-8. (Like hold
power, 8 is 100%, 4 is 50%, etc.)

For example, consider the following configuration:

::

    coils:
        some_coil:
            number: 1-3
            pulse_ms: 30
            pulse_power: 4

When MPF sends this coil a pulse command, the coil will be fired for
30ms at 50% power. You can even combine pulse_power and hold_power,
like this:

::

    coils:
        some_coil:
            number: 1-3
            pulse_ms: 30
            pulse_power: 4
            hold_power: 2


In this case, if MPF enables this coil, the coil will be fired at 50%
power for 30ms, then drop down to 25% power for the remainder of the
time that it's on.

Fine-tuning Power Values
------------------------

FAST Pinball hardware also allows you to fine-tune the exact timings of the
pulse_power and hold_power values. By default, the pulse_power and hold_power
values from 0 to 8 map to an 8-bit PWM mask, like this:

+ 0: 00000000
+ 1: 00000001
+ 2: 10001000
+ 3: 10010010
+ 4: 10101010
+ 5: 10111010
+ 6: 11101110
+ 7: 11111110
+ 8: 11111111

Each digit in the mask is 1ms, with a 1 being "on" and a 0 being "off". Then
that pattern is repeated as long as necessary. In other words, the power value
of 4 is 10101010 which is on for 1ms, off for 1ms, on for 1ms, etc.

That should work fine for most cases, there could be scenarios
where you might want more fine-grained control. To enable this, you
can use ``pulse_pwm_mask:`` and ``hold_pwm_mask:`` settings where you actually
enter an 8-digit strings of ones and zeros for the mask. For example:

::

    coils:
        some_coil:
            number: 1-3
            pulse_ms: 30
            hold_pwm_mask: 11001100

In the example above, the coil is still getting 50% power, but it's turning on
and off every 2ms instead of every 1ms. Again, usually this isn't something
you have to worry about, but it's nice to be able to fine tune things, especially
when you have non-standard coils or things like magnets.

For really fine-grained scenarios, FAST also has the ability to use
32-bit pwm masks, like this:

::

    coils:
        some_coil:
            number: 1-3
            pulse_ms: 30
            hold_power32: 10011100011001110001100111000110

The 32-bit mask is just like the 8-bit mask, where each digit represents 1ms.
It's just that the 32-bit version lets you specify a 32ms-long repeating pattern,
versus the 8-bit one which is an 8ms-long repeating pattern.

There are both ``hold_power32:`` and ``pulse_power32`` settings for coils and
drivers using FAST hardware.

.. note::

   In case it's not obvious, for each coil you can only choose one setting from
   ``pulse_power:``, ``pulse_power32:``, and ``pulse_pwm_mask:``, and one
   setting from the "hold" variants of the three of them.

Setting Recycle Times
---------------------

FAST Pinball controllers allow you to precisely control the
:doc:`recycle time </mechs/coils/recycle>` for coils or drivers.

A coil's ``recycle:`` setting is a boolean (True/False), which is
set to ``False`` by default. When using FAST Pinball hardware, if you set
``recycle: true``, then the recycle time is automatically set to twice the
coil's ``pulse_ms:`` setting. (e.g. a coil with a ``pulse_ms: 30`` and
``recycle: true`` will have a 60ms recycle time).

However, with FAST Pinball hardware, you can manually set a coil's recycle
time by adding a ``recycle_ms:`` setting, like this:

::

   coils:
      slingshot_r:
         number: 1-4
         pulse_ms: 30
         recycle_ms: 100

If you manually specify a recycle_ms value, then that's the value that's used
and the coil's ``recycle:`` (true/false) setting is ignored.
