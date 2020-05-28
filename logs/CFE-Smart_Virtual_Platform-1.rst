CFE-Smart_Virtual_Platform-1: Switch used in virtual_platform_start_active_switches was not found in switches section
=====================================================================================================================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/switches`                                                      |
+------------------------------------------------------------------------------+
| :doc:`/config/virtual_platform_start_active_switches`                        |
+------------------------------------------------------------------------------+

This error occurs when you use a switch in
``virtual_platform_start_active_switches`` which is not defined in your
``switches`` section.

Examples
--------

This is how it should look:

.. code-block:: mpf-config

   switches:
     s_ball_switch1:
       number:
     s_ball_switch2:
       number:
     s_ball_switch3:
       number:
   # Two switches should be active at start
   virtual_platform_start_active_switches:
     - s_ball_switch1
     - s_ball_switch2

Alternatively, this could be a comma separated list:

.. code-block:: mpf-config

   switches:
     s_ball_switch1:
       number:
     s_ball_switch2:
       number:
     s_ball_switch3:
       number:
   # Two switches should be active at start
   virtual_platform_start_active_switches: s_ball_switch1, s_ball_switch2

Common Pitfalls
---------------

Using spaces instead of commas
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In MPF versions before 0.54 you could also use spaces instead of commas.
Even though this syntax was never officially supported in lists it still was
supported code.
This was also used in previous versions of the documentation and the tutorial.

.. code-block:: yaml

   # INVALID SYNTAX
   virtual_platform_start_active_switches: s_ball_switch1 s_ball_switch2  # note the space instead of a comma

To fix this turn it into one of the two syntaxes above.
See :doc:`/config/instructions/lists` for details.

.. include:: config_error_footer.rst

Related How To guides
---------------------

* :doc:`/config/virtual_platform_start_active_switches`
* :doc:`/config/instructions/lists`
