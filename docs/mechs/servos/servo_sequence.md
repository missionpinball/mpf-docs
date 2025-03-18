---
title: Programming Servo Sequences
---

# Programming Servo Sequences


Related Config File Sections:

* [servos:](../../config/servos.md)
* [shows:](../../config/shows.md)
* [show_player:](../../config/show_player.md)

You often want to move servos to different positions sequentially. For
instance, an animated toy should open and close its mouth three times on
a hit to a target. The target will post one event and you could use that
to move the servo to one position. Servos do not prove position feedback
so there is no way to trigger something on arrival at that position
(unless you add additional switches). Instead you usually create a show
which triggers a timed series of movements. The advantage of this
solution is that you can easily integrate and synchonize it with sounds
and lights.

The following example will move the servo six times when `my_toy_hit` is
posted (three times to open and three times to close):

``` yaml
servos:
  my_toy:
    positions:
      0.0: open_mouth
      1.0: close_mouth
    reset_position: 1.0
    number: 1
shows:
  toy_hit:
    - duration: 1s
      events: open_mouth
    - duration: 2s
      events: close_mouth
show_player:
  my_toy_hit:
    toy_hit:
      loops: 2
```

To see how this can be used in a real machine we recommend this
explanation video by the pinball amigos:

<div class="video-wrapper">
<iframe width="560" height="315" src="https://www.youtube.com/embed/1QOOJNtsGxw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

You might also enjoy our video about servos in general:

<div class="video-wrapper">
<iframe width="560" height="315" src="https://www.youtube.com/embed/wA6KEODwQ5w" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
