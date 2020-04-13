
What if it did not work?
------------------------

In the following we list some common problems and solutions.
If you got another problem please ask in our `MPF User Forum <https://groups.google.com/forum/#!forum/mpf-users>`_.

YAML error on first start
^^^^^^^^^^^^^^^^^^^^^^^^^

You might see this error on startup when installing/upgrading to |version|/dev from an older version:

.. code-block:: doscon

   pkg_resources.VersionConflict: (ruamel.yaml 0.15.37 (c:\users\robert\appdata\local\programs\python\python36\lib\site-packages), Requirement.parse('ruamel.yaml<0.11,>=0.10')

What happened? You probably got incompatible versions of MPF, MPF-MC and/or the MPF-Monitor installed.
We used to install ruamel 0.11 and switched to 0.15 in MPF 0.53+.
MPF cannot start with two yaml libraries.
To fix this check your versions ``pip3 list`` and check ``mpf``, ``mpf-mc`` and ``mpf-monitor``.
Remove the wrong version and install the right one.
All versions need to match (for instance all |version| or all dev).

The following command will remove all three and install the latest release:

.. code-block:: doscon

   pip3 uninstall mpf mpf-mc mpf-monitor
   pip3 install mpf mpf-mc mpf-monitor
