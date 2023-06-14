---
title: MPF command-line utility
---

# MPF command-line utility


When you install MPF, it registers an executable called `mpf` and puts
it in your system path. Everything you do with MPF will use this tool
from the command line.

Simply running `mpf` by itself will start the MPF game engine and run
whatever machine configuration is in the current folder. But you can
also use `mpf` to launch other things, like `mpf mc` to start the media
controller, or `mpf migrate` to migrate your config files to the current
version of MPF.

A full list of all the available commands, along with the various
command line options, is
[here](index.md).

## Command line options

### --version

Prints the version of MPF and exits:

``` console
$ mpf --version
MPF v0.xx.yy
```

### <command>

Runs the MPF command (with or without additional options).

See the [commands/index](commands/index.md) documentation for
options.
