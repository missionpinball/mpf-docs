---
title: "FAQ: General"
---

# FAQ: General


## Why was the Mission Pinball Framework (MPF) created?

The Mission Pinball Framework was started in 2014 by Brian Madden for
a homebrew pinball machine he and Gabe Knuth were planning. Both of
them had dreamed of building their own pinball machines for years,
and in 2013 they discovered the P-ROC and the wonderful community of
homebrew pinball builders and hackers.

The P-ROC pinball control system worked with an open source project
called `pyprocgame` which is a Python-based game framework. Pyprocgame
is great, but it's pretty basic. (It's more of a pinball development
environment versus a complete framework.) One of the challenges we saw
was that people kept on having to "reinvent the wheel" with each game
they built. After reading forum posts about "How do you write code for
a trough?" about ten times, we thought, "Why isn't there a framework
that just 'does that' for you?"

Pyprocgame also requires everything to be written in Python code, and we
found that a lot of people who wanted to build their own pinball
machines weren't software developers. So we thought it would be cool to
create a framework where the majority of the "programming" could be
done with text-based configuration files.

Around the same time, FAST Pinball came onto the market to offer an
alternative control system to the P-ROC and P3-ROC. So we decided to
make MPF hardware-independent so it could work with any pinball control
system.

The first release of MPF was in May, 2014. (That's before the project was
even on GitHub!) (Check out the [MPF announcement post on Pinside](https://pinside.com/pinball/forum/topic/announcing-the-mission-pinball-framework-hw-independent-python-based-game-sw).) Since then, MPF has grown to be a complete framework
that's used by homebrewers and commercial pinball companies to power
real pinball machines around the world.

## Isn't using config files limiting?

Finding the balance between "config files" and "real programming" is
an age-old battle. We have a guide called
[Config files versus "real" programming](../start/dsl_vs_programming.md) which explains
this in more detail, including our perspective on it and why we decided
to make config files the focus on MPF.

## Can I mix "real" code in with MPF config files?

Yes! See
[developer.missionpinball.org](http://developer.missionpinball.org) for
details and examples.

## Where does the name come from?

Brian lived in San Francisco's "Mission" neighborhood when MPF was
first created. There were a lot of "Mission" things here, Mission
Bowling, Mission Coffee, Mission Ice Cream... He had registered the
Mission Pinball domain "just in case" and this project turned out to
be a great use for it!

## What pinball hardware does MPF work with?

The complete hardware compatibility list is
[here](../hardware/index.md).

## Who's behind this?

MPF is open source and is completely developed by volunteers. See the
[AUTHORS](https://github.com/missionpinball/mpf/blob/dev/AUTHORS) file
in the MPF package for the latest list.

## Is MPF stable?

MPF is open source software that is not yet at a 1.0 release. However
we've been working on it since 2014, and several complete pinball
machines have been built using it.

Furthermore, when we find crashes, we fix them. If you look at the list
of commits (code additions, changes, and fixes that we check in) on
[GitHub](https://github.com/missionpinball/mpf/commits/dev), you'll see
that we're busy with dozens of commits per week!

## Is MPF beta? When will v1 be released?

MPF is open source and continuously developed. We're currently say,
"Yes, it's beta" since we are not yet at a 1.0 release. However we
release new versions every few months and don't expect that to change
anytime soon.

We do expect to get to a 1.0 release at some point, but we don't have a
specific time-frame for that. The important thing is to look at the
[code commit
history](https://github.com/missionpinball/mpf/blob/dev/AUTHORS) and to
notice that MPF is being very actively developed!

## How can I download the documentation and read it offline?

Click the "Read the Docs" link in the lower-left corner of any page of
the MPF documentation on docs.missionpinball.org for links to PDF, HTML,
and Epub versions of the documentation.

## What other options are there besides MPF?

While we think MPF is awesome, our main goal is to see more pinball in
the world! Since all of us are working on MPF in our spare time (and not
being paid for it), we won't be offended if you don't use MPF. Just
please create more pinball!

At this time, if you don't want to use MPF, there are a few other
options:

* pyprocgame (P-ROC/P3-ROC only; website defunct)
* [PyProcGameHD+SkeletonGame](http://mjocean.github.io/PyProcGameHD-SkeletonGame/)
    (P-ROC/P3-ROC only, adds HD graphics and more to pyprogame)
* [Open Pinball Project
    framework](https://openpinballproject.wordpress.com/) (Open Pinball
    Project hardware only)
* Rampant Slug Framework (P-ROC/P3-ROC only; website defunct)
* [FreeWPC](https://github.com/bcd/freewpc) (WPC hardware only, lets
    you write new code in C, burn it to ROMS, and run it on original WPC
    hardware)
