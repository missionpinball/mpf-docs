Mechanical Switches
===================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/switches`                                                      |
+------------------------------------------------------------------------------+

Most switches in pinball machines are mechanical switches which are open by
default and close a circuit when pushed.
There are two common types of mechanical switches:
First, blade switches which are very cheap and reliable but cannot be used
everywhere:

:doc:`TODO: Add a picture of a blade switch </about/help_us_to_write_it>`

Second, micro switches which are very small and commonly used for roll over
switches:

:doc:`TODO: Add a picture of a micro switch </about/help_us_to_write_it>`

Electronically and logically both switches work similarly.

Switches can be connected to a direct input and ground on almost all
platforms.
Most direct inputs have an internal pull up which will pull the level to VCC
(usually around 10 kOhm).
When pushed the switch will pull the input to ground which will be detected as
a closed switch by the platform.

:doc:`TODO: Add electronical drawing for switch on direct input. </about/help_us_to_write_it>`

Additionally, you can use switches in a switch matrix. 
In a switch matrix columns are connected to drivers and rows to switches.
Columns are then pulsed sequentially and the rows are read.
Each switch has to use a diode to prevent closing other columns.

:doc:`TODO: Add electronical drawing for switch in matrix. </about/help_us_to_write_it>`

Switch matrices are driven using your hardware platform and MPF will read the
values from the platform. Usually the numbers for switches reflect their row
and column in the matrix. Consult your hardware platform documentation for
details.

This is an example of switches in MPF:

.. code-block:: mpf-config

   switches:
      my_direct_switch:
         number: 23    	# number depends on your platform
      my_matrix_switch_row_1_column_3:
         number: 1/3    # number depends on your platform
