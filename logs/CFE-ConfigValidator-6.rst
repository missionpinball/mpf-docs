CFE-ConfigValidator-6: Device not found in section in your config
=================================================================

This error occurs when MPF does not find a device which is referenced by one
of your settings in your config.

Examples
--------

For instance, a flipper device references a switch and a coil:

.. code-block:: mpf-config

   switches:
     s_flipper_left:
       number:
   coils:
     c_flipper_left:
       number:
   flippers:
     left_flipper:
       main_coil: c_flipper_left
       activation_switch: s_flipper_left

You can see to which type of device a setting references in the
:doc:`config reference </config/index>` of your device.
For this instance, check the :doc:`flipper config reference </config/flippers>`
and you will find that ``main_coil`` references a :doc:`coil </config/coils>`
and ``activation_switch`` references a :doc:`switch </config/switches>`.


Common Pitfalls
---------------

Typos
^^^^^

The most common source for this kind of error are typos.
Check the name of your referenced device with the setting.
Casing matters here (i.e. upper/lower case).
Using an :doc:`IDE with the MPF language server </tools/language_server/index>`
can help here.

Copy and Paste
^^^^^^^^^^^^^^

We all do this and there is nothing wrong with copying configs from the docs.
Almost all examples in the docs are tested and should not give this kind of
error.
However, sometimes we hide certain devices in the docs (i.e. switches and coils
which are referenced by an examplary flipper device as above).
This is done to improve readability but when copying those examples you might
get this error.
Nevertheless, you can click "Click to show full config" below all examples
to see the full tested example which is tested to work in the MPF version
corresponding to the docs.

Running Config from a different MPF Version
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sometimes MPF config specifications change.
Check if your MPF version fits the config.
If in doubt check the :doc:`config reference </config/index>`
for your device.


Referencing a different type of device
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you reference a different device MPF won't find it and show this error.
Check the :doc:`config reference </config/index>` of your device to see which
device is expected or setup your
:doc:`IDE with the MPF language server </tools/language_server/index>`.

.. include:: config_error_footer.rst

Related How To guides
---------------------

* :doc:`config reference </config/index>`
