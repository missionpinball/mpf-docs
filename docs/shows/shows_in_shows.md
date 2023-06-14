---
title: Playing Shows in a Show
---

# Playing Shows in a Show


Sometimes it can be useful to play other shows inside your show.
Luckily, a show can use any [Config Players](../config_players/index.md) and there is a
[Show player](../config_players/show_player.md).

This is an example of an attract mode:

``` mpf-config
##! show: my_show
- duration: 3s
  shows:
    attract_show_collectlights:
      loops: 1
      speed: 10
      show_tokens:
        color: blue
- duration: 3s
  shows:
    attract_show_collectlights:
      loops: 1
      speed: 10
      show_tokens:
        color: red
```

It will first run a show in blue and then the same show in red. You
would usually also add some sounds and slides which can be also in other
shows. The organisation of your shows is up to you. This allows you to
reuse shows with different parameters.

Video about shows:

<div class="video-wrapper">
<iframe width="560" height="315" src="https://www.youtube.com/embed/Ou5xqCAthZY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
