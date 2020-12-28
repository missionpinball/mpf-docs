Machine Management
==================

MPF includes many features to help you manage your pinball machine.

(There's a lot to add here. This will include things like the service mode,
auditor, remote monitoring and trouble reporting, etc. See: :doc:`/about/help_us_to_write_it`)

.. warning::

   If the ``service`` mode is added to ``modes``, the message "coil power off" will appear when the coin door is open.
   This is only a message: MPF cannot actually turn the coil power off. You must ensure that your power system is 
   wired appropriately to turn HV off when the coin door is open.
   
.. toctree::
   :hidden:

   auditor/index
   service_mode/index
   operator_settings/index
