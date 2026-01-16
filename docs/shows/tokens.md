---
title: Using "tokens" for run-time variable replacement in shows
---

# Using "tokens" for run-time variable replacement in shows

One of the most powerful features of shows in MPF is that you can build
shows that contain "placeholder" tokens which are dynamically replaced
with actual values when a show starts.

This lets you build reusable shows that you can then use in lots of
different situations with different lights, slides, events, etc.

## Shows without tokens

To understand how tokens work, let's first look at a show that does not
include any tokens, like this:

``` yaml
##! show: my_show
- time: 0
  lights:
    led_01: red
- time: 1
  lights:
    led_01: off
```

The example show above is simple. When it starts, it sets *led_01* to
red, then 1 second later it turns it off. You can run this show in a
loop to flash *led_01* between red and off.

If you called this show *flash_red*, you could play it via the
*show_player:* section of your config, like this:

``` yaml
show_player:
  some_event: flash_red
```

The problem with this show is that it's hard-coded. It only works for
*led_01*, and it only cycles the colors between red and off.

So what if you want to flash *led_01* between yellow and off? Or what if
you want to flash a different LED? With a show like the example above,
you'd have to write a new show for every LED with every possible color
combination you'd ever want. :(

## Adding tokens to shows

This is where tokens come in. Consider a slightly modified version of
the show above using a token instead of a hard-coded LED name:

``` yaml
##! show: my_show
- time: 0
  lights:
    (led): red
- time: 1
  lights:
    (led): off
```

Notice the second show is identical to the first, except every reference
to `led_01` has been replaced with `(led)`.

When MPF plays a show, it looks for words in the show contained in
parenthesis, and then it can use those parenthesis to replace values on
the fly.

So in the second show here, when you run the show, you could tell it
"replace the "leds" token with the value "led_02", which would make
a show like this:

``` yaml
##! show: my_show
- time: 0
  lights:
    led_02: red
- time: 1
  lights:
    led_02: off
```

The actual way that you start and send tokens to shows varies depending
on what you're doing in MPF. (Typically they're tied to shots or
events.)

For example, here's how you'd do it via the *show_player:*. (In this
example, we also add `loops: -1` which will cause the show to loop
(repeat) indefinitely.

``` yaml
show_player:
  some_event:
    flash_red:
      loops: -1
      show_tokens:
        led: led_02
```

MPF can run multiple instances of a show at the same time, so you could
run the above show multiple times (at the same time), passing different
tokens to each one, meaning you could use the same show to flash lots of
lights at once:

``` yaml
show_player:
  some_event:
    flash_red:
      loops: -1
      show_tokens:
        led: led_02
  some_other_event:
    flash_red:
      loops: -1
      show_tokens:
        led: led_03
```

## Putting multiple values into a single token

You can also use tags to insert multiple values into a single token. For
example, consider the following section from your machine config:

``` yaml
lights:
  led_01:
    number: 00
    tags: tag1
  led_02:
    number: 01
    tags: tag1
```

You can see that both *led_01* and *led_02* have the *tag1* tag applied.
So if you play the show above (with the *leds* token), you can actually
pass the tag name to the token instead:

``` yaml
show_player:
  some_event:
    flash_red:
      loops: -1
      show_tokens:
        led: tag1
```

This would result in a show that was equivalent to:

``` yaml
##! show: my_show
- time: 0
  lights:
    led_01: red
    led_02: red
- time: 1
  lights:
    led_01: off
    led_02: off
```

## Token names are arbitrary

The token show we've been working with so far includes a token called
*leds*. That's a good name for the token since it explains what it's
for. However, MPF doesn't care what the actual token name is. All it's
doing is a find-and-replace when the show starts with whatever token
names it was passed.

For example, this is a perfectly valid show:

``` yaml
##! show: my_show
- time: 0
  lights:
    (corndog): red
- time: 1
  lights:
    (corndog): off
```

In this case, you'd just pass a value for the *corndog* token when you
play the show:

``` yaml
show_player:
  some_event:
    flash_red:
      loops: -1
      show_tokens:
        corndog: led_02
```

## Tokens can be values too

You can use tokens anywhere in a show. The actual find-and-replace is
pretty simple, just looking for words in parentheses and then
substituting them with the tokens key/value pairs that were passed when
the show starts.

You can also pass multiple tokens. Consider the following show:

``` yaml
##! show: my_show
- time: 0
  lights:
    (led): (color1)
- time: 1
  lights:
    (led): (color2)
```

Notice there are three tokens in this show: *led*, *color1*, and
*color2*. You might call this show *color_cycle*, which you could then
play like this:

``` yaml
show_player:
  some_event:
    color_cycle:
      loops: -1
      show_tokens:
        led: led_02
        color1: green
        color2: blue
```

## Shot show tokens

Shots can take advantage of the token system to easily assign the same light across the different shows for each state of the shot profile.

In the following example, the shot uses the [built-in shows](../shows/default_shows.md) `flash` and `on`, sending the show token "led" with the value "my_led" in both.

``` yaml
shot_profiles:
  blink_to_solid_profile:
    states:
      - name: blink
        show: flash
      - name: solid
        show: on

shots:
  my_shot:
    profile: blink_to_solid_profile
    switch: my_switch
    show_tokens:
      led: my_led
```

Shot profiles also support setting up show_tokens, allowing some settings to be configured at a more common level.
For instance, using the default show `flash_color` we can have two shots share a color at the profile level, while each affecting a different light in the shot level.
The following example shows a simple case, where we only save a couple lines by moving color up to the profile level, but for complex shows (say, a fireworks show where there are ten different color variables used) using the profile tokens can significantly reduce duplication.

``` yaml
shot_profiles:
  different_blink_color_profile:
    states:
      - name: purple
        show: flash_color
        show_tokens:
          color: ff00ff
      - name: green
        show: flash_color
        show_tokens:
          color: 00ff00

shots:
  my_first_shot:
    profile: different_blink_color_profile
    switch: my_switch_1
    show_tokens:
      led: my_led_1
  my_second_shot:
    profile: different_blink_color_profile
    switch: my_switch_2
    show_tokens:
      led: my_led_2
```

## Using mpf variable values in tokens

In the examples above, the token values (ex: led_02) are object names from your config files or are color values.
Another way to provide token values is to supply variables, such as machine variables or event parameters.

### Event parameter (argument) values

Let's imagine the event [player_turn_started](../events/player_turn_started.md) is posted.
It automatically includes the parameter `number`, for the number of the player whose turn has started.

``` shell
INFO : EventManager : Event: ======'player_turn_started'====== Args={'player': <Player 1>, 'number': 1}
```

We can define a show player on the event, to play the show "player_number_show", proving the token "txt" with the value from that param (1 in this case.)

``` yaml
show_player:
  player_turn_started:
    player_number_show: #The name of the show to be started upon this event
      show_tokens:
        txt: (number)
```

Note: When using event arguments as tokens, just use the argument name without any prefix or dot notation.

### Variable values
You can also use variable values to populate tokens. For example if you want to access a player variable you can access it with `current_player.<variable>`

``` yaml
show_player:
  player_turn_started:
    ball_num_show: #The name of the show to be started upon this event
      show_tokens:
        txt: (current_player.ball)
```

In this example the ball number of the player is being used in your show once the player's turn has started. In case you want to access a variable of a specific player (which is not necessarily the current player) you can use `players[<player_number>].<variable>` where `player_number` is the player starting with 0, e.g. the second player needs the value 1 in this example.


You can also access game variables, machine variables, or settings. Just use the notation `game.<variable>`, `machine.<variable>`, or `settings.<variable>`.
You can learn more about using variables as tokens in the [Dynamic Values](../config/instructions/dynamic_values.md) reference page.

### Formatting of variable values

MPF is built with Python, so it is possible to use some Python-specific features in calculating variable values.
For instance, to format the variable value as a decimal, we can use a special Python syntax:

``` yaml
show_player:
  player_turn_started:
    ball_num_show: #The name of the show to be started upon this event
      show_tokens:
        txt: "{(current_player.ball):d}"
```

The `:d` tells MPF to format the value as a decimal.
To learn about the other Python formatting options see here https://docs.python.org/2/library/string.html#format-specification-mini-language

## Tokens vs Tags

Almost all devices support tags. In [config players](../config_players/index.md)
such as [light_player](../config_players/light_player.md) you can also reference multiple lights by their tags.

## The bottom line

Tokens are a very powerful way to reuse shows in multiple parts of your game and reduce duplication in show definitions.
There are many different ways to start shows in MPF, and all of them have ways to pass tokens to them.
