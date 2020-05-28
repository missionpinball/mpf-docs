CFE-ConfigValidator-2: Your config contains a value for the setting, but this is not a valid setting name
=========================================================================================================

This error occurs when MPF does not know a setting you specified in a device.

Examples
--------

For instance, a :doc:`switch </config/switches>` knows certain settings:

.. code-block:: mpf-config

   switches:
     s_flipper_left:
       number: 1
       label: My Left Flipper Switch Example
       tags: some_custom_tag

You can see which settings are allowed in the
:doc:`config reference </config/index>` of your device.

Common Pitfalls
---------------

Typos
^^^^^

The most common source for this kind of error are typos.
Check the name of your referenced device with the setting.
Casing matters here (i.e. upper/lower case).
Using an :doc:`IDE with the MPF language server </tools/language_server/index>`
can help here.

Mixing Devices
^^^^^^^^^^^^^^

Maybe you accidentially copied config attributes from a different type of
devices?
Double check if you refered to the documentation of the correct device.
If you find incorrect documentation please tell us in the forum.

Incorrect Indent
^^^^^^^^^^^^^^^^

With nested configs (i.e. slide_player or widget_player) you might have used
an option which should be indented one level further or one level less.
This can sometimes be a bit tricky.
Using an :doc:`IDE with the MPF language server </tools/language_server/index>`
can help here.

Running Config from a different MPF Version
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sometimes MPF config specifications change.
Check if your MPF version fits the config.
If in doubt check the :doc:`config reference </config/index>`
for your device.

.. include:: config_error_footer.rst

Related How To guides
---------------------

* :doc:`config reference </config/index>`

