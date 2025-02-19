---
title: How to create and understand YAML files
---

# How to create and understand YAML files

## Intro

YAML is a markup language used for creating structured data. MPF uses YAML files as
the way to declare the components in your game, the rules, and the interactions.
These files are not run the way you might normally think about a computer program (top to bottom as a list of commands to execute), and instead are read in by the MPF game engine and then used to tell the
engine how to behave.

## Structure:

### Keys and Values:

YAML basic structure is the key-value pair. In the following example, "name", "year", and "brand" are the keys and "Gorgar", the number 1979, and "Williams" are the values.

```yaml
name: Gorgar
year: 1979
brand: Williams
```

Other terms for "keys" are "attributes" and "properties", though these two terms can also be used to refer to the key _along_with_ its accompanying value.

### Objects:

In the above examples, these attributes are not grouped by anything, as they are just sitting at the top (indentation) level of the file. We can introduce the second piece of YAML structure to help with this - the "object" (aka "map" or "record", or even "namespace"). An object has a key at its top level, and then instead of a simple value, has a set of key-value pairs nested inside of it.

```yaml
game:
  name: Gorgar
  year: 1979
```

#### Illegal examples:

In YAML you cannot repeat the same key name in the same grouping level, so both of the following are illegal:
```yaml
game:
  name: TOTAN
  name: Tales of the Arabian Nights #This is illegal because "name" has already been used inside of "game"

game: #This is illegal because we already used "game" on the first line
  name: TRON
```

It is also illegal to give a key a simple value as well as a nested set of values.
```yaml
game: Gorgar #This is illegal because game has the simple value "Gorgar" AS WELL as the sub-object {year: 1979}
  year: 1979
```

### Lists:

The last basic building block of YAML is the list. With lists, we can repeat structures as many times as we want.
```yaml
# list style 1
games:
  - game_one
  - game_two

# list style 2
games:
  - name: Godzilla
    year: 2021
  - name: Gorgar
    year: 1979

# mpf inline list style
mpf_example:
  my_event_list: trigger_event_1, trigger_event_2
```
 In some cases you can write a list using the MPF inline list style. This is commonly found with event lists or switch lists.

## Comments:

In yaml you can "comment" any line to disable it, by putting a '#' before the first non-space character on the line.
You can also leave a comment at the end of the line, in case you need to leave a note for the future.

```yaml
#foo: bar #this line is commented out completely
name: Godzilla #this line is active (or "uncommented") but has a comment note after
```

If you comment out a **key** that has nested properties under it, you will need to comment out those lines as well! You _can_ comment out properties at the lowest level without commenting out the intermediate levels.

```yaml
# The following is legal:
game:
  name: The Shadow
  # year: 1994

# The following is illegal:
#game:
  name: The Shadow
```

Many code editors support hotkeys for quickly commenting/uncommenting the line the cursor is on. Try it with CTRL+'/' or CMD+'/'


## MPF Special comments:

Throughout this documentation website and the codebases found on the [Mission Pinball github](https://github.com/missionpinball/) you may see comments with extra symbols following the first '#'. For example, on [Scoring](../../game_logic/scoring.md) we have the example:

```yaml
##! mode: mode1
variable_player:
  s_your_switch_active:
    score: 100
```

Here the example is trying to help you decide where to put this sample code. In this case, `##! mode: mode1` means "put this code block in the mode file named mode1". Later on the same page we see more examples, with a different usage of the `##!`.

```yaml
##! test
#! start_game
#! assert_player_variable 1 multiplier
```

Here the `##! test` is actually a directive to the MPF testing utility to take the next lines (starting with `#!`) as test commands.

## Indentation

In most of the examples on this site you will see two spaces used for every indentation level. If you prefer, you can write your code with 3, 4, 8, or whatever number of spaces per level you want, _as long as you are consistent_

## Data types

MPF's use of YAML supports many simple data types - integer, float, boolean, string 


## Advance YAML

MPF supports 