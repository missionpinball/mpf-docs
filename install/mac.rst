Installing MPF on Mac (Aug 4 2022 update)
=========================================

This process is the new step-by-step process we are actively working out to get MPF 0.56 (current dev branch) installed on a Mac.

These instructions will change often over the next few days until we get the process dialed-in.

Also as we are working out the process, the installation instructions will involve lots of manual steps. We will integrate these into a more streamlined experience over time. For now we're just figuring out the process.

Overview of MPF on macOS
------------------------

MPF works on macOS running on both Intel and Apple Silicon (M1/M2 processors). These instructions are the same for both.

This process has been confirmed to work on macOS 12.5 and 12.6. It could in theory work as far back as macOS 10.9 (though possibly kivy requires 10.14 or something). If you have an older version of macOS, give it a shot and let us know.

These instructions will only work with Python 3.9. It will be possible to support 3.8 as well, but since these wheels are manually built at this time we are just targeting 3.9. If you need 3.8, let us know. (Though it's possible to have multiple Python versions side-by-side, so hopefully everyone can just use 3.9 and keep it easy for us.)

1. Install Python 3.9.13 from python.org. Be sure to get the Universal installer, not the Intel one. (https://www.python.org/ftp/python/3.9.13/python-3.9.13-macos11.pkg)
2. Install Homebrew (https://brew.sh/). This will also install the Xcode command line tools if you don't have them. A lot of stuff will scroll by and it might take awhile.
3. When homebrew is done, there are two "next steps" listed in the terminal. Copy both of those into the terminal and run them. They're used to ensure brew is on your path.
4. Install the libraries MPF MC needs: ``brew install SDL2 SDL2_mixer SDL2_image SDL2_ttf gstreamer gst-plugins-base gst-plugins-good gst-plugins-bad gst-plugins-ugly pkg-config``
5. Use pip to install / update some Python modules MPF needs to set up: ``pip3 install --upgrade pip setuptools wheel build virtualenv``
6. Install Kivy, also via the command line: ``pip3 install "kivy[full]"``
7. Download the MPF MC macOS "wheel" from here: https://www.dropbox.com/s/afnnc07v9b9hgj5/mpf_mc-0.56.0.dev3-cp39-cp39-macosx_10_9_universal2.whl?dl=1 (This is a temporary wheel in a temporary location.)
8. Install MPF MC from the .whl file you just downloaded via the command line: ``pip3 install mpf_mc-0.56.0.dev3-cp39-cp39-macosx_10_9_universal2.whl``
9. Finally, there's a library that Kivy installs that conflicts with some stuff that MPF uses, so remove that via ``pip3 uninstall pillow``

At this point, MPF 0.56.0.dev-something(20 maybe?) and MPF-MC 0.56.0.dev3 should be installed. To test, download the ``mpf-examples`` repo from here: https://github.com/missionpinball/mpf-examples. You can either clone it locally, or download the zip file and unzip it. Either is fine, just do what you're most comfortable with. Be sure to download / switch to the ``dev`` branch.

Then back in the terminal, change into the ``mpf-examples`` folder (or whatever folder you just unzipped that into), then change into the ``mc_demo`` folder, then run ``mpf both``. That should launch the mc_demo code (which is Media Controller demo). A window should open with a red background and some text about slides, you should be able to use the right arrow key to advance to the next slide. You should be able to use the left arrow key to go back to the previous slide and you should hear a drum and cymbal sound when you change the slide.

You will see a bunch of warnings about some classes implemented in multiple locations, and how one will be used, but which one is undefined. It sounds scary, but this is normal. (For now.) We are investigating whether this is something we need to fix, and how we'll fix it if so. But for now it's fine.

At this point, MPF is ready to go!

Notes, Caveats & Next Steps
---------------------------

This new installer process is actually part of the MPF-MC repo (the media controller), not core MPF itself. The reason is that the MPF-MC has font and audio code that needs to be compiled to integrate with the system's media frameworks and kivy, so it's a complicated installation.

The wheel file you download, and the new MPF-MC installer project, is all happening in a branch of MPF-MC called "new-installer": https://github.com/missionpinball/mpf-mc/tree/new-installer

Once these installers are done and tested, we will merge the new-installer branch into the MPF-MC dev branch (which you will be able to install via ``pip`` instead of having to download that wheel from dropbox.)

If you're familiar with Python, you should probably use Python virtual environments for this. Once we get a more final installer, we will probably prescribe using ``pipx`` which will automatically handle all that.

If have existing SDL and Gstreamer libraries installed (check the ``/Library/Frameworks`` folder), you can delete them. The versions that brew installs will go into the ``/opt/homebrew`` folder.

Do NOT use brew to install Python. Why? Because the Python in brew is meant to support other brew packages that need python, and as such it will automatically "upgrade" you to the latest Python, even on its own, which means your Python will flip to 3.10 and MPF won't work and you'll be sad. So that's why we install the "Framework Python" from python.org. (Why's it called "Framework Python"? Because it installs like a framework to that ``/Library/Frameworks`` folder.)

Eventually the installation process will handle many of the steps, like installing kivy, etc. It's just extra-manual for now.

Questions? Comments? Need help? You can post a reply into the MPF new installers for macOS thread in the MPF Users Google Group: https://groups.google.com/g/mpf-users/c/BIemtw17lx0

Or email me, Brian Madden, brian@fastpinball.com.

These installers are changing daily (or multiple times a day), and I'm hoping to get everything done and officially published in the next few days.