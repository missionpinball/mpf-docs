MPF commands
============

MPF offers multiple commandline commands.
Almost all of those commands should executed from within your MPF machine folder.

Usually you start MPF using:

.. code-block:: shell

   $ mpf both

Alternatively your can run MPF and MC separately:

.. code-block:: shell

   $ mpf game

and:

.. code-block:: shell

   $ mpf mc


To start the interactive service cli run (start mpf both before):

.. code-block:: shell

   $ mpf service

If you want to see details about your hardware (do not run MPF in parallel):

.. code-block:: shell

   $ mpf hardware scan

To update the firmware of your hardware controllers (if supported by your platform):

.. code-block:: shell

   $ mpf hardware firmware_update


.. toctree::
   :titlesonly:

   mpf both <both>
   mpf core <core>
   mpf diagnosis <diagnosis>
   mpf game <game>
   mpf mc <mc>
   mpf imc <imc>
   mpf migrate <migrate>
   mpf monitor <monitor>
   mpf hardware <hardware>
   mpf service <service>
   mpf build <build>
   mpf test <test>
   mpf format <format>
