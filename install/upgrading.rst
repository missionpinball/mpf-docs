How to update MPF to the latest version
=======================================

Since MPF is a work-in-progress that's changing often, there are times when
you'll need to update your installation to the latest version.

.. warning::

   This guide is written when MPF 0.31 was the current version, but it applies
   to any versions of MPF, so do not assume that 0.31 is the latest as you're
   reading it.

To check your MPF version:
--------------------------

You can list all of the Python packages you have installed (along with their versions),
via the "pip" command (same way you installed MPF), like this:

* Windows or Linux: ``pip list``
* Mac: ``kivy -m pip list``

.. note::

   If you have Python versions 2 and 3 installed, you'll have to use ``pip3 list``.

::

   C:\>pip list

   Kivy (1.9.1)
   Kivy-Garden (0.1.4)
   kivy.deps.glew (0.1.4)
   kivy.deps.sdl2 (0.1.12)
   kivy.deps.sdl2-dev (0.1.12)
   mpf (0.31.0)
   mpf-mc (0.31.0)
   pip (7.1.2)
   pypiwin32 (219)
   pyserial (3.1.1)
   requests (2.11.1)
   ruamel.base (1.0.0)
   ruamel.yaml (0.10.23)
   setuptools (18.2)

Search through the list for the "mpf" and "mpf-mc" entries to see what versions you have. If
you see the word "dev" in the version numbers for mpf or mpf-mc, that means you have a
pre-release/beta version. See the section on "downgrading" below if you want to move back
to the stable version.

Which version of MPF is the latest?
-----------------------------------

You can see what the latest stable versions of MPF and MPF-MC are by visiting the
`MPF Users forum on Google groups <https://groups.google.com/forum/#!forum/mpf-users>`_.
The forum home page will show the latest versions of both, like this:

.. image:: /install/images/stable_version.jpg

.. note::

   The "stable" release is another way of saying the "current" release. Since development of
   MPF is on-going, we also have a "dev" release which is one version ahead of the "stable"
   release. Details on that are at the end of this guide.

Updating your installation of MPF
---------------------------------

If the latest stable release of MPF or MPF-MC is newer than your installation, you can install
the latest version with pip:


* Windows or Linux: ``pip install mpf-mc --upgrade``
* Mac: ``kivy -m pip install mpf-mc --upgrade``

Upgrading MPF-MC should also upgrade MPF. If it doesn't, you can upgrade MPF by itself:

* Windows or Linux: ``pip install mpf --upgrade``
* Mac: ``kivy -m pip install mpf --upgrade``

When you're done, you can run ``pip list`` or ``kivy -m pip list`` again to verify that
you have the latest versions.

These commands are safe to run any time, and if a newer version of MPF is not available,
it will tell you that you have the latest version and exit.

Downgrading to an older version of MPF
--------------------------------------

If the latest release of MPF breaks something and you want to downgrade to an older version,
you can do so with the following commands. Note that when downgrading, you need to downgrade
MPF and MPF-MC separately.

Here's an example to downgrade to versions 0.31.0, but you can replace the "0.31.0" with
whichever version you want to downgrade to.

For Windows and Linux:

::

   pip install mpf-mc==0.31.0
   pip install mpf==0.31.0

For Mac:

::

   kivy -m pip install mpf-mc==0.31.0
   kivy -m pip install mpf==0.31.0

If you want to see a list of all the available versions, you can run the above commands with "0" as
the version (like ``pip install mpf==0``). That will cause an error (because there is no version 0),
but the error message will show a list of all the versions that are available which is nice.

For example:

::

   C:\>pip install mpf==0
   Collecting mpf==0
     Could not find a version that satisfies the requirement mpf==0 (from versions: 0.30.0, 0.30.1, 0.30.22,
     0.30.23, 0.30.24, 0.30.25, 0.30.26, 0.30.27, 0.30.28, 0.30.29, 0.30.30, 0.30.31, 0.30.32, 0.31.0, 0.31.1,
     0.32.0.dev1, 0.32.0.dev2)
   No matching distribution found for mpf==0

Upgrading to the "dev" (pre-release) version of MPF
---------------------------------------------------

Sometimes you might want to use the "dev" version of MPF to test out upcoming features. You can do
so with the following commands:

* Windows or Linux: ``pip install mpf --upgrade --pre``
* Mac: ``kivy -m pip install mpf --upgrade --pre``

(The ``--pre`` option tells pip to download the latest "pre-release" version.) You can run this
command at any time to update a current dev version to the latest dev version.

Dev versions have the word "dev" in the version number, like ``0.32.0dev123" or something similar.

If you're on a dev version and want to go back to the stable releases, follow the instructions in
the downgrading section above.
