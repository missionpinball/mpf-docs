RE-MPF_BCP_Server-1: Failed to bind BCP Socket to 127.0.0.1 on port 5051
========================================================================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/bcp`                                                           |
+------------------------------------------------------------------------------+

This error occurs when MPF cannot bind the port 5051 for incoming BCP
connections.
The same error can occur in MC when it cannot bind port 5050.


Common Pitfalls
---------------

Another Application is Running on that Port
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Yahoo Messager uses 5050 and some Symantec application uses 5051.
However, there might be other applications such a IIS which can also use those
ports.
Stop those applications or change the port in the
:doc:`bcp config section </config/bcp>`.

Firewalls and Antivirus Protection Soltions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Some firewalls might prevent MPF from binding ports.
Also antivirus or threat protection software might do that.
Try if disabling those help.
If it helps see if you can add an exception for MPF.


.. include:: config_error_footer.rst

Related How To guides
---------------------

* :doc:`/config/bcp`

