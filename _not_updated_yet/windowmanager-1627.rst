
The Mission Pinball Framework includes a Window Manager that is
responsible for controlling the on screen window that pops up when MPF
is running. Here's an example that's been configured with a background
image, some title text, and an on-screen virtual DMD. This on screen
window is completely optional. If you're running a production pinball
machine from a small single board computer, you probably just care
about the DMD and wouldn't even bother plugging in a monitor or having
an MPF window. On the other hand, if you're at home working on your
machine, it's nice to have the window pop up which can show you what's
on the DMD or other information about your machine. (The on screen
window can show whatever you want, in addition to troubleshooting and
game status information.) MPF can support multiple displays at the
same time. So it's absolutely possible to run both an on screen window
display and a physical DMD at the same time.



Using the on screen window as your pinball machine's primary display
--------------------------------------------------------------------

You can also put an LCD monitor in your pinball machine and use the
LCD window as your primary display. There are several options for
this, including:


+ Run a full size "virtual" DMD which looks just like a traditional
  DMD except you can get an LCD monitor for $70 instead of having to
  spend $400 for a real DMD panel.
+ Run a "color DMD" which is like a software DMD except the dots are
  different colors. (Or, put another way, it's like using a color
  monitor for your display but you make it look like it's running at a
  really low resolution and you have a filter to make the individual
  pixels look like dots.)
+ Run a fully size high resolution display, like Jersey Jack does with
  the Wizard of Oz and The Hobbit.


In all three of these scenarios, if you're using your LCD display as
your machine's primary display, then you'll probably run it full
screen mode and spend some time getting the placement of all the
display elements tuned perfectly. (You'll probably also use a "real"
computer and not a low-power single board computer, because real LCD
displays have 1-2 million pixels with 24-bit color, and pinball DMDs
have 4,096 pixels with 4-bit color.) ` `_



