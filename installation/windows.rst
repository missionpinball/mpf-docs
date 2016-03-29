Installing MPF on Windows
=========================



1. Install Python 3.4
=====================

On Windows platforms, MPF requires Python 3.4. If you're on
64-bit Windows, install the 64-bit version of Python. 32-bit should
use 32-bit. The easiest way to tell whether you have 32-bit or 64-bit
Windows is to open a command prompt and run (note this is case-sensitive):

::

    echo %PROCESSOR_ARCHITECTURE%

If it prints "x86", that's 32-bit. If it prints "x64", that's 64-bit.

+ `Download <https://www.python.org/ftp/python/3.4.4/python-3.4.4.msi>`_ the Python 3.4.4. x86 / 32-bit MSI installer.
+ `Download <https://www.python.org/ftp/python/3.4.4/python-3.4.4.amd64.msi>`_ the Python 3.4.4 x64 / 64-bit MSI installer.

Python 3 and Python 2 can run side-by-side no problem. If you just
installed Python for use with MPF, then you can first just remove the
old version of Python (via Add/Remove Programs). This will eventually
be our recommendation, but since MPF 0.30 is not done yet, you may
want to keep Python 2 and MPF 0.21 around for awhile. Then install
Python 3.4.4. On the "Customize Python 3.4.4" screen, we like to
select the option "Add python.exe" to Path. That way you can run
Python from anywhere. If you have both Python 3 and Python 2 installed
side-by-side, then every Python 3 command will have a "3" added to it.
(So you run "python3" instead of "python", "pip3" instead of "pip",
etc.) Once Python is installed, open a command prompt and type ``python --version <enter>``.
It should print ``Python 3.4.4``. If you get a
message about how 'python' is not recognized, log out and log back in.
(You have to do this when running a non-admin command prompt so it can
update the system path setting.) If you get a message that says you
have Python 2.x.x, then try ``python3 --version``.


2. Install MPF
--------------

If you have Python 2 and 3 installed on your computer, open a command prompt and
type the following command, then press <enter>:

::

    pip3 install mpf-mc

If you only have Python 3 installed (which is the case if you've never used
Python before), open a command prompt and type the following command, then press
 <enter>:

::

    pip install mpf-mc

*pip* is the name of the Python Package Manager. This command is telling pip to
install a package called "mpf-mc", which is the *Mission Pinball Framework -
Media Controller* package. When you run this, pip will connect to the internet
to the `Python Package Index <http:/pypi.python.org>`_  (called "PyPI") where
the *mpf-mc* is registered as a package. Pip will download MPF-MC, as well as
all the prerequisites for MPF-MC, and then install them onto your computer.

Note that the MPF-MC package is technically the package for the MPF Media
Controller, however, MPF-MC includes MPF in its list of prerequisites, meaning
if you install MPF- MC then you also get MPF. So installing MPF-MC right off the
bat is just a shortcut to install both MPF and MPF-MC in a single step.

3. Test your installation
-------------------------

.. todo:: Need to finish this.
