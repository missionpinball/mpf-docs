---
title: How to start MPF and run your game
---

# How to start MPF and run your game


MPF is a console-based application which you run from the command line.

## The quick version

1.  Open a command prompt
2.  Switch to your machine folder
3.  Run `mpf both`

## Starting the MPF game engine and media controller together

You can start both the MPF game engine and the
[media controller](../start/media_controller.md) at the same time with a single command.

Since this is done from the command line, you'll need to open a command
line window. On Windows, you can right-click on the Start Button (or
whatever it's called these days) and click the "Command Prompt". On
Mac OS X you can run the Terminal app. On Linux, well, if you're using
Linux, you know what a command line is. :)

From the command line, change to the directory which is the root of your
machine folder. This is the folder that contains your machine's
`config`, `modes`, `shows`, etc. folders.

!!! note

    Prior to MPF 0.30, we recommended that you put your machine's folder in
    the `/machine_files` folder inside the MPF package. That is changed now,
    and you can put your machine folder(s) wherever you want. In fact now
    that MPF has a "real" installer, the MPF package folder is hidden deep
    inside your system.

Then run:

``` console
mpf both <enter>
```

The `mpf both` command is what we use and probably what you'll use 99%
of the time.

## Starting the MPF media controller

Alternately you can choose to run just the media controller by itself
(still from within your machine folder) like this:

``` console
mpf mc <enter>
```

You should see a popup window and a bunch of stuff scroll by in the
console.

## Starting the MPF game engine

You can run the MPF game engine by itself (no media controller) by running:

``` console
mpf <enter>
```

Note that if you do not have a media controller running, the game engine
won't start fully because it will get stuck trying to connect to the
media controller. To avoid this if you just want to run the game engine
by itself, add the `-b` command line option. (Details below)

## Specifying command-line options

There are several command-like options you can use when you run MPF. To
use them, add them *after* the name of the MPF command you're running,
like:

``` console
mpf -x -v

mpf mc -xvV

mpf both -v -b
```

The full list of available commands is covered in the documentation for
each command (discussed below). For a list of all the 'mpf game' command-line options, see [C](../running/commands/game.md).

## Understanding how this works

When you install MPF, the command `mpf` is registered with your system.
Then you can open a command prompt and run "mpf" from any folder.

There are several sub-commands you can specify when you run MPF. You
specify a sub-command by running `mpf <command>`. (Some mpf commands
take additional options).

Here's a list of valid MPF commands. Click on any one of them for full
details and command-line options.

* [MPF command-line utility](mpf.md) (Starts the MPF game engine and other commands)
* [mpf](commands/game.md) (Starts the MPF engine)
* [mpf mc](commands/mc.md) (Starts the MPF Media Controller)
* [mpf both](commands/both.md) (Starts both the MPF engine and media controller at the same time)
* [mpf migrate](commands/migrate.md) (Migrates older config and show files to the current version)
* [mpf hardware](commands/hardware.md) (Scan, inspect and configure hardware)
* [mpf service](commands/service.md) (Service command line interface)
* [mpf build](commands/build.md) (Build production bundles)

## Specifying BCP ports

By default, the MPF game engine and the MC will connect via TCP port 5050.
[You can change that port to whatever you want though](ports.md).

* [MPF command launcher](mpf.md)
* [MPF commands](commands/index.md)
* [Specifying BCP ports](ports.md)
