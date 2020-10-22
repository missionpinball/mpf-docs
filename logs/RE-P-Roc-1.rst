RE-P-Roc-1 - Known Firmware Bug in P3-Roc
=========================================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/p_roc`                                                         |
+------------------------------------------------------------------------------+

This error occurs when you try to use ``pulse_power`` on drivers on the
P3-Roc with firmware 2.14 or earlier and enable a rule with hold.

This can be solved by either removing ``pulse_power`` from the coil in question
or by upgrading the firmware.
Firmware can be obtained from the Multimorphic Member Area.


.. include:: config_error_footer.rst

Related How To guides
---------------------

* :doc:`/hardware/multimorphic/index`
* :doc:`/hardware/multimorphic/troubleshooting`

