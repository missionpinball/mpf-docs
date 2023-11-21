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

## Background: How MPF tracks and replaces balls

When a ball enters a ball device that is not the trough, the ball device
checks for any locks that want to "claim" the ball. If the ball is
claimed by anything, such as an enabled `multiball_lock`, the ball
device will hold the ball and request a new ball be added from the
trough to the playfield. If nothing claims the ball, the ball device
will eject it back onto the playfield.

During this process, the number of "balls in play" never changes. When
a ball is claimed by a lock, MPF simply swaps the location of the
inactive ball from the trough to the ball device. From the game's
perspective the playfield always has only one ball in play.

## Setting up a simple multiball
Perhaps the two most common types of multiballs are *virtual-only* and *physical-only*. For *virtual-only* multiballs, you only need a `multiballs:` section to your config and a corresponding *start_event*. You do not need to configure a `multiball_locks:` section. Instead, a counter or *logic_block* is often used to track when the requirements for a multiball have been satisfied, such as a certain number of shots to the captive ball target in _Metallica_ for instance.

## Setting up a physical-only multiball
In order to use a physical lock in combination witha multiball, you just define a *ball_device* as well as define a *multiball_lock* within your config files. The *ball_device* must be listed as a `lock_device` within the settings of the `multiball_lock` config section.

## Making sure the right number of balls are in play

In MPF, any given multiball (configured within a `multiballs` config section) only has one configuration requirement: `ball_count`. However, there are optional settings you may need depending on what type of multiball you are creating. In the instance of a physical-only multiball (as typically seen in older machines), the machine must physically lock balls before multiball can start. Only when the physical lock is full can the multiball be started. Typically, the lock device continues to hold these locked balls across player turns, allowing for players to "steal locks" until the lock device is physically full, which in turn typically starts the multiball immediately. In MPF, you have control over what event triggers the start of a multiball mode. It could be the automatically posted event `multiball_lock_[multiball-lock-name]_locked_ball`, or some other event setup via an `event_player`.

In either scenario, both the `multiball_locks` and the `multiballs` config settings must be configured such that MPF knows how many balls are to be replaced when a "lock" locks a ball from the playfield. This can be set using the `replace_balls_in_play` setting. However, this setting requires another to be set within the corresponding multiball, specifically, the `balls_to_replace` setting.

!!! note

    Cheat sheet: set *replace_balls_in_play: true* and set *balls_to_replace:* 
    equal to the number of balls the lock holds minus one. So if you want two 
    balls to be locked and replaced from the trough, but the third ball not 
    to be replaced from the trough (because multiball is starting and all three 
    locked balls will come out as part of that), then set `balls_to_replace: 2`. 
    
    If for some reason the multiball doesn't start automatically on ball 3 
    entering, the game will get stuck with no balls on the playfield!

In order to setup a physical multiball lock and associated multiball, there must be a lock device assigned to your `multiball_locks` section of your config. 

!!! note

    Be careful with with *balls_to_replace* and *replace_balls_in_play*.
    They will only work in exactly this combination. Used in isolation they
    will likely lead to incorrect ball counts.

Video about ball locks and multiballs:

<div class="video-wrapper">
<iframe width="560" height="315" src="https://www.youtube.com/embed/2mFkgIlksC4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
