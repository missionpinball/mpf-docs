CFE-ConfigValidator-9: Required setting is missing from section in your config
==============================================================================

This error occurs when MPF does not find a required setting in one of your
config sections.

Examples
--------

For instance, every switch has to have a number in MPF:

.. code-block:: mpf-config

   switches:
     s_ball_switch1:
       number: 1

You can see which settings are required in the
:doc:`config reference </config/index>` of your device.
For this instance, check the :doc:`switch config reference </config/switches>`
and you will find that only ``number`` is a required setting.


Common Pitfalls
---------------

Omitting one of the required settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you omit on of the required settings you will see this error.
To this this browse to the :doc:`config reference </config/index>` of your
device and add all the required settings.
Alternatively, you could use your
:doc:`IDE with the MPF language server </tools/language_server/index>` to
auto-complete all required settings.


.. include:: config_error_footer.rst

Related How To guides
---------------------

* :doc:`config reference </config/index>`

