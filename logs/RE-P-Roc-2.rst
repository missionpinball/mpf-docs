RE-P-Roc-2 - Communication with P/P3-Roc broke down
===================================================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/p_roc`                                                         |
+------------------------------------------------------------------------------+

In your log you will probably find a line such as:

.. code-block:: doscon

   OSError: Error in WriteData: wrote 0 of 8 bytes

This error occurs when ``pinproc`` (the library MPF uses to talk to the
P/P3-Roc) reports an error while talking to the P/P3-Roc via USB.
This is most likely a bad cable or a power supply issue.
See :doc:`/hardware/multimorphic/troubleshooting` for potential causes and
solutions.

.. include:: config_error_footer.rst

Related How To guides
---------------------

* :doc:`/hardware/multimorphic/troubleshooting`
* :doc:`/hardware/voltages_and_power/wiring_and_connectors`
* :doc:`/hardware/voltages_and_power/voltages_and_power`

