---
title: mpf (default) (command-line utility)
---

# `mpf (default)` (command-line utility)


When you run the shell command `$ mpf` and you do not include the name of a command,
the default of `game` will be used.

So the following pairs are equivalent:

```shell
$ mpf game -btx
$ mpf -btx
```

or

```shell
$ mpf game path/to/game_folder -P
$ mpf path/to/game_folder -P
```

or

```shell
$ mpf game -c my_config
$ mpf -c my_config
```

For options and command reference, see: [mpf game](game.md)