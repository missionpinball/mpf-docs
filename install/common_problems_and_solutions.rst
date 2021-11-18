
What if it did not work?
------------------------

In the following we list some common problems and solutions.
If you got another problem please ask in our `MPF User Forum <https://groups.google.com/forum/#!forum/mpf-users>`_.

YAML error on first start
^^^^^^^^^^^^^^^^^^^^^^^^^

You will see this error if there is already a different version of ruamel.yaml installed on your system:

.. code-block:: doscon

   pkg_resources.VersionConflict: (ruamel.yaml 0.15.37 (c:\users\robert\appdata\local\programs\python\python36\lib\site-packages), Requirement.parse('ruamel.yaml<0.11,>=0.10')


This could have happened if you are upgrading to a newer version of MPF or you have incompatible versions of MPF, MPF-MC and/or the MPF-Monitor installed. The required ruamel.yaml version is different on newer MPF versions.
We used to install ruamel 0.11 and switched to 0.15 in MPF 0.53+.
MPF cannot start with two yaml libraries.
To fix this check your versions ``pip3 list`` and check ``mpf``, ``mpf-mc`` and ``mpf-monitor``.
Remove the wrong version and install the right one.
All versions need to match (for instance all |version| or all dev).

The following command will remove all three and install the latest release:

.. code-block:: doscon

   pip3 uninstall mpf mpf-mc mpf-monitor
   pip3 install mpf mpf-mc mpf-monitor

This error can also occur if you already have ruamel.yaml installed in your python system packages for a non-MPF package. Often times, you will have a newer version of ruamel.yaml than MPF requires. Unfortunately, MPF cannot use a newer version of this package because that caused issues in the past because newer versions dropped support (wheels for windows) for older python versions. In the case that you need a different version than the one MPF requires, it is advised to create a python virtual environment and install the required packages there, and use that virtual environment for running MPF. 
