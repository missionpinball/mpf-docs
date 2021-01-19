How to configure switches (Penny K Pinball PKONE)
=================================================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/pkone`                                                         |
+------------------------------------------------------------------------------+
| :doc:`/config/switches`                                                      |
+------------------------------------------------------------------------------+

To configure switches with Penny K Pinball PKONE hardware, you can follow the guides
and instructions in the :doc:`/mechs/switches/index` docs.

However there are a few things to know and some additional options you get
with Penny K Pinball PKONE hardware that is discussed here.

number:
-------

When you're using PKONE Extension boards, switches plug into individual Extension boards.
Then the Extension boards are connected together in a chain.

.. image:: /hardware/images/pkone-extension.png

The ``number:`` setting for each switch is its board's Address ID number in the
PKONE chain, then the dash, then the switch input number.

.. code-block:: mpf-config

   switches:
     my_switch:
       number: 0-0    # Extension board at address 0, switch 0
     some_other_switch:
       number: 2-24    # Extension board at address 2, switch 24

Notes:

   * The PKONE Extension board Address ID switches can be set from 0 to 7.

What if it did not work?
------------------------

Have a look at our :doc:`PKONE troubleshooting guide <troubleshooting>`.
