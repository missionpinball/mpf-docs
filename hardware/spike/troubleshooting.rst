Troubleshooting Spike
=====================

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
adding ``debug: true`` to your ``spike`` config section:

.. code-block:: mpf-config

   spike:
     debug: true

This will add a lot more debugging and might slow down MPF a bit.
We recommend to disable/remove it after finishing debugging.

.. include:: ../include_troubleshooting.rst
