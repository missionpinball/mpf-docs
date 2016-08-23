How to configure an "on screen" DMD
===================================

.. note::

   This page has not been updated for MPF 0.30 yet

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