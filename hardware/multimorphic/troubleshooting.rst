Troubleshooting P-Roc/P3-Roc
============================

If you got problems with your hardware platform we first recommend to read our
:doc:`troubleshooting guide </troubleshooting/index>`.
Here are some hardware platform specific steps:


Run Hardware Scan
-----------------

Using ``mpf hardware scan`` you can find out if your P/P3-Roc is talking
properly to MPF using USB.
Additionally, it will show you which ``SW-16`` are connected:

.. code-block:: console

   $ mpf hardware scan

   Firmware Version: 2 Firmware Revision: 6 Hardware Board ID: 1
   SW-16 boards found:
    - Board: 0 Switches: 16 Device Type: A3 Board ID: 0
    - Board: 1 Switches: 16 Device Type: A3 Board ID: 1
    - Board: 2 Switches: 16 Device Type: A4 Board ID: 2


Unfortunately, MPF cannot know which ``PD-16`` or ``PD-LED`` are connected
as this information is not available.
See :doc:`/running/commands/hardware` for details.

Enable Debugging
----------------

If you got problems with your platform try to enable ``debug`` first.
As described in the
:doc:`general debugging section </troubleshooting/general_debugging>`
of our :doc:`troubleshooting guide </troubleshooting/index>`
this is done by
adding ``debug: true`` to your ``p_roc`` config section:

.. code-block:: mpf-config

   p_roc:
     debug: true

This will add a lot more debugging and might slow down MPF a bit.
We recommend to disable/remove it after finishing debugging.

Enable Bus Tracing
------------------

If your hardware behaves different from the way you told it to in MPF or
if you are seeing lags or delays it might be wise to turn on bug tracing.

.. code-block:: mpf-config

   p_roc:
     debug: true
     trace_bus: true


This logs all calls to libpinproc.
This will cause a lot of additional log lines and might considerably slow down
MPF.
Definitely disable this after you finished debugging.

All Coils Turn On When I Power Up My Machine
--------------------------------------------

If this happens and MPF is not yet running you likely do not have common ground
between high voltage and logic power.
Turn your machine off and only turn it back on when you have fixed and verified
common ground.
Read the section about :doc:`common ground </hardware/voltages_and_power/voltages_and_power>`
for details or consult an electrical engineer.

If this happens shortly after MPF started and you are using a P-Roc this might
have to do with the polarity of your coils.
Check the ``polarity`` setting and make sure you configured the correct machine
type as there are different defaults in different machine types.

In any case we recommend that you test this with either less voltage (i.e. 12V
instead of 48V) or by using lamps instead of coils on your outputs as that
will prevent hardware damage due to overcurrent.

Serial Bus Issues
-----------------

Bad Cables/Interference
~~~~~~~~~~~~~~~~~~~~~~~

:doc:`/about/help_us_to_write_it`

Termination
~~~~~~~~~~~

:doc:`/about/help_us_to_write_it`

Correct Addressing
------------------

:doc:`/about/help_us_to_write_it`


.. include:: ../include_troubleshooting.rst
