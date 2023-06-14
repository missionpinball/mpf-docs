---
title: Show player
---

# Show player


The *show player* is a
[config player](index.md)
that's used to start, stop, pause, resume, advance, and/or update
shows.

Video about shows:

<div class="video-wrapper">
<iframe width="560" height="315" src="https://www.youtube.com/embed/Ou5xqCAthZY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

This is an example:

``` mpf-config
show_player:
  some_event: your_show_name
  some_other_event: another_show
```

In the example above, when the event *some_event* is posted, the show
called `your_show_name` will be played (started). When the event
*some_other_event* is posted, the show called `another_show` will be
played.

Notice that the config above has simple key/value pairs in the form of
*event: show*. You can list as many of those as you want in the show
player, and when each event is posted, it will start the show with the
same name.

However there are times when you might want to specify additional
options for a show. Perhaps you want to change the playback speed, or
configure how it repeats. In that case, instead of putting the show name
on the same line as the event, you can put the show name on a new line
under the event, and then add additional settings under it, like this:

``` mpf-config
show_player:
  some_event:
    your_show_name:
      loops: 0
  some_other_event:
    another_show:
      speed: 2
      sync_ms: 500
```

In the example above, the show `your_show_name` will play when the event
*some_event* is posted, but instead of playing with the default settings
only, it will also play with the setting `loops: 0` (meaning it will not
loop and just play once). Same for the other show above, which will play
with a `speed: 2` and `sync_ms: 500`.

You can also mix-and-match formats, like this:

``` mpf-config
show_player:
  some_event: your_show_name
  some_other_event:
    another_show:
      speed: 2
      sync_ms: 500
```

## Show keys

Each show played by a show player will be referenced internally using an
unique `key`. The show_player will use the show name as key for the show
by default if you do not specify a `key` (fine in most cases). This way
it refences the show when starting or stopping it:

``` mpf-config
show_player:
  start_my_show:
    your_show_name: play
  stop_my_show:
    your_show_name: stop
```

In this example the event `start_my_show` will start `your_show_name`
with key `your_show_name`. The event `stop_my_show` will then stop the
same show using the key `your_show_name`. This simple mechanism will
work fine for most cases.

However, in some cases you want to play multiple instances of one show
in a single show. You can manually assign keys to run distinct shows.
That way you can also specifically stop them later:

``` mpf-config
show_player:
  start_my_show1:
    your_show_name:
      action: play
      key: show1
      show_tokens:
        leds: my_led1
  start_my_show2:
    your_show_name:
      action: play
      key: show2
      show_tokens:
        leds: my_led2
  stop_my_show1:
    show1: stop
  stop_my_show2:
    show2: stop
```

In this example `start_my_show1` and `start_my_show2` will start
separate instances of `your_show_name` which can indendently be stopped
using `stop_my_show1` and `stop_my_show2`. If you omit `key` in this
example `start_my_show1` and `start_my_show2` would stop the other and
you would either see `your_show_name` with `my_led1` or `my_led2` but
not both at the same time.

A key is only unique to one show_player so different modes will not
interfere.

## Usage in config files

In config files, the show player is used via the `show_player:` section.

## Usage in shows

In shows, the show player is used via the `shows:` section of a step.
(Yes, you can include shows in shows, meaning you can essentially use a
parent show like a playlist, or as a controller that starts and stops
other shows.)

## Config Options

See [show_player:](../config/show_player.md) for config
details.
