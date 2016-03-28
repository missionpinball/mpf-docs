
The next step is to add an on-screen display to your game (and,
optionally, to configure the DMD if you're working with a physical
machine that includes a DMD). To do this, we're going to start using a
new component of MPF called the "Media Controller."



(A) Understand what the Media Controller is
-------------------------------------------

One of the most important things to understand about the architecture
of MPF is that the core MPF game engine is completely separate from
the process that controls graphics and audio. We call the thing that
handles graphics and audio a "media controller." So far we've only
been dealing with the MPF core engine (which is launched via the
Python file `mpf.py`). But when you run a complete pinball machine
with MPF, you actually run two processes—the MPF core and a separate
standalone media controller. The two processes communicate via a TCP
socket via a protocol called "BCP" (which stands for "Backbox Control
Protocol"). The MPF package you downloaded from GitHub includes a
Media Controller (which we call the "MPF Media Controller"), and you
launch it via the Python file `mc.py`.) The BCP protocol which is used
to communicate via the MPF core engine and the MPF media controller is
an open protocol, meaning that anyone is welcome to build either a
pinball controller or a media controller that uses it. So it's
possible that you might choose to use MPF as your core pinball engine
while using some other product as your media controller. (More on that
in a minute.) Here's a diagram which showswhat's handled by the MPF
core engine and what's handled by the media controller. (The details
of this are not important right now. But take a minute to read through
the bullets of each piece so you can start to understand how the roles
break down.) ` `_ At this point you are probably wondering why we
broke MPF into two pieces. After all, doesn't this seem more complex
than having everything in the same place? The answer is yes, this is
more complex, but there are two important reasons why we did this:


+ Breaking MPF into two processes means that we can get much better
  performance on multi-core processors.
+ Separating the media controller into its own standalone component
  means that you can swap out MPF's built-in media controller for a more
  advanced one if you have advanced needs.


Let's look at each of these more in depth, starting with the
performance thing. Running the MPF core engine and the media
controller as two separate processes means they can each run on their
own core on a multi-core system. This doesn't really matter if you're
running MPF on a fast desktop or laptop computer with a full-speed
Intel processor. But many people don't want to put full computers in
their pinball machines, rather, they want to use small single-board
computers like the Beaglebone Black, Raspberry Pi, ODOIRD, CubieBoard,
etc. Our experience running MPF on these tiny systems has been mixed.
We found that they were work fine for basic things, but when once you
started adding in lots of graphics, videos, animations, and multiple
tracks of audio, things start to slow down. What made it worse with
earlier versions of MPF is that while many of these small computers
are moving to multicore processors, MPF was a single process. So we'd
have MPF running on this little quad-core computer with MPF pegging
one core to the max while the other cores were sitting there doing
nothing. Breaking MPF into two processes means that we can run each
process on a separate core, essentially doubling the performance we
can get on one of these tiny computers. (Plus as an added bonus, since
the video and audio processing is on a separate core from the main MPF
engine, if we do run into any performance issues playing video or
anything then it won't actually slow down the core game engine.) The
second advantage to having a standalone media controller is that you
can replace MPF's built-in media controller with another one that's
more advanced. This is something that will become more important in
the future as more pinball machines adopt full-screen LCD-based
backboxes. This addresses a challenge we found in MPF once we started
building the DMD and LCD window support. We literally had to write
every single display function for MPF ourselves. We had to handle
building elements (text and images and animations and video), as well
as positioning those elements, handling layering and z-ordering,
transparencies, blends, movement, scaling, etc. Over time it seemed
like we were spending more time writing a graphical video game
creation engine instead of pinball machine software! The problem is
that graphical game engines already exist in the world! So why should
we, a bunch of pinheads, try to rewrite what essentially already
existed? Of course the existing game engines are geared towards video
games—they don't have the ability to control pinball hardware, and
they're not nearly as easy to use as MPF is. Around the same time that
we were thinking about ways to address this problem, some users of MPF
posted in the forum asking about whether it was possible to integrate
MPF with a "real" gaming engine such as the `Unreal Engine`_ or `Unity
3D`_. After several weeks of conversations in the forum, we decided to
take the plunge and to break MPF into the two pieces while also
defining a standard for communication (the BCP protocol) so that MPF
could be used withany media controller. Again, the MPF package you
download from GitHub has a media controller bundled in with it. (It's
what we call the MPF Media Controller.) It can handle multiple display
elements, animations, videos, and multiple tracks of audio. It's more
than capable of powering a DMD, a color DMD, and even the full LCD
display of a machine like *The Wizard of Oz*. (And the MPF Media
Controller can be configured with the same YAML-based configuration
files as the MPF core engine.) But if you want to do something very
advanced with your backbox display—perhaps something like 3D graphics
or surround sound—then you can still use MPF for your core and then
use another media controller in place of MPF's basic media controller.
There's a group of folks working on an open source advanced media
controller based on Unity 5 (which is also open source). We have some
more information about it `here`_ and a `forum`_ dedicated to it, but
it's very early and not ready. Stay tuned though if you're interested!



(B) Run the media controller to see how it works
------------------------------------------------

As we mentioned already, MPF's built-in media controller is launched
via a Python script `mc.py`. It takes command line options similar to
`mpf.py`, including the path to your machine folder and `-v` to write
verbose logging to the log file. Go ahead and run the Media Controller
by pointing it to your machine's config, like this:


::

    
    python mc.py your_machine


When you do this, you should see an 800x600 popup window with teeny-
tiny text that reads "WAITING FOR CLIENT CONNECTION...," similar to
this: (This example is from a prior version of MPF so the text is not
the same as the current version, but you get the idea.) ` `_ At this
point you can click your mouse back into the command window where you
ran the Python command to launch the media controller and press
`CTRL+C` to kill it. Before we work on connecting the media controller
to the MPF core engine, let's spend a few minutes adding some elements
to our media controller pop-up window so we can actually read what's
going on.



(C) Adda DMD
------------

Note: This tutorial shows how to setup a single-color traditional DMD
like what you'd find in a 1990s Williams or current Stern machine. If
you want to use a Color DMD (either rendered on an LCD screen or a
physical color LED-based DMD), we have `How To guides for those`_, but
it's probably easiest for now just to follow along here with the mono
DMD and then switch the settings to color once you finish the
tutorial.) The first thing we're going to do is to add a virtual DMD
to our popup window. If you have a physical machine with a physical
DMD, that's great, because we'll also be able to control the physical
DMD with this step. But if you don't have a physical machine, or you
have a physical machine but it doesn't have a DMD, that's fine too.
Let's add the DMD anyway since it's really easy, and then you can
remove it later. The first thing to do is totell MPF that we want to
use a DMD.To do this,add a dmd `:` section to your configuration file,
like this:


::

    
    dmd:
        physical: no
        width: 128
        height: 32


The settings for the this section are detailed in the ` `dmd:`
section`_ of the config file reference, so you can read about them
there if you want to know about what these settings mean or you want
to see what other options are available. The only thing we'll point
out here is the `physical:` setting which specifies whether you have a
physical DMD connected or not. (This is referring to the actual
physical DMD with the 14-pin ribbon cable.) Set it to `yes` (or
`true`) if you do, and `no` (or `false`) if not. It's perfectly fine
to use `physical: no` as a permanent solution if you want a virtual
DMD in your window but you have no intentions of ever hooking on up.
At this point if you have a physical machine with a physical DMD, you
canrerun the MPF core engine and you should see the physical DMD go
blank:


::

    
    python mpf.py your_machine


Your flippers should still work (just like they did in the last step),
except this time the P-ROC or FAST logo that's on the screen when you
power on your hardware should go blank. (In order for this to work
then you need to use `physical: yes` in your config. But you won't see
a virtual DMD in the on screen window since we haven't added that yet,
so let's do that now.)



(D) Add a "virtual" DMD element to your on-screen window
--------------------------------------------------------

Now that you've defined a DMD device (even if it's not a physical
DMD), you canadd the Virtual DMD `display element`_to your on-screen
window. Why is this a separate step? Because with MPF, the on-screen
window is just another display you can use for anything you want.While
some people might only want to use it to display a virtual DMD, you
can also use the windowto show light, switch, and coil states,
animation effects, troubleshooting information, multi-player scores,
orjust about anything else you want. So MPFcan't automatically assume
that you want to show a virtual DMD in your window just because you
have a physical DMD, so that'swhy you have to manually set it up here.
All the on-screen window settings are configured in the `window:`
section ofyour config file. Since we haven't specified any other
window settings so far in this tutorial, go ahead and a `window:`
entry now. Then you configure all the displayelements (the things that
show up on an MPF display) in the `elements:` subsection of the
`window:` section, so add that now too. Finally you can add a display
element for the DMD. Your `window:`section should now look like this:


::

    
    window:
        elements:
          - type: virtualdmd
            width: 512
            height: 128
            h_pos: center
            v_pos: center
            pixel_color: ff6600
            dark_color: 220000
            pixel_spacing: 1


Like everything else you've been adding to your config file, the
`window:` entry should be at the beginning of a line with no spaces in
front of it, and then each child element should be indented by four
spaces. (So `elements:` is indented by four spaces, type `:`,
`width:`, etc.all have eightspaces.) Note that there's a dash (a minus
sign) plus a space in front of the `type:` setting. This is a YAML
formatting thing and how MPF knows where one display element ends and
the next starts. Before we explain what all these settings mean, let's
run it again real quick to make sure it works. To do this, run the
*media controller*(since that's what controls the on-screen windows,
not the MPF core), like this:


::

    
    python mc.py your_machine


You should see something like this: ` `_ Pretty cool! Again the
"CLIENT DISCONNECTED" message is there because the media controller is
not connected to the MPF core engine (which makes sense because MPF
isn't running). (And again, the current version of MPF will actually
say "WAITING FOR CLIENT CONNECTION...") So back to what all those
virtual DMD settings mean.You can read all about them in the`Virtual
DMD display element in the MPF documentation`_, but here are the
basics: The entries for `width:` and `height:` are where you specify
the size (in pixels) of your on-screen virtual DMD. Notice that these
are different values than the `width:` and `height:` you configured in
the `dmd:` section of your config. The settings in the `dmd:` section
told MPF what size of the DMD was in terms of display pixels. The
settings in the `window:` section control how big you'd like to draw
the DMD in your on-screen window.The on-screen width and height can be
anything you want, though you should make sure you keep them at the
same aspect ratio as your physical DMD or else the contents of the
window will be stretched weird. Also it's probably best if they're an
exact multiple of your DMD pixels. The `h_pos:` and `v_pos:` settings
specify where within your window the virtual DMD element will be
drawn, with each representing the upper and left sides of the window.
You can use the value `center` for each one to center it, or integer
values from the upper left corner of your main window. So `h_pos: 0`
and `v_pos: 0` will put your DMD element in the upper left corner of
the on screen window, `h_pos: center` and `v_pos: 450` will center it
in the lower portion of your window. etc. You can read more about
positioning and placing elements `here`_. The `pixel_color:` setting
controls what color a fully "on" pixel will be in your on-screen
window. The example of `ff6600` is an orange-ish color which looks
pretty close to classic Williams DMDs. You can change it to red
`ff0000` or green `00ff00` or whatever you want.(This color
specification, like all colors in the config file, is a 6-character
HTML-style color representation. `ff` is full on (255), and `00` is
full off (0). White would be `ffffff`, red would be `ff0000`, yellow
is `ffff00`, etc. There's an online color picker `here`_. Note that
you do *not* add a preceding hash sign (#) to your color entries in
these configfiles since the hash sign is used to comment out a line in
YAML. By the way, you might be wondering why the pixel color setting
is a property of the virtual DMD window displayelement, rather than a
property of the actual DMD itself you just set up? That's because the
physical DMD's color is dictated by the actual DMD you have—MPF
doesn't know (or care) what color it is, rather, it just knows that it
needs to turn pixels on or off. But when it comes to displaying a
virtual DMD in an on-screen window, you can make it whatever you want.
(And ofcourse the on-screen pixel color setting doesn't have to match
what your actual physical DMD color is.) The `dark_color:` setting
controls what color is used when the pixels are "off" (fully dark). A
value of `220000` (dark red/brown)gives it a nice DMD-ish look. MPF
will automatically calculate all the in-between color shades which
range from `off_color` to `pixel_color` based on the number of shades
you specified in your DMD configuration back in Step (1). Finally you
can set a value for the `pixel_spacing:` which affects how much visual
space there is between pixels in the on screen DMD. The exact number
you pick is a matter of personal preference and how big your on screen
DMD is. We have some examples on our `Virtual DMD documentation
page`_.



(E) Draw a box around the DMD
-----------------------------

At this point we have a blank DMD on the screen, but it's kind ofhard
to see. So let's draw a box around it. We'll do this by adding another
display element to the `window:` section of your config. This time
we'll use a display element called "shape," and we can add it like
this:


::

    
          - type: shape
            shape: box
            width: 516
            height: 132
            color: aaaaaa
            thickness: 2


Notice that we didn't add `v_pos:` and `h_pos:` entries. That's
because MPF uses "center" as the default for both, so we don't have to
add them here. (Technically we didn't have to add them in the previous
step either, but we just wanted to include them there so you could
learn about them.) Now launch themedia controller again (via `python
mc.py c:\your_machine`) and your window should look like this: (Be
sure to save your `config.yaml`file first!) ` `_



(F) Run your media controller and the MPF core at the same time
---------------------------------------------------------------

Ok, so now we're able to run the media controller and to get a basic
DMD to show up in the on-screen window. The next thing to do is to run
them both at the same time and to make sure that they're able to talk
to each other. To do this, first launch the media controller as you
did in the previous steps.


::

    
    python mc.py c:\pinball\your_machine -v


Then open up a second command window so you can launch MPF while the
media controller is still running. (You have to open a new window
because the media controller "takes over" the first window which means
you can't launch anything else from it until the media controller
stops.) So instead, open up a second window and launch the MPF core
(using `mpf.py` instead of `mc.py`), except this time do *not* use the
*-b* option since we want the MPF core engine to connect to the Media
Controller::


::

    
    python mpf.py c:\pinball\your_machine -v


When you initially launch the media controller, it should open the
window with your virtual DMD (just like last time) with the "WAITING
FOR CLIENT CONNECTION..." message on the DMD. Then once you launch the
MPF core engine, it will automatically connect to the media controller
and you should see the message "CLIENT CONNECTED" flash briefly in the
DMD. The image below shows what this should look like. You might miss
the CLIENT CONNECTED message because once the attract mode starts, the
DMD will go blank. (In this screenshot we set the color of the console
window that launches the MPF core to be red just so we can tell the
two apart.) ` `_ If you have a physical machine with a DMD, you should
see the "CLIENT CONNECTED" message flash on the physical DMD. (If you
don't see this message on the DMD but your physical machine's flippers
work, make sure you have `physical: yes` in your `dmd:` section.) ` `_



(G) Using the batch file to launch MPF & the Media Controller at the
same time
---------

If you're using Windows, at this point you can probably switch over to
using our batch file called `mpf.bat` which you can use to launch both
the MPF core engine and the media controller at the same time. Using
this batch file is completely optional. To use it, simply run "mpf"
from the command line (which will run `mpf.bat`) and then pass it the
same parameters and options as when you launch `mpf.py`.For example:


::

    
    mpf c:\pinball\your_machine -v


What happens in the batch file is it takes whatever options you pass
it then first runs `python mc.py` with your options, and then it runs
`python mpf.py` with your options. The default behavior of the batch
file is to pop up two new console windows—one for the media controller
and one for the MPF core, and then when MPF exits it keeps the windows
open so you can see any errors or crashes that may have occurred. If
you edit `mpf.bat`, you'll see that there comments in there which
explain how to change this behavior (for example, you might want to
have the pop-up windows automatically close when MPF ends, or you
might want to launch MPF in the current window instead of a new
window). Here's what your desktop would look like if you use the
Windows batch file to launch both windows: (click on the image to see
it full size if it's too small on your screen) ` `_ You can click in
the pop-up window with the DMD and then hit `Esc` to shut down the
media controller, but you'll still have to click into the MPF window
and hit `CTRL+C`(or just click the "X" in the corner of the window) to
stop the MPF core process. The following image shows what your desktop
will look like after you stop the media player but while the MPF core
is still running. ` `_



(H) Getting some useful information to show up in your DMD window
-----------------------------------------------------------------

Okay, now we're finally ready to get some useful things to show up on
the DMD. There are a lot of different ways to do this, and as you get
deeper into your game development you'll end up mixing-and-matching
techniques, but at this point in the tutorial the easiestway is to use
the "Slide Player." MPF'sSlide Playerlets you group together one or
more display elements (`text`_, `images`_, `animations`_, `drawing
shapes`_, etc.) into `slides`_ which are then shown on a display when
certain events happen. We haven't really talked about *events* yet.
MPF is an event-driven framework, which means thatMPF posts "events"
when certain things happen, and then other parts of MPFwatch for those
events and act on them. (You can read more about MPF's event system
`here`_.) Events are really, really important in MPF. They happen
fast, like hundreds per second. Think of eventslike MPF's running
commentary on everything that's happening at all times. *The trough
just got a ball. The player just hit the flipper button. This switch
just became active. The DMD needs a new frame. The ball save timer
just expired. A ball just entered the VUK. etc*. Anyway, it's these
events you use to trigger the SlidePlayer to show a slide on the
display. Let's step through this using a plain-English example first,
and then we'll look at how you can set these up. Let's say you want a
the DMD to show the word "Jackpot" when a jackpot shot was made. First
you'd enter a configuration for your jackpot slide. That might include
a text element with the word "Jackpot" in a certain font at a certain
size. Then you use the Slide Player to link the displaying of that
slide to the "jackpot" game event, so then whenever the Slide Player
sees the jackpot event it will show the slide you configured for it.
The first step is to add a new top-level (i.e. no spaces before it)
section to your config file called `slide_player:` .Then underneath it
you create entries for the various events you want to display
slidesfor, and then under each event you add settingsfor what you want
to display.



(1) Adding "Press Start" text during attract mode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For example, let's say you want to show the text "PRESS START" on the
DMD while the machine is running its attract mode. To do that, you can
create a slide_player: entry which shows a slide when the event
*mode_attract_started* is posted. (How did we know that? We looked at
the list of events that MPF generates. We'll show you how to do that
later. For now just know that *mode_attract_started* is posted when
the attract mode starts. Add an entry to your *slide_player* like
this:


::

    
    slide_player:
        mode_attract_started:
            type: text
            text: PRESS START
            slide_priority: 10


You can make all sorts of adjustments to this text element, including
the `font`_, `size`_, `positioning`_, `decorations`_ (blinking, etc.),
`transitions`_ (sliding in), running it through the `alternate
languagemodule`_, etc, etc. But for now if you just enter like above,
you'll get the default font, at the default size, in the default
position. If you run your game again, your popup window should look
like the image on the left, and if you have a physical DMD (with
`physical: yes` in your `dmd:` section), then your physical DMD should
look like the picture on the right: Hey! This is a big step. You have
a working DMD now!!!



(I) Configure other window settings
-----------------------------------

While we're still working with the window, it's probably worth
mentioning that there are a few other settings you can use to control
the look and feel of the on screen window. These are all covered in
the ` `window:` section of the config file reference`_, so you can
take a look there and see if you want to configure anything else.
(These control things like the window title, the size in pixels,
whether it's full screen or has a frame, etc.) Taking some of these
settings and adding them into your existing `Window:` configuration
section would result in something that looks like this:


::

    
    window:
        title: My Awesome Game!
        elements:
          - type: virtualdmd
            width: 512
            height: 128
            h_pos: center
            v_pos: center
            pixel_color: ff6600
            dark_color: 220000
            pixel_spacing: 1
          - type: shape
            shape: box
            width: 516
            height: 132
            color: aaaaaa
            thickness: 2
          - type: text
            font: tall title
            text: MY AWESOME GAME
            h_pos: center
            v_pos: top
            y: 60
            size: 100
            antialias: yes
            layer: 1
            color: ee9900


Notice that we added another display element to our window, this time
adding text in the game font "tall title",size 60, color yellow
(ee9900), positioned 60 pixels down from the top center of the window,
with text that says "MY AWESOME GAME". We learned about these settings
from the documentation on the `Text display element`_, with
instructions for positioning from the `positioning & placement
documentation`_. If you run your game again, your on screen window
should look like this: ` `_



Check out the complete config.yaml file so far
----------------------------------------------

If you want to see a complete `config.yaml` file up to this point,
it’s available in the MPF package at
`<your_mpf_root>/machine_files/tutorial/config/step6.yaml`. (Again
remember you need to rename this file to `config.yaml` to use it.) And
remember if you're using physical hardware, your coil and switch
numbers will be different than the ones in the sample file, since
you'll need to configure them based on your driver boards' actual
inputs and outputs. You can run this tutorial example config via the
following command. (This assumes you're on Windows.)


::

    
    mpf tutorial -c step6 -v


.. _Unreal Engine: https://www.unrealengine.com/what-is-unreal-engine-4
.. _Text display element: https://missionpinball.com/docs/mpf-core-architecture/displays-dmd/display-elements/text/
.. _here: https://missionpinball.com/docs/displays/display-elements/positioning/
.. _forum: https://missionpinball.com/forum/f/unity-bcp-server/
.. _transitions: https://missionpinball.com/docs/mpf-core-architecture/displays-dmd/transitions/
.. _ section: https://missionpinball.com/docs/configuration-file-reference/dmd/
.. _slides: https://missionpinball.com/docs/displays/slides/
.. _here: http://html-color-codes.info/
.. _Unity 3D: http://unity3d.com/
.. _How To guides for those: https://missionpinball.com/docs/howto/smartmatrix-rgb-dmd/
.. _font: https://missionpinball.com/docs/mpf-core-architecture/displays-dmd/fonts/
.. _Virtual DMD documentation page: https://missionpinball.com/docs/mpf-core-architecture/displays-dmd/display-elements/virtual-dmd/
.. _here: https://missionpinball.com/docs/unity-media-controller/
.. _drawing shapes: https://missionpinball.com/docs/displays/display-elements/shape/
.. _ placement documentation: https://missionpinball.com/docs/mpf-core-architecture/displays-dmd/display-elements/positioning/
.. _here: https://missionpinball.com/docs/events/
.. _decorations: https://missionpinball.com/docs/mpf-core-architecture/displays-dmd/decorators/
.. _animations: https://missionpinball.com/docs/displays/display-elements/animation/
.. _images: https://missionpinball.com/docs/displays/display-elements/image/
.. _display element: https://missionpinball.com/docs/displays/display-elements/
.. _ section of the config file reference: https://missionpinball.com/docs/configuration-file-reference/window/
.. _module: https://missionpinball.com/docs/mpf-core-architecture/multi-language-support/
.. _text: https://missionpinball.com/docs/displays/display-elements/text/


