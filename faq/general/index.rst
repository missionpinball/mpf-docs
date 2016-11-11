FAQ: General
============

Why does this project exist?
----------------------------

The Mission Pinball Framework was officially started in 2014 by Brian Madden and Gabe Knuth. Both of
them had dreamed of building their own pinball machines for years, and in 2013, they discovered the
P-ROC and the wonderful community of home brew pinball builders and hackers.

The P-ROC pinball control system works with an open source project called `pyprocgame <http://www.pinballcontrollers.com/forum/index.php?board=9.0>`_
which is a Python-based game framework. Pyprocgame is great, but it's pretty basic. One of the challenges
we saw was that people kept on having to "reinvent the wheel" with each game they built. After reading
forum posts about "How do you write code for a trough?" about ten times, we thought, "Why isn't there a
framework that just 'does that' for you?"

Pyprocgame also requires everything to be written in Python code, and we found that a lot of people who
wanted to build their own pinball machines weren't software developers. So we thought it would be cool
to create a framework where the majority of the "programming" could be done with text-based configuration
files.

So in May 2014, we decided to start building the Mission Pinball Framework.

Around the same time, FAST Pinball came onto the market to offer an alternative control system to the
P-ROC and P3-ROC. At that we thought, "Great, let's make the Mission Pinball Framework so that's it's
hardware-independent and can work with the FAST Pinball or P-ROC systems (or any other future system
that would come out).

Isn't using config files limiting?
----------------------------------

Finding the balance between "config files" and "real programming" is an age-old battle. We have a guide
called :doc:`/start/dsl_vs_programming` which explains this in more detail, including our perspective on
it and why we decided to make config files the focus on MPF.

Where does the name come from?
------------------------------

Brian lives in San Francisco's "Mission" neighborhood. There are a lot of "Mission" things here, Mission
Bowling, Mission Coffee, Mission Ice Cream... So we thought "Mission Pinball" had a great ring to it!

What pinball hardware does MPF work with?
-----------------------------------------

The complete hardware compatibility list is :doc:`here </hardware/index`.

Who's behind this?
------------------

Even though MPF was started by Brian Madden and Gabe Knuth, our team has grown to involve lots of
people. See the `AUTHORS <https://github.com/missionpinball/mpf/blob/dev/AUTHORS>`_ file in the MPF
package for the latest list.

Is MPF stable?
--------------

MPF is open source software that is not yet at a 1.0 release. However we've been working on it since
2014, and several complete pinball machines have been built using it.

Furthermore, when we find crashes, we fix them. If you look at the list of commits (code
additions, changes, and fixes that we check in) on `GitHub <https://github.com/missionpinball/mpf/commits/dev>`_,
you'll see that we're busy with dozens of commits per week!

Is MPF beta? When will v1 be released?
--------------------------------------

MPF is open source and continuously developed. We're currently say, "Yes, it's beta" since we are not
yet at a 1.0 release. However we release new versions every few months and don't expect that to change
anytime soon.

We do expect to get to a 1.0 release at some point, but we don't have a specific time-frame for that.
Earliest would be late 2017, though who knows?

How can I download the documentation and read it offline?
---------------------------------------------------------

Click the "Read the Docs" link in the lower-left corner of any page of the MPF documentation on
docs.missionpinball.org for links to PDF, HTML, and Epub versions of the documentation.

What other options are there besides MPF?
-----------------------------------------

While we think MPF is awesome, our main goal is to see more pinball in the world! Since all of us are
working on MPF in our spare time (and not being paid for it), we won't be offended if you don't use
MPF. Just please create more pinball!

At this time, if you don't want to use MPF, there are a few other options:

* `pyprocgame <http://www.pinballcontrollers.com/forum/index.php?board=9.0>`_ (P-ROC/P3-ROC only)
* `PyProcGameHD+SkeletonGame <http://mjocean.github.io/PyProcGameHD-SkeletonGame/>`_ (P-ROC/P3-ROC only, adds HD graphics and more to pyprogame)
* `Open Pinball Project framework <https://openpinballproject.wordpress.com/>`_ (Open Pinball Project hardware only)
* `Rampant Slug Framework <http://rampantslug.com.au/#pinball>`_ (P-ROC/P3-ROC only)
* `FreeWPC <https://github.com/bcd/freewpc>`_ (WPC hardware only, lets you write new code in C, burn it to ROMS, and run it on original WPC hardware)

