---
title: How to create a multiball with a traditional ball lock
---

# How to create a multiball with a traditional ball lock


Related Config File Sections:

* [multiballs:](../../config/multiballs.md)
* [multiball_locks:](../../config/multiball_locks.md)

Most pinball machines use a "virtual" ball lock to track multiball
progress and MPF is designed to handle these by default. Machines that
physically lock multiple balls require a few extra configuration
settings to properly count locked balls and release them for a
multiball.

## Background](How MPF tracks and replaces balls

When a ball enters a ball device that is not the trough, the ball device
checks for any locks that want to "claim" the ball. If the ball is
claimed by anything, such as an enabled `multiball_lock`, the ball
device will hold the ball and request a new ball be added from the
trough to the playfield. If nothing claims the ball, the ball device
will eject it back onto the playfield.

During this process, the number of "balls in play" never changes. When
a ball is claimed by a lock, MPF simply swaps the location of the
inactive ball from the trough to the ball device. From the game's
perspective the playfield always has one ball in play.

## Setting up a simple multiball

An MPF multiball only has one configuration requirement)

!!! note

    Be careful with with *balls_to_replace* and *replace_balls_in_play*.
    They will only work in exactly this combination. Used in isolation they
    will likely lead to incorrect ball counts.

Video about ball locks and multiballs:

<div class="video-wrapper">
<iframe width="560" height="315" src="https://www.youtube.com/embed/2mFkgIlksC4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
