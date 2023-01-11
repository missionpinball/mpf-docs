Installing MPF on Windows (January 11, 2023 Update)
===============================================

This process walks through installing MPF 0.56 (current dev branch) a Windows machine. These instructions are for v0.56.0, which is the current "dev" branch of MPF.

Note that installing MPF is more complicated than a normal application. This is because MPF is a development tool you use to create your pinball software, not a finished app itself. So like everything in pinball, there are a lot of steps.

Help Needed!
------------

MPF is a community project that is created, maintained, supported, and documented by volunteers in their spare time. At this time, we do not have any Windows users who are able to help us test and update these instructions. If you are a Windows user and have any updates, additions, or corrections, please help us out by updating these instructions.

Remove prior versions of MPF
---------------------------

MPF and the MPF-MC have many dependencies and requirements. If you have an older version of MPF installed, it may have installed some of these dependencies in a way that is incompatible with the latest version of MPF. So it's best to remove any prior versions of MPF before installing the latest version.

Uninstall MPF by using this command:

.. code-block:: doscon

  pip uninstall mpf

If you are unsure which version of MPF you have installed, you can run this command to check what is installed:

.. code-block:: doscon

  mpf --version

Windows System Requirements
--------------------------

We test MPF on Windows 11. (Technically it's whatever the "windows-latest" Github Actions runner is, which is currently Windows Server 2022 which is the same core as Windows 11.) Older versions of Windows might (probably?) work too, we just don't test them. MPF requires 64-bit (x86) Windows running on Intel-compatible processors. It does not run on 32-bit systems and does not run on ARM processors on Windows.

MPF 0.56 requires Python 3.7, 3.8, or 3.9. It does not run on Python 3.10 or newer. (If you can figure out how to get it to run on Python 3.10+, please submit the fixes!)

Install Python
--------------

If you open a command prompt on a fresh Windows machine and type ``python``, the Microsoft App Store will open and try to install Python 3.7. This is not the version of Python we want. So don't do that. (While MPF runs on Python 3.7, Python installed from the app store is weird complicated. So don't do that unless you know what you're doing. And feel free to update these instructions if you do!)

So instead, install Python from python.org --> Downloads --> Windows --> Scroll down to the latest version of Python 3.9 (which is 3.9.13 at the time of this writing) --> Download Windows installer (64-bit).

Run the installer, and choose the "Customize installation" option, and make sure to check the box for "py launcher" and "pip". (The others don't matter either way.) Then on the next screen, check the box for "Add Python to environment variables". Then click "Install".

Then open a command prompt (you can just run "cmd"), and type each of these commands one at a time (and hit enter after each one). First, make sure Python is installed and make sure when you run "python" that it's the proper version. (Sometimes Windows will have multiple versions of Python installed and it's not always clear which one will be used when you type "python".)

.. code-block:: doscon

  python --version

You want a result like "Python 3.9.13" or whatever version you just installed.

Next, you'll run a command to install "pipx" which is a tool that will help you install and manage the MPF installation. You can read more about pipx here: https://pypa.github.io/pipx/

The second command below ensures that you can run "pipx" by typing "pipx" in the command prompt. (If you don't run this command, you'll have to type "python -m pipx" instead of just "pipx" to run pipx.)


.. code-block:: doscon

  pip install --user pipx
  python -m pipx ensurepath

After this, restart the cmd window. (Just close it and then open a new one.)

Install MPF
-----------

Now you're ready to install MPF. Open a new command window (cmd.exe) and type these commands and hit enter.

.. code-block:: doscon

    pipx install "mpf[cli]" --pip-args="--pre" --verbose --include-deps

A bunch of things will scroll by, and then hopefully MPF is installed. You can test it by typing this command:

.. code-block:: doscon

    mpf --version

This should print out something like "MPF 0.56.0.devXX" where the "XX" is the dev build number. (0.56.0.dev33 at the time of this writing.) If you get an error, something went wrong. If you get a result like "MPF 0.55.0" or "MPF 0.54.0" or something like that, then you have an older version of MPF installed and you need to uninstall it first. (See the "Remove prior versions of MPF" section above.)

You can now proceed with the getting started tutorials.

Install the MPF Media Controller (MPF-MC)
-----------------------------------------

The MPF Media Controller (MPF-MC) is a standalone package that is used to control the LCD or DMD graphics as well as sounds and music in a pinball machine. It is a separate package from MPF. Not every pinball machine uses MPF-MC, but most do. (There are also other media controllers that are not MPF-MC. For example, some people use Unity, the Unreal Engine, or Godot as their media controllers.)

Unfortunately there is currently a bug in the latest builds of MPF-MC on Windows where the audio doesn't work. That bug is being tracked `here <https://github.com/missionpinball/mpf-mc/issues/436>`_. In the meantime, the workaround is to install a specific version `0.56.0.dev33` of MPF-MC until the bug is fixed.

To install MPF-MC `0.56.0.dev33`, use the following command:

.. code-block:: doscon

    pipx inject mpf mpf-mc==0.56.0.dev33 --verbose --include-deps --include-apps

This command will install MPF-MC into the same virtual environment that MPF is installed in. (This is why we used pipx to install MPF in the first place.) It will also install a bunch of other dependencies that MPF-MC needs to run. When it's done, you should see a message like "Injected package mpf-mc into venv mpf".

If you want to install the newest build of MPF-MC, you can use this command instead (but audio will not work until the bug is fixed):

.. code-block:: doscon

    pipx inject mpf mpf-mc --pip-args="--pre" --verbose --include-deps --include-apps

Testing MPF-MC
--------------

Installing MPF-MC is pretty straightforward. Unfortunately just because it installs doesn't mean it works. :(

One way to test the MC is download the ``mpf-examples`` repo from here: https://github.com/missionpinball/mpf-examples. You can either clone it locally, or download the zip file and unzip it. Either is fine, just do what you're most comfortable with. Be sure to download / switch to the ``dev`` branch.

Then back in the command terminal, change into the ``mpf-examples`` folder (or whatever folder you just unzipped that into), then change into the ``mc_demo`` folder, then run ``mpf both``. That should launch the mc_demo code (which is Media Controller demo). A window should open with a red background and some text about slides, you should be able to use the right arrow key to advance to the next slide. You should be able to use the left arrow key to go back to the previous slide and you should hear a drum and cymbal sound when you change the slide.

You will see a bunch of warnings about some classes implemented in multiple locations, and how one will be used, but which one is undefined. It sounds scary, but this is normal. (For now.) We are investigating whether this is something we need to fix, and how we'll fix it if so. But for now it's fine.

You can also run the "demo_man" game from the ``mpf-examples`` folder. Change into the ``demo_man`` folder and run ``mpf both -X``. You should see the DMD window pop up. The window you ran the command from will have some warnings which cover up the nice
text UI display. Just grab a corner of the window with the mouse and resize the window (just make it a tiny bit bigger and smaller) and that will cause the window contents to completely refresh and you should see the expected MPF text UI display showing switch status, ball locations, etc. (See the screenshots below for details)

If you do not see the "normal" MPF text UI display, and instead see something like this:

.. image:: images/bad-display.jpg

This is because those warnings mentioned above print on top of the nice MPF display. To fix this, just grab a corner of the window with the mouse and resize it to be a bit bigger or smaller, which will cause the entire window to update and you should see the expected MPF text UI display showing switch status, ball locations, etc. (See the screenshots below for details)

.. image:: images/good-display.jpg

Alternately if you don't want to resize the window every time, you can open two different command prompt windows, and run ``mpf -X`` in one and ``mpf mc`` in the other.

At this point, MPF is ready to go!

Installing MPF Monitor
----------------------

Updated MPF Monitor instructions (which work with pipx) are :doc:`here </tools/monitor/installation>`.

Keeping MPF up-to-date
-----------------------

Once you have MPF installed via the procedure above, you can keep it up-to-date by running the final two pipx commands from above which you used to install MPF and MPF-MC.

Questions? Comments? Need help? You can post a reply into the MPF new installers for macOS thread in the MPF Users Google Group: https://groups.google.com/g/mpf-users/c/BIemtw17lx0
