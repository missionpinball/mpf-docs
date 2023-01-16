Installing MPF on Linux
=======================

As part of our automated build process, we build and test MPF and MPF-MC
against Ubuntu 20.04 & 22.04 and Debian Stretch & Buster.
MPF 0.54 supports Python 3.5 to 3.7.
MPF 0.55 supports Python 3.6 to 3.9.
MPF 0.56 supports Python 3.7 to 3.9

Installing MPF Using Our Installer
----------------------------------

Download the MPF Debian Installer (which is used for all of these) from
https://github.com/missionpinball/mpf-debian-installer/archive/0.55.x.zip

Unzip it, and from a terminal run ``chmod +x install && sudo ./install`` from the folder you unzipped the files to. If you are using a P-Roc
or P3-Roc also run ``chmod +x install-proc && ./install-proc`` (skip for other platforms). Consult the README for more information.

Installing MPF Manually
-----------------------
Current version these instructions are for v0.56.0, which is the current "dev" branch of MPF.

MPF 0.56 requires Python 3.7, 3.8, or 3.9. Various Linux distributions offer to install multiple versions of Python in parallel. First check what version of Python you might
have already running on your computer.

.. code-block:: doscon

  python3 --version

In some cases you might only get a Python version of 3.6, then run your admin tool and install a higher version of python, preferabyl the latest version of 3.9. If you don't want to remove the older version of Python
you can keep it in parallel, just make sure to run the installer commands with the right version of python. If you have for example installed Python 3.9 try to running

.. code-block:: doscon

  python3.9 --version

You will need pip further down the line to complete the installation. Same as above for Python, check what version of pip you are running and choose the command to match the version
you would like to use. Try the following commands to figure out what pip command works for you and has the right version.

.. code-block:: doscon

  pip --version
  pip3 --version
  pip3.9 --version

For the rest of the chapter I will always write python3.9 and pip3.9 as commands as reminder to use the right version, any of the above commands might work for you (or fail).

NOTE: If you already have an earlier version of MPF installed, uninstall that first by using this command:

.. code-block:: doscon

  sudo pip3.9 uninstall mpf-mc mpf

If you are unsure which version of MPF you have installed, you can run this command to check what is installed:

.. code-block:: doscon

  mpf --version


Now back to the installation, in a console run

.. code-block:: doscon

  pip3.9 install --user pipx
  python3.9 -m pipx ensurepath

After this it might be necessary to restart the console. Now run the following command (obey that this is pipx and here there is no need for a version)

.. code-block:: doscon

    pipx install "mpf[cli]" --pip-args="--pre" --verbose --include-deps
    pipx inject mpf mpf-mc --pip-args="--pre" --verbose --include-deps --include-apps

Updated MPF Monitor instructions (which work with pipx) are :doc:`here </tools/monitor/installation>`.

At this point, MPF 0.56.0.devXX and MPF-MC 0.56.0.devXX are installed. (The "XX" in the version will be the dev build numbers.)



Download & run the "Demo Man" example game
------------------------------------------

Now that you have MPF installed, you probably want to see it in action. The easiest way to do that is
to download a bundle of MPF examples and run our "Demo Man" example game. To do that, follow
the instructions in the :doc:`/example_games/demo_man` guide.

There's another example project you can also check out if you want called the "MC Demo" (for media controller demo)
that lets you step through a bunch of example display things (slides, widgets, sounds, videos, etc).
Instructions for running the MC Demo are :doc:`here </example_games/mc_demo>`.

Running MPF
-----------

See the :doc:`/running/index` for details and command-line options.

If you see a Failed to initialize MPF exception when trying to start MPF with Multimorphic P-ROC/P3-ROC boards with Python 3.8.

Example Error:

.. code-block::

    Failed to initialise MPF
    Traceback (most recent call last):
    File “/usr/local/lib/python3.8/dist-packages/mpf/platforms/p_roc_common.py”, line 31, in <module>
      import pinproc
    ModuleNotFoundError: No module named ‘pinproc’
    During handling of the above exception, another exception occurred:
    Traceback (most recent call last):
    File “/usr/local/lib/python3.8/dist-packages/mpf/platforms/p_roc_common.py”, line 41, in <module>
      raise ImportError
    ImportError: No module named ‘pinproc’

Try Changing `Edit install-proc:`

From:

.. code-block::

    cd pypinproc
    sudo python3 setup.py install

To:

.. code-block::

    cd pypinproc
    python3 setup.py install --user

Keeping MPF up-to-date
----------------------

To upgrade MPF just re-run the installer which will make sure that you will also get updated dependencies:

.. code-block:: console

  sudo ./install


If you have MPF installed via the manual procedure above, you can keep it up-to-date by running the final two pipx commands from above which you used to install MPF and MPF-MC.

.. warning::

   If you are upgrading from MPF 0.33 to 0.50 you will need to manually perform
   several migration steps to modify your configuration files or they will not
   work in MPF 0.50. Please refer to :doc:`Migrating from config version 4 to 5 of MPF </install/migrate4to5>`
   for step-by-step instructions.

To install the latest dev release (not generally recommended) which allows you to try bleeding-edge features run:

.. code-block:: console

  pip3 install mpf[all] mpf-mc --pre --upgrade

To downgrade (or install a specific release x.yy.z) run:

.. code-block:: console

  pip3 install mpf[all]==x.yy.z
  pip3 install mpf-mc==x.yy.z

Uninstalling MPF
----------------------

To remove MPF either because it is no longer needed or to perform a clean install run:

.. code-block:: console

  sudo pip3 uninstall mpf-mc mpf


Specific Hardware Devices
-------------------------

We got some write-ups for specific hardware platforms.
They follow the general linux installation schema but also cover some details
about that hardware.

.. toctree::
   :maxdepth: 1

   Raspberry Pi <raspberry>
   Pine64 <pine64>


Specific Linux Distributions
----------------------------

Specifics about certain linux distributions.

.. toctree::
   :maxdepth: 1

   Xubuntu Linux <xubuntu>

.. include:: /install/common_problems_and_solutions.rst
