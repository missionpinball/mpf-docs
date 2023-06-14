---
title: CFE-show-1: Show does not appear to be a valid show config
---

# CFE-show-1: Show does not appear to be a valid show config


Related Config File Sections:

* [shows:](../config/shows.md)

This error occurs when MPF loads a show which is not a list of steps.
There are two ways to add shows to your machine: either as file or
inside your config. Both can happen inside a mode or machine-wide inside
your global config folder.

## Examples

### File Shows

This is how a file show should look:

``` mpf-config
##! show: flash_red
#show_version=5
- duration: 1
  lights:
    led1: red
- duration: 1
  lights:
    led1: off
```

Please note that there can be only one show per dedicated show file as
MPF uses the filename as show name. See
[Creating standalone show files](../shows/file_shows.md) for details.

### Config Shows

This is how a show inside your config should look:

``` mpf-config
shows:
  flash_red:
    - duration: 1
      lights:
        led1: red
    - duration: 1
      lights:
        led1: off
```

See [/shows/index](../shows/config_shows.md) for details.

## Common Pitfalls

### Multiple shows inside one file show

This is NOT valid as file show:

``` yaml
# INVALID FILE SHOW
flash_red:
  - duration: 1
    # [...]
flash_blue:
  - duration: 1
    # [...]
```

Instead you have to create two files `flash_red.yaml` and
`flash_blue.yaml`.

### Missing hyphen for your step

You might have missed the hyphon in front of your first step (or in
front of all steps):

``` yaml
# INVALID FILE SHOW
#show_version=5
duration: 1    # note the missing dash here
lights:
  led1: red
```

The same can happen in config shows:

``` yaml
# INVALID CONFIG SHOW
shows:
  flash_red:
    duration: 1   # hyphen missing here
    lights:
      led1: red
```

This often happens with one step shows. See above for working examples.

## Need more help troubleshooting?

Have a look at our [Troubleshooting](../troubleshooting/index.md) section. It might give you some hints for certain classes of
problems.

## What if this did not fix your problem?

Please tell us about your error in the [MPF Users Google
Group](https://groups.google.com/forum/#!forum/mpf-users) and we might
be able to update this page afterwards. Or even better:
[You help us to update it afterwards](../about/help_docs.md).

## Is something missing here? Do you have a helpful hint for others experiencing this error?

Please
[create a Pull Request and add it](../about/help_docs.md). Alternatively, please tell us in the [MPF Users Google
Group](https://groups.google.com/forum/#!forum/mpf-users).

## Related How To guides

* [Shows](../shows/index.md)
