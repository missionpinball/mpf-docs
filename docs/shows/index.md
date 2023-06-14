---
title: Shows
---

# Shows


In MPF, *shows* are containers that hold steps of instructions for
things that can be "played" in a certain order with specific timings.

You can do almost anything in a step in a show, including setting the
color of LEDs, playing sounds, showing slides on the display, posting
events, firing drivers, etc.

You're going to use shows a lot.

!!! note

    Prior to MPF 0.30, "light shows" and "display shows" were two
    independent things. In MPF 0.30+, shows are now universal. There's only
    one type of show, and it can be used to do anything.

Shows are controlled and run by the MPF game engine, and if a show
contains actions in a step for the media controller, such as display or
sound actions, then those actions are sent via BCP to the media
controller when that step is played.

Shows are configured via the YAML formatting just like config files. You
can add the definitions for simple shows into your config files
directly, or you can create standalone shows files that you store in
your machine's\`shows\` folder.

It is totally viable to create simple shows by hand. However, there is a
[MPF Showcreator](../tools/showcreator.md) to create
complex light shows.

Read on for more info on how shows work:

* [format content file_shows config_shows tokens playing sync_ms
shows_in_shows](format content file_shows config_shows tokens playing sync_ms
shows_in_shows)

You should have a look at [Config Players](../config_players/index.md) to find more information about all the elements which are
possible in shows (i.e. lights, slides, widgets or sounds).

Videos about shows:

<div class="video-wrapper">
<iframe width="560" height="315" src="https://www.youtube.com/embed/Ou5xqCAthZY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

<div class="video-wrapper">
<iframe width="560" height="315" src="https://www.youtube.com/embed/bjDWm_pO9_I" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

<div class="video-wrapper">
<iframe width="560" height="315" src="https://www.youtube.com/embed/9hMsnGfUliM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
