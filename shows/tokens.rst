Using "tokens" for run-time variable replacement in shows
=========================================================

One of the most powerful features of MPF shows is that you
can build shows that contain "placeholder" tokens which are
dynamically replaced with actual values when a show starts.

This lets you build reusable shows that you can then use in
lots of different situations with different lights, slides,
sounds, etc.

Shows without tokens
--------------------

To understand how tokens work, let's first look at a show
that does not include any tokens, like this:

::

   - time: 0
     lights:
       led_01: red
   - time: 1
     lights:
       led_01: off

The example show above is simple. When it starts, it sets
*led_01* to red, then 1 second later, it turns it off.
You can run this show in a loop to flash *led_01* between red
and off.

If you called this show *flash_red*, you could play it via the
*show_player:* section of your config, like this:

::

   show_player:
      some_event:
         show: flash_red

The problem with this show is that it's hard-coded. It only
works for *led_01*, and it only cycles the colors between red
and off.

So what if you want to flash *led_01* between yellow and off? Or
what if you want to flash a different LED? With a show like the
example above, you'd have to write a new show for every LED with
every possible color combination you'd ever want. :(

Adding tokens to shows
----------------------

This is where tokens come in. Consider a slightly modified version
of the show above using a token instead of a hard-coded LED name:

::

   - time: 0
     lights:
       (led): red
   - time: 1
     lights:
       (led): off

Notice the second show is identical to the first, except every reference
to ``led_01`` has been replaced with ``(led)``.

When MPF plays a show, it looks for words in the show contained in
parenthesis, and then it can use those parenthesis to replace values on the
fly.

So in the second show here, when you run the show, you could tell it "replace
the "leds" token with the value "led_02", which would make a show like this:

::

   - time: 0
     lights:
       led_02: red
   - time: 1
     lights:
       led_02: off

The actual way that you start and send tokens to shows varies depending on what
you're doing in MPF. (Typically they're tied to shots or events.)

For example, here's how you'd do it via the *show_player:*. (In this example, we
also add ``loops: -1`` which will cause the show to loop (repeat) indefinitely.

::

   show_player:
      some_event:
         flash_red:
            loops: -1
            show_tokens:
               led: led_02

MPF can run multiple instances of a show at the same time, so you could run
the above show multiple times (at the same time), passing different tokens to each
one, meaning you could use the same show to flash lots of lights at once:

::

   show_player:
      some_event:
         flash_red:
            loops: -1
            show_tokens:
               led: led_02
      some_other_event:
         flash_red:
            loops: -1
            show_tokens:
               led: led_03

Putting multiple values into a single token
-------------------------------------------

You can also use tags to insert multiple values into a single token. For example,
consider the following section from your machine config:

::

   lights:
     led_01:
         number: 00
         tags: tag1
     led_02:
         number: 01
         tags: tag1

You can see that both *led_01* and *led_02* have the *tag1* tag applied. So if you play the
show above (with the *leds* token), you can actually pass the tag name to the token instead:

::

   show_player:
      some_event:
         flash_red:
            loops: -1
            show_tokens:
               led: tag1

This would result in a show that was equivalent to:

::

   - time: 0
     lights:
       led_01: red
       led_02: red
   - time: 1
     lights:
       led_01: off
       led_02: off

Token names are arbitrary
-------------------------

The token show we've been working with so far includes a token called *leds*. That's a good name
for the token since it explains what it's for. However, MPF doesn't care what the actual token name
is. All it's doing is a find-and-replace when the show starts with whatever token names it was passed.

For example, this is a perfectly valid show:

::

   - time: 0
     lights:
       (corndog): red
   - time: 1
     lights:
       (corndog): off

In this case, you'd just pass a value for the *corndog* token when you play the show:

::

   show_player:
      some_event:
         flash_red:
            loops: -1
            show_tokens:
               corndog: led_02

Tokens can be values too
------------------------

You can use tokens anywhere in a show. The actual find-and-replace is pretty simple, just looking
for words in parentheses and then substituting them with the tokens key/value pairs that were passed
when the show starts.

You can also pass multiple tokens. Consider the following show:

::

   - time: 0
     lights:
       (led): (color1)
   - time: 1
     lights:
       (led): (color2)

Notice there are three tokens in this show: *led*, *color1*, and *color2*. You might call this show *color_cycle*,
which you could then play like this:

::

   show_player:
      some_event:
         color_cycle:
            loops: -1
            show_tokens:
               led: led_02
               color1: green
               color2: blue

The bottom line
---------------

As you can see, tokens are very powerful. Again, keep in mind there are many different ways to start shows in
MPF, and all of them have ways to pass tokens to shows.
