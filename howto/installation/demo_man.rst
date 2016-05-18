How to run "Demo Man", the MPF example game
===========================================

Once you have MPF installed, you can run an example game to see how
MPF works and to verify that everything is installed correctly.

1. Download the MPF examples
----------------------------

There are several sample games and other things in a software repository
called "mpf-examples" on GitHub. This repo doesn't have an installer,
rather, you pretty much just download it and start using the examples
it contains.

The example machines in mpf-examples match the branch names of MPF.
In other words, if you're on the "master" branch of MPF, you need to
run the examples from the "master" branch of mpf-examples. (And "dev"
for "dev", etc.)

So to do that, download the ZIP file from `master <https://github.com/missionpinball/mpf-examples/archive/master.zip>`_
or `dev <https://github.com/missionpinball/mpf-examples/archive/dev.zip>`_ branch zip from from the mpf-examples repo.
(If you're familiar with git, you can just clone the repo. It's at `github.com/missionpinball/mpf-examples <https://github.com/missionpinball/mpf-examples>`_.)

Unzip the examples folder to any location you want. It doesn't have
to be in the same folder as MPF. (In fact when you installed MPF, it
was installed to some system folder that you probably can't even find.
So for these example files, just put them somewhere easy.)

2. Run *Demo Man*, a sample game that comes with MPF
----------------------------------------------------

One of the development machines we have for MPF is a 1994 Williams
*Demolition Man*, and we've included example game configuration files
for a game we call *Demo Man* (which runs on a Williams *Demolition
Man* machine) in the MPF examples package. So at this point you can run
*Demo Man* (using the software-only "smart virtual" platform* with no
physical pinball hardware attached since you probably don't have a
*Demolition Man* machine) just to make sure that everything is up and
running properly. To do this, open a command prompt and switch to the
folder where you unzipped the mpf-examples ZIP file, then change to
the ``demo_man`` folder and run ``mpf both -x -v``.

(The "mpf both" command launches both the MPF game engine and
media controller at the same time, and the "-x" command line option
tells MPF to *not* try to connect to the physical hardware since you
most likely don't have a Demolition Man machine connected to your
computer right now, and the "-v" option sets the logging level to
verbose):

::

   C:\mpf-examples\demo_man>mpf both -x -v

You should see a bunch of stuff scroll by and a pop up window which
shows the Demo Man DMD, like this:

.. image:: demo_man.jpg

If you don't see the DMD window pop up, make sure it isn't hiding behind another window.

3. "Play" your first game
-------------------------

Since you don't have physical hardware attached, you can use the
keyboard to simulate machine switch changes.


The *Demo Man* configuration files
have the "S" key mapped to start, so if you click in the graphical
window with the DMD in it (to give it focus) and push the ``S`` key,
then you should see the DMD attract mode stop and it change to a
score screen showing a score of *00* and *BALL 1 FREE PLAY*:

If your speakers are on you should also hear a music loop
playing. (Depending on your system, you might not hear the music when
the DMD window doesn't have focus.)

At this point you can "play" the
game via your keyboard. Hit the ``L`` key to launch the ball into play.
You should hear the music loop change to the main background music.

You can hit the ``X`` key to simulate the left slingshot hit which
should play a sound effect on top of the music as well as show a
score. You can hit the ``1`` key to simulate the ball draining and
entering the trough. Then you can hit the ``L`` key again to launch the
ball into play again. You can also press the ``S`` key additional times
during Ball 1 to add additional players.

When you play through a
complete game (3 balls per player), the machine should go back into
attract mode (or possibly the high score entry mode).

You can quit the game by making sure the *Demo Man* popup
window is in focus and hitting the *Esc* key.

To summarize the instructions for "playing" a game from the paragraphs above:


#. Launch both the MPF core engine and the media controller and make
   sure you see the the popup graphical
   window with the DMD in it.
#. Click the mouse into the DMD window so that it has "focus"
#. Press the ``S`` key to start a game. You should hear the music loop
   start.
#. Press the ``L`` key to launch a ball into play. You should her the
   music switch to the main background theme for the game.
#. Press the ``X`` key a few times to simulate hitting the left
   slingshot. You should see the score change each time you do this.
#. Press the ``1`` key to drain the ball.
#. Repeat Steps 4-6 until you finish your game or get bored.
#. If you get a high score, the ``Z`` and ``/`` keys are mapped to the
   left and right flipper buttons to highlight a letter, and the ``S`` key
   (start) selects it.
#. Press the ``Esc`` key to exit

4. Take a look at the log files to see what just happened!
----------------------------------------------------------

The MPF core engine and media controller always create log files.
Since we ran these with the ``-v`` command line option, we'll have
"verbose" log files to look at.

A new folder called */logs* should have been created in ``demo_man``
game folder. Inside that folder you
should see two new log files—-one from the MPF game engine and one from
the media controller. The files are named with a date & time stamp,
then either *mpf* or *mc* (for MPF game or media controller), then the
host name of the machine they were run on.

The files have a .log file extension, but they're just regular text files.
On Windows if you double-click them, they'll open with Notepad. On a
Mac they'll open with an app called Console which is a log file
viewer.

If you scan through that log file, you'll see that MPF does *a lot* in
the background. :)
