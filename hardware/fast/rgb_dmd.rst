How to configure an RGB DMD (FAST Pinball)
==========================================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/rgb_dmds`                                                      |
+------------------------------------------------------------------------------+

If you would like to use the FAST RGB LED DMD, follow the
instructions for the :doc:`/hardware/smartmatrix/index`.

You can copy the following example (and replace ``com12`` with your com port):

.. code-block:: mpf-config

    hardware:
      rgb_dmd: smartmatrix
    smartmatrix:
      smartmatrix_1:
        port: com12
        baud: 4000000
        old_cookie: false

What if it did not work?
------------------------

Have a look at our :doc:`FAST troubleshooting guide <troubleshooting>`.
