The Virtual Platform
====================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/hardware`                                                      |
+------------------------------------------------------------------------------+

MPF's virtual platform interface is a software-only platform you can
use if you don't have a physical pinball controller attached.

.. note:: MPF also has a :doc:`smart virtual platform <smart_virtual>`
   which is probably what you'd use in most cases instead of the
   virtual platform.

Note for P-ROC and P3-ROC users: P-ROC's pyprocgame includes a virtual P-ROC interface
called *FakePinPROC*. We don't use that in the MPF because doing so
requires that pyprocgame is installed, and it's likely that people
using MPF won't have pyprocgame. Using MPF's virtual hardware interface
is conceptually similar to *FakePinPROC*.

Using the virtual platform
--------------------------

There are three ways you can use the virtual platform:

1. Manually setting the platform
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can manually specify the virtual platform in the machine config, like this:

.. code-block:: mpf-config

    hardware:
      platform: virtual

3. Via the command line
^^^^^^^^^^^^^^^^^^^^^^^

You can also specify the smart virtual platform interface via the ``-x``
(lowercase *X*) from the command line, like this:

::

    mpf -x

Or

::

   mpf both -x

etc.

