---
title: Using a Virtual Environment for MPF
---

# What is a Virtual Environment?

There are many versions of Python and many packages that can be installed, each
with its own dependencies on specific versions of other packages. A single Python
installation can get problematic if different installed packages depend on different
versions of the same package, and such dependency conflicts can cause bugs and even
prevent certain packages (like MPF) from running properly.

A "virtual environment" is a way to create an isolated, sandboxed environment for
a specific Python version. Packages installed in this environment are separate from
packages installed in other environments, including their dependencies.

**It is *highly recommended* to install MPF in a virtual environment.**

In fact, current releases of Debian (12) and Ubuntu (23) do not allow Python
packages to be installed outside of a virtual environment, so on those platforms
a virtual environment is required.

# Create a Virtual Environment

To create a virtual enviroment, choose a folder where you want to install
a copy of Python and keep the enviroment's packages. For this example, we'll
call the environment "mpfenv" and put it in our home directory (known as "~").

``` console
python3 -m venv ~/mpfenv
```

Or if you want to explicitly define a directory, like this example of an "mpf" virtual environment in a common venvs directory (because remember you can have as many virtual environments as you like):

``` console
  python3 -m venv C:\Users\Rudy\venvs\mpf
```

!!! note

    If you have multiple versions of Python3 (say, 3.9 and 3.11), you can specify
    which one to use in the virtual environment: ``python3.9 -m venv ~/mpfenv``

A virtual environment is recommended for any general-use computer you'll be
using MPF on. For a dedicated MPF machine that will have no other programs
installed (for example, a computer inside a pinball cabinet), a virtual
environment is not required (except see above note regarding Debian and Ubuntu)
but can still be helpful for keeping packages organized and cleanly upgrading.

# Activate your Virtual Environment

To keep itself isolated from other programs, your virtual enviroment only
activates when you tell it to.

!!! note  Make note of this activation command

    You may want to write this step down, as you'll run it every time you open up
    a terminal window to work on MPF. If you are on a dedicated MPF machine, you
    could add this line to your bash/zsh profile to automatically run it at login.


If you defined a specific path when creating your virtual environment, replace
`mpfenv` below with the path to the given folder, e.g., ``C:\Users\Rudy\venvs\mpf``.

**Windows:**
For Windows users, you will activate with a bat/ps1 script depending on whether
you're using the Command Prompt or the PowerShell. The script lives in the "Scripts"
folder under where you created your virtual environment.

``` console
# Command Prompt:
> mpfenv/Scripts/activate.bat

# PowerShell:
PS > mpfenv/Scripts/Activate.ps1
```

**Mac:**

For users on Mac OSX, you will use the `source` command with the path to your venv:

``` console
  source ~/mpfenv/bin/activate
```

**Linux:**

Linux users can enable the virtual environment with the dot command from the terminal:
``` console
. ~/mpfenv/bin/activate
```

Note that the first character is a period, followed by a space, then the path
to your virtual environment and "/bin/activate". The period performs the same function as
the `source` command, and is POSIX compliant.


**All Platforms:**

After you run the activation, you'll know you're in the virtual environment
because the console prompt will include the name of your venv in parenthesis.

``` console
My-Mac:~ python --version
Python 2.7.10
My-Mac:~ source ~/mpfenv/bin/activate
(mpfenv) My-Mac:~ python --version
Python 3.9.13
(mpfenv) My-Mac:~
```

!!! note  "Virtual environments set a default python"

    The python you used to create the virtual environment will now be the
    default python. Outside the virtual environment "python" may be Python 2 or 3, and
    "python3" may be 3.6 or 3.9 or 3.11; inside the virtual environment,
    you can use "python" to refer to the exact version of Python 3 you used
    to create the virtual environment


!!! note  "Deactivation of virtual environments"

    If you want to deactivate your virtual environment, you can simply enter `deactivate` at the prompt.
    The virtual environment sets this up for us, usually as an alias. The console prompt now won't include
    the name of your venv in parenthesis.
    
