---
title: config_version 6
---

# Changes in MPF config version 6

MPF uses version numbers in its YAML config files which ensure that MPF is loading
files that are compatible with the version of MPF that's running. [More info on config versions](config_version.md)

MPF 0.57 moves from config version 5 to config version 6 (and from show version 5 to 6 as well). This page documents the changes.

## Why config version 6?

Back when MPF was new, we added some "hacks" to the YAML processor to make it easier to write config files. At the time we thought this would make the YAML files easier to use for non-programmers. While that was somewhat true, it turns out that the "hacks" we added made it harder to maintain MPF and to add new features. (These hacks are part of the reason it took us so long to support Python versions newer than 3.9.)

Those hacks are being removed in MPF 0.57, which means you'll need to update your config files so they use "pure" YAML and don't include any of our older hacks. Luckily this is a pretty straightforward process, mostly doing some "find and replace". (Details below) As part of that, you'll also need to update your config files to config version 6.

## Specific changes you need to make

If you want ot know what specific hacks MPF used prior to config version 6, see the
"What were the hacks?" section below. But if you just care about updating your YAML files,
here's what you need to do:

1. Find and replace `#config_version=5` with `#config_version=6`.
2. Find and replace `#show_version=5` with `#show_version=6`.
3. Find and replace `: +` with `: "+`. You'll need to also add the quote to the end of the line. Or if you only have a few different values, you can find and replace the entire line, like `time: +1` with `time: "+1"`, `time: +2` with `time: "+2"`, etc.
4. Search for any value that starts with a leading zero, like `: 0` and then see if it only has digits after the zero. If so, add quotes around the value. e.g. `: "000066"`.
5. You might have a bit of cleanup for some random other things which are now invalid YAML (as outlined below), but the easiest way to do that is just to run your game and then hunt down any last remaining errors as they come up.

That's it! Not too bad overall. We updated several configs for complete and mature machines, and
each machine's entire bundle of configs and shows only took a few minutes. It's really pretty quick.

## What were the hacks?

Here are hacks that MPF used prior to config version 6:

**Values beginning with "+" are strings**

   The YAML spec views values that begin with a plus sign as numbers. So a line like `time: +1`
   is the same as `time: 1`. But for MPF, these mean different things. (e.g. in shows, a time of
   `+1` means "one second after the previous step", while `1` means "one second after the show start".)

   The fix for this is to add quotes around the values that start with plus. e.g. `time: "+1"` instead of `time: +1`.

**Values beginning with a leading "0" are strings**

   The YAML spec will process values that are only digits with leading zeros as numbers.
   So in pure YAML, `color: 000066` would be processed as `color: 66` which is wrong.

   The fix for this is to add quotes around the values that are only numbers and start with a leading zero. e.g. `color: "000066"` instead of `color: 000066`.

**Values with only digits and "e" are strings**

   The YAML spec will process a value like ``123e45`` as "123 exponent 45". Since those could
   be hex color codes, MPF's YAML interface processes values that are all digits with a single
   "e" character as strings.
