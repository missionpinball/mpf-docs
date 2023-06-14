---
title: MPF commands
---

# MPF commands


MPF offers multiple command-line commands. Almost all of those commands
should executed from within your MPF machine folder.

Usually you start MPF using:

``` shell
$ mpf both
```

Alternatively your can run MPF and MC separately:

``` shell
$ mpf game
```

and:

``` shell
$ mpf mc
```

To start the interactive service cli run (start mpf both before):

``` shell
$ mpf service
```

If you want to see details about your hardware (do not run MPF in
parallel):

``` shell
$ mpf hardware scan
```

To update the firmware of your hardware controllers (if supported by
your platform):

``` shell
$ mpf hardware firmware_update
```

* [mpf both](both.md)
* [mpf core](core.md)
* [mpf diagnosis](diagnosis.md)
* [mpf game](../../game/index.md)
* [mpf mc](mc.md)
* [mpf imc](imc.md)
* [mpf migrate](migrate.md)
* [mpf
monitor](monitor)
* [mpf hardware](../../hardware/index.md)
* [mpf service](service.md)
* [mpf build](build.md)
* [mpf test](test.md)
* [mpf format](format.md)
