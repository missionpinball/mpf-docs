CFE-DeviceManager-3: Device does not have a valid config. Expected a dictionary.
================================================================================

This error occurs when MPF expects a dictionary in a config of a device but
found something else.

Examples
--------

For instance, the settings of a :doc:`switch </config/switches>` are
a dictionary (switches -> s_flipper_left).

.. code-block:: mpf-config

   switches:
     s_flipper_left:
       number: 1
       label: My Left Flipper


Common Pitfalls
---------------

Forgetting the Device Name
^^^^^^^^^^^^^^^^^^^^^^^^^^

This error usually occurs when you omit the device name.
For example if you omit ``s_flipper_left`` this would look like this:

.. code-block:: yaml

   # BROKEN CONFIG
   switches:
     number: 1
     label: My Left Flipper

Here MPF would see two switches with the names ``number`` and ``label``.
Each of them has an invalid config (just a single value but not a dictionary).

YAML Formatting Issues
^^^^^^^^^^^^^^^^^^^^^^

See :doc:`CFE-ConfigValidator-12` for more general common pitfalls.


.. include:: config_error_footer.rst


Related How To guides
---------------------

* :doc:`CFE-ConfigValidator-12`
* :doc:`config reference </config/index>`
