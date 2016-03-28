
Once you understand what you'll need for MPF, youcan move on to
actually downloading, installing, and getting MPF running. At this
point itreally doesn't matter what type of computer you use for this.
Most people do all their initial development work on a Mac or Windows
laptop(which they connect via USB to their pinball machine for
testing), and then when they get closer to actually finishing their
project they switch over to a small Linux-based single board computer
(like a Raspberry Pi 2 or BeagleBone Black) or a small Windows system
to run their final code. The good news is that all the Python files
and configuration files you build are 100% identical regardless of the
computing platform (and, frankly, regardless of whether you use a
P-ROC or FAST controller), so you can safely do all your development
on whatever computer you're reading this document from and then easily
transfer it to your final computer later.



(A) Install Python, MPF, and related components
-----------------------------------------------

We have a `dedicated page about installing MPF`_ that you can follow
to get everything installed. If you're using Windows or a Debian-based
Linux (Ubuntu, etc.), then we have installers you can download and use
which will automatically install everything in under 5
minutes—including the P-ROC, P3-ROC, or FAST Pinball drivers! Even if
you want to manually install MPF and all its related components, it
should only take you about 10 minutes. Note that this tutorial is
based on MPF 0.21. See `this how to guide`_ for details on how to
check what version of MPF you have.



(B) Run *Demo Man*, a sample game that comes with MPF
-----------------------------------------------------

Now that MPF is installed, let's run a sample game to make sure that
everything is working. Then we'll dig into creating your own game. One
of the development machines we have for MPF is a 1994 Williams
*Demolition Man*, and we've included sample game configuration files
for a game we call *Demo Man*(which runs on a Williams *Demolition
Man* machine) in the MPF download package. (You can `track our
progress`_ writing the *Demo Man* game code in our blog.) So at this
point you can run *Demo Man*(using the software-only *"smart virtual"
platform* with no physical pinball hardware attached since you
probably don't have a *Demolition Man* machine) just to make sure that
everything is up and running properly. To do this:


#. Open a command prompt.
#. Switch to the root *mpf*folder where you just installed MPF. This
   will be `c:\pinball\mpf` by default if you used our all-in-one Windows
   installer. You should see a bunch of files in that folder like
   *mpf.py*, *mc.py*, *mpf.bat*, *mph.sh*, etc., as well as various
   subfolders including */mpf*, */machine_files*, and */tools*.
#. Then the next step varies based on what OS you're using.




If you're on Windows...
~~~~~~~~~~~~~~~~~~~~~~~

For Windows we have a batch file that will launch the MPF core engine
and the MPF media controller (which handles the DMD, audio, and on-
screen popup window) together at the same time. You can launch *Demo
Man* like this:


::

    
    mpf demo_man -v


The *mpf* part of that command is running the batch file `mpf.bat`,
*demo_man*tells MPF that you're running the *Demo Man*machine code.
The *-v* option sets it so the log file is written in "verbose" mode.
You should see three popup windows when you run this:


+ A new command window with logging from the core MPF game engine.
+ A new command window with logging from the MPF media controller.
+ A graphical window which shows you a virtual on-screen DMD of the
  *Demo Man* game.


If you don't see the two command windows, try dragging the window you
do see with the mouse. Sometimes the two windows open on top of each
other so it just looks like one window. As *Demo Man* is running, your
desktop should look something like the image below. (Click the image
to see it full size.) Also, later in this tutorial we'll show you how
to customize this graphical pop-up window to show whatever you want,
including text, images, backgrounds, different color dots, change the
size of the DMD, etc. ` `_ (Note that this screenshot is from an older
version of MPF so the exact command line you run is different than
what's in the pictures, but the pictures show the gist of what's going
on.)



If you're using Linux...
~~~~~~~~~~~~~~~~~~~~~~~~

For Linux platforms, we haven't yet created a universal shell script
to to automatically launch both the MPF core engine and the media
controller. So instead, open up two terminal windows. In the first
window, launch the media controller for *Demo Man*, like this:


::

    
    python mc.py demo_man -v


(Note that depending on how you have Python installed, you might need
to specify a different Python executable besides just plain `python`.)
The `demo_man` parameter tells the media controller to launch with the
"demo_man" config, the `-v` tells it to write a log in verbose mode,
and the -V tells it to also write the verbose messages to the console
window. Then in your other terminal window, launch the MPF core engine
for *Demo Man*, like this:


::

    
    python mpf.py demo_man -v


The options here are similar to the media controller options, except
that the Python script you're running is `mpf.py` instead of `mc.py`.



(C) "Play" your first game
--------------------------

Since you don't have physical hardware attached, you can use the
keyboard to simulate machine switch changes If you don't see the DMD
window pop up, make sure it isn't hiding in the task bar, like this:
(click for full size image) ` `_ The *Demo Man*configuration files
have the "S" key mapped to start, so if you click in the graphical
window with the DMD in it (to give it focus) and push the "S" key,
then you should see the DMD attract mode stoop and it change to a
score screen showing a score of *00* and *BALL 1 FREE PLAY*, like
this: ` `_ If your speakers are on you should alsohear a music loop
playing. (Depending on your system, you might not hear the music when
the DMD window doesn't have focus.) At this point you can "play" the
game via your keyboard. Hit the "L" key to launch the ball into play.
You should hear the music loop change to the main background music.
You can hit the "X" key to simulate the left slingshot hit which
should play a sound effect on top of the music as well as show a
score. You can hit the "1" key to simulate the ball draining and
entering the trough. Then you can hit the "L" key again to launch the
ball into play again. You can also press the "S" key additional times
during Ball 1 to add additional players. When you play through a
complete game (3 balls per player), the machine should go back into
attract mode. You can quit the game by making sure the *Demo Man*popup
window is in focus and hitting the *Esc* key. If you ran MPF from the
Windows batch file, then you can just close the two popup command
windows by clicking the "X" button in the corner of each. If you're on
Mac or Linux, the media controller process will stop when you hit
*Esc* in the graphical window, and you can stop the MPF core process
by clicking in that terminal window and hitting *CTRL+C*. (You can use
the MPF config files to automatically launch and stop each process as
the other starts and stops. More on that later.) ` `_ To summarize the
instructions for "playing" a game from the paragraphs above:


#. Launch both the MPF core engine and the media controller and make
   sure you see the two processes running along with the popup graphical
   window with the DMD in it.
#. Click the mouse into the DMD window so that it has "focus"
#. Press the *S* key to start a game. You should hear the music loop
   start.
#. Press the *L* key to launch a ball into play. You should her the
   music switch to the main background theme for the game.
#. Press the *X* key a few times to simulate hitting the left
   slingshot. You should see the score change each time you do this.
#. Press the *1* key to drain the ball.
#. Repeat Steps 4-6 until you finish your game or get bored.
#. If you get a high score, the *Z* and */* keys are mapped to the
   left and right flipper buttons to highlight a letter, and the *S* key
   (start) selects it.
#. Press the *Esc* key to close the media controller.
#. Click in the window with the MPF game engine and press `CTRL+C` to
   exit from it.




(D) Take a look at the log files to see what just happened!
-----------------------------------------------------------

The MPF core engine and media controller always create log files.
Since we ran these with the `-v` command line option, we'll have
"verbose" log files to look at. A new folder called */logs* should
have been created in your root *mpf* folder. Inside that folder you
should see two new log files—one from the MPF core engine and one from
the media controller. The files are named with a date & time stamp,
then either *mpf* or *mc* (for MPF core or media controller), then the
host name of the machine they were run on. Here's an example from
playing a single-player complete game (3 balls) and entering initials
for a high score: ` `_ Note that since we did the log files in verbose
mode they are huge! About 2.5mb from a single game where basically
nothing happened. :) So verbose mode is really verbose, and only
something you'd use while troubleshooting. You can double-click on
them to see all the crazy things that MPF does behind the scenes. The
files have a .log file extension, but they're just regular text files.
On Windows if you double-click them, they'll open with Notepad. On a
Mac they'll open with an app called Console which is a log file
viewer. If you're just reading this documentation without following
along and you'd like to see log files, here are direct links to the
two files mentioned above:


+ `MPF core engine`_ (1.5MB .log file)
+ `MPF media player`_ (1MB .log file)


.. _MPF core engine: https://missionpinball.com/wp-content/uploads/2014/09/2015-11-29-18-51-25-mpf-DESKTOP-FBOHND6.log
.. _MPF media player: https://missionpinball.com/wp-content/uploads/2014/09/2015-11-29-18-51-25-mc-DESKTOP-FBOHND6.log
.. _track our progress: https://missionpinball.com/blog/category/building-demo-man/
.. _this how to guide: https://missionpinball.com/docs/howto/mpf-version/
.. _dedicated page about installing MPF: https://missionpinball.com/docs/installing-mpf/


