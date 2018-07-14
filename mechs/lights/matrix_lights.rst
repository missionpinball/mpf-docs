Matrix Lights (Bulbs)
=====================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/lights`                                                        |
+------------------------------------------------------------------------------+

.. contents::
   :local:

Some hardware platforms support lamps in a matrix.
Those lights are usually bulbs and single color (white).
Each of them is assigned to a unique column/row combination and driven
sequentially by the platform.

:doc:`TODO: Add a picture of bulbs in a matrix </about/help_us_to_write_it>`

Details differ by platform but the syntax for the number of such a light
is usually `column:row` or `column:row` (see your platform for details).
The config looks like this:

.. code-block:: mpf-config

  lights:
    my_matrix_light:
      number: 2:10      # or 2/10

Monitorable Properties
----------------------

For :doc:`dynamic values </config/instructions/dynamic_values>` and
:doc:`conditional events </events/overview/conditional>`,
the prefix for LEDs is ``device.lights.<name>``.

* *color*
* *corrected_color*

+------------------------------------------------------------------------------+
| Related How To Guides                                                        |
+==============================================================================+
| :doc:`/tutorial/17_add_lights_leds`                                          |
+------------------------------------------------------------------------------+

+------------------------------------------------------------------------------+
| Related Events                                                               |
+==============================================================================+
| None                                                                         |
+------------------------------------------------------------------------------+
