Installing MPF on Mac (Aug 19, 2022 update)
=========================================

This process is the new step-by-step process we are actively working out to get MPF 0.56 (current dev branch) installed on a Mac.

Overview of MPF on macOS
------------------------

MPF works on macOS running on both Intel and Apple Silicon (M1/M2 processors). These instructions are the same for both.

Apple Silicon (M1/M2 processors) require macOS Monterey as well as Python 3.9. With Intel processors, MPF can work as far back as 10.14 (or so? let us know!), and can use Python 3.7, 3.8, or 3.9.

Here is the quick version:

1. If you do not have Python, install Python 3.9.13 from python.org. If you have an M1/M2 Mac, be sure to get the Universal installer, not the Intel one. (https://www.python.org/ftp/python/3.9.13/python-3.9.13-macos11.pkg)
2. Install Homebrew (https://brew.sh/). This will also install the Xcode command line tools if you don't have them. A lot of stuff will scroll by and it might take awhile.
3. When homebrew is done, there are two "next steps" listed in the terminal. Copy both of those into the terminal and run them. They're used to ensure brew is on your path.
4. Use brew to install the libraries and other support files MPF needs: ``brew install SDL2 SDL2_mixer SDL2_image gstreamer gst-plugins-base gst-plugins-good gst-plugins-bad gst-plugins-ugly pipx``
5. Run ``pipx ensurepath`` which will configure things pipx installs to be able to run from anywhere.
6. Use pipx to install MPF with all optional components. ``pipx install mpf[all] --pip-args="--pre" --python $(which python3) --verbose --include-deps``
7. Use pipx to install MPF-MC. ``pipx install mpf-mc --pip-args="--pre" --python $(which python3) --verbose --include-deps``


At this point, MPF 0.56.0.devXX and MPF-MC 0.56.0.devXX are installed. (The "XX" in the version will be the dev build numbers.)

To test, download the ``mpf-examples`` repo from here: https://github.com/missionpinball/mpf-examples. You can either clone it locally, or download the zip file and unzip it. Either is fine, just do what you're most comfortable with. Be sure to download / switch to the ``dev`` branch.

Then back in the terminal, change into the ``mpf-examples`` folder (or whatever folder you just unzipped that into), then change into the ``mc_demo`` folder, then run ``mpf both``. That should launch the mc_demo code (which is Media Controller demo). A window should open with a red background and some text about slides, you should be able to use the right arrow key to advance to the next slide. You should be able to use the left arrow key to go back to the previous slide and you should hear a drum and cymbal sound when you change the slide.

You will see a bunch of warnings about some classes implemented in multiple locations, and how one will be used, but which one is undefined. It sounds scary, but this is normal. (For now.) We are investigating whether this is something we need to fix, and how we'll fix it if so. But for now it's fine.

At this point, MPF is ready to go!

Notes, Caveats & Next Steps
---------------------------

If have existing SDL and Gstreamer libraries installed (check the ``/Library/Frameworks`` folder), you can delete them. The versions that brew installs will go into the ``/opt/homebrew`` folder.

Do NOT use brew to install Python. Why? Because the Python in brew is meant to support other brew packages that need python, and as such it will automatically "upgrade" you to the latest Python, even on its own, which means your Python will flip to 3.10 and MPF won't work and you'll be sad. So that's why we install the "Framework Python" from python.org. (Why's it called "Framework Python"? Because it installs like a framework to that ``/Library/Frameworks`` folder.)

Keeping MPF up-to-date
-----------------------

Once you have MPF installed via the procedure above, you can keep it up-to-date by running the final two pipx commands from above which you used to install MPF and MPF-MC.

Questions? Comments? Need help? You can post a reply into the MPF new installers for macOS thread in the MPF Users Google Group: https://groups.google.com/g/mpf-users/c/BIemtw17lx0

Or email me, Brian Madden, brian@fastpinball.com.