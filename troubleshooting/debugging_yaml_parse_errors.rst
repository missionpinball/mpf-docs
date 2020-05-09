Debugging YAML Parse Errors
===========================

In case something goes wrong and you get errors like this:

.. code-block:: console

   ValueError: YAML error found in file config/config.yaml. Line 22,Position 10: mapping values are not allowed here
     in "config/config.yaml", line 22, column 10

This means that the error might be at line 22, just before it or shortly after it.
Sometimes it is tricky to tell whats wrong when one space is off.
A good editor might help but it might be still hard to spot the exact point.

Install an IDE
--------------

We recommend the :doc:`MPF language server </tools/language_server/index>` with
a supported IDE for that.

Install the extension
---------------------

If you are struggling to find the problem you can reformat your file using
``ruamel.yaml``.
To do that you first need to install the ``ruamel.yaml.cmd`` extension:

.. code-block:: console

   pip3 install ruamel.yaml.cmd==0.2

Make a backup
-------------

Before you continue: Make a backup of your machine config.
Seriously, do it!
Even better, use git and commit right now!

Reformatting YAML files
-----------------------

After that you can reformat single files using the ``round-trip`` command.
For example if you want to reformat ``your_file.yaml`` first check the changes
it would make:

.. code-block:: console

   yaml round-trip your_file.yaml

If that looks alright perform them by adding the ``--save`` flag:

.. code-block:: console

   yaml round-trip --save your_file.yaml

This will keep comments but reformat all your indents to two spaces per level.
It should be easier now to spot the problem.

Reformat Your Config Using MPF format
-------------------------------------

Run ``mpf format`` on your config.
See :doc:`/tools/format/index` for details.

What if it did not help?
------------------------

If this did not help you can ask in the
`mpf-users Google group <https://groups.google.com/forum/#!forum/mpf-users>`_.
Please post the full error message, your log file and the relevant config file.
