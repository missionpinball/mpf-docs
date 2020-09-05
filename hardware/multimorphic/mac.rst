How to install P-ROC / P3-ROC drivers on Mac OS
===============================================

Installing the P-ROC drivers (libpinproc and pypinproc) on the Mac is a manual
process that requires a few prerequisites and some supporting software. We
chose to use the `homebrew <http://brew.sh>`_ package manager to help us with
the install, which is similar to the apt-get package manager in Linux. The
following instructions will help you get homebrew installed, along with
everything else.

These instructions assume you have already installed MPF.app. If you haven't,
you will need to :doc:`go back and do that first </install/mac>`, since it has
to be installed before you can build the P-ROC drivers.

1. Install Brew
^^^^^^^^^^^^^^^

Open a Terminal and paste in the following commands (and then press <Enter>
after each one):

::

   cd /usr/local
   /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

If you're prompted to install Xcode, click Install, followed by Agree.

After Xcode installs (or right away if you already had it), press Return
to continue and then enter your password.

You'll see a bunch of stuff scroll by as things are downloaded and installed.

2. Create a folder in your user folder called “proc"
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

From the same terminal window, run:

::

  mkdir ^/proc

3. Download osx-proc-support
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Change to that new folder:

::

  cd ^/proc

And run the following command which will clone (download) the files you need
to make the P-ROC run on the Mac. (Even though this is called "osx-proc-support",
it also works with MacOS Sierra.)

::

  git clone https://github.com/missionpinball/osx-proc-support

4. Install prerequisites via Brew
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Now run:

::

  brew install libftdi libusb-compat cmake

5. Install yaml-cpp
^^^^^^^^^^^^^^^^^^^

The P-ROC/P3-ROC requires a library called yaml-cpp. While there is a yaml-cpp
package in brew, it's too new to use here. Adding to the fuss is that the
version we need is no longer available, so we included it on the
osx-proc-support package that you downloaded earlier.

Run the following commands to compile it from scratch:

::

    cd ^/proc/osx-proc-support
    tar -xzf yaml-cpp-0.2.5.tar.gz
    cd yaml-cpp-0.2.5
    mkdir bin
    cd bin
    cmake ..
    make
    sudo make install

6. Download & install libpinproc
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Libpinproc is the P-ROC/P3-ROC library that lets the host computer talk to the
P-ROC/P3-ROC hardware. Run the following commands:

::

    cd ^/proc
    git clone --branch=master https://github.com/missionpinball/libpinproc

Copy the Mac version of CMakeLists.txt to the libpinproc folder:

::

    cp -r ^/proc/osx-proc-support/CMakeLists.txt ^/proc/libpinproc

That avoids having to edit the file manually. It should work for nearly all
situations, but if libpinproc won't compile in the next steps, you should make
sure the paths in ``include_dirs`` within CMakeLists.txt are correct.

::

    cd libpinproc
    mkdir bin
    cd bin
    cmake -DBUILD_SHARED_LIBS=ON ..
    make
    sudo make install

7. Download & install pypinproc 2.1
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Pypinproc is a wrapper library that allows Python apps (like MPF) to talk to
the libpinproc that you installed in the previous step. Unfortunately the
version that is available from the multimorphic.com website only works
with Python 2.x, and MPF uses Python 3.x, so you have to download a version
that we modified to work with Python 3:

::

    cd ^/proc
    git clone https://github.com/missionpinball/pypinproc
    cd pypinproc
    python3 setup.py build
    sudo python3 setup.py install

(If you prefer to install pypinproc in a virtualenv, make sure it's activated
before this step, and omit sudo from the last line.)


8. Install D2xxHelper
^^^^^^^^^^^^^^^^^^^^^

D2xxHelper is provided by FTDI Chips, the maker of the chip which acts as the
USB interface on the P-ROC/P3-ROC boards. Mac OS comes with its own FTDI driver
that's loaded by default and prevents other FTDI drivers from running.
D2xxHelper adjusts the priorities of FTDI driver loading so that the FTDI
driver we need loads first, preventing the Apple FTDI driver from loading. This
is Apple Support's recommended method of solving the problem, so you're safe.
You'll be prompted by Gatekeeper to enter your password to accept installation
of the package- this is normal. You'll also be warned that this package may be
incompatible with future versions of macOS.

::

 cd ^/proc/osx-proc-support
 sudo installer -pkg D2xxHelper_v2.0.0.pkg -target /

9. Reboot
^^^^^^^^^

You have to reboot in order to have the changes D2xxHelper made take effect.
After that, you should be all set and can continue on with the :doc:`platform`
documentation to finish your MPF configuration for the P-ROC/P3-ROC.
