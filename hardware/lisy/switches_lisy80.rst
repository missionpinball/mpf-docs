Configuring Switches with LISY80
================================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/switches`                                                      |
+------------------------------------------------------------------------------+

LISY80 supports the System 80 switch matrix which consists of a maximum of 64
switches.
The switch number in the manual of your machine can be used within MPF.
However, you may not find all switches in your game manual as some switches
are the same along all System80/80A/80B games and Gottlieb decided not to
document them ;-).
Those are the following (according to pinwiki.com):

* 06 - left advance button (Sys80B only)
* 07 - play / test switch
* 16 - right advance button (Sys80B only)
* 17 - left coin switch
* 27 - right coin switch
* 37 - center coin switch
* 47 - replay button
* 57 - plumb bob and ball roll tilts (these have the same switch assignment as the playfield tilt switch)

.. note::

   The SLAM switch in system80, which is **not** part of the switch matrix and
   cannot be used in ``mpfserver`` for LISY80 in the current release.

You can start with this config:

.. code-block:: mpf-config

   switches:
     tilt:
       number: 57

Then just add your switches according to the manual of your machine.
See :doc:`/config/switches` for more details about switches.

What if it did not work?
------------------------

Have a look at our :doc:`LISY troubleshooting guide <troubleshooting>`.
