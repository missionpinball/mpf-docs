
The Mission Pinball Framework uses TrueType fonts for text on the DMD
and on screen window displays. Picking a good font for your on screen
window is pretty easy since the window is high resolution and it has
24-bit color. But when it comes to the DMD, that can be more
difficult. So in this tutorial we're going to show you how to adjust
your TrueType fonts so they look good and they're easy to use in MPF.
We'll use a font called *`He's Dead Jim`_,*which lives in a file
called `DEADJIM.TTF`. (If you want to follow along, pick a different
font because DEADJIM.TTF is already included and configured in the MPF
package. In other words, we already did this work for this font, and
it's ready to go!) Here's an example of what this fontlooks like: ` `_



(A)Copy the font file into your machine's fonts folder
------------------------------------------------------

In order to use a TrueType font with MPF, you have to copy the font
file to your pinball machine's `/fonts` folder in MPF. We briefly
considered allowing MPF to use fonts that were alreadyinstalled on the
host computer, but then we'drun into issues where things would be
messed up if you ran your game from a computer that didn't have the
same fonts installed. So we decided that each machine would keep its
own fonts in its own machine folder in MPF, meaning those machine
folders would be 100% self-contained and portable. So go into your
your machine's folder and create a new subfolder called `fonts`, and
copy your font file into it: ` `_



(B) Add this font to your machine config file
---------------------------------------------

Next you have to tell MPF that you want to use this font by picking a
name for it and entering the file location into your machine
configuration file. (The reason MPF doesn't just use the actual names
of the fonts is because often times you'll have the same .ttf font
files used for different sizes, and vice-versa.) Create a ` `Fonts:`
section`_ in your config file, then on the next line, indent 4 spaces
(must be spaces, not a tab) and type the name you'd like to refer to
this font as in MPF. We'll call it "space_title." Then on the next
line, indent 4 more spaces (so 8 total), and add a file setting for
the file that you just copied. (MPF will automatically look in your
machine's `fonts` folder for files entered here.) The `Fonts:` section
of your config file should now look like this:


::

    
    Fonts:
        space_title:
            file: DEADJIM.TTF


Now you can test out your font by adding it into an `Attract mode
display show`_ or into a `SlidePlayer entry`_. You'd set it up
something like this:


::

    
    - type: Text
      text: MISSION
      font: space_title
      size: 24


Now when you run your game, you'll see your new Text element come up
on the display, and.... ` `_ Gross. This does not look good. It's all
jagged and weird and kind of small and just pretty much ugly. So now
what?



(C) Run MPF'sfont_tester.py tool
--------------------------------

The next step to make this font look nice is to play with it with
different settings to see how it will look on the DMD. MPF includes a
graphical font testing tool to help you do this (and to help you pick
which fonts will work best in your machine). The tool's called
`font_tester.py` and it's in the `/tools` folder in your MPF package.
(Full instructions for the Font Tester tool, as well as a video walk
through, is available in the `Font Tester documentation`_.) Launch the
Font Tester from the command line, along with a command line argument
which is either (a) a path to a folder which contains .ttf font files,
or (b) the full path to a specific .ttf font file. We can launch the
Font Tester with our Dead Jim font like this:


::

    
    python font_tester.py c:\Windows\Fonts\DEADJIM.TTF


You should see a window pop up with looks something like this: It has
loaded the DEADJIM.TTF font at a default size of10 point with default
demonstration text which says "HELLO": ` `_ Nexthitthe up arrow a
bunch of times to increasethe font sizeup to 24, thenhit the space bar
a few times to clear out the world "HELLO," then type "MISSION." Now
you should see this (which is what how your machine displayed it back
in Step (B). ` `_ By the way, you can use the left and right arrow
keys to step back-and-forth through different fonts in the folder, so
if you accidentally switch off of the font you were working with, use
the arrows to find it again.



(D) Figure out whatfont size you like
-------------------------------------

We rendered the sample text back in Step (B) at a 24 point size. But
now that we have this font loaded in the Font Tester with a size of
24, it looks like it'srendering with characters that are 18 pixels
tall on theDMD. Is this right? Why's it 18 and not 24? This happens
becauseTrueType fonts are resolution independent, and there's no rhyme
or reason from font-to-font about sizing. Font A might be 24 pixels
tall at point size 24, Font B might be 20 pixels tall, and Font C
might be 30 pixels tall. It justdepends on the font. In our case we
want this font to be a nice and big 24 pixels tall, so hit the up
arrow a bunch of times until the font is rendering at the size you
want. In this example, it looks good to us when it's at size 32. (This
is according to the "Font Size:" text label in the upper right corner
of the Font Tester window.) ` `_



(E) Add the size to your config file
------------------------------------

So now that we have this font showing at a size we like, we haveto add
the font's "native" size to its configuration. Doing that is simple:


::

    
    Fonts:
        space_title:
            file: DEADJIM.TTF
            size: 32


Now when we ask for the "space title" font without specifying a size,
we'll get this `DEADJIM.TTF` font rendered at 32 point. (You can
stillspecify a size when calling it to override the default.)



(F) Decide whether you'll use antialiasing
------------------------------------------

Of courseeven though we have the size dialed in, it still doesn't look
too great. One option we can try is enabling antialiasing.
Antialiasing smooths out all the sharp edges on the font, and it makes
a noticeable difference on a low-resolution display such as a DMD.
Some people like it, and some hate it. So really whether you use it is
up to you. We have found that some fonts really require it, like the
one here in this example, and others don't need it—especially "bitmap"
or "pixel" fonts that were designed for low resolution use. Personally
we feel that it's probably best to be consistent throughout your
machine—either all or none should be antialiased—but again, it's just
a matter of taste which is up to you. Anyway you can try antialiasing
in the Font Tester by hitting `CTRL+A`. You should see the text in the
lower left corner change to tell you that antialiasing is enabled, an
you should see the font smooth out. You can hit `CTRL+A` again and
again to turn antialiasing on and off. In this case it looks like
enabling antialiasing is actually pretty good for this font: ` `_ We
can enable antialiasing in the this font's configuration so it will be
used by default. (Individual calls to use the font and always disable
it if they want.)


::

    
    Fonts:
        space_title:
            file: DEADJIM.TTF
            size: 32
            antialias: yes




(G) Trim the extra space off the top and bottom
-----------------------------------------------

The final step to fine-tuning this font is to trim the extra pixels
off the top and bottom. Of course if you're looking at an orange font
on a black screen, you have no idea which dark pixels are part of the
font and which are part of the background. So in the Font Tester tool,
you can hit `CTRL+B` to make the font's bounding box light up bright
green. When we did that for our Dead Jim font at 32 point, it was
immediately clear that they are extra rows of pixels along the top,
and at least four extra rows of pixels across the bottom. At this
point you might be wondering why this matters. Isn't this a little
nit-picky? The problem is that all fonts are different. When Pygame
(the Python add-inMPF uses for graphics and fonts) renders a given
font at a given size, it just produces a rectangle. For example if MPF
says, "I want the text 'MISSION' to be rendered with the font
'DEADJIM.TTF' at '32' point," Pygame's font engine says, "Okay here's
a rectangle that's 100 pixels wide and 30 pixels tall." The problem is
we don't actually know where the font is inside that rectangle. Some
fontstouch the top and bottom, other fonts are small and centered, and
others are small and offset. Again it just depends on the font. The
reason this a problem is that all of the placement MPF does for that
rendered text is actually based on the placement of the rectangle. So
if you want that text to be vertically centered on the screen, MPF can
center the rectangle that contains the font. But if the font is not
centered in the rectangle then it won't look centered. In some cases
this doesn't matter, but in others, man, some fonts are crazy and have
almost as much extra room on the top or bottom as they are tall! So
that's what this `CTRL+B` green box is. It's the actual rectangle that
this font renders into at that given size. And you're using it to see
how many rows of pixels you have to crop off the top and bottom of
this font. (These are size specific, so a font that requires 2 rows to
be cropped at 32 point might only require 1 row to be cropped at 28
point.) By looking at the top of this green bounding box, we can see
that we need to crop 2 rows of pixels from the top. ` `_ Now for the
bottom, notice that thegreen pixels extend all the way to the edge of
the DMD. It's possible for the bounding box to be larger than the on
screen DMD area, so we actually don't know how far down they go at
this point. You can use the SHIFT key plus the up and down arrow keys
to shift the font rectangle up and down, so hit `SHIFT+up` a few
timesto shift the entire image up until you can see where the edge of
the bounding box is. Ahh, there it is. So looking closely it looks
like there are 4rows of green pixels under the bottom of the font, so
we want to crop4 pixels from the bottom of this font when it's
rendered at size 32. ` `_ If you add the crop values to your config
entry, your font config should now look like this:


::

    
    Fonts:
        space_title:
            file: DEADJIM.TTF
            size: 32
            antialias: yes
            crop_top: 2
            crop_bottom: 4


At this point you might be wondering why you have to go through the
extra step of entering cropping values. Isn't this something that MPF
could figure out on its own? Theproblem with that is that different
text strings have different letter heights. So any kind of "automatic"
trimming of white space would change depending on whether the text had
characters that stuck up or down, and then you'd end up with
positioning that would change depending on what text was showing. So
that's why we just go through the process of setting up the fonts
ahead of time. At least this is something you only have to do once.



(H) Think about other sizes
---------------------------

While you have the font open in the Font Tester, you might want to
think about whether you'll want to use that font at any other sizes.
For example we'll create a "space_medium" version of this font which
we'll add to our config, bringing our final entry to this:


::

    
    Fonts:
        space_title:
            file: DEADJIM.TTF
            size: 32
            antialias: yes
            crop_top: 2
            crop_bottom: 4
        space_medium:
            file: DEADJIM.TTF
            size: 25
            antialias: yes
            crop_top: 3
            crop_bottom: 3


Note that rendering that font a 25 point actually increases the number
of rows to crop on top?!? Eh, who knows why. Whatever. (That's why we
made this tool!) One final note, the Font Tester tool as a snapshot
function which you can use with `CTRL+S`. When you do that it will
save an image (it will try .png but will fall back to .bmp on some
systems) of the window contents into a folder called `font_snapshots`.
This is nice because you can spend an hour going through all the fonts
on your system and playing with different sizes and settings, then if
you take a snapshot of ones that you like you'll end up with a folder
full of things you can use as a starting point for your config file.

.. _Attract mode display show: https://missionpinball.com/docs/shows/creating-shows/
.. _He's Dead Jim: http://www.dafont.com/hes-dead-jim.font
.. _Font Tester documentation: https://missionpinball.com/docs/tools/font-tester/
.. _ section: https://missionpinball.com/docs/configuration-file-reference/fonts/
.. _SlidePlayer entry: https://missionpinball.com/docs/configuration-file-reference/slideplayer/


