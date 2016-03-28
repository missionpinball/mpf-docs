
So you want a color DMD? No problem. MPF can do that. This how to
guide explains the process. ` `_



(A) Understand how Color DMDs work
----------------------------------

Color DMDs are all the rage now. You're probably heard of the company
called `ColorDMD Displays LLC`_ who sells add-on products. If you look
at physical pinball DMDs, you can only buy them in one color. Sure,
thanks to today's LED technology, that color doesn't have to be
orange, but it's still just one color. Maybe in the future we'll have
RGB LED displays which have a tiny RGB LED for each pixel, but we
don't have those yet. (At least not in the sizes we need for a
traditional pinball DMD.) So the way these color DMDs work is they
replace the physical DMD with an LCD monitor, then on the LCD monitor
they show high res images of round dots in any color which look like
low res full-color DMD images. If you want to create a color DMD-style
display in MPF, it's pretty easy.



(B) Create your "native" DMD
----------------------------

The first step to creating a color DMD in MPF is to create a ` `DMD:`
entry`_ in your machine configuration file. The only difference
between configuring a color DMD versusa standard DMD are (1)you have
to change `physical:` from `yes` to `no`, and you have to create a
setting called `type:` which you set to `color`. Here's an example:


::

    
    dmd:
        physical: no
        type: color
        width: 128
        height: 32
        fps: auto


The `physical: no` setting is needed because when you have a color
DMD, you don't actually have a physical pinball DMD connected up to
the 14-pin DMD header on your hardware controller. The `type:
color`tells MPF that the DMD display you're creating should use 24-bit
full color pixels instead of the limited 16-shade single color pixels.
By the way, since you don't have a physical DMD when using color, your
color DMD is not limited by a physical resolution. In other words
itdoesn't have to be 128x32. It can be 192x64, or 256x128, or 512x128,
or... you get the idea! To be clear, the `width:` and `height:`
settings in the `dmd:` section of your config file only represent the
number of virtual dots in your DMD. The actual resolution you display
this at is set up elsewhere.



(C) Create theon screen element for that native DMD
---------------------------------------------------

You can refer to the ` `window:` section`_ of the configuration file
reference for an example of how to create an on screen window (if you
don't already have one) and for an example of how to add your DMD
toit. Your settings will probably end up looking something like this:


::

    
            onscreen_dmd:
                type: VirtualDMD
                width: 512
                height: 128
                pixel_color: ff5500
                dark_color: 220000
                h_pos: center
                v_pos: center
                priority: 1
                pixel_spacing: 1


(Note the `pixel_color:` setting doesn't have an effect when you have
a color DMD.) ` `_ When you're ready to physically mount the LCD into
your backbox, you can delete all the other display elements except for
the `VirtualDMD`,set the window to run in full screen mode, set your
`width:` and `height:` settings to they exactly match the opening in
your speaker panel, and then use ` `x:` and `y:` settings to fine tune
the positioning`_ of the virtual DMD with pixel-level precision.



(D) Update your display elements so they're color
-------------------------------------------------

If you just change your DMD to be color and do nothing else and then
run your game, you'll see that all your pixels have turned from orange
(or whatever color they were before) to white. So what gives? This is
because the actual display elements are not in color. So your display
is showing color, but the content it's showing is mono. (This reminds
us of that old `Calvin & Hobbes comic about the world turning into
color`_.) The exact way you update yourdisplay elements depends on
what type of elements you have. For `Text`_ and `Shape`_ elements, you
simply add a `color:` setting followed by a six-digit hex color code.
(So pretty much everywhere you previously specified a `shade:` value,
you can now specify a `color:` value instead. In fact you can actually
keep both of the entries there, and MPF will use the `shade:` value
for traditional DMDs and the `color:` value for color DMDs and LCDs.)
For images in and animations, if you're importing full color files
(like .png, .jpg, .gif, .bmp, etc.), all you have to do is remove the
` `target: dmd` setting`_. So if MPF sees `target: dmd`, it will
convert your color image to 16-shade (or whatever your DMD is set for)
mono, and if it doesn't see it, it will keep the image as a full color
image. For DMD files (with the .dmd file extension) that are already
in their 16-shade format, obviously converting them to color isn't
going to do any good. They'll just continue to show up as white, (or
whatever `color:` value you set them to be), and if you want them to
be in proper full color then you should add the colors and then save
them as a full color .png or something instead of a .dmd. Let's look
at an example real quick of an original non-color DMD, a color DMD
with no settings changes, and then a color DMD with changes made to
the elements. Note these snippets of config files are not complete,
rather, they just show the relevant areas to the color settings and
the elements on this slide.



(1) Original with no color
~~~~~~~~~~~~~~~~~~~~~~~~~~

Here are the DMD and Images sections of the configuration file. Notice
that the DMD is configured like a traditional DMD, and the scary_guy
image has its target set to `dmd` which means it will be converted
from a full color PNG to a 16-shade DMD image.


::

    
    dmd:
        physical: no
        width: 128
        height: 32
        shades: 16
    images:
        scary_guy:
            file: scary_guy.png
            target: dmd


Here's the step from the attract mode show which builds this slide.
Notice there's a text element, a shape element (a rectangle for the
border), and an image element.


::

    
    - tocks: 3
      display:
      - type: Text
        text: JUDGE DREDD
        priority: 1
      - type: Shape
        shape: rect
        width: 128
        height: 32
        shade: 9
        priority: 1
      - type: Image
        image: death


Here's the result as seen in the on screen virtual DMD window with the
above settings:



(2) Switch the DMD type to "color"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now let's simply switch the DMD type to "color" by adding a `type:
color` entry.


::

    
    dmd:
        physical: no
        type: color
        width: 128
        height: 32
        shades: 16
    images:
        scary_guy:
            file: scary_guy.png
            target: dmd


If that's the only change we made, our slide now looks like this. ` `_
Notice that both the text and the border rectangle are white, and the
image doesn't show up at all.



(3) Properly setting the color settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To "fix" this for a proper color display, first we need to go into the
config file and remove the `target: dmd` setting for our image. Doing
so will mean MPF will not convert that image to the DMD 16-shade color
format (which is what we want now since we have a full color display).


::

    
    dmd:
        physical: no
        type: color
        width: 128
        height: 32
        shades: 16
    images:
        scary_guy:
            file: scary_guy.png


Next if we go into the show file, we can add some colors to our text
and rectangle elements. Right now they are both white since we don't
have any colors defined for either of them, so they're using the
default color (which happens to be white). So let's add `color:`
entries to the Text and Shape elements. (No color is specified for the
image element since images get their colors from their pixels.)


::

    
    - tocks: 3
      display:
      - type: Text
        text: JUDGE DREDD
        priority: 1
        color: ff0000
      - type: Shape
        shape: rect
        width: 128
        height: 32
        shade: 9
        priority: 1
        color: 0000ff
      - type: Image
        image: death


Notice that the rectangle shape element already had a `shade:`
specified which is the intensity it was set to on the traditional DMD.
You can either keep that setting or remove it. If you keep it then it
will be used if you ever run this show on a traditional DMD again. Now
if you rerun MPF, you'll see the properly colored slide in your
virtual DMD: ` `_

.. _ settings to fine tune the positioning: https://missionpinball.com/docs/displays/display-elements/positioning/
.. _ColorDMD Displays LLC: http://www.colordmd.com/
.. _ entry: https://missionpinball.com/docs/configuration-file-reference/dmd/
.. _ setting: https://missionpinball.com/docs/configuration-file-reference/images/
.. _Text: https://missionpinball.com/docs/displays/display-elements/text/
.. _ section: https://missionpinball.com/docs/configuration-file-reference/window/
.. _Shape: https://missionpinball.com/docs/displays/display-elements/shape/
.. _ Hobbes comic about the world turning into color: http://www.gocomics.com/calvinandhobbes/1989/10/29


