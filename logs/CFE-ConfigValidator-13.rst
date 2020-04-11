CFE-ConfigValidator-13: Cannot convert value to boolean
=======================================================

This error occurs when MPF expects a boolean value (i.e. ``true`` or ``false``)
for a config setting but got a value of a different type.

Examples
--------

For instance, the ``debug`` setting for a :doc:`switch </config/switches>` is
a boolean:

.. code-block:: mpf-config

   switches:
     s_flipper_left:
       number: 1
       debug: true   # we want all the details about this switch in the logs

You can see which settings are boolean in the
:doc:`config reference </config/index>` of your device.


Common Pitfalls
---------------

Widget Animations Repeat
^^^^^^^^^^^^^^^^^^^^^^^^

In MPF versions before 0.53 ``repeat`` in widgets has been an integer
which has been converted to boolean internally.
A lot of examples (and the tutorial) contained ``repeat: -1``.
You need to change this to ``repeat: false`` to fix this error.

Using Quotes
^^^^^^^^^^^^

If you use ``debug: "false"`` (with quotes around ``false``) MPF will not
recognize ``false`` as a boolean but as a string.
Remove the quotes to fix this.

.. include:: config_error_footer.rst


Related How To guides
---------------------

* :doc:`config reference </config/index>`
