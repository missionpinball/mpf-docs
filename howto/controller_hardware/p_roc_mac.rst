How to install P-ROC / P3-ROC drivers on Mac OS X
=================================================

Installing the P-ROC drivers (libpinproc and pypinproc) on the Mac is a manual process that requires a few prerequisites
and some supporting software. We chose to use the `homebrew <http://brew.sh>`_ package manager to help us with the
install, which is similar to the apt-get package manager in Linux. The following instructions will help you get homebrew
installed, along with everything else.

These instructions assume you have already installed MPF.app. If you haven't, you will need to
`go back and do that first </install/mac>`_, since it has to be installed before you can build the P-ROC drivers.

1. Install Brew
~~~~~~~~~~~~~~~

Open a Terminal and paste in

::

  /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)

Click Install, followed by Agree if prompted to install Xcode

After Xcode installs, press Return and enter your admin password in the terminal window

2. Create a folder in your user folder called “proc"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
::

  mkdir ~/proc

3. Download osx-proc-support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
::

  cd ~/proc

:: 

  git clone https://github.com/missionpinball/osx-proc-support

4. Install prerequisites via Brew
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
::

  brew install libftdi libusb-compat cmake

5. Install yaml-cpp
~~~~~~~~~~~~~~~~~~~
While there is a yaml-cpp package in brew, it's too new to use here. Adding to the fuss is that the version we need is
no longer available, so we included it on the osx-proc-support package that you downloaded earlier.

We have to compile it from scratch:
::

    cd ~/proc/osx-proc-support
    tar -xzf yaml-cpp-0.2.5.tar.gz
    cd yaml-cpp.0.2.5
    mkdir bin
    cd bin
    cmake ..
    make
    sudo make install

6. Download & install libpinproc
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
::

    cd ~/proc
    git clone --branch=master https://github.com/preble/libpinproc
    
Copy the Mac version of CMakeLists.txt to the libpinproc folder
::
    
    cp -r ~/proc/osx-proc-support/CMakeLists.txt ~/proc/libpinproc

That avoids having to edit the file manually. It should work for nearly all situations, but if libpinproc won't compile in the next steps, you should make sure the paths in ``include_dirs`` within CMakeLists.txt are correct.
::

    cd libpinproc
    mkdir bin
    cd bin
    cmake -DBUILD_SHARED_LIBS=ON ..
    make
    sudo make install

7. Download & install pypinproc 2.1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This is the special version of pypinproc made for Python 3. You cannot use the version that normally goes along with a P-ROC install.
::

    cd ~/proc
    git clone https://github.com/missionpinball/pypinproc
    cd pypinproc
    kivy setup.py build
    sudo kivy setup.py install

8. Install D2xxHelper 
~~~~~~~~~~~~~~~~~~~~~
D2xxHelper is provided by FTDI Chips, the maker of the USB interface on the P-ROC board. OS X comes with its own FTDI driver that is loaded by default and prevents other FTDI drivers from running. D2xxHelper adjusts the priorities of FTDI driver loading so that the FTDI driver we need loads first, preventing the Apple FTDI driver from loading. This is Apple Support's recommended method of solving the problem, so you're safe.

::
 
 cd ~/proc/osx-proc-support
 sudo installer -pkg D2xxHelper_v2.0.0.pkg -target /

9. Reboot
~~~~~~~~~
You have to reboot in order to have the changes D2xxHelper made take effect. After that, you should be all set!
