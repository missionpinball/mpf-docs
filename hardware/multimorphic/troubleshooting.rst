Troubleshooting P-Roc/P3-Roc
============================

If you got problems with your hardware platform we first recommend to read our
:doc:`troubleshooting guide </troubleshooting/index>`.
Here are some hardware platform specific steps:

Enable Debugging
----------------

If you got problems with your platform try to enable ``debug`` first.
As described in the
:doc:`general debugging section </troubleshooting/general_debugging>`
of our :doc:`troubleshooting guide </troubleshooting/index>`
this is done by
adding ``debug: true`` to your platform config section.
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



.. include:: ../include_troubleshooting.rst
