---
title: Display Concepts & Architecture
---

# Display Concepts & Architecture


The MPF Media Controller uses the same core architecture to power all
kinds of displays, regardless of whether it's a DMD (physical or
virtual, monochrome or color), an LCD (on screen window displays), or a
combination of both.

The MPF Media Controller's display system is based on Kivy (a
multimedia programming library) and uses technologies like SDL2 and
Gstreamer under the hood.

Here's an architecture diagram which details how the MPF Media
Controller's display system works. It's kind of complex to look at,
but we'll to step through it piece-by-piece. The good news is that you
don't have to understand all of it to use MPF. (You can follow our
step-by-step tutorial to get your display up and running just with a few
config file entries.) But as you start to create more advanced display
effects, it will be helpful to understand how everything fits together.

![image](../images/display_architecture.png)

The major components of the MPF Media Controller's display system are:

## Window

Every MPF-MC application has one (and only one) window. It is the
fundamental graphical element that maps directly to a graphical window
on the host operating system. If you do not provide a "window:"
section in your config, a default window will be created for you (800 x
600 pixels). The size settings (width, height) control the dimensions
(in pixels) of the host operating system window that will be created.
Various settings in the [window:](#) section control the
appearance and behavior of the main on-screen window which is created by
MPF-MC. These settings include things such as whether or not the window
has a border, is full screen, or whether special image processing is
applied to the window using effects. These effects perform image
processing to the source image of the window and can be used to get an
old-school "DMD look" or "color DMD" look to your window as well as
other special effects. Windows can be used in any monitor configuration
(portait or landscape) and will attempt to center themselves left/right
and top/bottom. Windows always use the left lower corner as the 0,0
location.

## Displays

Before anything can actually be shown on the window, it must first be
drawn in a display. Displays are an internal representation of a blank
canvas that holds graphical content. It is important to not confuse
these displays with physical hardware displays (like an LCD monitor or a
DMD). These displays can be shown on such physical devices, but there is
not necessarily a one-to-one mapping between them. One of the most
import features of displays are they are targets for showing slides (you
can think of them as slide managers). The MPF-MC can have multiple
display canvases at the same time, and you can map different ones to
different physical displays. You can even create sub-displays where one
display has a small region which is another display (kind of like
picture-in-picture). The most important setting for a display is its
size (with, height) in pixels. If you do not specify any displays in
your "displays:" section of your config files, a default display (800
x 600 pixels) will be automatically created for you. It is important to
remember that displays always use the left lower corner as the 0,0
location.

## Slides

Every display has a list of "slides", (which are the same height and
width of the display). One slide is "active" at a time, meaning it's the
slide that's showing. Think of these like slides in a slide projector.
You'll probably end up with hundreds of slides, but only one is showing
at a time. You can use transition effects to switch from one slide to
another (these are things like sliding in, pushing, fading, flipping,
etc.).

## Widgets

Widgets are the "things" you actually put on slides. There are lots of
different types of widgets, including text, images, videos, shapes, etc.
Different widgets have different properties, like their x,y position on
the slide, their size, color, etc. You can position widgets on slides
with pixel-level accuracy, or you can use relative positions like "10%
down from the top edge", or "centered", or "25% to the left of center",
etc. Using relative positions means that your display will be resolution
independent.

You can also animate the properties of a widget. For example, a widget
could start out at the bottom of the display and then move to the
center, or you can animate the size, color, scale, rotation, or the
opacity, or pretty much anything other widget property you desire. You
can chain together multiple animations to run back-to-back, or you can
configure multiple animations to happen at the same time. You can even
configure the "curve" of the formula that's used to animate widgets, so
you can have them smoothly accelerate and decelerate, or slow down as
they're animating, or pop into place, etc.

## Display Widget

One widget type of special importance (and deserving of its own
introductory paragraph) is the display widget. The display widget is
used to show the contents of a display on the screen (remember from
above a display is just an in-memory drawing canvas, the display widget
allows its contents to be shown). The main window automatically creates
a display widget that has the same dimensions of the window. Now if you
only require a simple graphical layout where one slide is shown at a
time and fills the entire window, then you need not concern yourself any
further with the display widget. However if you require a more advanced
layout, the display widget will enable you to accomplish that. Display
widgets can also be configured to apply special image processing to the
contents of the display. These effects can be used to get an old-school
"DMD look" or "color DMD" look to your window as well as other
special effects.

## All these concepts come from PowerPoint. :)

The original creators of MPF have day jobs that require them to spend a
lot of time with PowerPoint! If you've ever used PowerPoint, you should
notice that we used PowerPoint (or Keynote or whatever presentation
software you like) as the conceptual model for MPF's display system. In
PowerPoint, your content is a series of "slides." Each slide contains
one or more "elements (widgets)". Those elements can be text, images,
videos, drawing shapes, etc. Each element has a "size" (length &
width), a "position" on the slide (x,y coordinates), a "layer" which
controls how it overlaps with other elements, alpha transparencies, and
animation effects (blink, sparkle, move, etc).

And even though your entire PowerPoint presentation is made of of lots
of slides, only one slide is active on your "display" at a time. Then
when you change to another slide, you can have nice animated
"transitions" from one slide to the next.

So if the MPF display system seems kind of complex, just think of it
like a giant PowerPoint presentation and it should all hopefully make
sense. Now let's start digging into some of the details of each of the
parts of the display system.
