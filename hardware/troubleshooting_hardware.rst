Troubleshooting Hardware Platforms
==================================

If you got problems with your hardware platform we first recommend to read our
:doc:`troubleshooting guide </troubleshooting/index>`.
Here are some hardware platform specific steps.
This is a generic guide so please check if there is a more specific guide for
your specific platform.

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


.. include:: include_troubleshooting_lights.rst
.. include:: include_troubleshooting_coils.rst

.. include:: include_troubleshooting.rst
