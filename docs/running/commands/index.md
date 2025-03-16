---
title: MPF commands
---

# MPF commands


MPF offers multiple command-line commands. Almost all of those commands
should be executed from within your MPF machine folder. If you want to run
a command *not* inside your machine folder, you may include the path
to the game folder as [the first argument](#machine_folder) after the command name, BEFORE
any of the dashed options.


Each of the following commands can take a variety of options, which have
been omitted on this page to simplify the represented workflow steps.
See the specific command reference pages to determine which command line
options you will need for your particular use cases.



### Commands for starting your game



To start the MPF game engine as well as the media controller, you can use:

``` shell
$ mpf both
```

Alternatively your can run MPF and MC separately:

``` shell
$ mpf game
```

and in another shell window:

``` shell
$ mpf mc
```

*Note: MPF MC is the media controller used before MPF 0.80.
For MPF GMC with MPF 0.80+, see: [Godot Media Controller](../../gmc/index.md)*


### Commands to run alongside your game

Many commands can connect with the MPF game instance to assist with development tasks.
For these, make sure your game is running (e.g. with `game` or `both`), and then run the
command in another shell instance.

To start the interactive service cli, after starting your game run:

``` shell
$ mpf service
```

To start the interactive monitor tool (which requires a [separate install](../../tools/monitor/installation.md)) run:

```shell
$ mpf monitor
```

### Other commands

Some commands may need to be run ___without___ a running game.


If you want to see details about your hardware (while **NOT** running MPF in parallel):

``` shell
$ mpf hardware scan
```

To update the firmware of your hardware controllers (if supported by your platform):

``` shell
$ mpf hardware firmware_update
```

## Full Command Reference

* [mpf both](both.md)
* [mpf core](core.md)
* [mpf diagnosis](diagnosis.md)
* [mpf game](game.md)
* [mpf (default)](mpf.md)
* [mpf mc](mc.md)
* [mpf imc](imc.md)
* [mpf migrate](migrate.md)
* [mpf monitor](monitor.md)
* [mpf hardware](hardware.md)
* [mpf service](service.md)
* [mpf build](build.md)
* [mpf test](test.md)
* [mpf format](format.md)

There are over a dozen commands for `mpf`, but it is also possible to run `$ mpf` without
writing a command name at all. If you do not use any of the specific command names,
you are [defaulted](mpf.md) to `game`.

So `$ mpf` by itself is the same as `$ mpf game`.


## Optional Arguments


### machine_folder

To use the machine_folder optional argument, you must include it after the command name, for example:

```shell
$ mpf game ./path/to/machine_folder -P
```

If you do not include this argument, your current folder will be assumed to be the machine folder.
