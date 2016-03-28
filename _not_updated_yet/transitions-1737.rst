
Transitions are used to switch from on active slide to another in a
fun way. If you don't have a transition when you switch slides, then
the new slide will just instantly appear in place of the old slide.
Each transition has lots of different settings to control exactly how
it works,though they all have two things in common:


+ The duration of the transition (1 second, 5 seconds, 250 ms, etc.)
+ The new slide that will be transitioning in.


We already mentioned that each display in MPF only has one active
slide at a time. I guess you could say that's kind of not true,
because during a transition you actually have two active slides while
the transition is taking place—the outgoing old slide and the incoming
new slide. (Though technically speaking what happens is the transition
creates its own slide which itself is composed of the visible parts of
the incoming and outgoing slide.) When a transition is taking place,
both the incoming and outgoing slides are active, so if you have
animations or other moving elements then they will continue to play
and move even while the transition is taking place. Also if you want
to go nuts, you can actually run multiple transitions at the same
time. So you could have one slide fading in while it itself had
another slide revealing itself. Kind of cool. We currently have two
transitions written:


+ ` Move In `_. The new slide moves inin on top of the current slide.
  You can specify whether it moves in from the top, left, right, or
  bottom.
+ ` Move Out `_. The current slide movesout of the way, revealing the
  new slide below it.Like the Move In transition, you can specify which
  direction it moves out towards.


We will be creating lots more transitions in the future. If you want a
list of ideas, just open PowerPoint and take a look at all the slide
transitions in there. :) We'll probably end up creating all of those
for MPF. Here's the list we have so far:


+ Push: The new slide pushes the current one out of the way, so the
  current one slides out while the new one is sliding it.
+ Fade: Fade from one slide to the next.
+ Fade through color: Fade from the old slide to a color, then from
  the color to the new slide. If you do this with a bright color and
  really fast, then it's kind of cool, like a "flash" effect that ends
  up with a new slide under it.
+ Zoom: The currentslide zooms in to reveal the new slide.
+ Shrink: The current slide shrinks down to nothing, revealing the new
  slide.
+ Fall: The current slide "falls" down, revealing the new slide.
+ Pixelate: The new slide comes in pixel-by-pixel (but really fast) to
  reveal the new slide on top of the current slide.
+ Slice: The current slide is sliced into pieces to reveal the new
  slide.
+ Blinds: Like a reveal, except it happens in lots of rows at once.
+ Corners: The new slide comes in from all four corners to meet in the
  middle.


MPF's transition architecture is easily extendable, so it's very
straightforward for you to write your own transitions which we can
then at to MPF and share with everyone.

.. _Move In: https://missionpinball.com/docs/displays/transitions/move-in/
.. _Move Out: https://missionpinball.com/docs/displays/transitions/move-out/


