---
title: Show configuration format
---

# Show configuration format


Shows are defined via nested key/value pairs in YAML files.

A show contains multiple steps, and each step contains a time (for when
that step should run) and instructions (for what actions should happen
in that step).

Here is a very simple show with two steps. The first step sets the color
of *led1* to *red*, then one second later, it turns *led1* off again.
Then after another second, the show is over. (Most likely you'd
configure a show like this to *loop*, meaning this should could be used
to flash *led1* on and off.)

``` yaml
##! show: my_show
- time: 0
  lights:
    led1: red
- time: +1
  lights:
    led1: off
- time: +1
```

There are
[lots of different actions you can configure in a show step](../config_players/index.md) (LEDs, lights, sounds, coils, display slides, etc.), but for
now we'll just use this very simple show as an example.

## Defining steps

Shows are configured via YAML-like format, just like config files.

In the example show above, note that each *step* in the show starts with
a key/value pair that's separated with a dash, then a space. So you
could say that the example show above has three steps:

Step 1:

``` yaml
##! show: my_show
- time: 0
  lights:
    led1: red
```

Step 2:

``` yaml
##! show: my_show
- time: +1
  lights:
    led1: off
```

Step 3:

``` yaml
##! show: my_show
- time: +1
```

!!! note

    YAML formatting can be tricky. It's important that you include a space
    between the dash and the key name. `-time: 0` will not work and give you
    an error (since there is no space between `-` and `time`.). Also, make
    sure the individual setting names are all aligned vertically. (In the
    example above, *time:* and *lights:*) are left-aligned.

## Setting step time

!!! warning "Important Syntax change with mpf 0.57"

    In this chapter the used sytax for the time parameter is for versions up to 0.56. With mpf 0.57 and later (incl. 0.80)
    you need to add quotes around time values which are not zero, e.g. `time: "1"`, `time: "+1"` but `time: 0`.

The `time:` setting in each step represents the time when that step
*starts*. The first step will always be `time: 0`

If you just enter a number for the *time*, that number represents
seconds. However, you can enter the time in
[standard MPF time format](../config/instructions/time_strings.md), which could be *ms*, *secs*, etc. The following are all
valid *time* entries:

* `time: 1` (1 second)
* `time: 1.0` (1 second)
* `time: 1s` (1 second)
* `time: 1000ms` (1 second)

If you do not enter a `time:` setting for a step, MPF automatically uses
`time: +1`.

When shows are played, it's possible to specify a *speed* setting which
is a multiplier for how fast the show is played. The default is `1.0`
which would use the time values entered here, but keep in mind that
it's possible to play a show back at any speed. You can even change the
speed of a running show while it's in progress.

!!! note "Show timing precision"

    The precision of shows is limited to clock speed that MPF runs at. By
    default, MPF runs at 60fps, which means that each "tick" of MPF is
    about 16ms. So in that case, you can't get resolution of shows more
    precise than that.

### Absolute time

The time value for each step indicates when this step will play measured
in time since the start of the show. This is useful if you're
synchronizing show steps with sound or video.

### Relative time

Sometimes it's more convenient to specify the timing of a step in a
show relative to the step before it. To do that, enter the *time* value
with a + in front of it, like this:

``` yaml
##! show: my_show
- time: +1
```

Relative step times are nice because you can adjust the timing of one
step and then all the other relative steps after it are shifted back or
forwards automatically.

You can mix-and-match incremental and absolute times in the same show,
and you can also combine the plus sign for relative times with seconds
or millisecond values. For example:

``` yaml
##! show: my_show
- time: 0   # plays right away, at 0 seconds
  # ...
- time: +1  # plays 1 sec after the previous, 1 sec after show start
  # ...
- time: +1  # plays 1 sec after the previous, 2 secs after show start
  # ...
- time: 4   # plays 4 secs after show start, 2 secs after the previous
  # ...
- time: +1  # plays 1 sec after the previous, 5 secs after show start
  #...
```

Note that since shows use YAML formatting, you can use the hash sign
(`#`) to add comments which MPF ignores.

## Setting step duration

Instead of specifying the "time" when a step starts, you can also
specify the "duration" of how long a step lasts (which is essentially
specifying when a step ends). The difference is subtle, but each is
useful in different situations.

For example, the following to shows are identical:

``` yaml
##! show: my_show
- time: 0
  lights:
    led1: red
- time: +1
  lights:
    led1: off
- time: +1
```

``` yaml
##! show: my_show
- duration: 1
  lights:
    led1: red
- duration: 1
  lights:
    led1: off
```

You can also mix and match "time" and "duration" settings in the
same show (and even in the same step). The only thing you can't do is
have a "time" setting in a step that follows a step with "duration"
(since those two values would essentially mean the same thing and it
would be confusing).

## Setting the duration of the final step

Most people find it easiest to just use either "time" or "duration"
consistently throughout a show. The only practical difference you need
to think about is how the final step works.

For example, with "time"-based steps, you're specifying the time when
a step starts. So when does a step stop? When the next one starts. But
what about your last step in the show? How long should it run for? If
you just use time-based steps, you'd still want to specify a
"duration" for the final step, like this:

``` yaml
##! show: my_show
- time: 0
  lights:
    led1: red
- time: +1
  lights:
    led1: green
- time: +1
  duration: 1
  lights:
    led1: blue
```

## "Holding" the final step

You can set a `duration: -1` for an "infinite" duration of a step.
(Think of this like a hold or pause.) This is most useful in shows that
you want to run and then hold something in their final state. For
example, maybe you want a show that runs once (no loop) and flashes a
light which then stays on. You could do that like this:

``` yaml
##! show: my_show
- time: 0
  lights:
    led1: red
- time: +250ms
  lights:
    led1: off
- time: +250ms
  lights:
    led1: red
- time: +250ms
  lights:
    led1: off
- time: +250ms
  lights:
    led1: red
  duration: -1
```

In this example, the LED would stay on (red) until that show was
manually stopped or until the mode was stopped (if the `show_player:`
entry was in a mode config file).
