# Debugging

At some point in time you might have to debug either your own code or you want to debug the orginal MPF code. For this of course a Python debugger is needed. You can use your preferred tool and are not bound to a specific tool. In this chapter the debugging is explained using the [PyCharm Community Edition](https://www.jetbrains.com/pycharm/download/other.html). Regardless if you want to debug your own code or the MPF code itself, the process is the same and you can follow these instructions.

## Basic Setup
First of all you need to install MPF using a virtual environment and not using a precompile package, follow the [install chapter](../../install/index.md) for this. Then of course you need to install PyCharm, there is not much to do to install PyCharm after the download just run the installer.


## Open Project in PyCharm
Open the folder structure in PyCharm where you source file is located you would like to debug, that might be your machine folder with your own code extension or it might be the mpf sources which are located inside your virtual environment. From the `File` menu select `open`, if you don't see the `File` menu you have to click the three horizontal lines (Hamburger button) to make the menu visible.

A pop-up window will open, now either navigate and select your machine folder or your virtual environment folder:

![open menu](images/debug_open_project.png)

## Set breakpoint

On the left side you will find the file structure, here you need to navigate to the source file you want to debug. Open that file in the code editor.

By clicking on the line number you can set a breakpoint:

![open menu](images/debug_set_breakpoint.png)

## Attach to process

Now it is time to start mpf like you normally do. Keep in mind, that before you start mpf with e.g. `mpf -t -b`, that you need to [activate](../../install/virtual-environments.md) your Python virtual environment.

From the `Run` menu select `Attach to Process`

![open menu](images/debug_attach.png)

Afterwards a new pop-up window will open up

![open menu](images/debug_select_process.png)

from where you need to select your mpf process, depeding what other (Python) process you have running the list might be shorter or longer.

## Start Debugging

Run your game and wait until your game flow hits the debugger. Now you have the normal debugging options like stepping in or looking into variables.

![open menu](images/debug_code.png)
