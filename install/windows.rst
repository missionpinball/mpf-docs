Installing MPF on Windows (Aug 16, 2022 update)
===============================================

This process is the new step-by-step process we are actively working out to get MPF 0.56 (current dev branch) installed on a Windows machine.

Current version these instructions are for v0.56.0, which is the current "dev" branch of MPF.

Overview of MPF on Windows
--------------------------

We test MPF on Windows 10 and Windows 11. Older versions of Windows might (probably?) work too, we just don't test them. MPF requires 64-bit (x86) Windows running on Intel-compatible processors. It does not run on 32-bit systems and does not run on ARM processors on Windows.

MPF 0.56 requires Python 3.7, 3.8, or 3.9.

Here are the steps:

Install Python from python.org. Pick the latest version of Python 3.9 (which is 3.9.13 at the time of this writing).

Then open a command prompt (you can just run "cmd"), and type each of these commands one at a time (and hit enter after each one):

.. code-block:: doscon

  pip install --user pipx
  python -m pipx ensurepath

After this, restart the cmd window. (Just close it and then open a new one.) Then type these commands, hitting enter after each one:

.. code-block:: doscon

    pipx install mpf[all] --pip-args="--pre" --verbose --include-deps
    pipx install mpf-mc --pip-args="--pre" --verbose --include-deps

At this point, MPF 0.56.0.devXX and MPF-MC 0.56.0.devXX are installed. (The "XX" in the version will be the dev build numbers.)

To test, download the ``mpf-examples`` repo from here: https://github.com/missionpinball/mpf-examples. You can either clone it locally, or download the zip file and unzip it. Either is fine, just do what you're most comfortable with. Be sure to download / switch to the ``dev`` branch.

Then back in the command terminal, change into the ``mpf-examples`` folder (or whatever folder you just unzipped that into), then change into the ``mc_demo`` folder, then run ``mpf both``. That should launch the mc_demo code (which is Media Controller demo). A window should open with a red background and some text about slides, you should be able to use the right arrow key to advance to the next slide. You should be able to use the left arrow key to go back to the previous slide and you should hear a drum and cymbal sound when you change the slide.

You will see a bunch of warnings about some classes implemented in multiple locations, and how one will be used, but which one is undefined. It sounds scary, but this is normal. (For now.) We are investigating whether this is something we need to fix, and how we'll fix it if so. But for now it's fine.

At this point, MPF is ready to go!

Keeping MPF up-to-date
-----------------------

Once you have MPF installed via the procedure above, you can keep it up-to-date by running the final two pipx commands from above which you used to install MPF and MPF-MC.

Questions? Comments? Need help? You can post a reply into the MPF new installers for macOS thread in the MPF Users Google Group: https://groups.google.com/g/mpf-users/c/BIemtw17lx0

Or email me, Brian Madden, brian@fastpinball.com.