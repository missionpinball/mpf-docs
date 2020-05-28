Troubleshooting Pin2DMD
=======================

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
adding ``debug: true`` to your ``pin2dmd`` config section:

.. code-block:: mpf-config

   pin2dmd:
     debug: true

This will add a lot more debugging and might slow down MPF a bit.
We recommend to disable/remove it after finishing debugging.

Check Brightness
----------------

Your display is not showing your slides?
Check if your brightness is set high enough.
You can adjust brightness in your ``rgb_dmds`` section:


.. code-block:: mpf-config

    rgb_dmds:
      default:  # your DMD
        brightness: .8      # adjust the brightness of your display if it is too bright or dim
        fps: 30

.. include:: ../include_troubleshooting.rst
